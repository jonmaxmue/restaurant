from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.response import Response
from core.serializers.UserSerializer import UserSerializer
from project.models.MailJet import MailJet
from core.models.Authorization import Authorization
from core.models.User import User
from rest_framework.throttling import AnonRateThrottle
from core.exceptions import CodeOrTokenNotExpired, UserNotExsists, EmailNotInserted, EmailOrSMSNotSend, TokenOrIdFailed
from rest_framework import permissions, status, viewsets, decorators


class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = (DRYPermissions,)
    serializer_class = UserSerializer
    throttle_classes = [AnonRateThrottle]

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [DRYPermissions(),]
        return []

    def get_queryset(self):
        return get_user_model().objects.all()

    def log_out(self, request):
        response = Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
        logout(self.request)
        return response


    @decorators.action(
        detail=True,
        methods=['POST'],
    )
    def send_sms_code(self, request):
        try:
            # If the user exists, get the user
            user = User.objects.get(phone_number=request.data["phone_number"])
        except Exception:
            user = None

        if user:
            # Generate new authorization code and send sms to the existing user
            code = user.authorization.generate_sms_code_and_save(5, 2)
            MailJet.send_sms_with_code(user.phone_number, code)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        if not user:
            serializer = self.serializer_class(data=request.data, partial=True)

            if serializer.is_valid():
                # Create user
                user = User.objects.create(phone_number=serializer.validated_data['phone_number'])
                user.save()

                # Create users authorization
                authorization = Authorization.objects.create(user=user)
                user.authorization = authorization
                user.save()

                # Generate authorization code and send sms
                code = authorization.generate_sms_code_and_save(5, 1)
                MailJet.send_sms_with_code(serializer.validated_data['phone_number'], code)

                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @decorators.action(
        detail=True,
        methods=['PATCH'],
        url_name='update-password',
        url_path='update-password',
    )
    def update_password(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(id=self.kwargs['id'])
            password = serializer.validated_data["password"]

            if user.authorization.is_in_time(user.authorization.code_created, 2):
                user.authorization.is_authorized = True
                user.authorization.save()
                user.set_password(password)
                user.save()

                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response("Not valid", status=status.HTTP_401_UNAUTHORIZED)

    # NOT DONE SERIALIZER VALID SHOULD BE CHECKED
    @decorators.action(
        detail=True,
        methods=['POST'],
    )
    def send_mail_token(self, request):
        try:
            number = request.data["phone_number"].replace(" ", "")
            user = User.objects.get(phone_number=number)
        except Exception:
            raise UserNotExsists()

        if not user.email:
            raise EmailNotInserted()

        authorization = Authorization.objects.get(user=user)
        token = authorization.generate_email_token_and_save(81, 2)

        to_name = " ".join([user.profile.firstname, user.profile.lastname])
        MailJet().send_mail_with_token(user.email, to_name, token)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

    # NOT DONE WITH SERIALIZER
    @decorators.action(
        detail=True,
        methods=['POST'],
    )
    def update_phone_number(self, request, *args, **kwargs):
        token = request.data["token"]
        user_id = self.kwargs['id']
        new_phone_number = request.data['phone_number']

        try:
            authorization = Authorization.objects.get(
                email_token=token,
                user__id=user_id
            )
        except Exception:
            raise TokenOrIdFailed()

        if authorization.is_in_time(authorization.email_token_created, 120):
            user = User.objects.get(id=user_id)
            user.phone_number = new_phone_number
            user.username = new_phone_number
            user.save()

            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response("Not valid", status=status.HTTP_401_UNAUTHORIZED)

    # NOT DONE SERIALIZER VALID SHOULD BE CHECKED
    @decorators.action(
        detail=True,
        methods=['POST'],
    )
    def update_email(self, request, *args, **kwargs):
        code = request.data["code"]
        user_id = self.kwargs['id']
        new_email = request.data['email']

        try:
            authorization = Authorization.objects.get(
                code=code,
                user__id=user_id
            )
        except Exception:
            raise CodeOrIdFailed()

        if authorization.is_in_time(authorization.code_created, 2):
            user = User.objects.get(id=user_id)
            user.email = new_email
            user.save()

            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response("Not valid", status=status.HTTP_401_UNAUTHORIZED)

    @decorators.action(
        detail=False,
        methods=['GET'],
    )
    def get_csrf_token(self, request):
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user, context={'request': request}).data, status=status.HTTP_200_OK)
        return Response("csrftoken set", status=status.HTTP_200_OK)

    @decorators.action(
        detail=True,
        methods=['POST'],
    )
    def login(self, request):
        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            form = AuthenticationForm(data=request.data)
            if form.is_valid():
                user = form.get_user()
                if user.authorization.is_authorized:
                    login(request, user=user)
                    return Response(UserSerializer(user, context={'request': request}).data, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_401_UNAUTHORIZED)