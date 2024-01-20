#Deriving the latest base image
FROM python:latest

RUN pip install --no-cache-dir -U discord lxml requests bs4

#Labels as key value pair
LABEL Maintainer="bcshelto565"


# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /home/admin-shelton/docker-stuff/ARB-docker

#to COPY the remote file at working directory in container
COPY ARB.py ./
# Now the structure looks like this '/home/admin-shelton/docker-stuff/ARB-docker/ARB.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./ARB.py"]
