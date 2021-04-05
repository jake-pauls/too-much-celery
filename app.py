import os
from os.path import join, dirname
from flask import Flask
from celery import Celery
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

# Flask App
app = Flask(__name__)

# Configure Celery Worker
app.config['CELERY_BROKER_URL'] = os.environ.get("WORKER_URL")
app.config['CELERY_RESULT_BACKEND'] = os.environ.get("WORKER_URL")

# Init Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


# Flask Routes
@app.route('/', methods=['GET'])
def ping():
    return { "ping": "pong" }

@app.route('/celery', methods=['GET'])
def test():
    """
    @celery.task.delay() - shortcut for simple worker tasks
    @celery.task.apply_async() - default, supports broader execution options (such as linking tasks, error callbacks, etc.)
    """
    task = add.apply_async((4,4), expires=60)
    return { "message": "Hello from Celery!" }

# Celery Worker Tasks
@celery.task
def add(x, y):
    val = x + y
    print('add: {0} + {1} = {2}'.format(x,y, val))
    return val

if __name__ == '__main__':
    app.run(port=5000, debug=True)