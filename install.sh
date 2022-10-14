# sleep 20s
nohup jupyter-lab --no-browser --ip=0.0.0.0 --port=8900 --NotebookApp.password="" --allow-root --NotebookApp.token='' &> /dev/null &
cron
echo "22 3 * * * python3 -u /app/populate_db_aws_or_container.py >> /app/load-db.log 2>&1 " | crontab 
# echo "* * * * * echo helloRad >> /app/load-db.log 2>&1 " | crontab 
python3 config.py
# tail -f /dev/null
