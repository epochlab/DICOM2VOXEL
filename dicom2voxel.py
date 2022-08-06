#!/usr/bin/env python3

import os
import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt

def load_dicom(x):
    return dicom.dcmread(DATA + x)

DATA = 'path_to_directory'
dicom_files = [f for f in sorted(os.listdir(DATA)) if not f.startswith('.')]

index = 1
DICOM = load_dicom(dicom_files[index])

print('Min. density value:', np.amin(DICOM.pixel_array))
print('Max. density value:', np.amax(DICOM.pixel_array))
print(DICOM)

plt.imshow(DICOM.pixel_array)
plt.colorbar()
plt.show()
