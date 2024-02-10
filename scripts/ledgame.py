#ashley 1/20
#if, then control statements 
from include.rcc_library import Raft

myraft= Raft()

favcolor = "blue" 
age = 15

if favcolor == "blue" and age > 13:
    myraft.led_on()
