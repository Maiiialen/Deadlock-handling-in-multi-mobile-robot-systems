#!/usr/bin/env python
import datetime
# from Manager import Manager
# from Manager_goBack import Manager
from Manager_goSide import Manager
          
if __name__ == '__main__':
    # file_name, cell_capacity, 0[euklidian] or 1[Manhattan], resources management 1[on] 0[off]
    # manager = Manager("grid2.txt", 1, 0, 0)
    # print(manager.manage())

    for i in range(0,10):
        print("Start")
        a = datetime.datetime.now()
        manager = Manager("generated/generated_"+str(i)+".txt", 1, 0, 0)
        results = manager.manage()
        b = datetime.datetime.now()
        c = b - a
        with open("results/generated_100.txt", 'a') as f:
            f.write(results + " " + str(c.microseconds))
            f.write("\n")
        print("1 Done")
        a = datetime.datetime.now()
        manager = Manager("generated/generated_"+str(i)+".txt", 1, 0, 1)
        results = manager.manage()
        b = datetime.datetime.now()
        c = b - a
        with open("results/generated_101.txt", 'a') as f:
            f.write(results + " " + str(c.microseconds))
            f.write("\n")
        print("2 Done")
        a = datetime.datetime.now()
        manager = Manager("generated/generated_"+str(i)+".txt", 2, 0, 1)
        results = manager.manage()
        b = datetime.datetime.now()
        c = b - a
        with open("results/generated_201.txt", 'a') as f:
            f.write(results + " " + str(c.microseconds))
            f.write("\n")
        print("3 Done")
        a = datetime.datetime.now()
        manager = Manager("generated/generated_"+str(i)+".txt", 1, 1, 0)
        results = manager.manage()
        b = datetime.datetime.now()
        c = b - a
        with open("results/generated_110.txt", 'a') as f:
            f.write(results + " " + str(c.microseconds))
            f.write("\n")
        print("4 Done")
        a = datetime.datetime.now()
        manager = Manager("generated/generated_"+str(i)+".txt", 1, 1, 1)
        results = manager.manage()
        b = datetime.datetime.now()
        c = b - a
        with open("results/generated_111.txt", 'a') as f:
            f.write(results + " " + str(c.microseconds))
            f.write("\n")
        print("5 Done")
        a = datetime.datetime.now()
        manager = Manager("generated/generated_"+str(i)+".txt", 2, 1, 1)
        results = manager.manage()
        b = datetime.datetime.now()
        c = b - a
        with open("results/generated_211.txt", 'a') as f:
            f.write(results + " " + str(c.microseconds))
            f.write("\n")
        print("6 Done")
        print("___ Done " + str(i) + " ___")

    # for i in range(0,10):
        # print("Start")
        # a = datetime.datetime.now()
        # manager = Manager("generatedCells/generatedCells_"+str(i)+".txt", 1, 1, 0)
        # results = manager.manage()
        # b = datetime.datetime.now()
        # c = b - a
        # with open("results/generated_100.txt", 'a') as f:
        #     f.write(results + " " + str(c.microseconds))
        #     f.write("\n")
        # print("1 Done")
        # a = datetime.datetime.now()
        # manager = Manager("generatedCells/generatedCells_"+str(i)+".txt", 1, 1, 1)
        # results = manager.manage()
        # b = datetime.datetime.now()
        # c = b - a
        # with open("results/generated_100.txt", 'a') as f:
        #     f.write(results + " " + str(c.microseconds))
        #     f.write("\n")
        # print("1 Done")
        # a = datetime.datetime.now()
        # manager = Manager("generatedCells/generatedCells_"+str(i)+".txt", 2, 1, 1)
        # results = manager.manage()
        # b = datetime.datetime.now()
        # c = b - a
        # with open("results/generated_100.txt", 'a') as f:
        #     f.write(results + " " + str(c.microseconds))
        #     f.write("\n")
        # print("1 Done")
    exit()