
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
)




TEMPLATE_DIRS=(
    os.path.join(BASE_DIR,'templates'),
    )

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static"),
    )
