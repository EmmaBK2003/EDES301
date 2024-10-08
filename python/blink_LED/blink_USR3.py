"""
--------------------------------------------------------------------------
Blink USR3 LED
--------------------------------------------------------------------------
License:   
Copyright 2021-2024 - Emma Kirchhoff

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Blink USR3 LED

This program uses the Adafruit_BBIO library to blink the USR3 
LED on a PocketBeagle computer at 5 Hz (5 on/off cycles per second).
The LED will blink continuously until program is exited or user 
presses Ctrl+C to terminate loop. 

--------------------------------------------------------------------------
"""

import time
import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

USR3_LED_PIN    = "USR3"      # USR3 LED pin on PocketBeagle
BLINK_FREQUENCY = 5           # Blink frequency of LED in Hz
SLEEP_TIME      = 1.0 / (2 * BLINK_FREQUENCY)  # Sleep time for 5 Hz blinking

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def setup():
    """ Setup the USR3 LED pin """
    GPIO.setup(USR3_LED_PIN, GPIO.OUT)
    
# End def

def blink_led():
    """ Blink the USR3 LED on and off at 5 Hz """
    while True:
        GPIO.output(USR3_LED_PIN, GPIO.HIGH)  # Turn on the LED
        time.sleep(SLEEP_TIME)                # Wait for half a cycle
        GPIO.output(USR3_LED_PIN, GPIO.LOW)   # Turn off the LED
        time.sleep(SLEEP_TIME)                # Wait for half a cycle

# End def

def cleanup():
    """ Cleanup the GPIO settings """
    GPIO.cleanup()
    
# End def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    print("Blinking USR3 LED at 5 Hz.")
    
    # Use a Keyboard Interrupt (i.e., "Ctrl-C") to exit the blinking loop
    try:
        setup()         # Set up the LED pin
        blink_led()     # Start blinking the LED
    except KeyboardInterrupt:
        pass
    finally:
        print("\nCleaning up...")
        cleanup()       # Clean up the GPIO settings

    print("Program ended.")
# End main
