# string animation just like chat gpt
x = '''Any paragraph here which u need to print,
Any paragraph here which u need to print,Any paragraph here which u need to print,
Any paragraph here which u need to print,Any paragraph here which u need to print,
Any paragraph here which u need to print,Any paragraph here which u need to print,
Any paragraph here which u need to print,Any paragraph here which u need to print,'''

import time


def printA(x):
    for i in x:
        print(i, end='', flush=True)
        time.sleep(0.04)
printA(x)