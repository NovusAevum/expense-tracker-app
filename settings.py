INSTALLED_APPS += ['rest_framework']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your@email.com'
EMAIL_HOST_PASSWORD = 'yourpassword'

from django.core.mail import send_mail

send_mail(
    'Inventory Low',
    'Inventory for Book X is low!',
    'from@example.com',
    ['target@example.com'],
)

