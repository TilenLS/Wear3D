# Wear3D

Wear3D is a project under the COMP0016 module at UCL as a part of the Industry Exchange Network (IXN) program in partnership with the Eastman Dental Institute. It is an early stage Clinical Decision Support System (CDSS) app that aims to provide treatment plan suggestions for patients with tooth wear, to ultimately save dentists time, resources, and help provide more accurate prognosis. For an expansive overview of the project visit our website at: http://students.cs.ucl.ac.uk/2022/group10/

## Features

* Windows based app
* Rendering and viewing of 3D tooth models (STL/PLY)
* Database of tooth scans and corresponding medical background of patient
* Numerical tooth wear evaluation
* Broad treatment plan suggestions

## Dependencies

### Tools
* Python3
* Azure


### Python Libraries
* numPy==1.24.1
* Flask==2.2.2
* plyfile==0.7.4
* requests==2.23.0
* torch==1.13.1
* torchsummary==1.5.1
* tqdm==4.64.1
* PySide2==5.15.2.1
* open3D==0.16.1
* Win32GUI==221.6
* Custom_Widgets==0.6.4
* iconify==0.0.103
* pytorch3d==0.7.2
* matplotlib==3.6.2
* sqlite==3.41.2

## Running project 
This will only work on windows as we use the Win32GUI library. Either use a Windows device or a Windows virtual machine (VM). Moreover, since we host our database on an Azure VM, you could connect to our server before being able to use the application properly.

### Cloud Azure

You can also skip this step and run the software directly for testing, which will connect to our team's server by default.

**Step 1:**  Go to <a href="https://azure.microsoft.com/en-gb">Azure website</a> and create a virtual machine. Detailed guideline can be found <a href="https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal?tabs=ubuntu">here</a>. Make sure to take note of the username, password, and your vm ip address for the virtual machine.

**Step 2:** Use SSH to connect to the cloud server. 

``` 
ssh username@your-vm-ip-address
```
  
**Step 3:** Once you are connected to the remote virtual machine, you will need to clone our repository.

```
git clone https://github.com/HongruiTang/tooth-wear-dl.git
```
    
**Step 4:** Download related packages from the file requirements.txt:
```
cd tooth-wear-dl
pip install -r requirements.txt
```

**Step 5:** Navigate to the directory where the app.py file is located.
```
cd back-end/app/
```

**Step 6:** Run the back-end code by using the following command:
```
python app.py
```

If you want to run the app back-end code continuously on the server, you can use the following command:
```
nohup python app.py
```
  
Now the back-end preparation is done. You can now open Wear3D (after downloading it following the instructions below).
 
### Download and run Wear3D
Note: This must be done on Windows.

**Step 1:** Click on the most recent Wear3D release on our Github page.

**Step 2:** Click on the "executable.zip" file under Assets to download.

**Step 3:** When the downloading is complete, extract the zip file.

**Step 4:** Navigate into the app folder from the extracted zip file and open "Wear3D.exe" to run Wear3D.

Note: If your local device generates a "Windows protected your PC" warning when attempting to run the app, click on 'More info' and then 'Run anyway'.

### More info
For more information on how we implement the back-end: https://github.com/HongruiTang/tooth-wear-dl
