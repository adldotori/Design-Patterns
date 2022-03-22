from datasource import FileDataSource, CompressionDecorator, EncryptionDecorator

if __name__ == "__main__":
    data_source = FileDataSource("data.txt")
    data_source = CompressionDecorator(data_source)
    data_source = EncryptionDecorator(data_source)

    data_source.write_data("Hello World")
    print(data_source.read_data())
