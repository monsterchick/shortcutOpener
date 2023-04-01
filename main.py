import os
from get_icon_name_list import find_filenames as files
from actions import find_icon


for file in files():
    image_path = os.path.join(os.path.abspath('img'), file)
    print(image_path)
    find_icon(image_path)

