from pickle import TRUE
from .base import env
from .base import *


DEBUG = TRUE
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-)12^_9d9=-bj=f5bz*etb0+mwu@zgp+unl884fm&64lhsq3byx",
)


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "info@food-delivery.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Food Delivery"