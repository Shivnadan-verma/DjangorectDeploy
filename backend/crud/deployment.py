import os
from .settings import * 
from .settings import BASE_DIR


ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', 'localhost')]

CSRF_TRUSTED_ORIGINS = [f"https://{os.environ['WEBSITE_HOSTNAME']}"]
DEBUG = False
SECRET_KEY=os.environ['MY_SECRET_KEY']

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
#CORS_ALLOWED_ORIGINS = [
  
#]


STORAGE={
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },

}
CONECTION=os.enviorn['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONECTION_STR={pair.split('=')[0]:pair.split('=')[1] for pair in CONECTION.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONECTION_STR['dbname'],
        'USER': CONECTION_STR['user'],
        'PASSWORD': CONECTION_STR['password'],
        'HOST': CONECTION_STR['host'],
        'PORT': CONECTION_STR['port'],
    }
}
STATIC_ROOT = BASE_DIR/'staticfiles'