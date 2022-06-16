# gridSize_x = [10, 50, 100, 20, 100, 40, 80]
# gridSize_y = [10, 50, 100, 100, 20, 80, 40]
gridSize_x = [10, 20, 30, 40, 50, 60, 70]
gridSize_y = [10, 20, 30, 40, 50, 60, 70]
# gridSize_x = [70]
# gridSize_y = [70]
# robotsNumber_percent = [10]
# discs = [3]
robotsNumber_percent = [2, 5, 7, 10]
discs = [3, 8]

def couting(lines):
    Ended = []
    notEnded = []
    time = []
    for line in lines:
        data = line.split(" ")
        Ended.append(data[0])
        notEnded.append(data[1])
        time.append(data[2])
    resultEnded = 0
    resultNotEnded = 0
    zeros = 0
    for value in Ended:
        resultEnded += int(value)
    for value in notEnded:
        if int(value) == 1:
            resultEnded += 1
            zeros += 1
        else:
            resultNotEnded += int(value)
        if int(value) == 0:
            zeros += 1
    measure = 0
    number = 0
    for t in time:
        if float(t) != 0:
            measure += float(t)
            number += 1
    result_time = measure/number
    return resultEnded, resultNotEnded, result_time, zeros

def compute(cell_capacity, method, resource_management):
    for x in range(0, 3):
        if x == 0:
            with open("results/results_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        elif x == 1:
            with open("results/results_goSide_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        else:
            with open("results/results_goBack_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()

        resultEnded, resultNotEnded, result_time, zeros = couting(lines)

        # if(len(lines) < 10):
        #     print("free " + str(x) + " " + str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
        #         " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")

        if x == 1 and discs[k] == 3 and len(lines) < 70:
            print("___ free " +str(gridSize_x[i]) + " " + str(robotsNumber_percent[j]) + " " + str(cell_capacity) + str(method) + str(resource_management) +  " " + 
                " | " + str(len(lines)))

        if x == 0:
            with open("ended_results/ended_results_.txt", 'a') as f:
                f.write(str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
                " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")
        elif x == 1:
            with open("ended_results/ended_results_goSide_.txt", 'a') as f:
                f.write(str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
                " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")
        else:
            with open("ended_results/ended_results_goback_.txt", 'a') as f:
                f.write(str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
                " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")


def compute_grid(cell_capacity, method, resource_management):
    for x in range(0, 3):
        if x == 0:
            with open("results/results_grid_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        elif x == 1:
            with open("results/results_grid_goSide_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()
        else:
            with open("results/results_grid_goBack_" + str(gridSize_x[i]) + "_" + str(gridSize_y[i]) + "_" + str(robotsNumber_percent[j]) + "_" + str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) + ".txt", 'r') as f:
                lines = f.readlines()

        resultEnded, resultNotEnded, result_time, zeros = couting(lines)

        # if(len(lines) < 10):
        #     print("grid " + str(x) + " " + str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
        #         " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")

        if x == 1 and discs[k] == 3 and len(lines) < 70:
            print("___ grid " +str(gridSize_x[i]) + " " + str(robotsNumber_percent[j]) + " " + str(cell_capacity) + str(method) + str(resource_management) +  " " + 
                " | " + str(len(lines)))


        if x == 0:
            with open("ended_results/ended_results_grid_.txt", 'a') as f:
                f.write(str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
                " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")
        elif x == 1:
            with open("ended_results/ended_results_grid_goSide_.txt", 'a') as f:
                f.write(str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
                " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")
        else:
            with open("ended_results/ended_results_grid_goback_.txt", 'a') as f:
                f.write(str(gridSize_x[i]) + " " + str(gridSize_y[i]) + " " + str(robotsNumber_percent[j]) + " " + str(discs[k]) + " " + str(cell_capacity) + str(method) + str(resource_management) + 
                " " + str(resultEnded) + " " + str(resultNotEnded) + " " + str(len(lines)) + " " + str(result_time) + " " + str(zeros) + "\n")


with open("ended_results/ended_results_.txt", 'w') as f:
    pass
with open("ended_results/ended_results_goSide_.txt", 'w') as f:
    pass
with open("ended_results/ended_results_goback_.txt", 'w') as f:
    pass
with open("ended_results/ended_results_grid_.txt", 'w') as f:
    pass
with open("ended_results/ended_results_grid_goSide_.txt", 'w') as f:
    pass
with open("ended_results/ended_results_grid_goback_.txt", 'w') as f:
    pass

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
