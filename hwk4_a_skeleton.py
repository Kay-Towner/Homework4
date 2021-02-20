import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
#Finished by Kay Towner

class Charge:
    """a charge object defined by its position and
    charge"""
    def __init__(self, xpos=None, ypos=None,
                 charge=None):
        self.xpos = xpos
        self.ypos = ypos
        self.charge = charge

class Potential:
    """a potential object defined by a list of charges"""
    def __init__(self, charges=None, #<--list_of_charge_objects,
                 x_values=None, y_values=None):
        self.charge_list = list_of_charge_objects
        self.x_values = x_values
        self.y_values = y_values
        self.potential = self.calculate_total_potential(self.charge_list)

    def calculate_total_potential(self):
        potential = 0
        for charge in self.charge_list:
            charge_xpos = charge.xpos #<--example of how to
            charge_ypos = charge.ypos
            epsilon = 8.85418782*10^(-12)
            #function inputs here (important positions)
            #(Calc the partials of the potential)
            potential = (((charge) / (4*pi*(epsilon)* charge_xpos)) + ((charge) / (4*pi*(epsilon)*charge_ypos)))#<--function that calculates potential of a charge
            return potential

class Electric_field:
    """an electric field object defined by a potential"""
    def __init__(self, potential=None):
        self.potential = potential
        #deriv
        #analyt_deriv = 
        return None

def dist_between_points(x1, y1, x2, y2):
    """Function to find the distance between
    points (x1,x2) and (y1,y2)
    input: points
    output: the distance between points
    """
    
    x1 = 0
    x2 = 0.05
    y1 = 0 
    y2 = 0.07
    
    x_points = (x2 - x1)
    y_points = (y2 - y1)
    
    dist_x_y = (x_points)^2 - (y_points)^2
    dist = np.sqrt(dist_x_y)
    return dist

if __name__ == "__main__":
    Charge1 = Charge(xpos=-0.05, ypos=0, charge=0.05)
    Charge2 = Charge(xpos=-0.05, ypos=0, charge=0.05)
    #generate x,y values
    spacing = 0.01 #<--spacing 0.01 m = 1 cm
    x_range = np.arange(-0.5, 0.5, spacing)
    y_range = np.arange(-0.5, 0.5, spacing)
    xs, ys  = np.meshgrid(x_range, y_range)
    print('X coordinates')
    print(xs)
    print('Y coordinates')
    print(ys)


#plot the electric field
    widths = np.linspace(0, 2, xs.size)
    plt.quiver(xs, ys, x_range, y_range, linewidth=widths, edgecolors='k')
    plt.show()

    
