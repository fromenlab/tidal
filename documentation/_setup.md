# System Configuration

If you have any doubt, please read this from start to finish. Assume that where code is involved, you can copy and paste.

## OS

### Windows

As of v2023.2.2, Windows conventions for flow logging have been implemented in the main routine.
However, there are important differences in how threads/processes are handled between Windows and Linux, so the final tests should be confirmed with whatever system is being used in lab.

### Linux

This is default choice for running the system in a lab setting. We use a recent version of Ubuntu, but other Linux flavors should also be suitable.

Optional: add timestamps to command history.  
`echo 'export HISTTIMEFORMAT="%Y%m%d "' >> ~/.bashrc`

Less optional: add USB access permissions with the following command. Log out and log back in to take effect.  
`sudo usermod -a -G dialout $USER`

#### Fonts
Note that tkinter fonts on Linux with Anaconda-based Python [leave some things to be desired](#fonts-1). One alternative is to use the system Python version and install the dependencies via [pip](#pip).

## Arduino

This project no longer requires downloading the Arduino IDE or CLI directly. Use the version bundled with VS Code.

## VS Code

1. Install the following extensions. Some may be bundled together.
    - Git Graph
    - Python
    - Jupyter
    - Arduino
        - AVR boards (install from extension widget)
        - megaAVR boards (install from extension widget)
    - C/C++ Extension Pack
    - Serial Monitor

1. Configure the Python path in your user or workspace settings.

    ```json
    "terminal.integrated.env.linux": {
            "PYTHONPATH": "${workspaceFolder}"
        }
    ```

1. Locate the path to the VS Code `arduino-cli` and add it to your system's `PATH` environment variable.
    - Linux command:  
    `echo 'export PATH=$PATH:~/.vscode/extensions/vsciot-vscode.vscode-arduino-0.6.0-linux-x64/assets/platform/linux-x64/arduino-cli' >> ~/.bashrc`

## Python

If you don't have a version of Python on your system, try [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
Otherwise, it might be best to continue with your system version (as long as it's Python 3).

### pip

1. Install some dependencies if you're running [Linux](#linux)
    ```
    sudo apt-get install python3-tk
    sudo apt-get install python3-pil.imagetk
    ```
1. Install the requirements using the system Python, with or without a virtual environment
    ```
    pip install -r requirements.txt
    ```

### conda

This project has used Anaconda to easily manage Python environments in development. With more recent versions of the TIDAL software, this has become a point of trouble due to font support.

1. Install the latest Miniconda  
https://docs.conda.io/en/latest/miniconda.html
1. Create the environment with the following command 

    ```
    conda env create -f environment.yml
    ```
    where `environment.yml` should reference the YAML configuration file in this repo.

## References

#### tkinter install

- [https://tkdocs.com/tutorial/install.html](https://tkdocs.com/tutorial/install.html#install-x11-python:~:text=For%20example%2C%20running%20Ubuntu%2020.04LTS%2C%20Python%203.8.2%20is%20already%20installed.%20However%2C%20to%20use%20Tkinter%2C%20you%20need%20to%20install%20a%20separate%20package%2C%20named%20python3%2Dtk%3A)

#### Fonts

- [https://stackoverflow.com/questions/49187741/tkinter-looks-extremely-ugly-in-linux](https://stackoverflow.com/questions/49187741/tkinter-looks-extremely-ugly-in-linux)
- [https://github.com/ContinuumIO/anaconda-issues/issues/6833](https://github.com/ContinuumIO/anaconda-issues/issues/6833)
- [https://github.com/conda-forge/tk-feedstock/pull/40](https://github.com/conda-forge/tk-feedstock/pull/40)
- [https://github.com/conda-forge/tk-feedstock/pull/40#issuecomment-1803067221](https://github.com/conda-forge/tk-feedstock/pull/40#issuecomment-1803067221)