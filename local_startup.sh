#!/bin/bash
# Note: Will extract a local instance of redis to run/build locally

# Check venv
if [ ! -d venv ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

# Download redis
if [ ! -d redis-stable/src ]; then
    curl -O http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    rm redis-stable.tar.gz
fi

# Make redis instance, will default to redis://localhost:6379
cd redis-stable
make
src/redis-server