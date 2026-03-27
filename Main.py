# Drone Motor Test - Raspberry Pi Pico + 30A 4-in-1 ESC
# ESC signal: 50Hz PWM, 1ms (0% throttle) to 2ms (100% throttle)
# Pins: GPIO 6, 7, 8, 9 -> ESC signal inputs for motors 1-4
# SAFETY: Remove propellers before running this test on the bench.

from machine import Pin, PWM
import time

# --- Configuration ---
PWM_FREQ = 50           # Standard ESC frequency (Hz)
MIN_DUTY = 3277         # 1ms pulse at 50Hz = 0% throttle
MAX_DUTY = 6554         # 2ms pulse at 50Hz = 100% throttle
ESC_PINS = [6, 7, 8, 9]
TEST_THROTTLE = 0.50   # 50% - moderate test speed
RAMP_TIME = 3.0         # Seconds to ramp up/down
RAMP_STEPS = 30         # Number of steps during ramp
HOLD_TIME = 7.0         # Seconds to hold at test throttle

# --- Functions ---
def set_throttle(value):
    value = max(0.0, min(1.0, value))
    duty = int(MIN_DUTY + (MAX_DUTY - MIN_DUTY) * value)
    for esc in escs:
        esc.duty_u16(duty)

def ramp_throttle(start, end, duration, steps):
    step_time = duration / steps
    for i in range(steps + 1):
        t = start + (end - start) * (i / steps)
        set_throttle(t)
        if i < steps:
            time.sleep(step_time)

def stop_all():
    for esc in escs:
        esc.duty_u16(MIN_DUTY)
    time.sleep(0.5)
    for pin_num, esc in zip(ESC_PINS, escs):
        esc.deinit()
        Pin(pin_num, Pin.OUT, value=0)

# --- Test Sequence ---
escs = []

try:
    for p in ESC_PINS:
        pwm = PWM(Pin(p))
        pwm.freq(PWM_FREQ)
        escs.append(pwm)

    print("Arming ESCs... listen for beeps confirming arm.")
    set_throttle(0.0)
    time.sleep(3)

    print("Ramping up to", int(TEST_THROTTLE * 100), "% throttle...")
    ramp_throttle(0.0, TEST_THROTTLE, RAMP_TIME, RAMP_STEPS)

    print("Holding for", int(HOLD_TIME), "seconds...")
    time.sleep(HOLD_TIME)

    print("Ramping down...")
    ramp_throttle(TEST_THROTTLE, 0.0, RAMP_TIME, RAMP_STEPS)

    print("Test complete.")

except KeyboardInterrupt:
    print("\nInterrupted! Stopping motors...")

except Exception as e:
    print("Error:", e)

finally:
    stop_all()
    print("Motors stopped. All PWM disabled.")
