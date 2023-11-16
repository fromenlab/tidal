from api.arduino_motor import Arduino
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Assuming Windows
ard = Arduino('COM7')

pp.pprint(ard.check_connection())
pp.pprint(ard.check_parameters())

# Example: Set arbitrary motion and run

ard.prepare_maneuver(maneuver='inhale', steps=200, motors = '11100')
ard.prepare_maneuver(maneuver='inhale', steps=200, motors = '00011')
ard.run_maneuver()

# Example: Run a breathing profile

pp.pprint(ard.run_profile())

ard.close()