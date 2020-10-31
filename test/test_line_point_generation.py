import unittest
import math
from src.line_point_gen import *

class TestLinePointGenerationMethods(unittest.TestCase):

   def test_can_generate_2_points_on_line_starting_at_origin(self):
      start_point = [0, 0, 0]
      end_point = [10, 10, 10]
      num_of_points = 2

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_20_points_on_line_starting_at_origin(self):
      start_point = [0, 0, 0]
      end_point = [-30, 7, 5150]
      num_of_points = 20

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_2_points_on_line_ending_at_origin(self):
      start_point = [1984, -182.98476895236, 0.2]
      end_point = [0, 0, 0]
      num_of_points = 2

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_20_points_on_line_ending_at_origin(self):
      start_point = [64, 2, -666.6666]
      end_point = [0, 0, 0]
      num_of_points = 20

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)

   def test_can_generate_2_points_on_line_intersecting_origin(self):
      start_point = [10, 10, 10]
      end_point = [-10, -10, -10]
      num_of_points = 2

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_20_points_on_line_intersecting_origin(self):
      start_point = [-198, 720.360108, -2.515]
      end_point = [99, -360.180054, 1.2575]
      num_of_points = 20

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)

   def test_can_generate_2_points_on_line_aligned_to_X_plane(self):
      start_point = [-198, 720.360108, -2.515]
      end_point = [99, 720.360108, -2.515]
      num_of_points = 2

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_20_points_on_line_aligned_to_X_plane(self):
      start_point = [1, 0, 0]
      end_point = [-1000000, 0, 0]
      num_of_points = 20

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_2_points_on_line_aligned_to_Y_plane(self):
      start_point = [500, 72008, -2.515]
      end_point = [500, -3947.44, -2.515]
      num_of_points = 2

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_20_points_on_line_aligned_to_Y_plane(self):
      start_point = [0, 1, 0]
      end_point = [0, -1000000, 0]
      num_of_points = 20

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)

   def test_can_generate_2_points_on_line_aligned_to_Z_plane(self):
      start_point = [500, -3947.44, 34.546565]
      end_point = [500, -3947.44, -2515]
      num_of_points = 2

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_20_points_on_line_aligned_to_Z_plane(self):
      start_point = [0, 0, 1]
      end_point = [0, 0, -1000000]
      num_of_points = 20

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)

   def test_can_generate_2_points_on_non_axis_aligned_line(self):
      start_point = [500, -3947.44, 34.546565]
      end_point = [-3947.44, -2515, 500]
      num_of_points = 2

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)
   
   def test_can_generate_20_points_on_non_axis_aligned_line(self):
      start_point = [0.25, 0.25, 0.5]
      end_point = [0, 0, 1000000]
      num_of_points = 20

      generated_points = generate_points_on_line(start_point, end_point, num_of_points)
      self.assert_calculated_points_lie_on_line(start_point, end_point, generated_points)

   def test_can_not_generate_points_on_line_with_zero_magnitude(self):
      self.assertRaises(PointGenerationException, generate_points_on_line, [50, 50, 50], [50, 50, 50], 20)

   def test_can_not_generate_0_points_on_line(self):
      self.assertRaises(PointGenerationException, generate_points_on_line, [50, 50, 50], [150, 150, 150], 0)

   def distance_between_line_and_point(self, start_point, end_point, test_point):

      s_p = np.asarray(start_point)
      e_p = np.asarray(end_point)
      t_p = np.asarray(test_point)

      line = (e_p - s_p)
      line2 = (e_p - t_p)

      mag = np.linalg.norm(line)
      mag2 = np.linalg.norm(line2)

      if mag == 0 or mag2 == 0:
         return -1

      line = line / mag
      line2 = line2 / mag2

      return 1.0 - np.dot(line, line2)

   def assert_calculated_points_lie_on_line(self, start_point, end_point, generated_points):
      for test_point in generated_points:
         dist = self.distance_between_line_and_point(start_point, end_point, test_point)
         self.assertAlmostEqual(dist, 0.0, places=7, msg=None, delta=None)

if __name__=="__main__":
   unittest.main()  