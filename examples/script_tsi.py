import serial
from time import sleep
from datetime import datetime
import os
import pandas as pd
import time

from api.tsi import TSI


if __name__ == "__main__":
    # Establish connection to flow meter
    tsi = TSI('COM4')
    tsi.dev.readlines()
    sleep(1)
    tsi.set_output_dir(os.path.join(os.getcwd(), r"output"))

    # Confirm connection
    response = tsi.query_connection()
    print(f'Connection: {response}')

    # Query sample rate
    response = tsi.query_connection(message="RSR\r")
    print(f'Sample rate (ms): {response}')

    # Set sample rate
    response = tsi.query_connection(message="SSR0010\r")
    print(f'Set sample rate: {response}')

    # Confirm sample rate
    response = tsi.query_connection(message="RSR\r")
    print(f'Sample rate (ms): {response}')

    sleep(1)

    # Read and save set of 1000 flow measurements until terminated
    while True:
        tsi.query_flow_set()