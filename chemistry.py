# This program calculates the molecular weight of a given chemical formula, 
# counts the total number of protons in the molecule, 
# and prints the number of moles based on the user's mass input.

from formula import parse_formula

def make_periodic_table():
    # Create a dictionary to store the elements and their atomic masses
    periodic_table = {
        "Ac": ("Actinium", 227),
        "Ag": ("Silver", 107.8682),
        "Al": ("Aluminum", 26.9815386),
        "Ar": ("Argon", 39.948),
        "As": ("Arsenic", 74.9216),
        "At": ("Astatine", 210),
        "Au": ("Gold", 196.966569),
        "B": ("Boron", 10.811),
        "Ba": ("Barium", 137.327),
        "Be": ("Beryllium", 9.012182),
        "Bi": ("Bismuth", 208.9804),
        "Br": ("Bromine", 79.904),
        "C": ("Carbon", 12.0107),
        "Ca": ("Calcium", 40.078),
        "Cd": ("Cadmium", 112.411),
        "Ce": ("Cerium", 140.116),
        "Cl": ("Chlorine", 35.453),
        "Co": ("Cobalt", 58.933195),
        "Cr": ("Chromium", 51.9961),
        "Cs": ("Cesium", 132.9054519),
        "Cu": ("Copper", 63.546),
        "Dy": ("Dysprosium", 162.5),
        "Er": ("Erbium", 167.259),
        "Eu": ("Europium", 151.964),
        "F": ("Fluorine", 18.9984032),
        "Fe": ("Iron", 55.845),
        "Fr": ("Francium", 223),
        "Ga": ("Gallium", 69.723),
        "Gd": ("Gadolinium", 157.25),
        "Ge": ("Germanium", 72.64),
        "H": ("Hydrogen", 1.00794),
        "He": ("Helium", 4.002602),
        "Hf": ("Hafnium", 178.49),
        "Hg": ("Mercury", 200.59),
        "Ho": ("Holmium", 164.93032),
        "I": ("Iodine", 126.90447),
        "In": ("Indium", 114.818),
        "Ir": ("Iridium", 192.217),
        "K": ("Potassium", 39.0983),
        "Kr": ("Krypton", 83.798),
        "La": ("Lanthanum", 138.90547),
        "Li": ("Lithium", 6.941),
        "Lu": ("Lutetium", 174.9668),
        "Mg": ("Magnesium", 24.305),
        "Mn": ("Manganese", 54.938045),
        "Mo": ("Molybdenum", 95.96),
        "N": ("Nitrogen", 14.0067),
        "Na": ("Sodium", 22.98976928),
        "Nb": ("Niobium", 92.90638),
        "Nd": ("Neodymium", 144.242),
        "Ne": ("Neon", 20.1797),
        "Ni": ("Nickel", 58.6934),
        "Np": ("Neptunium", 237),
        "O": ("Oxygen", 15.9994),
        "Os": ("Osmium", 190.23),
        "P": ("Phosphorus", 30.973762),
        "Pa": ("Protactinium", 231.03588),
        "Pb": ("Lead", 207.2),
        "Pd": ("Palladium", 106.42),
        "Pm": ("Promethium", 145),
        "Po": ("Polonium", 209),
        "Pr": ("Praseodymium", 140.90765),
        "Pt": ("Platinum", 195.084),
        "Pu": ("Plutonium", 244),
        "Ra": ("Radium", 226),
        "Rb": ("Rubidium", 85.4678),
        "Re": ("Rhenium", 186.207),
        "Rh": ("Rhodium", 102.9055),
        "Rn": ("Radon", 222),
        "Ru": ("Ruthenium", 101.07),
        "S": ("Sulfur", 32.065),
        "Sb": ("Antimony", 121.76),
        "Sc": ("Scandium", 44.955912),
        "Se": ("Selenium", 78.96),
        "Si": ("Silicon", 28.0855),
        "Sm": ("Samarium", 150.36),
        "Sn": ("Tin", 118.71),
        "Sr": ("Strontium", 87.62),
        "Ta": ("Tantalum", 180.94788),
        "Tb": ("Terbium", 158.92535),
        "Tc": ("Technetium", 98),
        "Te": ("Tellurium", 127.6),
        "Th": ("Thorium", 232.03806),
        "Ti": ("Titanium", 47.867),
        "Tl": ("Thallium", 204.3833),
        "Tm": ("Thulium", 168.93421),
        "U": ("Uranium", 238.02891),
        "V": ("Vanadium", 50.9415),
        "W": ("Tungsten", 183.84),
        "Xe": ("Xenon", 131.293),
        "Y": ("Yttrium", 88.90585),
        "Yb": ("Ytterbium", 173.054),
        "Zn": ("Zinc", 65.38),
        "Zr": ("Zirconium", 91.224)
    }
    return periodic_table

def main():
    # Get chemical formula and mass from user
    formula = input("Enter the molecular formula (e.g., H2O): ")
    mass = float(input("Enter the mass in grams: "))

    # Call the make_periodic_table function and store the result
    periodic_table = make_periodic_table()

    # Parse the formula to get element counts
    element_counts = parse_formula(formula)
    total_mass = 0
    total_protons = 0

    # Print the name and atomic mass for each chemical element
    print("\nChemical Elements and Their Atomic Masses:")
    for symbol, count in element_counts.items():
        if symbol in periodic_table:
            element_name, atomic_mass = periodic_table[symbol]
            element_total_mass = atomic_mass * count
            total_mass += element_total_mass
            total_protons += count * get_protons(symbol)
            print(f"{element_name}: {atomic_mass} g/mol, Total Mass in {formula}: {element_total_mass:.2f} g")
        else:
            print(f"{symbol} is not a valid element in the periodic table.")

    # Calculate and print total moles
    moles = mass / total_mass if total_mass > 0 else 0
    print(f"\nTotal mass of {formula}: {total_mass:.2f} g")
    print(f"Total number of protons in {formula}: {total_protons}")
    print(f"Number of moles of {formula}: {moles:.4f} mol")

def get_protons(symbol):
    """Return the number of protons for the given element symbol."""
    periodic_table = make_periodic_table()
    # This uses the atomic number based on the periodic table
    atomic_numbers = {
        "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7,
        "O": 8, "F": 9, "Ne": 10, "Na": 11, "Mg": 12, "Al": 13,
        "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19,
        "Ca": 20, "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25,
        "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30, "Ga": 31,
        "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37,
        "Sr": 38, "Y": 39, "Zr": 40, "Nb": 41, "Mo": 42, "Tc": 43,
        "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49,
        "Sn": 50, "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55,
        "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60, "Pm": 61,
        "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67,
        "Er": 68, "Tm": 69, "Yb": 70, "Lu": 71, "Hf": 72, "Ta": 73,
        "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79,
        "Hg": 80, "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85,
        "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90, "Pa": 91,
        "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97,
        "Cf": 98, "Es": 99, "Fm": 100, "Md": 101, "No": 102, "Lr": 103,
        "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109,
        "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115,
        "Lv": 116, "Ts": 117, "Og": 118
    }
    return atomic_numbers.get(symbol, 0)

if __name__ == "__main__":
    main()