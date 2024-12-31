from time import sleep
from gpiozero import PWMLED
from engine_commands import engine_read, engine_write

# /// LEDS
led_engine_status = PWMLED(17)
led_ssh_status = PWMLED(24)


while  engine_read(1) == '1':
    # /// BREAK ONE
    ...

    if engine_read(1) == '1':
        led_engine_status.value = 0.15
    
    sleep(0.125)

    # /// BREAK TWO
    ...
    
    led_engine_status.value = 0

    sleep(0.125)

    # /// BREAK THREE
    ...

    if str(engine_read(2)) == '1': led_ssh_status.value = 0.2
    else: led_ssh_status.off()   

    sleep(0.125)

    # /// BREAK FOUR
    ...

    led_ssh_status.off()

    sleep(0.125)

    # /// BREAK FIVE
    ...

    if str(engine_read(2)) == '1': led_ssh_status.value = 0.2
    else: led_ssh_status.off()  
    
    sleep(0.125)

    # /// BREAK SIX
    ...

    led_ssh_status.off()
    
    sleep(0.125)

    # /// BREAK SEVEN
    ...
    
    sleep(0.125)

    # /// BREAK EIGHT
    ...
    
    sleep(0.125)