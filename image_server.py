import grpc
import image_sender_pb2
import image_sender_pb2_grpc
import numpy as np
import base64
from concurrent import futures
import logging

MAX_MESSAGE_LENGTH = 104857600


def save_image(encoded_img, w, h):
    decoded_img = base64.b64decode(encoded_img)
    imgarr = np.frombuffer(decoded_img, dtype=np.uint8).reshape(w, h, -1)
    np.save('send_file.npy', imgarr)
    return 'File sent and saved.'


class ImageSenderServicer(image_sender_pb2_grpc.ImageSenderServicer):
    def Send(self, request, context):
        response = image_sender_pb2.Response()
        response.ack = save_image(
            request.image, request.width, request.height)
        return response


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=12), options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH), ],)
    image_sender_pb2_grpc.add_ImageSenderServicer_to_server(
        ImageSenderServicer(), server)
    print('Starting server. Listening on port 5005.')
    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    server()
