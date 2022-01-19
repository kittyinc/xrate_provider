#!/bin/bash
pip install -r requirements.txt
python xrate_provider/manage.py collectstatic --noinput 
python xrate_provider/manage.py migrate
echo "Post deploy done, restarting..."