# MatFileViewer
![](https://github.com/worlddatong/MatFileViewer/blob/main/imgs/3.png)

This is a simple GUI viewer to view the binary MATLAB files (.mat) without MATLAB.

Every time I want to view a .mat file, I have to launch MATLAB, which is time-consuming.

So I write MatFileViewer to view the mat file.

**This software supports reading 1D and 2D mat files, but does not support 3D data.**

## How to use it
Here is an example of  [three_mat.mat](https://github.com/worlddatong/MatFileViewer/blob/main/TestData/three_mat.mat) which contains a, b and c variables.

1. Users can use MatFileViewer by running python script or executable  (only for windows x64)
2. In the GUI, click the button "Load mat" and select a mat file.
3. Choose the variable you want to view if the mat file contains multiple variables.

![](https://github.com/worlddatong/MatFileViewer/blob/main/imgs/4.png)
![](https://github.com/worlddatong/MatFileViewer/blob/main/imgs/5.png)

## Python script
Run MatFileViewer.py in a Python environment .

MatFileViewer requires:

- Python 
- NumPy 
- SciPy 
- wxPython
--------------------------

## Executable 
Just run MatFileViewer.exe (only for windows x64).

## Download
- [Python Script](https://github.com/worlddatong/MatFileViewer/blob/main/Script/MatFileViewer.py)
- [MatFileViewer.exe](https://github.com/worlddatong/MatFileViewer/releases/tag/1.0)
