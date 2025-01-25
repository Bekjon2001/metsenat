INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
LOCAL_APPS = [
    'apps.users',
    'apps.appeals',
    'apps.general',
    'apps.sponsors',
]
THIRD_PARTY_APPS = [
    'rest_framework',
]
INSTALLED_APPS += LOCAL_APPS +THIRD_PARTY_APPS