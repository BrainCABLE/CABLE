# Example raw data 
* The example data 'CJ4ROI.ims' can be accessed via [http://cable.bigconnectome.org](http://cable.bigconnectome.org).
# Installation
## Software requirements
This project depends on MRtrix3. Here are the installation methods for different operating systems:
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
## Docker
We also provide a Docker image that contains all the dependencies for the project to run with the following command:
```sh
docker run -it unrealz/cable
```
The code uses GPU to accelerate the computation, if using CPU, please change cupy to numpy and remove the part where pytorch calls cuda.

# Usage
* After installing “MRtrix3” and downloading “CJ4ROI.ims”, place “CJ4ROI.ims” in the same folder as the code under this repository and execute the python file

```sh
python main.py CJ4ROI.ims
```
* The program will generate Fiber Orientation Distribution (FOD) and tractography (.tck) files which can be viewed with 'mrview' in 'Mrtrix3', use 'ODF Display' and 'Tractography' in 'Tools' toolbar to view them.


![image](https://github.com/user-attachments/assets/d4bc4912-22bd-4619-8c1c-b28797cf7b9f)
