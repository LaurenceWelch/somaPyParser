#Laurence Welch

import re

#filters
resIp = '([0-9]{1,3}\.){3}[0-9]{1,3}'
resDate = '[a-zA-Z]{3} [0]{0,2}[0-9]'

#lambdas
f1 = lambda x: x.group(0)

#print a dictionary
def printD(d):
    obj = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in obj:
        print('**********')
        print(i)

#filter a log file and return a list of specific lines
def file2List(filename, reStr, s=slice(None), invert=False):
    result = []
    with open(filename) as f:
        for line in f.readlines()[s]:
            match = re.search(reStr, line)
            if match and not invert: result.append(line)
            elif not match and invert: result.append(line)
    return result

#WIP
def getInfo(f, mainFilter):
    #create dictionary
    d = {}

#get the number of times an event occured and return a dictionary
def getCount(l, countFilter, f1):
    #create dictionary 
    d = {}
    for line in l:
        cfv = re.search(countFilter, line)
        cfv = f1(cfv) if cfv else '[nullVal]'
        if cfv in d: d[cfv] += 1
        else: d[cfv] = 1 
    return d

#main
def countIP(filename):
    l = file2List(filename, resIp)
    d = getCount(l, resIp, f1)
    printD(d)    

