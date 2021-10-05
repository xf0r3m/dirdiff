#! /usr/bin/env python

import sys
import os

#https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def help():
    print("dirdiff - skrypt poszukujący różnic w zawartości katalogu")
    print("morketsmerke @ 2021; COPYLEFT; ALL RIGHTS REVERSED")
    print()
    print("$ ./dirdiff <katalog_docelowy> <katalog_źródłowy>")


myname=sys.argv[0]

if len(sys.argv) == 3:
    dest=sys.argv[1]
    src=sys.argv[2]
else:
    help();
    os._exit(1);

if not os.path.isdir(dest) or not os.path.isdir(src):
    help();
    os._exit(1);


destListDir=os.listdir(dest)
srcListDir=os.listdir(src)

i=0;
j=0;
destLDLen=len(destListDir)
srcLDLen=len(srcListDir)
#endValue='\t\t'

print(f"{dest}[{destLDLen}]:\t{src}[{srcLDLen}]:")

while i<=(destLDLen - 1) or j<=(srcLDLen - 1):
    if i<=(destLDLen - 1):
        #if len(destListDir[i]) > 25:
        #    endValue='\t'
        #elif len(destListDir[i]) >= 20:
        #    endValue='\t\t'
        #else:
        #    endValue='\t\t\t'
        #if os.path.isdir(f"{dest}/{destListDir[i]}"):
        #    print(f"[{i}]: {destListDir[i]}/", end=endValue)
        #else:
        #    print(f"[{i}]: {destListDir[i]}", end=endValue)
        i=i+1

    if j<=(srcLDLen - 1):
        if os.path.isdir(f"{src}/{srcListDir[j]}"):
            fileName=f"{srcListDir[j]}/"
        else:
            fileName=f"{srcListDir[j]}"
        if j < i:
            if os.path.exists(f"{dest}/{srcListDir[j]}"):
                flag=bcolors.BOLD
            else:
                flag=bcolors.FAIL
            print(f"[{j + 1}]: {flag}{fileName}{bcolors.ENDC}")
        else:
            if os.path.exists(f"{dest}/{srcListDir[j]}"):
                flag=bcolors.BOLD
            else:
                flag=bcolors.OKCYAN
            
            print(f"[{j + 1}]: {flag}{fileName}{bcolors.ENDC}")
        #if j <= i:
        #    if destListDir[j] == srcListDir[j]:
        #        print(f"{bcolors.BOLD}{destListDir[j]}{bcolors.ENDC}")
        #    else:
        #        print(f"{bcolors.FAIL}{destListDir[j]}{bcolors.ENDC}")
        #
        #else:
        #    print(f"{bcolors.OKCYAN}{destListDir[j]}{bcolors.ENDC}")
        j=j+1
