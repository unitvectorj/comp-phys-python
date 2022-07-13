# comp-phys-python

A collection of simple, single purpose programs to simulate physical systems and generate visualizations using matplotlib. Each script reproduces plots from [*Computational Physics, 2nd Ed.*](https://www.amazon.com/Computational-Physics-2nd-Nicholas-Giordano/dp/0131469908)  by N. Giordano and H. Nakanishi. These were written as assignments in a collegiate computational physics course and may be freely used to aid in any application. Please do not copy this work in order to complete school assignments.

#### Dependencies:
Matplotlib must be installed to generate plots. Install it with 'pip install matplotlib'.

## List of program groups:

### 1. **Bicycle**
  - bicycle.py: Calculates velocity vs. time with and without simplified air resistance, given a constant amount of work.

### 2. **Baseball**
  - baseball-trajectory-wind.py: calculates the arc of a pop fly under different wind conditions. Simplified wind.
  - baseball-curveball.py: calculates drop and curve of a curveball.
  
### 3. **Simple Pendulum**
  - simple-pendulum.py: simulates pendulum motion with zero drag and wind resistance.
  - driven-simple-pendulum.py: simulates three pendulums with drag and different driving forces.

### 4. **Billiards** (bouncing ball off containing walls)
   - billiards-circular.py: simple bouncing off inner-walls of circle
   - billiards-stadium.py: same but with small flat section in the middle, altering the shape and bouncing behavior

### 5. **Planetary Precession**
   - <u>elliptical-orbit-left.py</u>: simulates planet with large precession rate
   - <u>elliptical-orbit-right.py</u>: simulates planet with low precession rate
   - <u>mercury.py</u>: simulates Mercury's high precession rate

### 6. **3 Body Problem**
   - <u>jupiter_1.py</u>: simulates Jupiter's effect on Earth's orbit at its actual mass.
   - <u>jupiter_10.py</u>: simulates Jupiter's effect on Earth's orbit if it had 10 times its actual mass.
   - <u>jupiter_1000.py</u>: simulates Jupiter's effect on Earth's orbit if it had 1000 times its actual mass

### 7. **Electric Potential Field**
   - Generates 3 plots to illustrate the electrical potential fields around 3 different objects. Shows equipotential lines, a 3D representation of the field strength in 2D, and a vector field.
   - <u>1_square_conductor.py</u>: shows electric potential field around a square cnducting plate
   - <u>2_parallel_plates.py</u>: shows the electric potential field around and between 2 conducting plates of opposite charge.
   - <u>3_point_charge.py</u>: shows the electric potential field around a positive point charge.

*more soon*
