SHELL=/bin/bash

alembic:
	alembic upgrade head
run:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload
