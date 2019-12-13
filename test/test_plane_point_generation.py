import unittest
import math
from src.plane_point_gen import *

class TestSpherePointGenerationMethods(unittest.TestCase):

    def test_can_generate_1_point_on_plane_within_a_radius(self):
        position = [0, 0, 0]
        normal = [0, 0, 1]
        radius = 5

        points = generate_points_on_plane(position, normal, radius, number_of_points=1)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_10_points_on_plane_within_a_radius(self):
        position = [0, 0, 0]
        normal = [0, 1, 0]
        radius = 5

        points = generate_points_on_plane(position, normal, radius, number_of_points=10)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_100_points_on_plane_within_a_radius(self):
        position = [0, 0, 0]
        normal = [1, 0, 0]
        radius = 5

        points = generate_points_on_plane(position, normal, radius, number_of_points=100)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_1_point_on_plane_within_a_small_radius(self):
        position = [30, -4.765, 606.5]
        normal = [0, 0.5, 0.5]
        radius = 1

        points = generate_points_on_plane(position, normal, radius, number_of_points=1)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_10_points_on_plane_within_a_small_radius(self):
        position = [-67, 4.235, -102235.3464574]
        normal = [0.25, 0.25, 0.5]
        radius = 1

        points = generate_points_on_plane(position, normal, radius, number_of_points=10)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_100_points_on_plane_within_a_small_radius(self):
        position = [-33.339, -4587, -34]
        normal = [0.333, 0.333, 0.333]
        radius = 1

        points = generate_points_on_plane(position, normal, radius, number_of_points=100)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_1_point_on_plane_within_a_large_radius(self):
        position = [0, -494.684, 72.55]
        normal = [45, 2, 2]
        radius = 100

        points = generate_points_on_plane(position, normal, radius, number_of_points=1)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_10_points_on_plane_within_a_large_radius(self):
        position = [654856, 0, -98]
        normal = [-4, 6.666, 1.4]
        radius = 50

        points = generate_points_on_plane(position, normal, radius, number_of_points=10)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_can_generate_100_points_on_plane_within_a_large_radius(self):
        position = [-9, 45.23, 0]
        normal = [0, 0, -1]
        radius = 100

        points = generate_points_on_plane(position, normal, radius, number_of_points=100)

        self.assert_calculated_points_lie_on_plane(position, normal, radius, points)

    def test_cannot_generate_0_points_on_plane(self):
        self.assertRaises(PointGenerationException, generate_points_on_plane, [0, 0, 0], [-1, 0, 0], 5, number_of_points=0)

    def test_cannot_generate_points_on_plane_within_radius_of_size_0(self):
        self.assertRaises(PointGenerationException, generate_points_on_plane, [0, 0, 0], [-1, 0, 0], 0, number_of_points=1)

    def test_cannot_generate_points_on_plane_with_a_zeroed_normal(self):
        self.assertRaises(PointGenerationException, generate_points_on_plane, [0, 0, 0], [0, 0, 0], 5, number_of_points=1)

    def assert_calculated_points_lie_on_plane(self, position, normal, radius, points):

        norm = np.asarray(normal)
        
        for point in points:
            # check each point lies on the plane
            a = np.asarray(point)
            p = np.asarray(position)
            aMinusP = (a - p)

            dotProd = np.dot(norm, aMinusP)

            self.assertAlmostEqual(dotProd, 0, places=7, msg=None, delta=None)

            # check points are all within [RADIUS] distance away from the defining point of the plane
            vector = []
            for i in range(len(a)):
                vector.append(a[i] - p[i])

            magnitude = math.sqrt(pow(vector[0], 2) + pow(vector[1], 2) + pow(vector[2], 2))
            self.assertAlmostEqual(magnitude, radius, places=7, msg=None, delta=None)

if __name__=="__main__":
    unittest.main()