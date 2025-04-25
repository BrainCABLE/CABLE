# Overview
CABLE (Cytoarchitecture-Based Link Estimation) is a method for inferring fiber tracts in the brain by analyzing nuclear/somal anisotropy and spatial cell arrangement. 
The method leverages high-resolution whole-brain 3D fluorescence imaging data acquired using VISoR2 (Xu et al., Nature Biotechnology 2021, DOI:10.1038/s41587-021-00986-5).\
\
This repository provides sample data and code to get started quickly:\
**1. Download sample data.\
2. Install MRtrix3 and python code dependencies / install docker image.\
3. Execute code.**
# Example raw data 
The example data 'CJ4ROI.ims' can be accessed via [http://cable.bigconnectome.org](http://cable.bigconnectome.org).
# Installation

## Software requirements
This project depends on MRtrix3. Here are the installation methods for Linux and Windows:
#### Linux
* You can install MRtrix3 using conda:
```sh
conda install -c mrtrix3 mrtrix3
```
* For Ubuntu, it is convenient to install MRtrix3 by:
```sh
sudo apt-get install mrtrix3
```
#### Windows
* Installation via **Windows Subsystem for Linux 2 (WSL2)**:\
We recommend installing MRtrix3 under WSL2 which provides excellent support for GUI programs.\
First, enter the command ```wsl --install``` in the Windows terminal. This command will automatically install the default Ubuntu distribution of the Linux subsystem. 
Then, use the command ```sudo apt-get install mrtrix3``` in the Ubuntu subsystem to install MRtrix3.
* Installation via msys2:\
Alternatively, you can refer to the official MRtrix3 documentation at https://www.mrtrix.org/download/windows-msys2/ and install it using msys2. In this case, the call to MRtrix3 within **main.py** needs to be executed manually.

## Code dependencies  
Code dependencies are in 'requirement.txt'.  
```sh
pip install -r requirements.txt
```
#### (Optional) Asymmetric ODF filtering
If you want to perform asymmetric ODF filtering, a well - implemented toolkit (repository) can be directly applied to the cODF (https://github.com/CHrlS98/aodf - toolkit). It's important to note that currently, MRtrix3 does not support asymmetric ODF. Therefore, other visualization methods may be required, such as FSLeyes (see https://open.win.ox.ac.uk/pages/fsl/fsleyes/fsleyes/userdoc/).
## Docker
We also provide a Docker image that contains all the dependencies for the project to run with the following command:
```sh
docker pull unrealz/cable
```
For WSL2-based Docker Desktop users, use the following command to execute and display:
```sh
docker run -it -v /run/desktop/mnt/host/wslg/.X11-unix:/tmp/.X11-unix `
                -v /run/desktop/mnt/host/wslg:/mnt/wslg `
                -e DISPLAY=:0 `
                -e WAYLAND_DISPLAY=wayland-0 `
                -e XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir `
                -e PULSE_SERVER=/mnt/wslg/PulseServer `
                unrealz/cable python main.py CJ4ROI.ims
```


# Usage
* After installing “MRtrix3” and downloading “CJ4ROI.ims”, place “CJ4ROI.ims” in the same folder as the code under this repository and execute the python file

```sh
python main.py CJ4ROI.ims
```
* The program will generate Fiber Orientation Distribution (FOD) and tractography (.tck) files which can be viewed with 'mrview' in 'Mrtrix3', use 'ODF Display' and 'Tractography' in 'Tools' toolbar to view them.
# Example input and output
![image](https://github.com/user-attachments/assets/c143885d-33c9-46aa-bab5-047178527211)
![image](https://github.com/user-attachments/assets/837e1dca-5903-4fdc-af52-76019a369849)


