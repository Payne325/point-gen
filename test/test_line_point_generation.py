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
      self.assert_(False, "Not yet implemented")
   
   def test_can_generate_20_points_on_line_aligned_to_Y_plane(self):
      self.assert_(False, "Not yet implemented")

   def test_can_generate_2_points_on_line_aligned_to_Z_plane(self):
      self.assert_(False, "Not yet implemented")
   
   def test_can_generate_20_points_on_line_aligned_to_Z_plane(self):
      self.assert_(False, "Not yet implemented")

   def test_can_generate_2_points_on_non_axis_aligned_line(self):
      self.assert_(False, "Not yet implemented")
   
   def test_can_generate_20_points_on_non_axis_aligned_line(self):
      self.assert_(False, "Not yet implemented")

   def test_can_not_generate_points_on_line_with_zero_magnitude(self):
      self.assertRaises(PointGenerationException, generate_points_on_line, [50, 50, 50], [50, 50, 50], 20)

   def test_can_not_generate_0_points_on_line(self):
      self.assertRaises(PointGenerationException, generate_points_on_line, [50, 50, 50], [150, 150, 150], 0)

   def distance_between_line_and_point(self, start_point, end_point, test_point):

      v = np.asarray(start_point)
      w = np.asarray(end_point)
      test = np.asarray(test_point)

      vec = (w-v)
      length_squared = pow(vec[0], 2) + pow(vec[1], 2) + pow(vec[2], 2)

      if length_squared < 0:
         length_squared *= -1

      start_to_point = (test - v)
      if length_squared == 0.0:
         return math.sqrt(pow(start_to_point[0], 2) + pow(start_to_point[1], 2) + pow(start_to_point[2], 2))
         
      debug = np.dot(start_to_point, vec)
      t = max(0, min(1, debug / length_squared))
      projection = v + (t * vec)

      result_vec = (projection - test)
      return math.sqrt(pow(result_vec[0], 2) + pow(result_vec[1], 2) + pow(result_vec[2], 2))

   def assert_calculated_points_lie_on_line(self, start_point, end_point, generated_points):
      for test_point in generated_points:
         dist = self.distance_between_line_and_point(start_point, end_point, test_point)
         self.assertAlmostEqual(dist, 0.0, places=7, msg=None, delta=None)

if __name__=="__main__":
   unittest.main()  