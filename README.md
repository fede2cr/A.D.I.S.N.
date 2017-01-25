# A.D.I.S.N.
An aproximation of the A.D.I.S.N. notebook from Project MC2

## Description
An artisanal notebook with electronic componets in order to aproximate some of the behavior for the notebook A.D.I.S.N. from the series Project MC2

## Components
Initially I wanted to use a CircuitPython to use the LED ring as well as the microphone and other componets. But unfortunately, this board doesn't have enough pins for the Music Maker sound board.

This is the current components list:

- Microcontroler ESP8266 Feather Huzzah from Adafruit
- 8x8 Matrix Backpack from Adafruit, for A.D.I.S.N.'s face
- Neopixel Ring from Adafruit for backlight in the cover
- Music Maker FeatherWing from Adafruit
- Mono 2.5W Class D Audio Amplifier from Adafruit
- 40mm Thin Speaker
- Lithium Ion Polymer Battery (350mAh or 250mAh)
- Pyralux (Flexible PCB) for 3.3V and GND connections
- Kapton tape to cover the Pyralux 3.3V and GND connections

## Functions
We are trying to emulate the notebook as much as possible with the available hardware.

Most of the funtions will be activated by using the copper tape inside the notebook to detect open/close pages.

- Light up the cover by using the Neopixel Ring, under a light diffuser made out of paper. The light pattern tries to follow closely with the audio. Since the ESP8266 doesn't have a microphone, I'll have to fake this somehow.
- Play audio fraces from the series. The audiofiles for this won't be shared because of possible copyright issues.
- Emulate the face for A.D.I.S.N. by using the 8x8 LED Matrix.
- Coordinate light on the cover, faces on the inside with the audio fraces.

### Wishlist
This I want to include in the project:

- CircuitPython
- Web REPL interface for simple control
- AP with webapp, for controlling from cellphone

### This, it won't do (yet?)

- Speech Synth
- AI Chatbot
- RFID bracelet for authentication, and some form of lock
