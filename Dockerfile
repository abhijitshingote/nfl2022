FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 python3-pip

COPY ./requirements.txt /requirements.txt
# COPY ./install.sh /install.sh


RUN pip3 install -r /requirements.txt

WORKDIR /app
# RUN nohup jupyter-lab --no-browser --ip=0.0.0.0 --port=8900 --NotebookApp.password="" --allow-root --NotebookApp.token='' &> /dev/null &

# RUN echo "hello Radhika" > hellorad.txt
# COPY . /app
CMD ["/bin/bash","/app/install.sh"]

# ENTRYPOINT [ "python3" ]

# CMD [ "app.py" ]

 # CMD ["bash"]

 # CMD ["tail", "-f" ,"/dev/null"]  