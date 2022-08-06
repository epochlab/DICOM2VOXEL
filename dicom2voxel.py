#!/usr/bin/env python3

import os
import pydicom
import numpy as np
import matplotlib.pyplot as plt

def load_dicom(path):
    slices = [pydicom.dcmread(path + s) for s in sorted(os.listdir(path))]
    slice_thickness = slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2]
    return slices, slice_thickness

def pixel_hu(data):
    image = np.stack([slice.pixel_array for slice in data])
    image = image.astype(np.int16)

    intercept = data[0].RescaleIntercept
    slope = data[0].RescaleSlope

    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)

    image += np.int16(intercept)
    return inp.array(image, dtype=np.int16)

def largest_label_volume(im, bg=-1)
    vals, counts = np.unique(im, return_counts=True)
    
    counts = counts[vals != bg]
    vals = vals[vals != bg]

    if len(counts) > 0:
        return vals[np.argmax(counts)]
    else:
        return None

DATA = '/Volumes/artemis/library/datasets/dicom/ANGIO_CT_9712/dicom/'

index = 1
dicom, depth = load_dicom(DATA)
pixels = pixel_hu(dicom)



# density_min = np.amin(dicom[index].pixel_array)
# densiry_max = np.amax(dicom[index].pixel_array)

# print(dicom[index])
# print(dicom[index].pixel_array)

# plt.imshow(pixels[0], cmap=plt.cm.bone)
# plt.colorbar()
# plt.show()