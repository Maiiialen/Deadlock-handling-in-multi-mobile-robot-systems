#!/usr/bin/env python
import time
from Manager import Manager
from Manager_goSide import Manager_goSide
from Manager_goSide_Grid import Manager_goSide_Grid
from Manager_goBack import Manager_goBack
          
gridSize_x = [70]
gridSize_y = [70]
# gridSize_x = [10, 20, 30, 40, 50, 60, 70]
# gridSize_y = [10, 20, 30, 40, 50, 60, 70]
# gridSize_x = [10, 50, 100, 20, 100, 40, 80]
# gridSize_y = [10, 50, 100, 100, 20, 80, 40]
#robotsNumber_percent = [10]
robotsNumber_percent = [7]
discs = [3]


# file_name, cell_capacity, 0[euklidian] or 1[Manhattan], resources management 1[on] 0[off], wizualization 1[on] 0[off]

def runTest(cell_capacity, method, resource_management):
    # manager = Manager("configurations/free_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt", cell_capacity, method, resource_management, 0)
    # a = time.time()
    # results = manager.manage()
    # b = time.time()
    # c = b - a
    # with open("results/results_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt", 'a') as f:
    #     f.write(results + " " + str(c))
    #     f.write("\n")
    # print("Done 1")

    manager = Manager_goSide("configurations/free_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt", cell_capacity, method, resource_management, 0)
    a = time.time()
    results = manager.manage()
    b = time.time()
    c = b - a
    with open("results/results_goSide_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt", 'a') as f:
        f.write(results + " " + str(c))
        f.write("\n")
    print("Done 2")

    # manager = Manager_goBack("configurations/free_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt", cell_capacity, method, resource_management, 0)
    # a = time.time()
    # results = manager.manage()
    # b = time.time()
    # c = b - a
    # with open("results/results_goBack_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt", 'a') as f:
    #     f.write(results + " " + str(c))
    #     f.write("\n")
    # print("Done 3")


def runTest_grid(cell_capacity, method, resource_management):
    # manager = Manager("configurations/grid_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt", cell_capacity, method, resource_management, 0)
    # a = time.time()
    # results = manager.manage()
    # b = time.time()
    # c = b - a
    # with open("results/results_grid_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt", 'a') as f:
    #     f.write(results + " " + str(c))
    #     f.write("\n")
    # print("Done 4")

    manager = Manager_goSide_Grid("configurations/grid_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt", cell_capacity, method, resource_management, 0)
    a = time.time()
    results = manager.manage()
    b = time.time()
    c = b - a
    with open("results/results_grid_goSide_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt", 'a') as f:
        f.write(results + " " + str(c))
        f.write("\n")
    print("Done 5")

    # manager = Manager_goBack("configurations/grid_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+".txt", cell_capacity, method, resource_management, 0)
    # a = time.time()
    # results = manager.manage()
    # b = time.time()
    # c = b - a
    # with open("results/results_grid_goBack_"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt", 'a') as f:
    #     f.write(results + " " + str(c))
    #     f.write("\n")
    # print("Done 6")
    
if __name__ == '__main__':
    number = 0
    for i in range(0, len(gridSize_x)):
        for j in range(0, len(robotsNumber_percent)):
            for k in range(0, len(discs)):
                for _ in range(0, 21):
                    print("_ Start " + str(number) + str(" [") + str(gridSize_x[i]) + "x" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + str("]") + " ___")
                    print("")

                    # runTest(1, 0, 0)
                    # runTest(1, 0, 1)
                    # runTest(2, 0, 1)
                    # runTest(1, 1, 0)
                    # runTest(1, 1, 1)
                    # runTest(2, 1, 1)
                    runTest_grid(1, 1, 0)
                    runTest_grid(1, 1, 1)
                    runTest_grid(2, 1, 1)

                    number += 1
