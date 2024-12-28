from time import sleep
from gpiozero import PWMLED
from re import findall, compile

expression = compile(r'.\d')
def find(i):
    return (findall(expression, i))[0]

def engine_write(line, value):
    try:
        line = int(line)
        value = str(value)
    except: return _

    with open('./engine_comms', 'r') as f:
        lines = f.readlines()
        lines[line] = ''
        lines[line] = str('{ '+value+' }\n')
        with open('./engine_comms', 'w') as f:
            f.writelines(lines)

def engine_read(line):
    line = line - 1
    with open('./engine_comms', 'r') as f:
        return str(find(f.readlines()[line])).strip()

# /// LEDS
led_engine_status = PWMLED(17)


while  engine_read(1) == '1':
    # /// BREAK ONE
    ...

    if engine_read(1) === '1':

    
    sleep(0.125)

    # /// BREAK TWO
    ...
    
    sleep(0.125)

    # /// BREAK THREE
    ...
    
    sleep(0.125)

    # /// BREAK FOUR
    ...
    
    sleep(0.125)

    # /// BREAK FIVE
    ...
    
    sleep(0.125)

    # /// BREAK SIX
    ...
    
    sleep(0.125)

    # /// BREAK SEVEN
    ...
    
    sleep(0.125)

    # /// BREAK EIGHT
    ...
    
    sleep(0.125)