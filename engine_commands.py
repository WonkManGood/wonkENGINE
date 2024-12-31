from re import findall, compile
import subprocess

expression = compile(r'.\d')
def find(i):
    return (findall(expression, i))[0]

def engine_write(line, value):
    try:
        line = int(line) - 1
        value = str(value)
    except: return _

    with open('/home/ej/wonkENGINE/engine_comms', 'r') as f:
        lines = f.readlines()
        lines[line] = ''
        lines[line] = str('{ '+value+' }\n')
        with open('/home/ej/wonkENGINE/engine_comms', 'w') as f:
            f.writelines(lines)

def engine_read(line):
    line = line - 1
    with open('/home/ej/wonkENGINE/engine_comms', 'r') as f:
        return str(find(f.readlines()[line])).strip()

def engine_check_node01(value):
    command = ['ping', '-c', '1' , '192.168.0.11']
    ran = subprocess.run(command, capture_output=True)
    print(ran.stdout)
    print(ran.stderr)
engine_check_node01(1)