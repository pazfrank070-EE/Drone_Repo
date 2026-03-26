from machine import Pin, PWM
import time

# Set PWM frequency (50 Hz for ESCs)
FREQ = 50

# Initialize PWM on pins
esc_pins = [6, 7, 8, 9]
escs = []

for pin in esc_pins:
    pwm = PWM(Pin(pin))
    pwm.freq(FREQ)
    escs.append(pwm)

# Function to set throttle (0.0 to 1.0)
def set_throttle(esc, throttle):
    # Map throttle to duty cycle (1ms to 2ms pulse)
    min_duty = 1638   # ~1ms
    max_duty = 8192   # ~2ms
    duty = int(min_duty + (max_duty - min_duty) * throttle)
    esc.duty_u16(duty)

# ARM ESCs (IMPORTANT!)
print("Arming ESCs...")
for esc in escs:
    set_throttle(esc, 0)  # minimum throttle

time.sleep(3)  # wait for ESC to arm

# TEST: ramp motors slowly
print("Starting motors...")
for t in range(0, 101):
    throttle = t / 100
    for esc in escs:
        set_throttle(esc, throttle)
    time.sleep(0.05)

# Stop motors
print("Stopping motors...")
for esc in escs:
    set_throttle(esc, 0)