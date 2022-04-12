# Salon Scheduling System

A simple appointment management project for the class "MSYS 42: Business Applications Development Class," built using Django, Bootstrap, and MySQL. This allows the customers to schedule their appointment in advance. 

---

## How To Setup The Application Locally
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
   In the login page, use the credentials iscs:admin12345


5. Shut down the container when not in use. 
   NOTE: When collapsing a Docker container, volumes get left behind so that when you restart the containers, the data inside the container persists.
   If you need to "clear" the database contents before closing the container and restarting anew, you can run:

   ```powershell
   docker-compose down -v
   ```
