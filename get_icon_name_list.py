import os


def find_filenames():
    img_folder_path = os.path.abspath('img')
    # print(img_folder_path)

    for root, dirs, files in os.walk(img_folder_path):
        # print('root:',root)    # type: # str
        # print('dirs:',dirs)    # type: list
        # print('files:',files)    # type: list
        return files    # return a filename list