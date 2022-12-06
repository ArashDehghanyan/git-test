from mod1 import double_
from mod2 import halve
from mod3 import inc_

if __name__ == "main::
    x = 10
    y = double_(inc_(halve(x)))
    print(y)
