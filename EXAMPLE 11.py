
"""A person on average can jump off the ground with a speed of 11 kilometers per hour
without having to fear leaving the Earth's surface. Conversely, if a person jumped
with the same speed while on Halley's Comet, would he or she be able to return to the
surface? Create a program that allows the user to input a launch speed (in kilometers
per hour) from the surface of Halley's Comet, and determine whether the person jumping
will be able to return to the surface. If not, the program will need to calculate how
much more mass the comet would have to have for that to happen.

Hint: the escape velocity is equal to
Vππ ππππ = β(2*πΊ*π)/βπ
where πΊ = 6.67 Γ 10^11π π*π/ ππ*ππ
is the gravitational constant, π is the mass of the celestial
body, and π is the radius. Halleyβs Comet has a mass of 2.2 Γ 10^14 ππ and a
diameter of 9.4ππ ."""

import math

# Gravitational constant in N m^2/kg^2
GRAVITATIONAL_CONSTANT = 6.67 * 10**(-11)

# Mass of Halley's Comet in kg
COMET_MASS = 2.2 * 10**14

# Diameter of Halley's Comet in km
COMET_DIAMETER = 9.4

# Radius of Halley's Comet in km
COMET_RADIUS = COMET_DIAMETER / 2

# Escape velocity of Halley's Comet in km/h
COMET_ESCAPE_VELOCITY = math.sqrt(2 * GRAVITATIONAL_CONSTANT * COMET_MASS / math.sqrt(COMET_RADIUS))

# Prompt user for launch speed in km/h
launch_speed = float(input("Enter launch speed in km/h: "))

# Determine whether the person will be able to return to the surface
if launch_speed >= COMET_ESCAPE_VELOCITY:
  print("The person will be able to return to the surface.")
else:
  # Calculate how much more mass the comet would have to have
  mass_difference = ((launch_speed ** 2) * (COMET_RADIUS ** 2)) / (2 * GRAVITATIONAL_CONSTANT)
  print("The comet would have to have", mass_difference, "kg more mass for the person to be able to return to the surface.")
