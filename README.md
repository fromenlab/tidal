# tidal
Control interfaces for dynamic lung system

# System Configuration

## OS

### Linux

This is default choice for running the system in a lab setting. We use a recent version of Ubuntu, but other Linux flavors should also be suitable.

Optional: add timestamps to command history.  
`echo 'export HISTTIMEFORMAT="%Y%m%d "' >> ~/.bashrc`

Add USB access permissions with the following command. Log out and log back in to take effect.  
`sudo usermod -a -G dialout $USER`

### Windows

Windows can be used for development purposes out of lab. However, there are important differences in how threads/processes are handled between Windows and Linux, so the final tests should be confirmed with whatever system is being used in lab. Separate versions are maintained for certain features, but Windows will not be the primary OS for the current state of development.

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

1. Configure the Python path

    ```json
    "terminal.integrated.env.linux": {
            "PYTHONPATH": "${workspaceFolder}"
        }
    ```

1. 

## Python

1. Install the latest Miniconda  
https://docs.conda.io/en/latest/miniconda.html
1. Create the environment with the following command 

    ```
    conda env create -f environment.yml
    ```
    where `environment.yml` should reference the YAML configuration file in this repo.

    ```yaml
    name: dynamic
    dependencies:
    - python=3.9
    - pyserial
    - numpy
    - pandas
    - matplotlib
    - jupyter
    ```