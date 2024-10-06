### Change the port appropriately
### we force close all usage of port 8100. Note that this will only work in a Unix environment (Linux, MacOS)
lsof -ti :8100 | xargs --no-run-if-empty kill -9
### Also, Gunicorn a=only works in a Unix environment. On windows, use uvicorn with or without the ssl
gunicorn app.main:app --bind 0.0.0.0:8100 -w 1 -k uvicorn.workers.UvicornWorker --reload --timeout 600
### If there's a cert file for https, the below can be used.
# uvicorn app.main:app --host 127.0.0.1 --port 8100 --reload --ssl-keyfile=/some/path/to/cert-key.pem --ssl-certfile=/some/path/to/cert.pem