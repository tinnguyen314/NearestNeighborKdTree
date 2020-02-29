from scipy import spatial
import numpy as np
import random
import matplotlib.pyplot as plt
import timeit


#number of dimension for each data point
dimension = 2;
#number of points
n = 50;

# list of test points
points = (np.random.random(((n,dimension)))*100)
tree = spatial.KDTree(points)
print("This is all the sample point: ")
print(tree.data)
#target point
test_point = np.random.random((1,dimension))*100
print("\n")
print("This is the test point: ")
print(test_point)
print("\n")
start = timeit.default_timer()
distance, index = tree.query(test_point)
stop = timeit.default_timer()
elapsed_time = start - stop
print("Total number of points: %d"%(n))
print("Test point coordinate: "+ np.array2string(test_point))
print("Nearest neighbor: " + np.array2string(tree.data[index]))
print("Query time: %2.5fs" %elapsed_time)
print("Distance to the nearest point: " + np.array2string (distance[0]))
for i in range(len(points)):
    plt.plot(points[i][0],points[i][1],"or")
for i in range(len(test_point)):
    plt.plot(test_point[i][0],test_point[i][1],"bo")
plt.title("K-nearest Neighbors")
plt.show()
total_sample = 50000;
n = 20
loop = 6
number_of_point = []
number_of_dimension = []
time_complexity = []
target_point = []
for i in range (loop):
    n = n * i + 20
    #n = 5
    dimension = 2
    dimension = dimension * i + dimension + 5
    points = (np.random.random(((50000, dimension))) * 100)
    tree = spatial.KDTree(points)
    test_point = np.random.random((n, dimension)) * 100
    start = timeit.default_timer()
    distance, index = tree.query(test_point)
    stop = timeit.default_timer()
    elapsed_time = stop - start
    number_of_point.append(points.size/dimension)
    number_of_dimension.append(dimension)
    time_complexity.append(elapsed_time)
    target_point.append(test_point.size/dimension)
print("\n")
print (" Table of Kd-Tree Time Complexity - Increasing N & D")
print("\t----------------------------------------------------------------------------")
print("\t|| Sample Points || Numbers of Dimension || Target Points || Queries Time || ")
for i in range (loop):
    print("\t|| \t %8d\t || \t %8d \t\t || \t %5d \t  || %8.5f\t  ||"%(number_of_point[i],
                        number_of_dimension[i],target_point[i],time_complexity[i]))
print("\t----------------------------------------------------------------------------")


