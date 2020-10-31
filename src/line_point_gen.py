import numpy as np
#import argparse as argparse
import math

class PointGenerationException(Exception):
    #Raised when an error occurs generating point data
    pass


def generate_points_on_line(start_point, end_point, number_of_points):
   
   if number_of_points <= 0:
      raise PointGenerationException('Line Point Generation: num of points should be at least 1. Actual value {}'.format(number_of_points))

   s_p = np.asarray(start_point)
   e_p = np.asarray(end_point)

   #Calculate vector
   vec = (e_p - s_p)

   #Calculate vector magnitude
   mag = math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2) + math.pow(vec[2], 2))

   if mag == 0.0:
      raise PointGenerationException('Line Point Generation: Start and End Point cannot be the same')
   
   #Calculate vector normal
   normaliser = 1.0 / mag
   vec_norm = [i * normaliser for i in vec]

   #Generate points
   line_points = []

   for _ in range(number_of_points):
      distance = np.random.uniform(0.0, mag)
      offset = [i * distance for i in vec_norm]
      generated_point = s_p + offset
      line_points.append(generated_point)

   return line_points