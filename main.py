# PSMA-Hornet main function for Raiven

#%% IMPORTS
# ===========

# Deployment env
import os

import numpy as np
import glob
import matplotlib.pyplot as plt
import markdown
import shutil

import hornetlib as hlb
import tensorflow as tf

#%% Input data folder

INPUT_DIR = 'path_to_input_data'
# The folder specified as INPUT_DIR should have two sub-folders.
# Subfolder 1 should contain PET series (.dcm), and subfolder 2 should contain CT series (.dcm).
# The names of the subfolders can be custom.
# ===========

#%% Get the list of dicom files in the directory

if __name__ == "__main__":
    #plt.ioff() # disable interactive mode to prevent plottingg

    # Determine PET and CT directories in the impot
    modality_dirs = hlb.list_of_modality_dirs(INPUT_DIR)

    slices_pt = hlb.read_slices_from_dir(modality_dirs['PT'])
    slices_ct = hlb.read_slices_from_dir(modality_dirs['CT'])

    print(modality_dirs)
    # this is to check that the PET and CT folders have been determined correctly

    # get reference header for metadata
    ref_dcm_pt = slices_pt[0]
    ref_dcm_ct = slices_ct[0]

    # build volume image, apply correct scaling
    img3d_pt = hlb.volume_from_slices_with_scaling(slices_pt, True)
    img3d_ct = hlb.volume_from_slices_with_scaling(slices_ct, False)

    print('Created volumes')

    img3d_pt = np.flip(img3d_pt,axis=2)
    img3d_ct = np.flip(img3d_ct,axis=2)
    # convert to SUV units
    img3d_pt = hlb.convert_activity_to_suv(img3d_pt,ref_dcm_pt)

    # convert images to model space
    img3d_pt, img3d_ct = hlb.orig_to_model_space(img3d_pt, img3d_ct, ref_dcm_pt, ref_dcm_ct)

    print('Transformed images to model space')

    # preprocess images
    img3d_pt_proc = hlb.preprocess_input_pt(img3d_pt)
    img3d_ct_proc = hlb.preprocess_input_ct(img3d_ct)
    
    # inititate the model
    model_name = 'unet2D_inputfusion_vlarge_singleoutput'
    modelWeightsFile = 'hornet_model.h5'
    model = hlb.initialize_model(model_name, modelWeightsFile)

    print('Model initialized.')
    print('Running inference...')
    # run model inference
    predicted_image = hlb.makeModelPredictions_multislice(model, img3d_ct_proc, img3d_pt_proc)

    # convert to integer classes
    predicted_image_max = np.max(predicted_image,axis=3)
    background_mask = predicted_image_max < 0.99
    predicted_image_lab = tf.argmax(predicted_image[:,:,:,:], axis=3).numpy()
    predicted_image_lab[background_mask] = 0
    print('Model inference successful.')
