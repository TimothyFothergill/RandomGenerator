FROM python
COPY RandomGenerator.py /
CMD chmod +x ./RandomGenerator.py
CMD ./RandomGenerator.py
RUN apt-get update && apt-get install -y python-pip
RUN pip3 install spotipy --upgrade
