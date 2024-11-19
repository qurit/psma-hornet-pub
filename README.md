# PSMA-Hornet: Fully-automated, multi-target segmentation of healthy organs in PSMA PET/CT images

<p align="left">
    <img alt="PyPI - License" src="https://img.shields.io/badge/license-MIT-blue" height="18" />
</p>

This repository contains an AI model and accompanying Python scripts for fully-automated simultaneous segmentation of 14 healthy organs with high tracer uptake onPET/CT images. The imaging tracer used in model development was [18F]DCFPyL.

Required model inputs:
(a) DICOM PET series acquired with a PSMA tracer (tracers other than [18F]DCFPyL may work); (b) DICOM CT series
The PET and CT inputs must be co-registered.
   
For details regarding model architecture, training methodology, and testing results please refer to the following publication:
Klyuzhin IS, Chaussé G, Bloise I, et al. PSMA-Hornet: Fully-automated, multi-target segmentation of healthy organs in PSMA PET/CT images. Med Phys. 2024; 51: 1203–1216.
https://doi.org/10.1002/mp.16658
PMID: 37544015

<p align="left">
  <a href="https://www.bccrc.ca/dept/io-programs/qurit/"><img src="https://www.bccrc.ca/dept/io-programs/qurit/sites/qurit/files/FINAL_QURIT_PNG_60.png" height="70"/></a>
</p>

---

## Requirements
- Python 3.8+
- Python packages:
	- tensorflow==2.3.1
	- numpy
	- pydicom
	- glob2
	- scipy
	- rt_utils
	- opencv-python  
	
## Installation
- You should be able to run the test inference script (main.py) from a native or virtual Python/Conda environment
- Ensure that `hornetlib.py` is included in your Python search path
- Ensure that `unet2D_pretrain_inputfusion_vlarge_multioutput.200ep.fold0.h5` is included in your Python search path

## Configuration
In the script `main.py`, set the variable `INPUT_DIR` to the folders where the PET and CT series are located

## Usage (inference)
1. Copy DICOM PET and CT series in the pre-specified directory
2. Run `main.py`

> **_Note:_** Inference results will be saved as numpy ndarray in the variables `predicted_image` (multi-channel) and `predicted_image_lab` (single-channel). You will need to convert it to the desired format.

## Project Structure 
```md
psma-hornet/
├── main.py                # Python script for evaluating the model
├── hornetlib.py           # Utility functions and architecture definitions
├── hornet_model.h5        # Model trained parameters
├── README.md              # Project documentation
└── LICENSE                # License file
```
## Licence 

This project is licenced under the MIT License.

## How to cite

If you are including PSMA-Hornet into your projects, kindly include the following citation:

*Klyuzhin IS, Chaussé G, Bloise I, et al. PSMA-Hornet: Fully-automated, multi-target segmentation of healthy organs in PSMA PET/CT images. Med Phys. 2024; 51: 1203–1216.*

## Acknowledgments

This project was supported by the Canadian Institutes of Health Research Project grant PJT-162216, National Institutes of Health / Canadian Institutes of Health Research QIN grant 137993, and Mitacs Accelerate grant IT18063. Azure Cloud compute credits were provided by Microsoft for Health.
