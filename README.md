# Командий проект Портал групи
Мета проекту: Створення порталу групи, де буде розміщуватися інформація про групу, новини групи, форум, електронний щоденник, події та календар подій, система опитувань, система голосувань, оголошення, матеріали, портфоліо, галерея(можно розширювати функціонал).

# Встановлення
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver