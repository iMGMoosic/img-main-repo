# Metro Transit CLI Tool

The Metro Transit CLI Tool is an unofficial Python 3.10 tool to pull Metro Transit bus departure times for specific routes.

## Features / To-Dos

- [x] Prints bus departure times for specified routes
- [ ] Outputs to an RGB LED matrix powered by a Raspberry Pi
- [ ] Outputs estimated time to a specified stop on the same route

## Installation

### Requirements

- requests

You can install requirements by either running the Python script (the script attempts to install dependencies if import fails) or by using pip on the command-line

```bash
pip install requests
```

### Usage

```bash
python main.py
```

Make sure to modify the JSON file before running, otherwise the default values will be used.

## Settings

| Setting                 | Type    | Description                                                 | Default Values |
| ----------------------- | ------- | ----------------------------------------------------------- | -------------- |
| preferred               |         | Options for preferred routes and stops                      | N/A            |
| preferred_stops         | Array   | An array of preferred stops                                 | ["17978"]      |
| preferred_routes        | Array   | An array of preferred routes                                | ["11", "18"]   |
| settings                |         | Application settings                                        | N/A            |
| refresh_rate_seconds    | Integer | How long between data refreshes in seconds                  | 60             |
| print_delay             | Bool    | (currently unused) Prints delay of current trip             | true           |
| print_delayed_departure | Bool    | (currently unused) Prints departure time factoring in delay | true           |

## Flags

Disregard this section for now, as the RGBMatrix implementation hasn't been finished yet.

You can configure the LED matrix with the same flags used in the [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library. More information on these arguments can be found in the library documentation.

| Flag                     | Description                                                                                                                                         | Default Value    |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| --led-rows               | Display rows. 16 for 16x32, 32 for 32x32                                                                                                            | 32               |
| --led-cols               | Panel columns. Typically 32 or 64                                                                                                                   | 32               |
| --led-chain              | Daisy-chained boards                                                                                                                                | 1                |
| --led-parallel           | For Plus-models or RPi2: parallel chains. 1-3                                                                                                       | 1                |
| --led-pwm-bits           | Bits used for PWM. Range 1-11                                                                                                                       | 11               |
| --led-brightness         | Sets brightness level. Range: 1-100                                                                                                                 | 100              |
| --led-gpio-mapping       | Hardware Mapping: regular, adafruit-hat, adafruit-hat-pwm                                                                                           | adafruit-hat-pwm |
| --led-scan-mode          | Progressive or interlaced scan. 0 = Progressive, 1 = Interlaced                                                                                     | 1                |
| --led-pwm-lsb-nanosecond | Base time-unit for the on-time in the lowest significant bit in nanoseconds.                                                                        | 130              |
| --led-show-refresh       | Shows the current refresh rate of the LED panel.                                                                                                    | false            |
| --led-slowdown-gpio      | Slow down writing to GPIO. Range: 0-4                                                                                                               | 1                |
| --led-no-hardware-pulse  | Don't use hardware pin-pulse generation                                                                                                             | false            |
| --led-rgb-sequence       | Switch if your matrix has led colors swapped                                                                                                        | RGB              |
| --led-pixel-mapper       | Apply pixel mappers. e.g Rotate:90, U-mapper                                                                                                        | none             |
| --led-row-addr-type      | 0 = default; 1 = AB-addressed panels                                                                                                                | 0                |
| --led-multiplexing       | Multiplexing type: 0 = direct; 1 = strip; 2 = checker; 3 = spiral; 4 = Z-strip; 5 = ZnMirrorZStripe; 6 = coreman; 7 = Kaler2Scan; 8 = ZStripeUneven | 0                |
| --led-limit-refresh=<Hz> | Limit refresh rate to this frequency in Hz. Useful to keep a constant refresh rate on loaded system. 0 = no limit                                   | 0                |
| --led-pwm-dither-bits    | Time dithering of lower bits                                                                                                                        | 0                |
| --config                 | Specify a configuration file name other, omitting json xtn                                                                                          | config           |

## Contributing

Contributions are very much appreciated, especially if you have experience working with hzeller's rpi-rgb-led-matrix library.
