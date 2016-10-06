.PHONY: update \
		dependencies backend-dependencies frontend-dependencies \
		test test-backend test-frontend \
		check check-backend check-frontend \
		db-setup db-migrate db-load-data admin \
		export-data-to-csv

# -----------------------------------------------------------

update: dependencies db-setup

# -----------------------------------------------------------

dependencies: backend-dependencies frontend-dependencies

backend-dependencies:
	@echo "== Install Python dependencies. =="
	pip install -r requirements.txt

frontend-dependencies:
	@echo "== Install frontend dependencies. =="
	  npm update

# -----------------------------------------------------------

test: test-backend test-frontend

test-backend:
	@echo "===== Backend tests ====="
	python manage.py test --traceback

test-frontend:
	@echo "===== Frontend tests ====="
	cd frontend
	@echo "TBA"
	

# -----------------------------------------------------------

check: check-backend check-frontend

check-backend:
	@echo "===== Backend linting ====="
	pylint --reports=n --disable=E501,E225,E123,E128 --ignore=migrations,urls.py,wsgi.py practice

check-frontend:
	@echo "===== Frontend linting ====="
	cd frontend &&
	@echo "TBA"


# -----------------------------------------------------------

db-setup: db-migrate db-flush admin db-load-data

db-migrate:
	@echo "===== Set up database ====="
	python manage.py migrate --noinput

db-flush:
	python manage.py flush --noinput

admin:
	python manage.py create_admin

db-load-data:
	python manage.py load_static_data

# -----------------------------------------------------------
