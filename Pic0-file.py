import machine
import utime

button_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

bin_filepath = 'Pokemon Red.gb'

led_bit7 = machine.Pin(6, machine.Pin.OUT)
led_bit6 = machine.Pin(7, machine.Pin.OUT)
led_bit5 = machine.Pin(8, machine.Pin.OUT)
led_bit4 = machine.Pin(9, machine.Pin.OUT)
led_bit3 = machine.Pin(10, machine.Pin.OUT)
led_bit2 = machine.Pin(11, machine.Pin.OUT)
led_bit1 = machine.Pin(12, machine.Pin.OUT)
led_bit0 = machine.Pin(13, machine.Pin.OUT)

leds = [led_bit0, led_bit1, led_bit2, led_bit3, led_bit4, led_bit5, led_bit6, led_bit7]

led_onboard = machine.Pin(25, machine.Pin.OUT)


def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data >> shift) & 0x1

while True:
    
    if button_pin.value():
        
        bin_file = open(bin_filepath, 'rb')
        binArray = bytearray(bin_file.read(1024))
        # binArray = bytearray(bin_file.read(1048575)) # 1MB file
        bin_file.close
        
        print(binArray)
        
        for byte in range(0, len(binArray)):
            
            print(f'binArray[{byte}]: {hex(binArray[byte])}')
            print(f'access_bit({binArray[byte]}, 0): {access_bit(binArray[byte], 0)}')
            
            ledVals = [access_bit(binArray[byte],i) for i in range(0, 8)]
            
            print(f'ledVals: {ledVals}')
            
            for num, led in enumerate(leds):
                led.value(ledVals[num])
            
            utime.sleep(0.5)
