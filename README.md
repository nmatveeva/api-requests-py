# api-requests-py
SOAP and REST API test automation solution using Python.

## Project Setup

1. Clone this repository.
2. Run `cd api-requests-py` to enter the project.
3. Run `pipenv install` to install the dependencies.
   NOTE: to add a new package run `pipenv install <new-package>`.

## ReportPortal Setup

1. Start the Docker desktop app.
2. Download the Docker compose file from this command:
`curl https://raw.githubusercontent.com/reportportal/reportportal/master/docker-compose.yml -o docker-compose.yml`
3. Run this Docker compose file:
`docker-compose -p reportportal up -d --force-recreate`
>NOTE: If you have run this command once, and don't want to recreate the containers from scratch, then you can always eliminate this flag `--force-recreate.`
> To start the ReportPortal after it is already setup use command: `docker-compose -f docker-compose.yml -p reportportal up -d`
4. Check whether all the processes are running fine by doing: `docker ps -a`
5. Go to `localhost:8080` and login as `superadmin/erebus`.
6. To run tests with Report Portal you must provide '--reportportal' flag: `python -m pytest ./tests --reportportal`
7. To run tests with Report Portal in parallel use command: `python -m pytest -n auto ./tests --reportportal`
