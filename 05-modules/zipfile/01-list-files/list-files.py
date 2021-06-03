from zipfile import ZipFile
import sys

filename = sys.argv[1]
with ZipFile (filename) as zip_file:
    for elem in zip_file.namelist():
        print(elem)
