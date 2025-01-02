from sys import path as sys_path
from os import path as os_path
sys_path.append(os_path.abspath(os_path.join(os_path.dirname(__file__), '..')))

from commands.engine_commands import engine_write

engine_write(2, 0)