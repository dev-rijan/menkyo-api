run:
	poetry run uvicorn app.main:create_app --reload --factory

upgrade:
	poetry run alembic upgrade head

migration:
	poetry run alembic revision --autogenerate -m "$(message)"
