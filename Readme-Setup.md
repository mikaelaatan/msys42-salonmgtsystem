# Salon Scheduling System

A simple appointment management project for the class "MSYS 42: Business Applications Development Class," built using Django, Bootstrap, and MySQL. This allows the customers to schedule their appointment in advance. 

---
## GitLab CI/CD Deployment
[CI/CD Pipeline](https://gitlab.com/admu-cicd-zaavedra-2021-2022-2nd-sem/tan-tish-quisido-arnaiz/cicd-salonappointmentsystem)

---
## How to setup locally hosted application

* Instructions are written for Windows OS. Directory and file commands may vary in other OS. 
1. Install git from [https://git-scm.com/downloads]()
2. Open command prompt to clone this project:
   
   ```powershell
   git clone https://github.com/mikaelaatan/msys42-salonmgtsystem.git
   ```
3. Go to Project Directory and activate the virtual environment:
   
   ```powershell
   cd msys42-salonmgtsystem
   python -m venv env
   cd env/Scripts/Activate #linux: source env/bin/activate
   ```
4. Return to project directory and install requirements
   
   ```powershell
   cd app/
   pip install -r requirements.txt
   # linux only: sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
   # pip install mysqlclient
   ```
5. Change mySQL DB credentials 
   * Located at **Beautywand folder > settings.py > line 101, 102

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
8. Check the deployed project
- `localhost:8000` 
- use the credentials `iscs:admin12345`

---
## How To Setup The Application using the Docker file
- Instructions are written for Windows OS. Directory and file commands may vary in other OS. 
- Pre-requisites: Docker (or Docker Desktop) and Python installed on your system. Installation instructions can be googled. For Windows users, you have to set-up (https://docs.microsoft.com/en-us/windows/wsl/install-win10)[WSL 2 (Windows Subsystem for Linux)] to run Docker speedily.

1. Confirm that you have `docker` and `docker-compose` installed

   ```powershell
   docker --version
   docker-compose --version
   ```

   If there are no problems (e.g. "command not found"), then it means you have installed them correctly

2. Use git to clone this project:
   
   ```powershell
   git clone git@gitlab.com:admu-cicd-zaavedra-2021-2022-2nd-sem/tan-tish-quisido-arnaiz/cicd-salonappointmentsystem.git
   ```

3. Run command to create the docker container and run the app
   The build takes around 3-5 minutes to initialize.
   
   ```powershell
   docker-compose up -d --build
   ```

4. Open browser and go to `localhost:8000`
   In the login page, use the credentials `iscs:admin12345`


5. Shut down the container when not in use. 
   NOTE: When collapsing a Docker container, volumes get left behind so that when you restart the containers, the data inside the container persists.
   If you need to "clear" the database contents before closing the container and restarting anew, you can run:

   ```powershell
   docker-compose down -v
   ```
