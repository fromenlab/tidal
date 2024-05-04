# TIDAL
This software provides interfaces control and minimal analysis of the TIDAL dynamic lung system. It is primarily a graphical means of configuring the system, setting parameters for breathing profiles, and analyzing breathing profile output.

For users interested in scripting, there are also Python APIs and an Arduino motor control protocol available.

Ready to get started? [Read the docs here!](documentation)

## Main components

- Lung system and motors
- Computer
    - Tested on Linux and Windows
- Python
- Arduino MEGA or clone
- TSI/Copley flow meter
    - RS232 to USB

## Usage

1. Get the source
    - `git clone https://github.com/fromenlab/tidal.git`
    - No git: Download the zip file and extract.
    - Version names are a combination of semantic and calendar versioning.
1. Install the dependencies in your Python environment.
    - Conda: `conda create -f environment.yml`
    - Pip: `pip install -r requirements.txt`
1. Run `gui/main.py` from the main `/tidal/` directory.

[For more details on configuring the computer, see the notes in the documentation.](documentation/_setup.md)

## Citing this work

This work is currently in preparation for publication. If you have come by it via means other than official channels, please contact the authors immediately.

## Disclaimers
This work has been supported by the National Institutes of Health and National Science Foundation.
IRW (`irw-udel`) was also supported by a GAANN Fellowship funded by the Department of
Education. The content is solely the responsibility of the authors and does not necessarily 
represent the official views of the National Institutes of Health, National Science Foundation, 
or Department of Education.

### Awards
- NIH R35 GM142866
- NSF 2237430
- ED P200A210065