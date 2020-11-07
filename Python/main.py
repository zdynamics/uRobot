import Movements as mv
import numpy as np
import Robot

# 1. Create robot's generalized coordinates (as two dimensional array) and links' lengths
q = np.random.rand(1, 4)
L = [600, 300, 200]

# 2. Create robot as an object
uRobot = Robot.System(jointsPositions = q, linksLengths = L, name = 'uRobot')

# 3. Set rigid bodies' Denavit - Hartenberg parameters
uRobot.denavitHartenberg()

"""
  4. Compute robot's forward kinematics
"""
uRobot.forwardKinematics(q, L, m = 5)

"""
  5. Plot robot (uncomment any of these)
"""
# uRobot.plot()

"""
  5.1 Plot robot with new joints' positions (this also modifies them in the object)
"""
# uRobot.plot(np.random.rand(1, 4))

"""
  5.2 Plot robot animation, iterating joints' positions (this also modifies them in the object). «delayPerFrame» in milliseconds
""" 
# uRobot.plot(q = np.array([np.linspace(-np.pi, np.pi, 50) for column in range(4)]).T, delayPerFrame = 100)

"""
  6. Compute Axis - Angle vector using Homogeneous Transformation Matrices (if necessary. This is OPTIONAL)
""" 

