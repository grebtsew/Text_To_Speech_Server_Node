FROM ubuntu:18.04

# Copy all files!
RUN mkdir -p /home/SpeechNode/
COPY . /home/SpeechNode/

# Web HTTP(s) & Socket Site-to-Site Ports
EXPOSE 8000

# Install needed programs
RUN apt-get update && \
	  apt-get install -y \
		curl \
    nano \
    libespeak1 \
    python3-pip \
    python3-dev  && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*


# Install python packages
RUN pip3 install -r /home/SpeechNode/requirements.txt --no-cache-dir

WORKDIR /home/SpeechNode/
CMD [ "python3", "/home/SpeechNode/main.py" ]
