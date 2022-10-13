# sleep 20s
nohup jupyter-lab --no-browser --ip=0.0.0.0 --port=8900 --NotebookApp.password="" --allow-root --NotebookApp.token='' &> /dev/null &
cron
echo "55 23 * * * python3 /app/populate_db_aws_or_container.py  >> /app/load-db.log" | crontab 
python3 config.py
# tail -f /dev/null
