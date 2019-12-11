import unittest
import math
from sphere_point_gen import *

class TestSpherePointGenerationMethods(unittest.TestCase):

    def test_can_generate_5_points_on_sphere_at_origin(self):

        position = [0, 0, 0]
        radius = 10

        points = generate_points_on_sphere(position, radius, number_of_points=5)
        #print(points)
        self.assert_calculated_points_lie_on_sphere_surface(position, radius, points)

    # def test_can_generate_10_points_on_sphere_at_origin(self):
    #     self.assertTrue(False)

    # def test_can_generate_100_points_on_sphere_away_from_origin(self):
    #     self.assertTrue(False)

    # def test_can_generate_5_points_on_sphere_away_from_origin(self):
    #     self.assertTrue(False)

    # def test_can_generate_10_points_on_sphere_away_from_origin(self):
    #     self.assertTrue(False)

    # def test_can_generate_100_points_on_sphere_away_from_origin(self):
    #     self.assertTrue(False)

    # def test_can_generate_5_points_on_sphere_with_large_radius(self):
    #     self.assertTrue(False)

    # def test_can_generate_10_points_on_sphere_with_large_radius(self):
    #     self.assertTrue(False)

    # def test_can_generate_100_points_on_sphere_with_large_radius(self):
    #     self.assertTrue(False)

    # def test_can_generate_5_points_on_sphere_with_small_radius(self):
    #     self.assertTrue(False)

    # def test_can_generate_10_points_on_sphere_with_small_radius(self):
    #     self.assertTrue(False)

    # def test_can_generate_100_points_on_sphere_with_small_radius(self):
    #     self.assertTrue(False)

    # def test_exception_thrown_when_asked_to_generate_4_points_on_sphere(self):
    #     self.assertTrue(False)

    # def test_exception_thrown_when_asked_to_generate_0_points_on_sphere(self):
    #     self.assertTrue(False)

    def assert_calculated_points_lie_on_sphere_surface(self, position, radius, points):
        for point in points:
            vector = []

            for i in range(len(point)):
                vector.append(point[i] - position[i])

            magnitude = math.sqrt(pow(vector[0], 2) + pow(vector[1], 2) + pow(vector[2], 2))
            self.assertAlmostEqual(magnitude, radius, places=7, msg=None, delta=None)

if __name__=="__main__":
    unittest.main()