from machine import Pin, PWM
import time

# Very slow frequency (1 Hz)
FREQ = 1

esc_pins = [6, 7, 8, 9]
pwms = []

for pin in esc_pins:
    pwm = PWM(Pin(pin))
    pwm.freq(FREQ)
    pwms.append(pwm)

# Set duty cycle (0 to 65535)
def set_duty_all(duty):
    for pwm in pwms:
        pwm.duty_u16(duty)

print("Starting slow PWM demo...")

while True:
    # 25% duty (short ON, long OFF)
    set_duty_all(16384)
    time.sleep(3)

    # 50% duty (equal ON/OFF)
    set_duty_all(32768)
    time.sleep(3)

    # 75% duty (long ON, short OFF)
    set_duty_all(49152)
    time.sleep(3)