from pypcf8574 import PyPCF8574
import time

def test_relay(pcf):
    # test a relay on pin 3
    while True:
        pcf.set_pin(3, True)
        print "OPEN"
        time.sleep(2)
        pcf.set_pin(3, False)
        print "CLOSE"
        time.sleep(2)

def read_pin(pcf, pin_num):
    # read pin 6 of pcf
     while True:
        time.sleep(1)
        print str(int(time.time()))," P" + str(pin_num) + ":", pcf.get_pin(pin_num)

if __name__ == '__main__':
    pcf = PyPCF8574(0x20, 1)
    test_relay(pcf)
    # read_pin(pcf, 6)

