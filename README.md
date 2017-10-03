## Synopsis

At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)


## Code Example


pcf = PyPCF8547(0x20, 1)
# Set Pin
pcf.set_pin(6, True)
# Get Pin
print pcf.get_pin(6)

## Motivation

The Raspberry Pi's GPIOS pins were not enough for my project so I used the PCF8547 chip to add 8 more.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## License

Just do what ever you want with that.
