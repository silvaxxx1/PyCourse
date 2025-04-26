# --- Logic Functions ---

# Circle Functions
def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return 3.14159 * (radius ** 2)

def calculate_circle_perimeter(radius):
    """Calculate the perimeter (circumference) of a circle."""
    return 2 * 3.14159 * radius

# Rectangle Functions
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_rectangle_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

# Triangle Functions
def calculate_triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def calculate_triangle_perimeter(side1, side2, side3):
    """Calculate the perimeter of a triangle."""
    return side1 + side2 + side3

# --- Usage Example ---

# Circle calculations
radius = 5
circle_area = calculate_circle_area(radius)
circle_perimeter = calculate_circle_perimeter(radius)
print(f"Circle - Area: {circle_area:.2f}, Perimeter: {circle_perimeter:.2f}")

# Rectangle calculations
length = 10
width = 4
rectangle_area = calculate_rectangle_area(length, width)
rectangle_perimeter = calculate_rectangle_perimeter(length, width)
print(f"Rectangle - Area: {rectangle_area:.2f}, Perimeter: {rectangle_perimeter:.2f}")

# Triangle calculations
side1 = 3
side2 = 4
side3 = 5
base = 4
height = 3
triangle_area = calculate_triangle_area(base, height)
triangle_perimeter = calculate_triangle_perimeter(side1, side2, side3)
print(f"Triangle - Area: {triangle_area:.2f}, Perimeter: {triangle_perimeter:.2f}")
