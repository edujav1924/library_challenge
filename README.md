## Library APP

A simple book management application.

## Features

- Add, edit, and delete books
- Search and filter books
- Add, edit and delete authors
- Search and filter authors

## Installation

```bash
git clone https://github.com/edujav1924/library.git

cd library

# Follow project-specific setup instructions
```

## Usage PROD

Run the application in containers with:

```
./deployer
```
For testing purposes .env files are showed in this repo, for real project must be ignore from git.

For use Django admin the credentials are:
- **User:** `admin`
- **Password:** `admin`


## DJANGO DRF

The endpoints are:
 - ${ip}:{$APP_PORT}/api/book - GET
 - ${ip}:{$APP_PORT}/api/book/<id> - GET | PUT | DELETE
 - ${ip}:{$APP_PORT}/api/author - GET
 - ${ip}:{$APP_PORT}/api/author/<id> - GET | PUT | DELETE
 
 Note: $APP_PORT is declared in .env file.
## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.