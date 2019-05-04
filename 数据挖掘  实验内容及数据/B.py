# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: a.py
# Created:  2019.05.04(UTC+0800)09.38.36(星期六)
'''

def main():
    csvAll = ""
    with open("实验2-Groceries.csv", "r") as CSV:
        csvAll = CSV.read().split('\n')

    csvData = []
    idset = set()
    idmap = {}
    for i in range(1, len(csvAll)):
        a = csvAll[i];
        if a == "":
            break
        b = list(map(str.strip, a[a.find("{") + 1: a.rfind("}")].split(",")))
        for c in b:
            if c not in idset:
                idmap[c] = len(idset)
                idset.add(c)
        csvData.append(b.copy())

    n = len(idset)
    for i in range(len(csvData)):
        cd = csvData[i].copy()
        s = "0" * n
        for cx in cd:
            s = s[:idmap[cx]] + "1" + s[idmap[cx] + 1:]
        csvData[i] = s
    
    with open("实验2-Groceries.arff", "w") as arffFile:
        arffFile.write("@relation Groceries\n\n")
        for k in idmap.keys():
            arffFile.write("@attribute \"" + k + "\" {0,1}\n")
        arffFile.write("\n@data\n")
        for cd in csvData:
            s = ""
            for i in range(n - 1):
                s += cd[i] + ","
            s += cd[n - 1]
            arffFile.write(s + "\n")

if __name__ == "__main__":
    main()
