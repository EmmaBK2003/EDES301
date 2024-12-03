"""
--------------------------------------------------------------------------
Smart Curtains
--------------------------------------------------------------------------
License:   
Copyright 2024 Emma Kirchhoff

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

Use the following hardware components to make light-sensitive curtains:  
  - BH1750 Light Sensor
  - 2 Buttons
  - Stepper motor and driver 

User Interaction:
–Pressing the close button will close curtains while pressed
–Pressing the open button will open curtains when pressed
–Light sensor will automatically open curtains when light is 
above a certain threshold value, default is for sunrise but 
can be changed 
–Switch will be implemented to manually turn off light sensor
if user does not want curtains to open from light
 
 """
import time
from button import ThreadedButton
import stepper_motor 
import light as LIGHT

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

LIGHT_THRESHOLD = 400  # Lux level to trigger curtain opening

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class SmartCurtains:
    """Control opening and closing of curtains in response to buttons and light"""

    def __init__(self, open_button_pin, close_button_pin, i2c_bus=1, i2c_address=0x23):
        """Initialize the smart curtains."""

        self.open_button = button.Button(open_button_pin)
        self.close_button = button.Button(close_button_pin)
        self.light_sensor = light.LIGHT(bus=i2c_bus, addr=i2c_address)
        self.stepper_motor = stepper_motor.StepperMotor()
        self.debug = True

        self._setup()

    def _setup(self):
        """Setup the hardware components."""
        self.stepper_motor.stop()

    def open_curtain(self):
        """Open the curtain."""
        if self.debug:
            print("Opening the curtain...")
        self.stepper_motor.open_curtain()

    def close_curtain(self):
        """Close the curtain."""
        if self.debug:
            print("Closing the curtain...")
        self.stepper_motor.close_curtain()

    def check_light_and_open(self):
        """Check the light level and open the curtain if the threshold is exceeded."""
        light_level = self.light_sensor.get_value()
        if self.debug:
            print("Light level: {light_level} Lux")
        if light_level > LIGHT_THRESHOLD:
            self.open_curtain()

    def run(self):
        """Run the smart curtains."""
        if self.debug:
            print("SmartCurtains is running.")
        while True:
            try:
                # Check for button presses
                if self.open_button.is_pressed():
                    self.open_curtain()
                elif self.close_button.is_pressed():
                    self.close_curtain()

                # Check light sensor
                self.check_light_and_open()

                time.sleep(0.1)

            except KeyboardInterrupt:
                # Cleanup on interrupt
                self.cleanup()
                break

    def cleanup(self):
        """Cleanup the hardware components."""
        if self.debug:
            print("Cleaning up hardware.")
        self.stepper_motor.stop()
        self.open_button.cleanup()
        self.close_button.cleanup()

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    print("Smart Curtains Program Start")

    # Instantiate the smart curtains
    smart_curtains = SmartCurtains(open_button_pin="P2_04", close_button_pin="P2_02")

    try:
        # Run the smart curtains
        smart_curtains.run()

    except KeyboardInterrupt:
        # Clean up hardware on exit
        smart_curtains.cleanup()

    print("Program Complete")

