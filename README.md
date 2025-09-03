# Text To Speech Server Node
![license](https://img.shields.io/github/license/grebtsew/Text_To_Speech_Server_Node)
![size](https://img.shields.io/github/repo-size/grebtsew/Text_To_Speech_Server_Node)
![commit](https://img.shields.io/github/last-commit/grebtsew/Text_To_Speech_Server_Node)

 A super simple speaking server node using `gTTS` that receives `POST JSON` requests and reads them through the speakers. A python application running on Docker.

# Install local
Installing on your local machine.

1.Make sure python3 is installed on your device. 

2.Download or clone this repo.

3.Install required packages:
```bash
pip3 install -r requirements.txt
```
If you want this program to autostart on Ubuntu 22.04 you could add it by:
```bash
# Type
crontab -e
# Add in bottom of file
@reboot path/to/repo/main.py
```
On windows, things should run without extra installs, but on Linux, try running if it doesn't start:
```bash
# Make script runnable
chmod +x ./setup/ubuntu.sh
# Start setup script
./setup/ubuntu.sh
```


# Install with Docker
This will only work on Linux. Another container has to be built for windows.
For now I would recommend just running the python code on your device by installing
the requirements and run implementation.
```bash
# One liner (make sure to add sound device!)
docker-compose up # Will create a tts-api-server

# Or

# Build image
docker build . --tag=speak:1.0

# Run image
docker run -it --device /dev/snd --net=host speak:1.0 bash
```

# Run implementation

Run `./src/main.py` to start implementation.

Change ports and address in `./src/server.py`.


# Example data to send
See test_client.py. For more detailed information of the json format used, checkout the `template/template.json` file!
```
data = {
        'api_rate':150, # set speed of voice
        'api_volume':0.7, # set volume
        'api_text':"TEXT_TO_READ", # actual text
        'api_voice': english ,# set voice id
        'api_tune': False, # link to audio to play
        'password': "password-1" # password REQUIRED
        } 
```

# Release Notes

The current release is version `0.0.2` see more at [RELEASE_NOTES](./RELEASE_NOTES.txt).

# Logging

Server logs are stored in local `.log` file.

# Testing

[![Build Docker Container](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/build_docker.yml/badge.svg)](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/build_docker.yml)
[![Check Python Format](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_format.yml/badge.svg)](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_format.yml)
[![Pylint Check](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_lint.yml/badge.svg)](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_lint.yml)
[![Python Test and Coverage](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_coverage.yml/badge.svg)](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_coverage.yml)
[![Run Pytest](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_unit_test.yml/badge.svg)](https://github.com/grebtsew/Text_To_Speech_Server_Node/actions/workflows/py_unit_test.yml)

This repository does not contain mandatory ci/cd pipelien that must pass in order for merge requests to pass. For manual testing see `./tests/manual/*`.

# License

This repository is created using [MIT LICENSE](./LICENSE)


# Issues

Let me know if there are any questions or issues.

@ Grebtsew 2024
