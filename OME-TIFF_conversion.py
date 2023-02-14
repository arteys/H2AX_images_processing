from pyometiff import OMETIFFReader
import numpy as np
import cv2

path = "C:/Users/Modern/Desktop/Kirill/B8/B8/B8_IX_Red_T0_Z0.ome.tif"
save_path = "C:/Users/Modern/Desktop/Kirill/B8/B8/Images/"

reader = OMETIFFReader(fpath=path)
img_array, metadata, xml_metadata = reader.read()

n=0

for i in img_array:
    number = str(f'{n:03}')
    name = save_path + number + "_B8_IX_Red_T0_Z0.tiff"
    cv2.imwrite(name,i)
    n = n+1
    print(number)



