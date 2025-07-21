import math

def main():
    # Example radius and height of a cylinder
    radius = float(input("Enter the radius of the can (in cm): "))
    height = float(input("Enter the height of the can (in cm): "))

    # Calculate volume, surface area, and storage efficiency
    vol = calculate_volume(radius, height)
    area = calculate_surface_area(radius, height)
    efficiency = calculate_storage_efficiency(vol, area)

    # Display the results
    print(f"\nFor a can with radius {radius} cm and height {height} cm:")
    print(f"Volume: {vol:.2f} cm³")
    print(f"Surface Area: {area:.2f} cm²")
    print(f"Storage Efficiency: {efficiency:.4f}")

def calculate_volume(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * radius**2 * height

def calculate_surface_area(radius, height):
    """Calculate the surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)

def calculate_storage_efficiency(volume, surface_area):
    """Calculate the storage efficiency of a cylinder."""
    return volume / surface_area

# Entry point of the program
if __name__ == "__main__":
    main()