import unittest
import math
from plane_point_gen import *

class TestSpherePointGenerationMethods(unittest.TestCase):

    def test_can_generate_1_points_on_plane_within_a_radius(self):
        position = [0, 0, 0]
        normal = [0, 0, 1]
        radius = 5

        points = generate_points_on_plane(position, normal, radius, number_of_points=1)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def assert_calculated_points_lie_on_plane(self, position, normal, radius, points):

        norm = np.asarray(normal)
        
        for point in points:
            a = np.asarray(point)
            p = np.asarray(position)
            aMinusP = (a - p)

            dotProd = np.dot(norm, aMinusP)

            self.assertAlmostEqual(dotProd, 0, places=7, msg=None, delta=None)

            vector = []
            for i in range(len(a)):
                vector.append(a[i] - p[i])

            magnitude = math.sqrt(pow(vector[0], 2) + pow(vector[1], 2) + pow(vector[2], 2))
            self.assertAlmostEqual(magnitude, radius, places=7, msg=None, delta=None)

if __name__=="__main__":
    unittest.main()