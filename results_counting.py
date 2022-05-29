
# gridSize_x = [10, 50, 100, 20, 100, 40, 80]
# gridSize_y = [10, 50, 100, 100, 20, 80, 40]
# robotsNumber_percent = [5, 10, 15, 20]
# discs = [3, 10]
gridSize_x = [50]
gridSize_y = [50]
robotsNumber_percent = [5, 10]
discs = [3, 8]


def compute(cell_capacity, method, resource_management):
    for x in range(0, 6):
        if x == 1:
            with open("results/results_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        elif x == 2:
            with open("results/results_goSide_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        else:
            with open("results/results_goback_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()

        notEnded = []
        time = []
        for line in lines:
            data = line.split(" ")
            notEnded.append(data[1])
            time.append(data[2])
        result = 0
        for value in notEnded:
            if int(value) != 0:
                result += 1
        measure = 0
        number = 0
        for t in time:
            if float(t) != 0:
                measure += float(t)
                number += 1
        result_time = measure/number

        if x == 1:
            with open("ended_results/ended_results_" + "_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'w') as f:
                f.write(str(result) + " " + str(len(lines)) +
                        " " + str(result_time))
        elif x == 2:
            with open("ended_results/ended_results_goSide_" + "_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'w') as f:
                f.write(str(result) + " " + str(len(lines)) +
                        " " + str(result_time))
        else:
            with open("ended_results/ended_results_goback_" + "_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'w') as f:
                f.write(str(result) + " " + str(len(lines)) +
                        " " + str(result_time))


def compute_grid(cell_capacity, method, resource_management):
    for x in range(0, 3):
        if x == 1:
            with open("results/results_grid_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        elif x == 2:
            with open("results/results_grid_goSide_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        else:
            with open("results/results_grid_goBack_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()

        notEnded = []
        time = []
        for line in lines:
            data = line.split(" ")
            notEnded.append(data[1])
            time.append(data[2])
        result = 0
        for value in notEnded:
            if int(value) != 0:
                result += 1
        measure = 0
        number = 0
        for t in time:
            if float(t) != 0:
                measure += float(t)
                number += 1
        result_time = measure/number

        if x == 1:
            with open("ended_results/ended_results_grid_" + "_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'w') as f:
                f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))
        elif x == 2:
            with open("ended_results/ended_results_grid_goSide_" + "_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'w') as f:
                f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))
        else:
            with open("ended_results/ended_results_grid_goback_" + "_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'w') as f:
                f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))


for i in range(0, len(gridSize_x)):
    for j in range(0, len(robotsNumber_percent)):
        for k in range(0, len(discs)):
            compute(1, 0, 0)
            compute(1, 0, 1)
            compute(2, 0, 1)
            compute(1, 1, 0)
            compute(1, 1, 1)
            compute(2, 1, 1)
            compute_grid(1, 1, 0)
            compute_grid(1, 1, 1)
            compute_grid(2, 1, 1)
