import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "so-secret-i-cant-believe-you-are-looking-at-this"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "djangocms_export_page.db"),
    }
}

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "cms",
    "menus",
    "treebeard",
    "filer",
    "easy_thumbnails",
    "djangocms_text_ckeditor",
    "meta",
    "djangocms_alias",
    "djangocms_page_meta",
    "djangocms_export_page",
    "testapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "sekizai.context_processors.sekizai",
            ],
        },
    },
]

ROOT_URLCONF = "testapp.urls"

SITE_ID = 1

LANGUAGE_CODE = "nl"
LANGUAGES = [
    ("nl", "Dutch"),
    ("en", "English"),
]

# (CMS) Page Meta settings
META_SITE_PROTOCOL = "https"
META_SITE_DOMAIN = "www.example.com"

# CMS settings
CMS_CONFIRM_VERSION4 = True

CMS_TEMPLATES = [("test.html", "Test page")]

CMS_PLACEHOLDER_CONF = {
    None: {
        "plugins": ["TextPlugin"],
    },
}
