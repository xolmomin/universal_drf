migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

reindex:
	python manage.py search_index --rebuild
