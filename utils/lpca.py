import numpy as np
from dipy.core.gradients import gradient_table
from dipy.denoise.localpca import localpca
from dipy.io.image import load_nifti, save_nifti
import os

def run_lpca(DWI, tau=3, patch_radius=(2,2,2)):
    data, affine = load_nifti(DWI)
    bvecs = np.loadtxt("./utils/45.txt")[:, :-1].astype(np.float32)
    bvals = np.loadtxt("./utils/45.txt")[:, -1].astype(np.float32)
    gtab = gradient_table(bvals, bvecs=bvecs)
    print("Performing LPCA...")
    x = localpca(data, gtab=gtab, tau_factor=tau, patch_radius=patch_radius)
    save_nifti("./DWI-lpca.nii", x, affine=affine)
    return "./DWI-lpca.nii"


