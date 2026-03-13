from machine import Pin, PWM
import time

# Create PWM objects for motor pins
motor1 = PWM(Pin(2))
motor2 = PWM(Pin(3))
motor3 = PWM(Pin(4))
motor4 = PWM(Pin(5))

# Set PWM frequency (good for motors)
freq = 1000
motor1.freq(freq)
motor2.freq(freq)
motor3.freq(freq)
motor4.freq(freq)

# Function to set all motors speed
def set_speed(duty):
    motor1.duty_u16(duty)
    motor2.duty_u16(duty)
    motor3.duty_u16(duty)
    motor4.duty_u16(duty)

while True:

    # Gradually accelerate
    for duty in range(0, 65535, 2000):
        set_speed(duty)
        time.sleep(0.05)

    # Hold medium speed
    set_speed(35000)
    time.sleep(3)

    # Gradually decelerate
    for duty in range(65535, 0, -2000):
        set_speed(duty)
        time.sleep(0.05)

    # Stop motors
    set_speed(0)
    time.sleep(2)