# Wear3D
## Description

Wear3D is a project under the COMP0016 module at UCL as a part of the Industry Exchange Network (IXN) program in partnership with the Eastman Dental Institute. It is an early stage Clinical Decision Support System (CDSS) app that aims to provide treatment plan suggestions for patients with tooth wear, to ultimately save dentists time, resources, and help provide more accurate prognosis. For an expansive overview of the project visit our website at: http://students.cs.ucl.ac.uk/2022/group10/

## Features

* Windows based app
* Rendering and viewing of 3D tooth models (STL/PLY)
* Database of tooth scans and corresponding medical background of patient
* Numerical tooth wear evaluation
* Broad treatmen plan suggestions

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
* open3D==0.16.0
* Win32GUI==221.6
* Custom_Widgets==0.6.4
* iconify==0.0.103
* pytorch3d==0.7.2
* matplotlib==3.6.2
* sqlite==3.41.2

## Running project 
This will only work on windows as we use the Win32GUI library. Either use a Windows device or a Windows virtual machine (VM). Moreover, since we host our database on an Azure VM you could connect to our server before being able to use the application properly.

### Cloud Azure

**Step 1:** Open command prompt or terminal on your local computer. 

**Step 2:** Use SSH to connect to the cloud server. The password for the VM is: Team10Toothwear!

``` 
ssh team10@20.127.200.67 
```
Enter the password when you are prompted
  
**Step 3:** Once connected to the remote VM you will need to navigate to the directory where the "app.py" file is located. This can be done with the following command:

```
cd tooth-wear-dl/back-end/app/
```
    
**Step 4:** Run the back-end code with this command:
```
python app.py
```
  
Now the back-end preperation is done. You can now open Wear3D (after downloading it following the instructions below).
 
### Download and run Wear3D
Note: This must be done on Windows.

**Step 1:** Click on the most recent Wear3D release on our Github page.

**Step 2:** Click on the "executable.zip" file under Assets to download.

**Step 3:** When the downloading is complete, extract the zip file.

**Step 4:** Navigate into the app folder from the extracted zip file and open "main.exe" to run Wear3D.

Note: If your local device generates a "Windows protected your PC" warning when attempting to run the app, click on 'More info' and then 'Run anyway'.
