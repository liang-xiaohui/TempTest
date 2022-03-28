#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess
import sys

from pip._internal.index import collector

stlpath = "C:\\Users\\xiaof\\Desktop\\SAT-20220315\\SAT-20220315_PrintDatas"
trimfilepath = "C:\\Users\\xiaof\\Desktop\\SAT-20220315\\SAT-20220315_CuttingDatas"
outputpath = "C:\\Users\\xiaof\\Desktop\\SAT-20220315\\SAT-20220315_Trimpathline_Test_2"
PG = "H:\\CPP_Project\\AngelAlignTrimming\\Release\\AngelAlignTrimming.exe"
for root, dirnames , filenames in os.walk(stlpath):
    for file in filenames:
        ss = file.split("_",4)
        arch = ss[0]
        step = ss[1]
        id = ss[2]
        trimfile = trimfilepath + "\\trimline_" + arch + "_" + step + "_" + id + ".json"
        tmfile = stlpath + "\\" + file
        trimpathline = outputpath + "\\trimpathline_" + arch + "_" + step + "_" + id + ".json"
        args = (PG,tmfile,"test", trimfile,trimpathline,"MC-0.76")
        print(args)
        p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        while True:
            if subprocess.Popen.poll(p) == 0:  # 判断子进程是否结束
                break
            line = p.stdout.readline()
            if(line != " "):
                print(line)

