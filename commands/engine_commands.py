import subprocess

def engine_write(line, value):
    try:
        line = int(line) - 1
        value = str(value)
    except ValueError: ...

    with open('/home/ej/wonkENGINE/engine_comms', 'r') as f:
        lines = f.readlines()
        lines[line] = ''
        lines[line] = str(value+'\n')
        with open('/home/ej/wonkENGINE/engine_comms', 'w') as f:
            f.writelines(lines)

def engine_read(line):
    line = line - 1
    with open('/home/ej/wonkENGINE/engine_comms', 'r') as f:
        lines = f.readlines()
        return str(lines[line][0])

def engine_check_node01(value):
    command = ['ping', '-c', '1' , '192.168.0.11']
    ran = subprocess.run(command, capture_output=True)
    print(ran.stdout)
    print(ran.stderr)

def engine_roundtrip_check(line):
    with open('/home/ej/wonkENGINE/engine_comms', 'r') as f:
        lines = f.readlines()

        try:
            value = int(lines[(line - 1)][0])
        except ValueError: ...

        value = value + 1

        engine_write(line, value)




