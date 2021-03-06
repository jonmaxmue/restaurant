"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


# SECRETS
def get_secret(secret_name):
    try:
        with open('/run/secrets/{0}'.format(secret_name), 'r') as secret_file:
            return secret_file.read().strip()
    except IOError:
        return None

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
PRODUCTION_ENVIROMENT = False

if PRODUCTION_ENVIROMENT:
    DEBUG = False
    LOCALENV = False
else:
    DEBUG = True
    LOCALENV = True


if LOCALENV:
    # First index is FILEPATH_HOST
    ALLOWED_HOSTS = ['localhost', '0.0.0.0', "127.0.0.1", '10.0.2.2', 'api.restaurant.de', '192.168.0.133']
else:
    ALLOWED_HOSTS = ['api.restaurant.de']

if LOCALENV:
    FILEPATH_HOST = ALLOWED_HOSTS[0] + ":8002"
else:
    FILEPATH_HOST = ALLOWED_HOSTS[0]


BASE_DIR_MEDIA = BASE_DIR

MEDIA_ROOT = os.path.join(BASE_DIR_MEDIA, 'media/')

# Media files
if LOCALENV:
    MEDIA_ROOT = os.path.join(BASE_DIR_MEDIA, 'media/')
else:
    MEDIA_ROOT = "/opt/services/djangoapp/src/project/media"

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static/') #"/opt/services/djangoapp/static/"
STATIC_URL = '/static/'

# Search static files in this pfads too / because project is no app
STATIC_DIR = os.path.join(BASE_DIR, 'project/static/')
STATICFILES_DIRS = [STATIC_DIR]


CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = True

if LOCALENV:
    #CSRF_COOKIE_DOMAIN = '192.168.217.35'
    #CSRF_COOKIE_DOMAIN = '192.168.0.133'
    CSRF_COOKIE_DOMAIN = 'localhost'
else:
    CSRF_COOKIE_DOMAIN = ".restaurant.de"
    #SESSION_COOKIE_SECURE = True THIS CURRENTLY DOES NOT WORK WITH WEBSOCKET FROM APP SIDE BUT IT WORKS FROM WEBSITE
    CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    "https://*.restaurant.de",
    "wss://*.restaurant.de",
    "http://localhost:8081"
]

CORS_ALLOWED_ORIGINS = [
    "https://api.restaurant.de",
    "wss://*.restaurant.de",
    "http://localhost:8081"
]
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# DEPLOY SECURITY OPTIONS
"""
if not LOCALENV:
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    X_FRAME_OPTIONS = 'DENY'
"""

# Contrip.sites
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'core',
    'reservation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'polymorphic',
    'django_filters',
    'mailjet_rest',
    'dry_rest_permissions',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
		#'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '40/day',
    },
    # THIS SECTION IS FROM djangorestframework-json-api project
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        # If you're performance testing, you will want to use the browseable API
        # without forms, as the forms can generate their own queries.
        # If performance testing, enable:
        # 'example.utils.BrowsableAPIRendererWithoutForms',
        # Otherwise, to play around with the browseable API, enable:
        'rest_framework_json_api.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework_json_api.schemas.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',
        'rest_framework_json_api.filters.OrderingFilter',
        'rest_framework_json_api.django_filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        #'project.models.JsonApiCustomize.MyQPValidator'
    ),
    'SEARCH_PARAM': 'filter[search]',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}

#JSON_API_FORMAT_FIELD_NAMES = 'dasherize'
#JSON_API_FORMAT_TYPES = 'dasherize'



# When option UPDATE_ON_DUPLICATE_REG_ID is set to True, then any creation of device with an already existing registration ID will be transformed into an update.
# The UPDATE_ON_DUPLICATE_REG_ID only works with DRF.

PUSH_NOTIFICATIONS_SETTINGS = {
    "APNS_AUTH_KEY_PATH": BASE_DIR + "/AuthKey_6Q5RLL2A4G.p8", # TODO HOW TO SECRET THE AUTHKEY
    "APNS_AUTH_KEY_ID": "6Q5RLL2A4G",
    "APNS_TEAM_ID": "M37Q5PLJW3",
    "APNS_TOPIC": "com.restaurant.restaurant",
    'APNS_USE_SANDBOX': True if LOCALENV else False,
    "UPDATE_ON_DUPLICATE_REG_ID": True,
    # "GCM_API_KEY": "[your api key]",
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/debug.log',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'ERROR',
    },
}



ROOT_URLCONF = 'project.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            STATIC_DIR,
            STATIC_DIR + '/project/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'libraries': {
                #'navigation': 'project.templatetags.navigation',
            },
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
if PRODUCTION_ENVIROMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'defaultdb',
            'USER': 'doadmin',
            'PASSWORD': get_secret("postgres_passwd_restaurant_db"),
            'HOST': 'db-api-restaurant-online-do-user-4458520-0.b.db.ondigitalocean.com',
            'PORT': '25060',
            'OPTIONS': {
                'sslmode': 'verify-full',
                'sslrootcert': os.path.join(BASE_DIR, 'ca-certificate.crt')
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'restaurant_db',
            'USER': 'restaurant_db_role',
            'PASSWORD': 'restaurant_db_password',
            'HOST': 'restaurant_db',  # <-- IMPORTANT: same name as docker-compose service!
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Check if a module exists or not
def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


# Check if module exists, because local we dont use netifaces.
if module_exists("netifaces"):
    import netifaces

    # Find out what the IP addresses are at run time
    # This is necessary because otherwise Gunicorn will reject the connections
    def ip_addresses():
        ip_list = []
        for interface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(interface)
            for x in (netifaces.AF_INET, netifaces.AF_INET6):
                if x in addrs:
                    ip_list.append(addrs[x][0]['addr'])
        return ip_list


    # Discover our IP address
    ALLOWED_HOSTS = ip_addresses()


# Reference to the custom user
AUTH_USER_MODEL = 'core.User'





# Images Upload Qualitys
BACKGROUND_IMAGES_LONGEST_SIDE = 1800
BACKGROUND_IMAGES_QUALITY = 70
PRODUCTION_IMAGES_LONGEST_SIDE = 600
PRODUCTION_IMAGES_QUALITY = 70
AVATAR_LONGEST_SIDE = 300
AVATAR_QUALITY = 100

CREATION_PHOTO_LONGES_SITE = 700
CREATION_PHOTO_QUALITY = 70


# Channel configuration
ASGI_APPLICATION = 'project.routing.application'
if PRODUCTION_ENVIROMENT:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [('rediss://default:' + get_secret("redis_passwd") + '@redis-api-restaurant-online-do-user-4458520-0.b.db.ondigitalocean.com:25061')],
            },
        },
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer',
        },
    }

# SECRETS DJANGO
SECRET_KEY = get_secret('django_secret_key')


MAILJET_MAIL_API_URL = "https://api.mailjet.com/v4/sms-send"

# SECRETS EMAIL
MAILJET_MAIL_API_KEY = get_secret('mailjet_api_mail_key')
MAILJET_MAIL_API_SECRET = get_secret('mailjet_api_mail_secret')
MAILJET_SMS_API_SECRET = get_secret('mailjet_api_sms_2fa_token')
MAIL_AUTH_SENDER = {"email": "admin@restaurant.de", "first_name": "admin", "last_name": "restaurant"}
'''
MAILJET_TEMPLATE_IDS = {
	"CONTACT_QUESTION": 878950,
	"CONTACT_PRAYER": 878939,
	"REGISTRATION_ACTIVATE": 878010,
	"PASSWORD_RESET": 1224686
}
'''

# SECRETS STRIPE
STRIPE_API_PUBLIC_KEY = get_secret('stripe_api_public_key')
STRIPE_API_SECRET_KEY = get_secret('stripe_api_secret_key')
STRIPE_WEBHOOK_SIGNING_SECRET = get_secret('stripe_webhook_signing_secret')