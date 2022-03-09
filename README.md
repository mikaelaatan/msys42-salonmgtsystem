# Salon Scheduling System

A simple appointment management project for the class "MSYS 42: Business Applications Development Class," built using Django, Bootstrap, and MySQL. This allows the customers to schedule their appointment in advance. 

## 

## How To Setup Application

* Instructions are written for Windows OS. Directory and file commands may vary in other OS. 
1. Install git from [https://git-scm.com/downloads]()
2. Open command prompt to clone this project:
   
   ```powershell
   git clone https://github.com/mikaelaatan/msys42-salonmgtsystem.git
   ```
3. Go to Project Directory and activate the virtual environment:
   
   ```powershell
   cd msys42-salonmgtsystem
   python -m venv env
   cd env/Scripts/Activate
   ```
4. Return to project directory and install requirements
   
   ```powershell
   cd ..
   pip install -r requirements.txt
   ```
5. Change mySQL DB credentials 
   * Located at **Beautywand folder > settings.py > line 101, 102**
6. Create migrations, migrate the database, and create superuser account in Django
   
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
7. Finally Run The Project
   
   ```powershell
   python manage.py runserver
   ```
