
import numpy as np
import argparse as argparse
import math

class PointGenerationException(Exception):
    #Raised when an error occurs generating point data
    pass

def generate_points_on_plane(position, normal, radius, number_of_points):
    plane_points = []

    for i in range(number_of_points):
        random_point = []

        while True:
            #calculate random point on plane
            random_vector = np.random.normal(0.0, 1, 3)

            random_point = np.cross(random_vector, normal)

            if not np.array_equal(random_point, np.array([0, 0, 0])):
                break

        #normalise each component of the random point
        normaliser = 1.0 / math.sqrt(math.pow(random_point[0], 2) + math.pow(random_point[1], 2) + math.pow(random_point[2], 2))
        random_point = [j * normaliser for j in random_point]

        #place it within the constraining radius
        random_point = [j * radius for j in random_point]

        #translate to the plane
        random_point += position

        plane_points.append(random_point)

    return plane_points

if __name__=="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--number-of-points", type=int, help="number of points to be distributed on the sphere")
    ap.add_argument("-r", "--radius", type=int, help="Radius around the plane position that points can be generated within")
    ap.add_argument("-p", "--position", nargs='+', type=int, default = [0, 0, 0], help="position of the plane")
    ap.add_argument("-v", "--vector-normal", nargs='+', type=int, default = [0, 0, 0], help="normal of the plane")

    data = vars(ap.parse_args())

    points_on_plane = generate_points_on_plane(data["position"], data["vector_normal"], data["radius"], data["number_of_points"])

    outFile = open("Test Data.txt", "w")

    outFile.write("Constraint Radius: {}\n".format(data["radius"]))
    outFile.write("Position: {}\n".format(data["position"]))
    outFile.write("Normal: {}\n".format(data["vector_normal"]))
    outFile.write("")

    for pt in points_on_plane:
        outFile.write("{}\n".format(pt))

    outFile.close()