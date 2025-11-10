"""
Configuración de Django para el proyecto backend_TiendadeMagia.
"""

import os
from pathlib import Path

# Construye rutas dentro del proyecto como esta: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================================
# CONFIGURACIÓN DE SEGURIDAD
# =========================================================================

SECRET_KEY = 'django-insecure-tu_clave_secreta_aqui'

DEBUG = True

ALLOWED_HOSTS = []


# =========================================================================
# APLICACIONES INSTALADAS (Paso 25)
# =========================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Aplicación de la tienda de magia
    'app_TiendadeMagia',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_TiendadeMagia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_TiendadeMagia.wsgi.application'


# =========================================================================
# BASE DE DATOS
# =========================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================================================================
# VALIDACIÓN DE CONTRASEÑAS
# =========================================================================

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


# =========================================================================
# INTERNACIONALIZACIÓN
# =========================================================================

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City' # Zona horaria ajustada para México

USE_I18N = True

USE_TZ = True


# =========================================================================
# ARCHIVOS ESTÁTICOS
# =========================================================================

STATIC_URL = 'static/'


# =========================================================================
# CLAVE PRIMARIA PREDETERMINADA
# =========================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'