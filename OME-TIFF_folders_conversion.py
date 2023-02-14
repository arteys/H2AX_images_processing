from pyometiff import OMETIFFReader
import numpy as np
import cv2
import os
import re

def ome_to_tiff(file_path,save_path):

    well_name = re.search(r'([B-G]\d{1,2})',str)

    if "Blue" in file_path:
        well_type = "_Blue_"
    if "Red"  in file_path:
        well_type = "_Red_"
    if "Trans" in file_path:
        well_type = "_Trans_"

    reader = OMETIFFReader(fpath=file_path)
    img_array, metadata, xml_metadata = reader.read()

    n=0
    for i in img_array:
        number = str(f'{n:03}')
        name = save_path + well_type + number + str(well_name[0])
        cv2.imwrite(name,i)
        n = n+1
        print(number)



path_dir = os.path.join("C:","Users","Modern","Desktop","Kirill","Images")
save_path = os.path.join("C:","Users","Modern","Desktop","Kirill","TIFF")

for address, dirs, files in os.walk(path_dir):
    for file in files:
        if ".ome.tif" in str(file):
            path = os.path.join(address, file)
            # ome_to_tiff(path,save_path)
            print(path)