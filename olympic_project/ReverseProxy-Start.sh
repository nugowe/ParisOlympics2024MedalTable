#!/bin/bash
set -x

cd /opt

echo "STARTING THE GUNICORN WSGI WEBSERVER...."
/usr/bin/gunicorn -w 4 --bind unix:/opt/gunicorn.sock olympic_project.wsgi

