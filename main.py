import numpy as np
import argparse as argparse
import math

if __name__=="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--number-of-points", type=int, help="number of points to be distributed on the sphere")
    ap.add_argument("-r", "--radius", type=int, help="radius of the sphere")
    ap.add_argument("-p", "--position", nargs='+', type=int, default = [0, 0, 0], help="position of the sphere")

    data = vars(ap.parse_args())

    SPHERE_POSITION = data["position"]
    SPHERE_RADIUS = data["radius"]
    NUM_OF_POINTS = data["number_of_points"]
    generated_nums = np.random.normal(0.0, 1, NUM_OF_POINTS * 3)
    points_on_sphere = []

    for i in range(NUM_OF_POINTS):
        #get points x, y, z components
        point = [generated_nums[i], generated_nums[i+1], generated_nums[i+2]]

        #normalise each component of the point
        normaliser = 1.0 / math.sqrt(math.pow(generated_nums[i], 2) + math.pow(generated_nums[i+1], 2) + math.pow(generated_nums[i+2], 2))
        point = [j * normaliser for j in point]

        #Scale for sphere radius
        point = [j * SPHERE_RADIUS for j in point]

        #Offset by sphere centre
        point =  [k + SPHERE_POSITION[j] for j, k in enumerate(point)]

        points_on_sphere.append(point)

    
    outFile = open("Test Data.txt", "w")

    outFile.write("Radius: {}\n".format(SPHERE_RADIUS))
    outFile.write("Position: {}\n".format(SPHERE_POSITION))
    outFile.write("")

    for pt in points_on_sphere:
        outFile.write("{}\n".format(pt))

    outFile.close()