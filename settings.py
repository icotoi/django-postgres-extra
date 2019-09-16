import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'this is my secret key'  # NOQA

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DATABASES = {
    'default': dj_database_url.config(default='postgres:///psqlextra'),
    'pw_test': dj_database_url.config(default='postgres:///psqlextra_pw?user=tester_role&password=tester_password')
}

DATABASES['default']['ENGINE'] = 'psqlextra.backend'

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('ro', 'Romanian'),
    ('nl', 'Dutch')
)

INSTALLED_APPS = (
    'psqlextra',
    'tests',
)

POSTGRES_EXTRA_MIGRATION_DEFAULT_TIMEOUT = None
