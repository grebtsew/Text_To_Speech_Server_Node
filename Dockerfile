FROM ubuntu:22.04

LABEL maintainer="@ Grebtsew 2024"

WORKDIR /home/app/

# Copy all files!
RUN mkdir -p /home/app/

# Web HTTP(s) & Socket Site-to-Site Ports
EXPOSE 8000

# Install needed programs
RUN apt-get update && \
	  apt-get install -y \
		curl \
    nano \
    alsa-utils \
    libespeak1 \
    python3-pip \
    python3-dev  && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# Install python packages
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt 

# Copy project
COPY . /home/app/

CMD [ "python3", "/home/app/main.py" ]
