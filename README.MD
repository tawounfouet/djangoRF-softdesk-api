# SoftDesk Support API - Django REST Framework

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-092e20?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![OpenClassrooms](https://img.shields.io/badge/OpenClassrooms-FFC700?style=flat&logo=openclassrooms&logoColor=white)

<p align="center">
  <img src="https://user.oc-static.com/upload/2023/06/28/16879473703315_P10-02.png" alt="Logo & Banner LITRevue"/>
</p>

## Description
This project is a REST API for a ticketing system. It allows you to create projects, tickets, comments and assign users to them. It also allows you to create users and assign them to projects.



## Setup Instructions

These instructions will guide you through setting up and running the Softdesk Support API locally on your machine.

### Prerequisites

- [Python](https://www.python.org/) (3.6 or higher)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Clone the Repository and Setup Dev Environment

```bash
# Clone the repository
git clone https://github.com/tawounfouet/djangoRF-softdesk-api.git
cd djangoRF-softdesk-api

# Install Pipenv if you haven't already
pip install pipenv

# Create and activate the virtual environment
pipenv install --dev
pipenv shell

# Install project dependencies
pipenv install

# Apply database migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver

# Navigate to http://localhost:8000/api
  - http://127.0.0.1:8000/api/softdesk/users
  - http://127.0.0.1:8000/api/softdesk/projects
```

## Auteur
- [Thomas AWOUNFOUET]()