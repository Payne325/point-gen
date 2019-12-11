import numpy as np
import argparse as argparse
import math

def generate_points_on_sphere(position, radius, number_of_points):
    generated_nums = np.random.normal(0.0, 1, number_of_points * 3)
    points_on_sphere = []

    for i in range(number_of_points):
        #get points x, y, z components
        point = [generated_nums[i], generated_nums[i+1], generated_nums[i+2]]

        #normalise each component of the point
        normaliser = 1.0 / math.sqrt(math.pow(generated_nums[i], 2) + math.pow(generated_nums[i+1], 2) + math.pow(generated_nums[i+2], 2))
        point = [j * normaliser for j in point]

        #Scale for sphere radius
        point = [j * radius for j in point]

        #Offset by sphere centre
        point =  [k + position[j] for j, k in enumerate(point)]

        points_on_sphere.append(point)

    return points_on_sphere

if __name__=="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--number-of-points", type=int, help="number of points to be distributed on the sphere")
    ap.add_argument("-r", "--radius", type=int, help="radius of the sphere")
    ap.add_argument("-p", "--position", nargs='+', type=int, default = [0, 0, 0], help="position of the sphere")

    data = vars(ap.parse_args())

    points_on_sphere = generate_points_on_sphere(data["position"], data["radius"], data["number_of_points"])

    outFile = open("Test Data.txt", "w")

    outFile.write("Radius: {}\n".format(data["radius"]))
    outFile.write("Position: {}\n".format(data["position"]))
    outFile.write("")

    for pt in points_on_sphere:
        outFile.write("{}\n".format(pt))

    outFile.close()