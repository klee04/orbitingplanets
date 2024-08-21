
class Vector:
    # class constructor
    def __init__(self, x: float=0, y: float=0, z: float=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    # unbambiguous representation of the object
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    # proper vector notation
    def __str__(self) -> str:
        return f"{self.x}i + {self.y}j + {self.z}k"

    # vector indexing
    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        if index == 2:
            return self.z
        raise IndexError("Index out of range")
    
    # vector addition
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x,y,z)
    
    # vector subtraction
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x,y,z)
    
    # scalar multiplication and dot product
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            z = self.z * other
            return Vector(x,y,z)
        elif isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z 
            return x + y + z
        else:
            raise TypeError("Invalid operand type")
    
    # scalar division
    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            x = self.x / other
            y = self.y / other
            z = self.z / other
            return Vector(x,y,z)
        else:
            raise TypeError("Invalid operand type")
    
    # vector magnitdue 
    def get_magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    # normalize vector
    def normalize(self):
        magnitude = self.get_magnitude()
        x = self.x / magnitude
        y = self.y / magnitude
        z = self.z / magnitude 
        return Vector(x,y,z)