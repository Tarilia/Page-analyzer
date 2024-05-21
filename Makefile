install:
	poetry install

dev:
	poetry run flask --app page_analyzer:app --debug run

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

build:
	./build.sh

lint:
	poetry run flake8

collect:
	poetry build
	poetry publish --dry-run
	pip install --user --force-reinstall dist/*.whl

celery:
	celery -A page_analyzer.celery_config.celery_app worker --loglevel=info

celery_beat:
	celery -A page_analyzer.celery_config.celery_app beat --loglevel=info

redis:
	docker run -d --name=analyzer_redis_example -p 6333:6379 redis:latest
