from pathlib import Path
from src.templates.templates_setting import TEMPLATES

# 基本路徑設定
BASE_DIR = Path(__file__).resolve().parent.parent

# 基本開發用設定
SECRET_KEY = 'secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# 安裝的 APP
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'rest_framework',
    'drf_yasg',
    'src.leave',
]

# 中介軟體
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# 路由設定
ROOT_URLCONF = 'src.config.urls'

# 資料庫設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 其他設定
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'zh-tw'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
