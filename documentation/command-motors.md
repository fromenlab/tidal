---
title: Motor Command Protocol
subtitle: Revision 2 - Software v2023.2.2
slug: 
author:
  - irw
toc: true
toc-depth: 2
numbersections: false
abstract-title: Summary
abstract: |
  The following includes a description of the available commands used to control
  the motors.
tags:
  - 
other-notes-header: 
other-notes:
  - 
header-includes:
  - \usepackage{draftwatermark}
changes:
  - R2 - Updated from legacy version. Content, formatting, methods
---
\newpage
# Usage

- All commands are case-sensitive
- All commands must be enclosed in angle brackets (i.e. `<Command>`)
- Maximum command length is 32 characters between brackets
- The separator to be used within commands is `/`
- If a command has multiple parameter options, they are denoted within braces (`{}`). For example, the command `SD{IEP}/X` can take the form `<SDI/X>` or `<SDP/X>` to set respective values
- If a command is not defined, `Invalid command` will be returned
- A maximum of 700 consecutive steps can be executed per maneuver
- One motor corresponds to one lobe, and they are listed in a five-bit sequence (`00000`)


    |   Lobe/Motor      | Abbreviation      | Bit           |
    |    :---           |      :---:        |    ---:       |
    |   Right upper     |     (RU)          |   `1----`     |
    |   Right middle    |     (RM)          |   `-1---`     |
    |   Right lower     |     (RL)          |   `--1--`     |
    |   Left upper      |     (LU)          |   `---1-`     |
    |   Left lower      |     (LL)          |   `----1`     |

## Main commands

The main commands to use in a ready-to-run setting are for checking motor parameters, preparing a single maneuver, and running a profile (series of inhale/exhale maneuvers).

### Check commands

- `?` 
    - Query connection
- `?S` 
    - Query parameters


### Run commands

- `SM{Maneuver}/{Steps}/{Motors}`
    - Prepare a maneuver
- `RUN`
    - Run the prepared maneuver
-  `PROFILEC`
    - Run a constant-delay breathing profile series. This uses a single delay 
    value for both inhale and exhale maneuvers, set by the default value 
    and number of steps for each lobe.
- `PROFILEV`
    - Run a variable-delay breathing profile series. This uses the specific 
    values stored in memory for inhale and exhale delays. The number of steps 
    is based on the default value.



\newpage
# General commands

## `?`

Query the connection to the controller.

### Input

None

### Output

Returns `OK-Motors` if the connection is working.

---

## `?S`

Query the global and lobe-specific default settings.

### Input

None

### Output

Returns the following:

- Profile delay
- Profile cycles
- Motor default number of steps
- Motor default delay
- Motor step position (recorded since time on)
- Inhale delay (before inhalation maneuver)
- Exhale delay (before exhalation maneuver)
- Starting maneuver (first maneuver in cycle: `1` for inhale, `-1` for exhale)

---

## `?A`

Query all delays for each lobe.

### Input

None

### Output

Returns the following:

- Current delay values for each lobe
- Inhale delay values stored in memory
- Exhale delay values stored in memory

---

\newpage
# Global settings

Format: `S{Setting}/{Value}/{Additional parameters}`

## `SN/X`

Set number. Sets the number of breathing cycles performed in a profile, a set of paired inhalation and exhalation maneuvers.

### Inputs

- `X` - The number of cycles. Positive integer.

### Outputs

None

---

## `SD{IEP}/X`

Set delay inhale/exhale/profile. Set the delay value taken before the inhalation maneuver, exhalation maneuver, or breathing profile, in seconds. 

Takes one of the following forms: `SDI`, `SDE`, `SDP`.

### Input
- `SD{IEP}`
    - `I` - inhalation
    - `E` - exhalation
    - `P` - profile (repeated breathing cycles)
- `X` - Number of seconds to pause before a maneuver
    - Float (decimal value) acceptable

### Output

None

---

## `SO{IE}`

Set order inhale/exhale. Set the order of the maneuvers for profile breathing. 

Takes one of the following forms: `SOI`, `SOE`.

### Input
- `SO{IE}`
    - `I` - start with inhalation (`1`)
    - `E` - start with exhalation (`-1`)

### Output

None

---

# Lobe settings

## `SLS/X/00000`

Set lobe steps. Sets the default number of steps to be taken by a given set of motors. Multiple motors can be set simultaneously.

### Input

- `X` - Number of steps. Integer value. Max = 700.
- `00000` - Motor bits

### Output

Prints "Not set" if a motor is not set by this command.

---

## `SLD/X/00000`

Set lobe delay. Set the default delay value for each in a given set of motors. Multiple motors can be set simultaneously.

### Input

- `X` - Integer value of the delay. Arbitrary units related to processor cycles. (0-65535)
- `00000` - Motor bits

### Output

Prints "Not set" if a motor is not set by this command.


---

## `SM{IE}/X/00000`

Set maneuver inhale/exhale. For a given set of motors, prepares a maneuver of `X` steps, 
in the given direction. Sending this command does not run the motion. This command should be followed by `RUN` to start a maneuver.

Takes one of the following forms: `SMI/X/00000`, `SME/X/00000`.

Sending an updated command with the same motor bit(s) set, before sending 
the `RUN` command, will invalidate previous maneuver settings for the 
same motor (i.e. only one maneuver can be set for a given motor at a time).

### Input
- `SM{IE}` - Set the maneuver type (`I` - inhale/`E` - exhale)
- `X` - Set the number of steps for the maneuver. Max = 700.
- `00000` - Motor bits

---

## `SAC`

Set all constant. Set the delay values for all motors and all steps to the default value for each motor.

### Input

None

### Output

None

---

## `SAC/X/00000`

A special case of the [`SAC`](#sac) command with parameters. For the given motors, set the supplied value as the delay value for all steps.

### Input

- `X` - Delay value (0-65535)


### Output

None

---


## Scripting commands

### `SAI/I/X/00000`

Set at index. For a given set of motors, set the delay value at an individual step. Check that the value was written correctly.

#### Input

- `I` - index of the step to write
- `X` - value of the delay
- `00000` - motor bits

#### Output

`OK` if the value was written correctly. `Error` if the value stored in the array does not match the value supplied.

---

### `C/S/X/00000`

_Experimental. Not for general use._

Constant. Manually set constant value for delays. Set the supplied value as the delay for the given motors, up to the given number of steps.

#### Input

- `S` - Number of steps. Integer value. Max = 700.
- `X` - Delay value (0-65535)
- `00000` - Motor bits

#### Output

`OK` if function completes.

---

\newpage
# Run commands

## `RUN`

Runs the single most recent maneuver stored for each motor via the [`SM`](#smiex00000) command. 
Only runs maneuvers since the last `RUN` command. If multiple [`SM`](#smiex00000) command have been sent, only the most recent is performed.

### Input

None

### Output

None

## `PROFILEC`

Runs a constant-delay breathing profile based on the global breathing parameters and default delay arrays for each motor.

Executes the following:

- Set constant-value delays
- Delay profile
- For the given number of breaths:
  - Prepare first maneuver (inhale/exhale)
  - Delay first maneuver (inhale/exhale)
  - Run maneuver and wait until completion
  - Prepare second maneuver (inhale/exhale)
  - Delay second maneuver (inhale/exhale)
  - Run maneuver and wait until completion

### Input

None

### Output

None

## `PROFILEV`

Runs a variable-delay breathing profile based on the global breathing parameters and Bezier-defined delay arrays for each motor.

Executes the following:

- Delay profile
- For the given number of breaths:
  - Prepare first maneuver variable-value delays (inhale/exhale, assigned to each lobe)
  - Prepare first maneuver (inhale/exhale)
  - Run maneuver and wait until completion
  - Prepare second maneuver variable-value delays (inhale/exhale, assigned to each lobe)
  - Prepare second maneuver (inhale/exhale)
  - Run maneuver and wait until completion

### Input

None

### Output

None

