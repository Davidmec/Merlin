# Merlin
System for doing some python base data analytics

# [Creat python environment](https://code.visualstudio.com/docs/python/python-tutorial)
# [Add docker files to workspace](https://code.visualstudio.com/docs/containers/quickstart-python)
# [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
# [Enabeling Longpath](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later)
Pip nees Longpath enabled in order to install Jupyter on your machine (you will probably want this for the machine, not just the project)
## Enable longpath
Run powershell with elevated privledges, from the terminal `cmd.exe`:
```
Start-Process powershell -Verb runAs
```
In new window:
```
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
-Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```
## Install JupyterLab
```
 pip3 install jupyterlab
```
# Vevn
Venv is a system in python, that allows for you to install dependencies locally for a package, without having to isntall them system wide

## Create `.venv`

### VS code:
Command Pallet `python.createEnvironment` -> `Venv` -> `requirements.txt`

### [Command Line](https://docs.python.org/3/library/venv.html#creating-virtual-environments):

`python -m venv .venv`

## Activate
Activating a virutal environment will make it so that python uses the environments not global liraries
### VS code:
Open a terminal (it should be activated already and will show that) by prefixing the prompt with `(.venv)`
![Alt text](image.png)
### Command line:
To activate the venv without running a shell from `vscode`

    `.\.venv\Scripts\activatee`
## Update `.venv`

### VS code: 
1. Delete dir [.venv](.venv)
2. Command Pallet `python.createEnvironment` -> `Venv` -> `requirements.txt`

### Command line
When inside an activated environment, any library changes should be isolated to the virtual environment

    `pip3 install -r requirements.txt`

