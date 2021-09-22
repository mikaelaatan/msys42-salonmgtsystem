# msys42-salonmgtsystem
Salon Scheduling System- A project in MSYS 42 Business Applications Development Class

## How To Setup
1. Install git from `https://git-scm.com/downloads`
2. Open command prompt- clone This Project `git clone https://github.com/mikaelaatan/msys42-salonmgtsystem.git`
3. Go to Project Directory `cd msys42-salonmgtsystem`
4. Create a Virtual Environment `python -m venv env`
5. Go to your environment and activate `cd env/Scripts/Activate`
6. Return to project directory  `cd ..`
7. Install Requirements Package `pip install -r requirements.txt`
8. Change mySQL DB credentials (beautywand folder > settings.py > line 101, 102)
9. Create Migration `python manage.py makemigrations`
10. Migrate Database `python manage.py migrate`
11. Create Super User `python manage.py createsuperuser`
12. Finally Run The Project `python manage.py runserver`
