---
title: Flow Meter API
subtitle: Revision 1 - Software v2023.2.2
slug: 
author:
  - irw
toc: true
toc-depth: 2
numbersections: false
abstract-title: Summary
abstract: |
  The following includes a description of the available methods used to interact with the flow meter via Python. See the official TSI/Copley documentation for the command set.
tags:
  - 
other-notes-header: 
other-notes:
  - 
header-includes:
  - \usepackage{draftwatermark}
changes:
  - 
---
\newpage
# `TSI` class

Instantiate a flow meter of the `TSI` class with the following:

```py
meter = TSI(port = 'COM1') # Windows
meter = TSI(port = '/dev/USB0') # Linux
```

The available methods are listed below, including an example and description of each.

---

## `connect(self, port = None)`

`meter.connect()`

Connect to the flow meter at the specified port. If no port is specified, attempt to connect on the default port supplied when creating the TSI object.

If successful, sets the 'dev' instance variable from the serial connection.

---

## `close(self)`

`meter.close()`

Closes the connection to the flow meter.

---

## `set_output_dir(self, dir)`

`meter.set_output_dir(r'./data')`

Sets the path for saving data. Creates the directory if it does not exist.

---

## `read(self)`

`meter.read()`

Reads and returns a single line from the serial connection to the flow meter.

---

## `query_connection(self, message = "?\r")`

`meter.query_connection()`

Default behavior: tests the serial connection to the flow meter.  
If a message is supplied, sends the message to the flow meter.

Returns the flow meter response after reading all lines.

---

## `query_flow_set(self)`

`meter.query_flow_set()`

Requests read of 1000 flow data points in binary format. Waits for the confirmation response and then reads, converts, and saves the return values as a CSV.

---

## `query_volume(self)`

`meter.query_volume()`

Requests a volume measurement over 1000 data points.

Implicitly prints the measured volume.

---

## `convert(self, byte = None)`

`meter.convert(self.dev.read(1))`

_Internal_

Converts the bytes received from the flow meter to values of flow rate in the set units (typically SLPM).

---

## `setup_single(self)`

`meter.setup_single()`

_Internal_

Requests read of 1000 flow points. Returns `True` if request successful.

---

## `convert_single(self)`

`meter.convert_single()`

_Internal_

Used for live plotting.

---

## `convert_volume(self, byte = None)`

`meter.convert_volume()`

_Internal_

Processes the request from [`query_volume()`](#query_volumeself)

---

## `save_flow_set(self, data)`

`meter.save_flow_set(results)`

_Internal_

Saves supplied data to a timestamp-named csv file in the configured output directory.

The saved format is of a Pandas dataframe, using the `to_csv()` method.

---
