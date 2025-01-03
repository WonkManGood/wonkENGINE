from time import sleep
from gpiozero import PWMLED
from commands.engine_commands import engine_read, engine_write, engine_roundtrip_check

# /// LEDS
led_engine_status = PWMLED(17)
round_x4 = PWMLED(27)
round_x8 = PWMLED(22)
led_ssh_status = PWMLED(24)


while True:
    # /// BREAK ONE ────────────────────────────────────────────────────────────────────
    ...

    # / Off Switch for everything. . .
    round_x4.value = 0
    round_x8.value = 0
    
    sleep(0.125)

    # /// BREAK TWO ────────────────────────────────────────────────────────────────────
    ...
    
    led_engine_status.value = 0

    sleep(0.125)

    # /// BREAK THREE ───────────────────────────────────────────────────────────────────
    ...

    if str(engine_read(2)) == '1': led_ssh_status.value = 0.2
    else: led_ssh_status.off()   

    sleep(0.125)

    # /// BREAK FOUR ────────────────────────────────────────────────────────────────────
    ...

    led_ssh_status.off()

    sleep(0.125)

    # /// BREAK FIVE ────────────────────────────────────────────────────────────────────
    ...

    if str(engine_read(2)) == '1': led_ssh_status.value = 0.2
    else: led_ssh_status.off()  
    
    sleep(0.125)

    # /// BREAK SIX ─────────────────────────────────────────────────────────────────────
    ...

    led_ssh_status.off()
    
    sleep(0.125)

    # /// BREAK SEVEN ────────────────────────────────────────────────────────────────────
    ...
    
    sleep(0.125)

    # /// BREAK EIGHT & FINAL CHECKS FOR ROUND ───────────────────────────────────────────
    ...

    if engine_read(1) == '1':
        led_engine_status.value = 0.2

        if engine_read(10) == '3':
            round_x4.value = 0.2
            engine_write(10, 0)
            engine_roundtrip_check(11)

            if engine_read(11) == '3':
                round_x8.value = 0.2
                engine_write(11, 0)
            
            else: ...
        else: engine_roundtrip_check(10)
    else: break
    
    sleep(0.125)