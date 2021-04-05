import os
from os.path import join, dirname
from flask import Flask
from celery import Celery
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

# Flask App
app = Flask(__name__)

# Configure Celery Worker
redis = os.environ.get("WORKER_URL")
app.config['CELERY_BROKER_URL'] = redis

# Init Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.result_backend = redis
celery.conf.update(app.config)

# Flask Routes
@app.route('/', methods=['GET'])
def ping():
    return { "ping": "pong" }, 200

@app.route('/celery', methods=['GET'])
def test():
    """
    Test endpoint to access worker
    @celery.task.delay() - shortcut for simple worker tasks
    @celery.task.apply_async() - default, supports broader execution options (such as linking tasks, error callbacks, etc.)
    """
    task = add.apply_async((4,4), expires=60)
    return { "task":"add", "result":task.result, "status":task.status }, 200

# Celery Worker Tasks
@celery.task()
def add(x, y):
    """
    Test worker task
    In progress results are posted to client, once finished, the worker posts task result to console
    """
    result = x + y
    return { "result":result, "status": "Task completed succesfully!" }

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")