# Vibrofeel.py

Python handler script to control microcontroller 

Arduino code can be found here 
https://github.com/Vibrofeel/vibrofeel.ino

```py
import vibrofeel_com # Import the module
import time

# parameters port String small_motor_standby_voltage Number, large_motor_standby_voltage Number
# port String ex Windows COM5 Linux /dev/ttyACM0
# 
# In case you want to motors to instantly spin up on input you can feed them small amount of voltage
# keep in mind that this can generate high pitch noise coming from the motors 
# small_motor_standby_voltage = Number
# large_motor_standby_voltage = Number
vibrofeel_com.setup("COM5", 13,13)

# Put motors in standby mode
vibrofeel_com.turn_on_motors()
time.sleep(2)

# Spin motors with full speed  
vibrofeel_com.update_motors(255, 255)
time.sleep(1)

# Get motors back to standby voltage
vibrofeel_com.reset_motors()
time.sleep(1)

# Spin motors with quarter of the speed
vibrofeel_com.update_motors(64, 64)
time.sleep(1)

# We should turn off motors at end of our code to prevent standby
# voltage being applied even when we close the program
vibrofeel_com.turn_off_motors()
```