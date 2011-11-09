DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ db_name }}',
        'USER': '{{ db_user }}',
        'PASSWORD': '{{ db_password }}',
        'HOST': '{{ db_host }}',
        'PORT': '{{ db_port }}',
    }
}
