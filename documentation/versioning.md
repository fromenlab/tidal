---
date: '2023-12-04'
changes:
    - 
---

# Versioning

The version naming scheme is a combination of [semantic versioning](https://semver.org/) and [calendar versioning](https://calver.org/).  
The choice behind this was to enhance future users' ability to identify when the version was developed (how old it is/what paper) and when features were added or updated (experimental consistency, backwards compatibility).  
This scheme applies only to released versions of the software -- working versions will be logged by the commit associated with the running software, which is tracked in the version control (available locally and on GitHub).

# Format

YYYY.MAJOR.MINOR

## YYYY

The year the major version was released (e.g. 2023). 

This will roughly coincide with phases of the project or manuscripts, but development of the software may not be active on an annual basis. If the software is not revised in a major way after version 2023.2.X, future versions would remain at 2023.2.Y, even if released in 2026.

## MAJOR

Major version of the software (e.g. 1 or 2).

From the semantic versioning convention, increment the major version when there are changes made that are incompatible with previous versions of the software. For example:
- When the format/values of a configuration file change, and loading a new config file would cause an old software version to crash
- When the meaning of a command changes or an additional parameter is added to a method/command, which the software or controller would not be able to interpret
- Overhaul of the controls or graphical user interface

## MINOR

Minor or patch version of the software (e.g. 2.1 or 2.12). In this case, I have decided to include minor and patch in the same place, to maintain the convention of three-digit versions. Small patches should be held until there is a minor feature to add or the number of patches is sufficient to warrant a new minor release.

From the semantic versioning convention, increment the minor version when there are changes made that are compatible with previous versions; increment the patch version when there are fixes made that are compatible with previous versions. For example:
- Adding the behavior of saving the configuration to the run folder when a run is cleared
- Printing a value to the console during an operation -- or removing print functions
- Changing the text of a button
- Adding the controller logic to return new relevant values and a GUI button to direct the communications