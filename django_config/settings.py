"""
Django settings for Productivity project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import platform

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')g@^(l6+_uc*ckf%rj2i+89v^4^r3k!$l76husfgc74nk1#&g+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '*']

# define my applications with full path
MY_APPS = {

    # 'system_metadata': 'excursion.system_metadata',
}

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'bootstrap3',
    'registration',


    'doc',
    'office365',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'django_config.urls'

if platform.node() == 'az84cqc01':
    LOGIN_REDIRECT_URL = '/tpe_toolkit/'
    LOGOUT_REDIRECT_URL = '/tpe_toolkit/'

else :
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL = '/'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/html')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



#install social auth pip install social-auth-app-django
#https://fosstack.com/how-to-add-google-authentication-in-django/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY  = '272448904965-lg70vakdq457btb1o3a1hjhbpdu1mpjf.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET  = 'bQJvx1awfUQiorsJ3jBcv2--'

# SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_KEY = '050ceeba-818d-49f9-9abf-b0c246721310'
# SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_SECRET = 'wyNSD07wghkbNING828]|]$'

SOCIAL_AUTH_AZUREAD_OAUTH2_KEY = 'af21624b-1a3d-4749-8325-8e877a3aaddd'
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET = 'tYjeEpqVureH/bzCwIU6NSqaDP4qpwO930NDuw2hen8='

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'


AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
 'social_core.backends.google.GoogleOpenId',  # for Google authentication
 'social_core.backends.google.GoogleOAuth2',  # for Google authentication
 'social_core.backends.github.GithubOAuth2',  # for Github authentication
 'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
 'social_core.backends.azuread.AzureADOAuth2',  # for Microsoft authentication
 'social_core.backends.azuread_tenant.AzureADTenantOAuth2',  # for Microsoft authentication

 'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static/')
# STATIC_URL = 'D:/Source/development/web/cqc_web/static'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
