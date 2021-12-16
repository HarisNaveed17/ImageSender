import grpc
import image_sender_pb2
import image_sender_pb2_grpc
import numpy as np
import base64
import os


MAX_MESSAGE_LENGTH = 104857600
# if os.environ.get('https_proxy'):
#     del os.environ['https_proxy']
# if os.environ.get('http_proxy'):
#     del os.environ['http_proxy']


def run():

    # with grpc.insecure_channel('127.0.0.1:5005', options=(('grpc.enable_http_proxy', 0),)) as channel:
    channel = grpc.insecure_channel('localhost:5005', options=[('grpc.enable_http_proxy', 0),
                                                               ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), ],)
    stub = image_sender_pb2_grpc.ImageSenderStub(channel)

    for _ in range(10):
        frame = np.random.randint(0, 255, (5, 720, 1280, 3), dtype=np.uint8)
        h = frame.shape[0]
        w = frame.shape[1]
        data = base64.b64encode(frame)
        image_req = image_sender_pb2.Image(image=data, height=h, width=w)
        response = stub.Send(image_req)
        print(response)
    channel.close()


if __name__ == '__main__':
    run()
