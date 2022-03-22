import pytest
from datasource import FileDataSource, CompressionDecorator, EncryptionDecorator


def test_comp_encryp():
    data_source = FileDataSource("data.txt")
    data_source = CompressionDecorator(data_source)
    data_source = EncryptionDecorator(data_source)

    data_source.write_data("Hello World")
    assert data_source.read_data() == "Hello World"


def test_comp():
    data_source = FileDataSource("data.txt")
    data_source = CompressionDecorator(data_source)

    data_source.write_data("Hello World")
    assert data_source.read_data() == "Hello World"


def test_encrypt():
    data_source = FileDataSource("data.txt")
    data_source = EncryptionDecorator(data_source)

    data_source.write_data("Hello World")
    assert data_source.read_data() == "Hello World"


def test_basic():
    data_source = FileDataSource("data.txt")

    data_source.write_data("Hello World")
    assert data_source.read_data() == "Hello World"
