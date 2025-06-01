<!-- filepath: /app/README.md -->
## Library APP

A simple book management application.

## Features

- Add, edit, and delete books
- Search and filter books
- Add, edit, and delete authors
- Search and filter authors

## Installation (PROD)

```bash
git clone https://github.com/edujav1924/library.git

cd library

./deployer
```

For testing purposes, .env files are visible in this repository, but in a real project they should be ignored by git.

To use the Django admin panel, the credentials are:

- **User:** `admin`
- **Password:** `admin`

## DJANGO DRF

The endpoints are:

- http://localhost:5000/api/book - GET
- http://localhost:5000/api/book/<id> - GET | PUT | PATCH | DELETE
- http://localhost:5000/api/author - GET
- http://localhost:5000/api/author/<id> - GET | PUT | PATCH | DELETE

Note: $APP_EXTERNAL_PORT=5000 is declared in the .env file. If you need to change the port, modify it in `prod/.env` and run the application again.

## DOCUMENTATION
- http://localhost:5000/api/swagger
- http://localhost:5000/api/redoc

## TESTS

If you want to run the tests, you must execute the following command:

```
cd prod
docker compose exec app python manage.py test

```