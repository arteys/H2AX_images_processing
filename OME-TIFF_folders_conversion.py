from pyometiff import OMETIFFReader
import numpy as np
import cv2
import os
import re
import tkinter.filedialog as fd

def ome_to_tiff(file_path,save_path,file_name):

    well_name = re.search(r'([B-G]\d{1,2})',file_name)

    # print(well_name)

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
        name = save_path + well_type + number + "_" + str(well_name[0]) + ".tiff"
        cv2.imwrite(name,i)
        n = n+1
        # print(number)



# path_dir = os.path.join("C:","Users","Modern","Desktop","Kirill","Images")
# save_path = os.path.join("C:","Users","Modern","Desktop","Kirill","TIFF")

path_dir = "C:/Users/Modern/Desktop/Kirill/Images"
save_path = "C:/Users/Modern/Desktop/Kirill/TIFF//"

# path_dir = fd.askdirectory()

for address, dirs, files in os.walk(path_dir):
    for file in files:
        if ".ome.tif" in str(file):
            path = os.path.join(address, file)
            correct_path = path.replace("\\","/")
            ome_to_tiff(correct_path,save_path,file)
            # print(correct_path)