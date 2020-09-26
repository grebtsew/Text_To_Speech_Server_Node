# Text To Speech Server Node
![license](https://img.shields.io/github/license/grebtsew/Text_To_Speech_Server_Node)
![size](https://img.shields.io/github/repo-size/grebtsew/Text_To_Speech_Server_Node)
![commit](https://img.shields.io/github/last-commit/grebtsew/Text_To_Speech_Server_Node)

 A speaking server node that receives POST JSON requests and reads them through speakers. A python application run on Docker.

# Install local
Make sure python3 is installed on your device. 
Download or clone this repo.
Install required packages:
```
pip3 install -r requirements.txt
```
If you want this program to autostart on Ubuntu 18.04 you could add it by:
```
# Type
crontab -e
# Add in bottom of file
@reboot path/to/repo/main.py
```


# Install with Docker
This will only work on Linux. Another container has to be built for windows.
For now I would recommend just running the python code on your device by installing
the requirements and run implementation.
```
# One liner (make sure to add sound device!)
docker-compose up

# Build image
docker build . --tag=speak:1.0

# Run image
docker run -it --device /dev/snd --net=host speak:1.0 bash
```

# Run implementation

Run main.py to start implementation.

Change ports and address in server.py.


# Example data to send
See test_client.py
```
data = {
        'api_rate':150, # set speed of voice
        'api_volume':0.7, # set volume
        'api_text':"TEXT_TO_READ", # actual text REQUIRED
        'api_crypt':CRYPT # crypt key REQUIRED
        } 
```
