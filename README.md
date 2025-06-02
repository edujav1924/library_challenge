<!-- filepath: /app/README.md -->
## Library APP

A simple book management application.

## Features

- Add, edit, and delete books
- Search and filter books
- Add, edit, and delete authors
- Search and filter authors
- Add, edit, update, and delete authors via nested book URLs, e.g., `/api/books/1/authors`
- Add, edit, update, and delete books via nested author URLs, e.g., `/api/authors/1/books`

## Installation (PROD)

```bash
git clone git@github.com:edujav1924/library_challenge.git
cd library_challenge
./deployer deploy  # to run services
```
If you need to stop the containers, run:
```bash
./deployer stop
```
> **Note:** The application runs on `PORT=5000`. If you need to change the port, update the value of `APP_EXTERNAL_PORT` in `prod/.env` and restart the application.

For testing purposes, .env files are visible in this repository, but in a real project they should be ignored by git.

To use the Django admin panel, the credentials are:

- **User:** `admin`
- **Password:** `admin`

- **admin site** `http://localhost:5000/admin`
- **api endpoints** `http://localhost:5000/api/*`

## DJANGO DRF

For API usage, please refer to the Swagger documentation available at:

```
- http://localhost:5000/api/swagger
- http://localhost:5000/api/redoc
```

## TESTS

If you want to run the tests, you must execute the following command:

```
cd prod
docker compose exec app python manage.py test

```