dbinit:
	poetry run alembic init migrations

createmigration:
	poetry run alembic revision --autogenerate -m "$(message)"

dbupgrade:
	poetry run alembic upgrade head

dbdowngrade:
	poetry run alembic downgrade head