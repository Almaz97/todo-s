# ToDo app

ToDo app is smart task list for everyday use.

Key Features:
* CRUD category (categories can be nested) for todo list. 
* CRUD todo list

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
```
1) virtualenv venv
2) source project-env/bin/activate
3) pip install -r requirements.txt
```
Setup Env Variables. Create .env file along-side manage.py module

|    NAME   |                      DESCRIPTION                      |DEFAULT VALUE|
|-----------|-------------------------------------------------------|-------------|
|DEBUG      |Debug mode for local machine, set `False` on porduction|     False    |
|SECRET_KEY |Secret key for encrypting password and etc secure value|  - |
|SQL_ENGINE |Configuration str, what db do you use| `django.db.backends.sqlite3` |
|SQL_DATABASE |Name of your db | `sqlite3.db` |
|SQL_USER |Name of db user | user
|SQL_PASSWORD |DB password | password |
|SQL_HOST | DB host | localhost |
|SQL_PORT | DB port | 5432 |
|ALLOWED_HOSTS | DB port | 5432 |

```
5) python manage.py migrate 
6) python manage.py runserver 
```

## Deployment

You can deploy project. Project is already dockerized.
All you have to do is add a few more envs. There are 3 services in compose: `django`, `db`, `nginx`. 
`db` service based on PostgreSQL image for database setup.

Add Env Variables.

|    NAME   |                      DESCRIPTION                      |DEFAULT VALUE|
|-----------|-------------------------------------------------------|-------------|
|DATABASE |Set value 'postgres'. This config for entrypoint.sh | - |
|POSTGRES_DB |Name of your db | - |
|POSTGRES_USER |Name of db user | - |
|POSTGRES_PASSWORD |DB password | - |
|POSTGRES_HOST | DB host | - |
|POSTGRES_PORT | DB port | - |

Before run next commands, make sure, that you have `docker` and `docker-compose` installed.
```
1) docker-compose -f dev.yml build
2) docker-compose -f dev.yml up
```
## Versioning.

Using [SemVer](http://semver.org/) for versioning. 

## Authors

* **Almaz Yusupov** - [Almaz97](https://github.com/Almaz97)


## Acknowledgments

* Category model was built with [django-mptt](https://django-mptt.readthedocs.io/en/latest/) lib, which implements "Modified Preorder Tree Traversal" idea.
  If you want to go into the details, there’s a good explanation here: ["Storing Hierarchical Data in a Database"](https://www.sitepoint.com/hierarchical-data-database/)
