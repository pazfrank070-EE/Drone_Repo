from machine import Pin, PWM
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
    time.sleep(5)