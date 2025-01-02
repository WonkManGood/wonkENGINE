def engine_write(line, value):
    try:
        line = int(line) - 1
        value = str(value)
    except: return _

    with open('engine_comms', 'r') as f:
        lines = f.readlines()
        lines[line] = ''
        lines[line] = str(value+'\n')
        with open('engine_comms', 'w') as f:
            f.writelines(lines)

engine_write(1, 0)