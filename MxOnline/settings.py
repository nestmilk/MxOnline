# _*_ encoding: utf-8 _*_


"""
Django settings for MxOnline project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""



import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#引入apps和extra_app的路径，这样在命令行中也可以启动
sys.path.insert(0, os.path.join(BASE_DIR,"apps"))
sys.path.insert(0, os.path.join(BASE_DIR,"extra_app"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z_q-62hc((82#31o6-8i4c1jwy)m0ce1&(x8v$=2&pf$=ydr$8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#当debug=false时候必须配置这个，'*"表上所有都可以
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'organization',
    'operation',
    'xadmin',
    'crispy_forms',
    'captcha',
    'pure_pagination',
    'DjangoUeditor',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MxOnline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'MxOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxonline',
        'USER': 'root',
        'PASSWORD': 'lius0037',
        'HOST': '127.0.0.1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#用于页面中的{%  load staticfiles %} {% static “css/...” %}
STATIC_URL = '/static/'


#当debug=False时候，会失效，需要配饰STATIC_ROOT
#这个在collectstatics时候打开，并需要注释掉下面的STATICFILES_DIRS
# STATIC_ROOT = os.path.join(BASE_DIR,'static')


#用于页面中herf=“/static/css/..."  当debug=False时候，会失效，需要配饰STATIC_ROOT
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
# 替换自带auth_user
AUTH_USER_MODEL = 'users.UserProfile'
#替换自带的authenticate，校验自己设定的字段
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackends',
)

EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "56164612@qq.com"
EMAIL_HOST_PASSWORD = "ahldsiiphpdocabg"
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
EMAIL_FROM = EMAIL_HOST_USER

#xadmin后台上传文件需要以下两个配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

PAGINATION_SETTINGS = {
    #显示3+1页
    'PAGE_RANGE_DISPLAYED': 3,
    'MARGIN_PAGES_DISPLAYED': 1,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}