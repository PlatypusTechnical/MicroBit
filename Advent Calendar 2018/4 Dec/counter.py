#Uses the TM1637 module from https://github.com/mcauser/microbit-tm1637
#Install it using the files feature in Mu (see: PTC blog)

from microbit import *
from tm1637 import TM1637
tm = TM1637(clk=pin1, dio=pin2)

tm.show('cool')