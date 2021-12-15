import grpc
import image_sender_pb2
import image_sender_pb2_grpc
import numpy as np
import base64


def run():

    # with grpc.insecure_channel('127.0.0.1:5005', options=(('grpc.enable_http_proxy', 0),)) as channel:
    channel = grpc.insecure_channel('127.0.0.1:5005',options=(('grpc.enable_http_proxy', 0),))
    stub = image_sender_pb2_grpc.ImageSenderStub(channel)

    for _ in range(1000):
        frame = np.random.randint(0, 255, (720, 1280, 3), dtype=np.uint8)
        h = frame.shape[0]
        w = frame.shape[1]
        data = base64.b64encode(frame)
        image_req = image_sender_pb2.Image(image=data, height=h, width=w)
        response = stub.Send(image_req)
        print(response)
        
    channel.close()
    
 


if __name__ == '__main__':
    run()
