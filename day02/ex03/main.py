from csvreader import CsvReader


# if __name__ == "__main__":
#     with CsvReader('good.csv', header=True) as file:
#         # data = file.getdata()
#         header = file.getheader()
#         print(header)


if __name__ == "__main__":
    with CsvReader('bad2.csv') as file:
        if file == None:
            print("File is corrupted")