import utime
from machine import Pin, PWM

def main():
    motor1pin = Pin(14, Pin.OUT)  # 14 is a GPIO Pin, Replace with other as necessary
    motor2pin = Pin(15, Pin.OUT)  # 15 is a GPIO Pin, Replace with other as necessary

    motor1= machine. PWM(motor1pin)
    motor2 = machine.PWM(motor2pin)

    motor1.freq(500)  #frequency is 500 Hz
    motor1.duty(512)  #duty cycle is 50% (0-1023 is complete duty)
    motor2.freq(500)
    motor2.duty(512)

    motor1Pos(position)
    motor2Pos(position)

def motor1Pos(value):
    slider1= ############Value Recieved from Slider1
    return slider1
def motor2Pos(value):
    slider2=  ############Value Recieved from Slider2
    return slider2

if __name__ == '__main__':
    main()