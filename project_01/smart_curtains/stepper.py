"""
--------------------------------------------------------------------------
Stepper Driver
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

Driver for control of curtain opening and closing mechanisms using stepper motor, 
control driver using GPIO pins

Uses: 
  - 28BYJ-48 Stepper Motor and Driver Board (4 GPIO pins to control)

open_curtain() rotates motor pre-specified amount of steps forward
close_curtain() rotates motor same amount of steps but backwards


"""

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

import time
import Adafruit_BBIO.GPIO as GPIO

class StepperMotor:
    """ Stepper motor driver class for controlling stepper motor to open/close curtains. """
    
    def __init__(self, pin_a, pin_b, pin_c, pin_d):
        # Motor pin setup
        self.pins = [pin_a, pin_b, pin_c, pin_d]
        self.current_state = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
        self.step_sequence = [
            [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH],  # Step 1
            [GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW],  # Step 2
            [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],  # Step 3
            [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH]   # Step 4
        ]
        
        # Set up the GPIO pins as outputs
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

        # Initialize the motor to the "stopped" state
        self.is_open = False
        self.is_moving = False
      
      # End def

    def _step(self, sequence):
        """ Step the motor one step in the current direction. """
        for i in range(4):
            GPIO.output(self.pins[i], sequence[i])
        time.sleep(0.01)
      
      # End def

    def open_curtain(self):
        """ Open the curtain by rotating the stepper motor. """
        if self.is_moving:
            print("Motor is already moving.")
            return
        
        print("Opening curtain...")
        self.is_moving = True
        self.is_open = False
        
        # Rotate stepper motor to open curtain
        # Adjust steps based on curtain opening mechanism
        for _ in range(512):  
            self._step(self.step_sequence[0])
            self._step(self.step_sequence[1])
            self._step(self.step_sequence[2])
            self._step(self.step_sequence[3])
        
        self.is_open = True
        self.is_moving = False
        print("Curtain is open.")
      
      # End def

    def close_curtain(self):
        """ Close the curtain by rotating the stepper motor. """
        if self.is_moving:
            print("Motor is already moving.")
            return
        
        print("Closing curtain...")
        self.is_moving = True
        self.is_open = True
        
        # Rotate stepper motor to close curtain
        # Adjust steps based on curtain closing mechanism
        for _ in range(512):  
            self._step(self.step_sequence[3])
            self._step(self.step_sequence[2])
            self._step(self.step_sequence[1])
            self._step(self.step_sequence[0])
        
        self.is_open = False
        self.is_moving = False
        print("Curtain is closed.")
      
      # End def

    def is_stopped(self):
        """ Check if the stepper motor is stopped """
        return not self.is_moving
      
      # End def

    def is_open(self):
        """ Return True if the curtain is open, otherwise False. """
        return self.is_open
      
      # End def

    def cleanup(self):
        """ Clean up GPIO pins when done. """
        for pin in self.pins:
            GPIO.cleanup(pin)
          
      # End def

# End Class

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

import time

    """Test the stepper motor functionality."""
    print("Stepper Motor Test")
    
    # Initialize the stepper motor
    # Specify the pins connected to IN1, IN2, IN3, IN4
    motor_pins = [P2_18, P2_20, P2_22, P2_24]
    motor = StepperMotor(motor_pins)

    try:
        # Test: Open curtains
        print("Opening curtains...")
        motor.open_curtain()
        time.sleep(2)  # Allow time for the motor to complete opening
        motor.stop()
        print("Curtains opened.")

        # Pause before closing
        time.sleep(2)

        # Test: Close curtains
        print("Closing curtains...")
        motor.close_curtain()
        time.sleep(2)  # Allow time for the motor to complete closing
        motor.stop()
        print("Curtains closed.")
        
        # Use a Keyboard Interrupt (i.e. "Ctrl-C") to exit the test
        print("Test interrupted by user.")
      
    finally:
        # Cleanup the motor resources
        print("Cleaning up...")
        motor.cleanup()
        print("Test complete.")

if __name__ == "__main__":
    main()




