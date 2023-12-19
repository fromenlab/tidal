# tidal
Control interfaces for dynamic lung system

# System Configuration

## OS

### Linux

This is default choice for running the system in a lab setting. We use a recent version of Ubuntu, 
but other Linux flavors should also be suitable.

Optional: add timestamps to command history.  
`echo 'export HISTTIMEFORMAT="%Y%m%d "' >> ~/.bashrc`

Add USB access permissions with the following command. Log out and log back in to take effect.  
`sudo usermod -a -G dialout $USER`

For using the Arduino CLI bundled with the VS Code extension:  
`echo 'export PATH=$PATH:~/.vscode/extensions/vsciot-vscode.vscode-arduino-0.6.0-linux-x64/assets/platform/linux-x64/arduino-cli' >> ~/.bashrc`

### Windows

As of the current working version (F2023), Windows conventions for flow logging have been implemented in the main routine.
 However, there are important differences in how threads/processes are handled between Windows and Linux, so the final 
 tests should be confirmed with whatever system is being used in lab.

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

1. Configure the Python path in user settings

    ```json
    "terminal.integrated.env.linux": {
            "PYTHONPATH": "${workspaceFolder}"
        }
    ```

1. Locate the path to the VS Code `arduino-cli` and add it to your system's `PATH` environment variable.

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
    - matplotlib
    - pandas
    - jupyter
    - plotly # only for interactive plot
    - dash # only for more-interactive plot
    ```