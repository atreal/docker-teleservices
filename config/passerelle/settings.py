# Configuration for passerelle.
# You can override Passerelle default settings here

# Passerelle is a Django application: for the full list of settings and their
# values, see https://docs.djangoproject.com/en/1.7/ref/settings/
# For more information on settings see
# https://docs.djangoproject.com/en/1.7/topics/settings/

# WARNING! Quick-start development settings unsuitable for production!
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# This file is sourced by "execfile" from /usr/lib/passerelle/debian_config.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = False

ADMINS = (
  ('Admins IMIO', 'admints@example.net'),
)

# ALLOWED_HOSTS must be correct in production!
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'local-passerelle.example.net',
]

# Databases
# Default: a local database named "combo"
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# Warning: don't change ENGINE
DATABASES['default']['NAME'] = 'passerelle'
DATABASES['default']['USER'] = 'postgres'
DATABASES['default']['PASSWORD'] = 'password'
DATABASES['default']['HOST'] = 'database'
DATABASES['default']['PORT'] = '5432'

CACHES = {
    'default': {
        'BACKEND': 'hobo.multitenant.cache.TenantCache',
        'REAL_BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '172.17.0.1:11211',
    }
}

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Brussels'

# Email configuration
EMAIL_SUBJECT_PREFIX = '[passerelle local]'
SERVER_EMAIL = 'passerelle@example.net'
DEFAULT_FROM_EMAIL = 'passerelle@example.net'

# SMTP configuration
EMAIL_HOST = 'localhost'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 25

# HTTPS Security
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = True

INSTALLED_APPS += ('passerelle_imio_ts1_datasources',)
TENANT_APPS += ('passerelle_imio_ts1_datasources',)
PASSERELLE_APP_PASSERELLE_IMIO_TS1_DATASOURCES_ENABLED = True

