"""from machine import Pin, PWM
import time

pins = [6, 7, 8, 9]
pwms = []

# Initialize PWM
for p in pins:
    pwm = PWM(Pin(p))
    pwms.append(pwm)

def set_all(freq, duty):
    print("Setting freq:", freq)
    for pwm in pwms:
        pwm.freq(freq)
        pwm.duty_u16(duty)

while True:
    # 1 kHz (nice and stable)
    set_all(1000, 32768)   # 50%
    time.sleep(5)

    # 100 kHz (fast)
    set_all(100000, 32768)
    time.sleep(5)

    # 500 kHz (very fast)
    set_all(500000, 32768)
    time.sleep(5)"""

from machine import Pin, PWM
import time

# ESC pins
pins = [6, 7, 8, 9]
escs = []

# Create PWM objects
for p in pins:
    pwm = PWM(Pin(p))
    pwm.freq(50)  # Standard ESC frequency
    escs.append(pwm)

# Convert throttle (0.0–1.0) → duty
def set_throttle(value):
    min_duty = 1638   # 1ms pulse
    max_duty = 8192   # 2ms pulse
    duty = int(min_duty + (max_duty - min_duty) * value)
    
    for esc in escs:
        esc.duty_u16(duty)

# -----------------------
# 🔑 ARMING SEQUENCE
# -----------------------
print("Arming ESCs...")

set_throttle(0)      # Minimum throttle
time.sleep(3)        # Wait for ESC beeps

# -----------------------
# 🚀 START MOTORS
# -----------------------
print("Starting motors...")

set_throttle(0.15)   # Start low (adjust if needed)

while True:
    pass  # keep running