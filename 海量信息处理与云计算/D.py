# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: D.py
# Created:  2019.05.14(UTC+0800)17.48.27(星期二)
'''

def has_infrequent_subset(c, L):
    for i in range(len(c)):
        tmp = c[:i] + c[i + 1:]
        if tmp not in L:
            return True
    return False

def apriori_gen(L, min_sup):
    Ck, cset =[], set()
    for l1 in L:
        for l2 in L:
            ok = (l1[-1] != l2[-1])
            for i in range(len(l1) - 1):
                if ok and l1[i] != l2[i]:
                    ok = False
            if ok:
                ls = list(l1)
                ls.sort()
                l1 = tuple(ls)
                c = l1 + (l2[-1],)
                if c in cset or has_infrequent_subset(c, set(L)):
                    del c
                else:
                    cset.add(c)
                    Ck.append(c)
    return Ck

def apriori(D, min_sup, min_conf):
    L1, cnt1, idset, lenD, s = [], {}, set(), len(D), ""
    for ds in D:
        for di in ds:
            if di not in idset:
                idset.add(di)
                cnt1[(di,)] = 0
            cnt1[(di,)] += 1
    for k, v in cnt1.items():
        if v >= lenD * min_sup:
            L1.append(k)

    for k in range(2, len(idset)):
        if L1 == []:
            break
        Ck, L2, cnt2 = apriori_gen(L1, min_sup), [], {}
        for t in Ck:
            cnt2[t] = 0
            for d in D:
                if set(t).issubset(set(d)):
                    cnt2[t] += 1
        for t in Ck:
            if cnt2[t] >= lenD * min_sup:
                L2.append(t)
                if cnt2[t] / cnt1[t[:-1]] >= min_conf:
                    s += "(" + str(t[0])
                    for i in range(1, len(t) - 1):
                        s += "," + str(t[i])
                    s += ") ==> ({0}) conf({1})\n".format(t[-1], round(cnt2[t] / cnt1[t[:-1]], 3))
            L1 = L2.copy()
        cnt1 = cnt2.copy()
    return s

import tkinter
from tkinter import ttk
import tkinter.messagebox
import pandas

def lodaData(path, data):
    try:
        for dr in pandas.read_csv(path.get(), header = None).values.tolist():
            tmp = tuple()
            for dc in dr:
                if dc == dc:
                    tmp += (int(dc), )
            data.append(tmp)
        tkinter.messagebox.showinfo(path.get(), "Okay")
    except Exception as e:
        tkinter.messagebox.showerror(path.get(), e)

def startApriori(Text, data, min_sup, min_conf, outItem):
    if data == []:
        tkinter.messagebox.showwarning("Warning", "数据未载入")
    elif outItem == "True":
        Text.insert("end", apriori(data, min_sup, min_conf))

def main():
    data = []

    root = tkinter.Tk()
    root.title("Apriori")
    root.geometry("600x220")

    strPath, svMinSup, svType, svMinConf, svOutItem = [tkinter.StringVar() for i in range(5)]
    strPath.set("沃尔玛购物数据.csv")
    svMinSup.set("0.1")
    svType.set("Confidence")
    svMinConf.set("0.7")
    svOutItem.set("True")

    tkinter.Button(root, text = "loadData", command = lambda: lodaData(strPath, data)).place(x = 10, y = 10)
    tkinter.Entry(root, textvariable = strPath, width = 16).place(x = 120, y = 10)

    tkinter.Label(root, text = "minSuport").place(x = 10, y = 50)
    tkinter.Entry(root, textvariable = svMinSup, width = 16).place(x = 120, y = 50)

    tkinter.Label(root, text = "metricType").place(x = 10, y = 80)
    ttk.Combobox(root, width = 15, state = "readonly", values = ("Confidence"), textvariable = svType).place(x = 120, y = 80)

    tkinter.Label(root, text = "minConfince").place(x = 10, y = 110)
    tkinter.Entry(root, width = 16, textvariable = svMinConf).place(x = 120, y = 110)

    tkinter.Label(root, text = "outputItemSets").place(x = 10, y = 140)
    ttk.Combobox(root, width = 15, state = "readonly", textvariable = svOutItem, values = ("True", "False")).place(x = 120, y = 140)

    tkinter.Label(root, text = "频繁项集和关联规则").place(x = 300, y = 10)
    Text_output = tkinter.Text(root, width = 40, height = 7)
    Text_output.place(x = 270, y = 42)

    tkinter.Button(root, text = "开始", width = 13, command = lambda: startApriori(Text_output, data, float(svMinSup.get()), float(svMinConf.get()), svOutItem.get())).place(x = 120, y = 175)
    tkinter.Button(root, text = "清空", width = 13, command = lambda: Text_output.delete("0.0", "end")).place(x = 270, y = 175)
    tkinter.Button(root, text = "关闭", width = 13, command = root.quit).place(x = 420, y = 175)

    root.mainloop()

if __name__ == "__main__":
    main()
