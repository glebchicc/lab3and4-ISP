release: python manage.py migrate

web: gunicorn lab3_4.wsgi --log-file -

worker: python manage.py rqworker default