# -*- coding: UTF-8 -*-
import os
def append_name(path, name):
    for file in os.listdir(path):
        if os.path.isdir(path + "/" + file):
            append_name(file, name)
        else:
            file_name = file.split(".")[0]
            extension = file.split(".")[1]
            if (name in file_name) == False:
                new_file_name = path + "/" + file_name + name + "." + extension
                os.rename(path + "/" + file, new_file_name)
                print(new_file_name)


if __name__ == "__main__":
    append_name("/Users/jichonggula/Downloads/newUser","_v2")

