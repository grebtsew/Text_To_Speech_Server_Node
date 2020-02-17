# Text To Speech Server Node
 A speaking server node that recieves requests to speak. A python application run on Docker.


# Install with Docker
This will only work on Linux. Another container has to be built for windows.
For now I would recommend just running the python code on your device by installing
the requirements and run implementation.
'''

# Build image
docker build . --tag=speak:1.0

# Run image
docker run -it --device /dev/snd --net=host speak:1.0 bash
'''

# Run implementation

Run main.py to start implementation.

Change ports and address in server.py.

# License
See !(LICENSE)[LICENSE]!
