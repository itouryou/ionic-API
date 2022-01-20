#!/bin/sh
cd src
gunicorn --access-logfile - --error-logfile - --log-level DEBUG  --keep-alive=20 --timeout 4000 --bind :80 app:app --max-requests 100 --max-requests-jitter 20 --workers 2 --threads 1 --worker-class uvicorn.workers.UvicornWorker