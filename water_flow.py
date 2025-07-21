# water_flow.py
# water_flow.py

def water_column_height(tower_height, tank_height):
    """Calculate the height of a column of water."""
    return tower_height + tank_height

def pressure_gain_from_water_height(height):
    """Calculate the pressure caused by Earth's gravity on the water."""
    density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density * gravity * height) / 1000  # Pressure in kPa

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate the pressure loss due to friction in a pipe."""
    density = 998.2  # kg/m^3
    return -(friction_factor * pipe_length * density * fluid_velocity**2) / (2 * pipe_diameter)

def pressure_loss_from_fittings(fitting_coefficient, fluid_velocity):
    """Calculate the pressure loss due to fittings."""
    density = 998.2  # kg/m^3
    return -(fitting_coefficient * density * fluid_velocity**2) / 2

def reynolds_number(diameter, fluid_velocity, kinematic_viscosity):
    """Calculate the Reynolds number."""
    return (fluid_velocity * diameter) / kinematic_viscosity

def pressure_loss_from_pipe_reduction(diameter_in, diameter_out, fluid_velocity):
    """Calculate the pressure loss due to a reduction in pipe diameter."""
    density = 998.2  # kg/m^3
    return density * fluid_velocity**2 * ((1 / diameter_out**2) - (1 / diameter_in**2)) / 2

def main():
    # Example values
    tower_height = 10  # meters
    tank_height = 5  # meters
    pipe_diameter = 0.1  # meters
    pipe_length = 50  # meters
    friction_factor = 0.02
    fluid_velocity = 2  # m/s
    fitting_coefficient = 0.5
    kinematic_viscosity = 1.003e-6  # m^2/s
    diameter_in = 0.1  # meters
    diameter_out = 0.05  # meters

    # Function calls for testing
    height = water_column_height(tower_height, tank_height)
    pressure_gain = pressure_gain_from_water_height(height)
    pressure_loss_pipe = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
    pressure_loss_fittings = pressure_loss_from_fittings(fitting_coefficient, fluid_velocity)
    re_number = reynolds_number(pipe_diameter, fluid_velocity, kinematic_viscosity)
    pressure_loss_reduction = pressure_loss_from_pipe_reduction(diameter_in, diameter_out, fluid_velocity)

    # Output results
    print(f"Water Column Height: {height} m")
    print(f"Pressure Gain: {pressure_gain} kPa")
    print(f"Pressure Loss from Pipe: {pressure_loss_pipe} kPa")
    print(f"Pressure Loss from Fittings: {pressure_loss_fittings} kPa")
    print(f"Reynolds Number: {re_number}")
    print(f"Pressure Loss from Pipe Reduction: {pressure_loss_reduction} kPa")

if __name__ == "__main__":
    main()