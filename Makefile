migrate:
	python manage.py makemigrations && python manage.py migrate

run:
	python manage.py runserver

start: ## Start all or c=<name> containers in background
	docker-compose -f $(or $(DOCKER_COMPOSE_FILE), docker-compose.yml) up -d $(c)

test:
	pytest -vv

