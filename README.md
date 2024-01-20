lorentz factor calculation (lorentz_factor function):
   - this function calculates the lorentz factor, a crucial term in special relativity equations.
   - ![image](https://github.com/danielstevanusp/Twin-Paradox/assets/157248078/cc915cb3-7481-4e02-b644-b4cee7fc49e6)

time dilation calculation (time_dilation function):
   - this function uses the lorentz factor to calculate time dilation.
   - formula: ![Screenshot 2024-01-21 062522](https://github.com/danielstevanusp/Twin-Paradox/assets/157248078/72439fc1-40b4-4660-b2a2-07232e11a63f) is the lorentz factor.

twin paradox simulation (twin_paradox function):
   - simulates the twin paradox scenario in special relativity.
   - takes user inputs for earth's velocity, spaceship's velocity, and elapsed time on earth.
   - calculates time dilation effect and prints elapsed time on both earth and the spaceship.

how to use:
   - run python3 twin-paradox.py
   - enter earth's velocity, spaceship's velocity, and elapsed time on earth when prompted.
   - the tool calculates and displays the elapsed time on both earth and the spaceship.

example:
   
   example input:
   enter relative velocity on earth (in m/s): 50000
   enter relative velocity of the spaceship (in m/s): 250000
   enter elapsed time on earth (in years): 10

   output:
   elapsed time on earth: 10 years
   elapsed time on the spaceship: 8.660254037844385 years

disclaimer: sorry if there are errors and calculations in the code, i'm still learning to improve it.
