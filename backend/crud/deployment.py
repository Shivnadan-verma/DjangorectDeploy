import os
from .settings import *
from .settings import BASE_DIR

# ✅ Get hostname safely for both local & Azure
hostname = os.environ.get('WEBSITE_HOSTNAME', 'localhost')

# ✅ Allowed Hosts and CSRF
ALLOWED_HOSTS = [hostname, '127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = [
    f"https://{hostname}",
    f"http://{hostname}"
]

# ✅ Debug and Secret Key
DEBUG = False
SECRET_KEY = os.environ.get('MY_SECRET_KEY', 'django-insecure-fallback-key')

# ✅ Middleware (no change, but confirmed order)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ CORS - allow frontend domain or temporarily *
CORS_ALLOWED_ORIGINS = [
    f"https://{hostname}",
    f"http://{hostname}",
]
CORS_ALLOW_ALL_ORIGINS = True  # (optional for testing)

# ✅ Correct STORAGES setting (Django 4+)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ✅ Database connection (safe parse)
connection_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING', '')
connection_dict = {}

if connection_str:
    # Split by space or semicolon depending on Azure format
    for pair in connection_str.replace(';', ' ').split():
        if '=' in pair:
            key, value = pair.split('=', 1)
            connection_dict[key] = value

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': connection_dict.get('dbname', ''),
        'USER': connection_dict.get('user', ''),
        'PASSWORD': connection_dict.get('password', ''),
        'HOST': connection_dict.get('host', ''),
        'PORT': connection_dict.get('port', '5432'),
    }
}

# ✅ Static files (important for Azure)
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
