# encoding: utf-8
# Revisión 2019 (a Python 3 y base64): Pablo Ventura
# Copyright 2014 Carlos Bederián
# $Id: connection.py 455 2011-05-01 00:32:09Z carlos $

import socket
from constants import *
from base64 import b64encode
import os

class Connection(object):
    """
    Conexión punto a punto entre el servidor y un cliente.
    Se encarga de satisfacer los pedidos del cliente hasta
    que termina la conexión.
    """

    def __init__(self, socket, directory):
        # FALTA: Inicializar atributos de Connection
        self.socket = socket
        self.directory = directory

    def handle(self):
        """
        Atiende eventos de la conexión hasta que termina.
        """
        
        server = self.socket
    
        CHUNKSIZE = 10000000

        data = server.recv(4096).decode("ascii").strip()

        msg = str(CODE_OK).encode() + b' OK\r\n'

        if data == 'get_file_listing':
        
            for path,dirs,files in os.walk(self.directory):
                for file in files:
                    filename = os.path.join(path,file)
                    relpath = os.path.relpath(filename, self.directory)

                    with open(filename,'rb') as f:
                        if data == 'get_file_listing':
                            msg += relpath.encode() + b'\r\n'

            server.send(msg + b'\r\n')

        elif "get_metadata" in data:

            data = data.split(" ")
            try:
                filesize = os.path.getsize("files/" + data[1])
                server.send(msg + str(filesize).encode() + b'\r\n')
            except:
                server.send(str(FILE_NOT_FOUND).encode() + b'\r\n')

        elif "get_slice" in data:

            data = data.split(" ")

            filename = "files/" + data[1]
            offset = data[2]
            size = data[3]

            with open(filename, "r") as file:
                # file.seek(offset)
                # slice_ = file.read(size)
                slice_ = file.read()

                slice_ = slice_[int(offset):int(size)].encode()

                slice_ = b64encode(slice_)

                server.send(msg + slice_ + b'\r\n')

        elif "quit" == data:

            server.send(msg)

            server.close()

            return 1

        return 0