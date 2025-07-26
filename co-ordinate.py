import math
class Coordinate:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.point = (x,y)

    def __str__(self):
        return f"Coordinate: {self.point}"

    def dist_from_origin(self):
        return round(math.sqrt(pow(self.x, 2)+ pow(self.y, 2)),2)
    
    def dist_to_another(self, other):
        x_diff = self.point[0] - other.point[0]
        y_diff = self.point[1] - other.point[1]

        return round(math.sqrt(pow(x_diff,2) + pow(y_diff,2)), 2)
    
    def line_equation(self, other):
        x1, y1 = self.point
        x2, y2 = other.point

        if x1 == x2:
            return f"equation of line : {x1}" 
        
        slope = round((self.y - other.y) / (self.x - other.x), 2)
        c = round(y1 - slope * x1, 2)

        return f"Equation of Line : y = {slope} * x + {c}"

    def check_if_point_lies(self, slope, intersept):
        return True if self.y == self.x * slope + intersept else False
    
    def point_to_line_distance(self, slope, coeff_y, intersept):
        '''
        Kindly use the intersept value considering y = mx + c format
        '''
        normalized_dist = math.sqrt(pow(slope, 2) + pow(coeff_y, 2))
        line_mod = abs(slope * self.x + coeff_y * self.y + intersept)

        return round(line_mod / normalized_dist, 2)



