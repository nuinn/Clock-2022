from time import sleep
import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
# now call function we defined above
uh = input("Set hour:")
h = int(uh)
um = input("Set minute:")
m = int(um)
us = input("Set seconds:")
s = int(us)
while s >= 00:
    s = s + 1
    if s == 60:
        s = 00
        m = m + 1
        if m == 60:
            m = 00
            h = h + 1
            if h == 24:
                h = 00
    sleep(1)
    screen_clear()
    print("%02d" % (h,),":","%02d" % (m,),":","%02d" % (s,))
