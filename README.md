# Fast API - Backend

This project contains a uvicorn server having few important and intresting APIs.

### Running the project

#### Using Docker

1. Build the docker image

```shell
docker build . -t fastapi-backend
```

2. Run the image. Pass your environment variables via the `.env` file

```shell
docker run --rm -p 8000:8000 --env-file .env fastapi-backend
```

#### Local Machine

1. Optional. Create a virtual environment

```shell
# To activate the environment
python -m venv venv
source venv/bin/activate
```

```shell
# To deactivate the environment
deactivate
```

2. Run the server

```shell
uvicorn main:app --reload
```