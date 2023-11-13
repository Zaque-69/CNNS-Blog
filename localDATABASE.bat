REM USE RUN THIS FILE ONLY WHEN YOU MODIFY loc/settings.py AND YOU BRING BACK LOCAL DATABASE 
REM DELETE MODELS MIGRATIONS FROM EVERY APP AND OLD DATABASE
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
