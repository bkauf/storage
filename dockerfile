FROM ubuntu:latest

# Create app directory
RUN mkdir -p /var/www/html

#change working DIR
WORKDIR /var/www/html

# restart server on file change for dev
#RUN npm install -g nodemon

# Copy app files
COPY storage-traffic.py /var/www/html
# Install app dependencies
RUN apt update -y && apt install vim -y && apt install python3 -y
