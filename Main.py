from machine import Pin, PWM
import time

# Use a valid low frequency
FREQ = 10  

pins = [6, 7, 8, 9]
pwms = []

for p in pins:
    pwm = PWM(Pin(p))
    pwm.freq(FREQ)
    pwms.append(pwm)

def set_duty_all(duty):
    for pwm in pwms:
        pwm.duty_u16(duty)

print("Slow PWM demo (10 Hz)")

while True:
    set_duty_all(16384)  # 25%
    time.sleep(3)

    set_duty_all(32768)  # 50%
    time.sleep(3)

    set_duty_all(49152)  # 75%
    time.sleep(3)