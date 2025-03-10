## Example data 
* The example data 'CJ4ROI.ims' can be accessed via [http://cable.bigconnectome.org](http://cable.bigconnectome.org).
## Software requirements
This project depends on MRtrix3. Here are the installation methods for different operating systems:
### Linux
* You can install MRtrix3 using conda:
```sh
conda install -c mrtrix3 mrtrix3
```
* For Ubuntu, it is convenient to install MRtrix3 by:
```sh
sudo apt-get install mrtrix3
```
### Windows
* Installation via **Windows Subsystem for Linux 2 (WSL2)**:\
We recommend installing MRtrix3 under WSL2 which provides excellent support for GUI programs.\
First, enter the command ```wsl --install``` in the Windows terminal. This command will automatically install the default Ubuntu distribution of the Linux subsystem. After the installation is complete, find the newly installed Ubuntu in the Start menu and open it.
Then, use the command ```sudo apt-get install mrtrix3``` in the Ubuntu subsystem to install MRtrix3.
* Installation via msys2:\
Alternatively, you can refer to the official MRtrix3 documentation at https://www.mrtrix.org/download/windows-msys2/ and install it using msys2. In this case, the call to MRtrix3 within **main.py** needs to be executed manually.
## Code dependencies.  
Code dependencies are in 'requirement.txt'.  
```sh
pip install -r requirements.txt
```
The code uses GPU to accelerate the computation, if using CPU, please change cupy to numpy and remove the part where pytorch calls cuda.

## Usage
* After installing “MRtrix3” and downloading “CJ4ROI.ims”, place “CJ4ROI.ims” in the same folder as the code under this repository and execute the python file

```sh
python main.py CJ4TEST.h5
```
* The program will generate Fiber Orientation Distribution (FOD) and tractography (.tck) files which can be viewed with 'mrview' in 'Mrtrix3', use 'ODF Display' and 'Tractography' in 'Tools' toolbar to view them.
## Docker
We also provide a Docker image that contains all the dependencies for the project to run with the following command:
```sh
docker run -it unrealz/cable
```
![image ](https://github.com/Euyz/CABLE/assets/33593212/e1d11bad-6171-4077-97b4-680b15ebdd21)
![image](https://github.com/Euyz/CABLE/assets/33593212/76fca208-a825-4109-bf2c-1382c2fbb889)

