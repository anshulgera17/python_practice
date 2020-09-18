import math
class Tire:
    """
    """
    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self):
        """
        represent tires
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}" 
                + f"{self.construction}{self.diameter}" )

    def circumference(self):
        """
        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        8.1
        """
        side_wall_inches = (self.width * (self.ratio / 100 )) / 25.4
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4

class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        The circumference of a tire w/ snow chains in inches.
        >>> tire = SnowTire('P', 205, 65, 15, 2) 
        >>> tire.circumference()
        92.7
        """    
        total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1 )

    def __repr__(self):
        return super().__repr__() + "  (Snow) "