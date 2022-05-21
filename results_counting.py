
# gridSize_x = [10, 50, 100, 20, 100, 40, 80]
# gridSize_y = [10, 50, 100, 100, 20, 80, 40]
# robotsNumber_percent = [5, 10, 15, 20]
# discs = [3, 10]
gridSize_x = [10]
gridSize_y = [10]
robotsNumber_percent = [5]
discs = [3]
type = ["goSide", "goBack"]
# type = ["goSide", "goBack"]

def compute(cell_capacity, method, resource_management):
    # with open("results/results_grid_goSide"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    with open("results/results" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results_" + name +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
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
        if int(t) != 0:
            measure += int(t)
            number += 1
    result_time = measure/number

    # with open("ended_results/ended_results_grid_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    with open("ended_results/ended_results_" + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_free_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
        f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))
    
    # with open("results/results_grid_goSide"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    with open("results/results_" + name +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
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
        if int(t) != 0:
            measure += int(t)
            number += 1
    result_time = measure/number

    # with open("ended_results/ended_results_grid_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_" + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    with open("ended_results/ended_results_free_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
        f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))
        
def compute_grid(cell_capacity, method, resource_management):
    with open("results/results_grid"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results_" + name +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
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
        if int(t) != 0:
            measure += int(t)
            number += 1
    result_time = measure/number

    with open("ended_results/ended_results_grid_" + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_" + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_free_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
        f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))
    
    
    with open("results/results_grid_goSide"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results_" + name +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
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
        if int(t) != 0:
            measure += int(t)
            number += 1
    result_time = measure/number

    with open("ended_results/ended_results_grid_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_" + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_free_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
        f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))
    
    
    with open("results/results_grid_goBack"+str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k]) + "_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
    # with open("results/results_" + name +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'r') as f:
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
        if int(t) != 0:
            measure += int(t)
            number += 1
    result_time = measure/number

    with open("ended_results/ended_results_grid_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_" + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
    # with open("ended_results/ended_results_free_" + name + "_" +str(gridSize_x[i])+"_"+str(gridSize_y[i])+"_"+str(robotsNumber_percent[j])+"_"+str(discs[k])+"_" + str(cell_capacity) + str(method) + str(resource_management) +".txt",'w') as f:
        f.write(str(result) + " " + str(len(lines)) + " " + str(result_time))

for name in type:
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
                