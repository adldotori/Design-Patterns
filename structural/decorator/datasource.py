from abc import ABC, abstractmethod
from typing import List

import base64
from Crypto.Cipher import AES
import zlib


class DataSource(ABC):
    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data: str):
        with open(self.filename, "w") as f:
            f.write(data)

    def read_data(self) -> str:
        with open(self.filename, "r") as f:
            return f.read()


class DataSourceDecorator(DataSource):
    def __init__(self, data_source):
        self.data_source = data_source

    def write_data(self, data: str):
        self.data_source.write_data(data)

    def read_data(self) -> str:
        return self.data_source.read_data()


class EncryptionDecorator(DataSourceDecorator):
    secret_key = b"1234567890123456"

    def write_data(self, data: str):
        self.write_cipher = AES.new(self.secret_key, AES.MODE_EAX)
        super().write_data(
            base64.b64encode(self.write_cipher.encrypt(data.encode())).decode()
        )

    def read_data(self) -> str:
        cipher = AES.new(self.secret_key, AES.MODE_EAX, self.write_cipher.nonce)
        return cipher.decrypt(base64.b64decode(super().read_data())).decode()


class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data: str):
        super().write_data(base64.b64encode(zlib.compress(data.encode())).decode())

    def read_data(self) -> str:
        return zlib.decompress(
            base64.b64decode(bytes(super().read_data().encode()))
        ).decode()
