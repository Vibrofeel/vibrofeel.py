import serial
import time

small_motor_standby_voltage = 0
large_motor_standby_voltage = 0
MAX_VALUE = 255
arduino = None

def setup(port, small_motor_standby_voltage = 0, large_motor_standby_voltage = 0):
    global arduino
    arduino = serial.Serial(port=port, baudrate=115200,timeout=0.01)
    return arduino

def write_read(value):
    print(value)
    arduino.write(value)

def update_motors(small_motor, large_motor):
    packet = bytearray()
    small_motor = calculate(small_motor, 255,  MAX_VALUE - small_motor_standby_voltage) + small_motor_standby_voltage
    large_motor = calculate(large_motor, 255,  MAX_VALUE - large_motor_standby_voltage) + large_motor_standby_voltage
    
    packet.append(small_motor)
    packet.append(large_motor)
    write_read(packet)

def reset_motors():
    packet = bytearray()
    packet.append(small_motor_standby_voltage)
    packet.append(large_motor_standby_voltage)
    write_read(packet)

def turn_off_motors():
    packet = bytearray()
    packet.append(0)
    packet.append(0)
    write_read(packet)

def turn_on_motors():
    reset_motors()

def clamp(value, min_value, max_value):
    if value <= min_value:
        return min_value
    if value >= max_value:
        return max_value
    return value

def calculate(value, max_value, max_target):
    percentage = value / max_value
    return int(percentage * max_target)