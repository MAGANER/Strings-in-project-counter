import os
import io

str_number = 0
_files = []
path = input("введите путь к директории:")

os.chdir(path)
files = os.listdir(path=".")

def count_str_number(file):
    d= 0
    for f in file:
        d = d+1
        print(f)
    return d



i = 0
while i < len(files):
    _files.append(files[i])
    i = i+ 1
i = 0

while i < len(_files):
    _files[i] = path+"/"+_files[i]
    i = i + 1
i = 0

while i < len(_files):
    _file_ = io.open(_files[i], 'r')
    sn = count_str_number(_file_)
    str_number = sn+str_number
    i = i +1


print(str_number)