#!/usr/bin/env python3

import os, pydicom
import numpy as np
import matplotlib.pyplot as plt

def load_dicom(path):
    slices = [pydicom.dcmread(path + s) for s in sorted(os.listdir(path))]
    return slices

def pixel_hu(data):
    image = np.stack([slice.pixel_array for slice in data])
    image = image.astype(np.int16)

    intercept = data[0].RescaleIntercept
    slope = data[0].RescaleSlope

    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)

    image += np.int16(intercept)
    return np.array(image, dtype=np.int16)


DATA = '/Volumes/artemis/library/datasets/dicom/ANGIO_CT_9712/dicom/'

index = 1

dicom = load_dicom(DATA)
print(dicom[index])

pixels = pixel_hu(dicom)[index]
print(pixels)

plt.imshow(pixels, cmap=plt.cm.bone)
plt.colorbar()
plt.show()