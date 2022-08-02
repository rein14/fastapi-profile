## How To Use Docker To Make Local Development A Breeze

This API Shows you you could use Docker easily with FastAPI

Video: https://youtu.be/zkMRWDQV4Tg.

## Usage

```
pip install -r requirements.txt
```

This is how you run the code locally (without Docker):

```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

Build and run the Docker image locally, as follows:

```
docker build -t channel-api .
docker run -d -p 8080:80 channel-api
```

In order to run the example server with docker compose, use this:

```
docker-compose up --build
```
