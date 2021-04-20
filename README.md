# msys42-salonmgtsystem
Salon Scheduling System- A project in MSYS 42 Business Applications Development Class

## How To Setup
1. Install git from `https://git-scm.com/downloads`
2. Open command prompt- clone This Project `git clone https://github.com/mikaelaatan/msys42-salonmgtsystem.git`
3. Go to Project Directory `cd msys42-salonmgtsystem`
4. Create a Virtual Environment `python -m venv env`
5. Go to your environment `cd env`
6. Activate Virtual Environment `Scripts/Activate`
7. Install Requirements Package `pip install django`
8. Create Migration `python manage.py makemigrations`
9. Migrate Database `python manage.py migrate`
10. Create Super User `python manage.py createsuperuser`
11. Finally Run The Project `python manage.py runserver`
