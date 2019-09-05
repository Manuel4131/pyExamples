#!/usr/bin/env python
#-*- coding:utf-8 -*-

f = open('data','r')
f2 = open('convertedData','w')
l = f.readline()

while l:
    p=l.strip().split(',')
    print(p[1].strip())
    print(p[0])
    f2.write(p[1]+','+p[0]+'\n')
    l=f.readline()
