# too-much-celery
Testing the capabilities of Celery for high load asynchronous operations (ex: performing operations on cloud-sourced multimedia) using Flask and Redis.

## Docker (recommended)
Run the compose to start the Flask app, Redis, and Celery worker.
```
docker-compose up -d
```

## Local dev
To download all the dependencies locally in the quickest fashion, run this adapted startup script that copies/makes a local redis instance and activates a virtual environment.
```
./local_startup.sh
```