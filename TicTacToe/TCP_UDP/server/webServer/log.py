import time
from colorama import Fore, Back, Style
timeFormat = "%Y.%m.%d @ %H:%M:%S"
def log(*args, **kwargs):
    print("LOG ", Fore.GREEN, time.strftime(timeFormat, time.gmtime())+":",Style.RESET_ALL, *args, **kwargs)

def warn(*args, **kwargs):
    print("WARN", Fore.BLUE, time.strftime(timeFormat, time.gmtime())+":",Style.RESET_ALL, *args, **kwargs)

def err(*args, **kwargs):
    print("ERR ",Fore.RED, time.strftime(timeFormat, time.gmtime())+":",Style.RESET_ALL, *args, **kwargs)
