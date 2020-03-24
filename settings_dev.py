from .settings_common import *



# ロギング設定

LOGGING = {
    'version': 1,
    "disable_existing_loggers": False,

    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },

    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev"
        }
    },

    "formatters": {
        "dev": {
            "format": "\t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:%(lineno)d)",
                "%(message)s"
            ])
        },
    }
}
EMAIL_HOST = ["localhost"]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")