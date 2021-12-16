# ImageSending service Implemented in gRPC
## Brief explanation

This service implements a client, server architecture to send an image from a client system to a server system. The server downloads the image and returns an acknowledgement. 
 
### Proto file:

The .proto file specifies the services implemented and the message types they exchange.

### image_client.py

The client file sends a batch of images (numpy arrays for now) via a Stub. The Stub can access all the methods implemented in the .proto file. The channel over which the client and server communicate is also configured here.

### image_server.py
Implements procedures defined in the .proto file, also activates the server.

## Usage

You need to have the packages installed in requirements.txt. This can be via conda:


```
conda create -n grpc python=3.8
conda activate grpc
conda install numpy
python -m pip install grpcio
python -m pip install grpcio-tools

```

or using virtualenv:

```
python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
python -m pip install grpcio
python -m pip install grpcio-tools

```

After this, all you need to do is run image_server.py in one terminal and run image_client.py in another. The last simulated numpy image will be stored in the current directory. To change the size or number of images send you can modify the image_client.py file. 

