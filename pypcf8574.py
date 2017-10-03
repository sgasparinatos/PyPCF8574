import smbus
import math

#lib for


class PyPCF8574:

    def __init__(self, addr=0x20, bus=1):
        self.address = addr
        self.pin_array = [False, False, False, False, False, False, False, False]
        self.bus = smbus.SMBus(bus)

    def set_number(self, num):
        try:
            self.bus.write_byte(self.address, num)
        except Exception as ex:
            print "SMBus Error:", ex
            return

    def set_pin(self, pin_num, status):
        self.pin_array[pin_num] = status
        self.set_number(255 - self.bool_to_int())  # subtract 255 to get the complement

    def bool_to_int(self):
        out = 0
        for i in range(8):
            if self.pin_array[i]:
                out += math.pow(2, i)

        return int(out)

    def int_to_bool(self, n):
        try:
            ar = list(reversed([bool(int(digit)) for digit in bin(n)[2:].rjust(8, '0')]))
            # [2:] to chop off the "0b" part
        except Exception as ex:
            print ex
            return None

        return ar

    def get_pin(self, pin_num):
        self.set_pin(pin_num, False)
        res = self.int_to_bool(self.get_number())
        if res is None:
            return None

        return res[pin_num]

    def get_number(self):
        try:
            in_byte = self.bus.read_byte(self.address)
        except Exception as ex:
            print ex
            return None

        return in_byte
