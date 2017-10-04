## Synopsis

This is a quick lib I created in order to utilize the functionality of PCF85474 chip.
The code simple and self explanatory. I used for raspberry pi but it should work anywhere with i2c bus.

## Code Example

pcf = PyPCF8547(0x20, 1)

pcf.set_pin(6, True)
\# Set Pin

print pcf.get_pin(6)
\# Get Pin


## Motivation

The Raspberry Pi's GPIOS pins were not enough for my project so I used the PCF8547 chip to add 8 more.


## Tests

The above code example is included in file test.py

## License

Just do whatever you want with that.
