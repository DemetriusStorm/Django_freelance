# Django_freelance
Local Library website in Django using DRF, Postgres, Gunicon and Nginx - Dockerizing..

Production uses gunicorn + nginx.

1. Clone repo: got clone https://github.com/DemetriusStorm/Django_freelance.git
2. Create .env.dev.prod file:
<code>DJANGO_DEBUG=1
DJANGO_SECRET_KEY=change-me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres</code>
3. Update the environment variables in the .env.dev.prod file.
4. 
- build: `docker-compose -f docker-compose.prod.yml up -d --build`
- migrate: `docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`
- collectstatic: `docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`