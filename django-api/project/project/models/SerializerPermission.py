

class SerializerPermission:

    def __init__(self, permission_class, context):
        self.perm = permission_class
        self.req = context["request"] if "request" in context else None

    def is_owner(self, obj):
        return self.perm.is_user_owner(self.req, obj) if self.req else False

    def is_manager(self, obj):
        return self.perm.is_user_manager(self.req, obj) if self.req else False

    def is_user_or_manager(self, obj):
        return self.is_owner(obj) or self.is_manager(obj) if self.req else False