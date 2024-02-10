from machine import Pin 

#setup imput pin 

input_pin = Pin(4, Pin.IN, Pin.PULL_UP)
output_pin = Pin(3, Pin.IN, Pin.OUT)


while True:
    print(input_pin.value(), output_pin.value())

