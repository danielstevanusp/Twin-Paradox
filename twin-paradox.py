import math

def lorentz_factor(velocity):
    # Calculate Lorentz factor
    return 1 / math.sqrt(1 - (velocity ** 2 / (299792458 ** 2)))

def time_dilation(time, velocity):
    # Calculate time dilation
    gamma = lorentz_factor(velocity)
    return time / gamma

def twin_paradox():
    # Twin Paradox scenario
    earth_velocity = float(input("Enter relative velocity on Earth (in m/s): "))
    spaceship_velocity = float(input("Enter relative velocity of the spaceship (in m/s): "))
    earth_time = float(input("Enter elapsed time on Earth (in years): "))

    # Twin's journey to a distant star
    spaceship_time = earth_time / lorentz_factor(spaceship_velocity)

    print(f"\nElapsed time on Earth: {earth_time} years")
    print(f"Elapsed time on the spaceship: {spaceship_time} years")

if __name__ == "__main__":
    twin_paradox()
