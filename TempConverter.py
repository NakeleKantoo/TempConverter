#!/bin/python3
import math
import sys


args=sys.argv[1:]

TimeK=0
TimeC=0
TimeF=0

if args[0]=="-c":
    TimeC=int(args[1])
    TimeK=TimeC-273.15
    TimeF=TimeC*9/5+32
elif args[0]=="-k":
    TimeK=int(args[1])
    TimeC=TimeK+273.15
    TimeF=(TimeK-273.15)*9/5+32
elif args[0]=="-f":
    TimeF=int(args[1])
    TimeC=(TimeF-32)*5/9
    TimeK=TimeC-273.15
elif args[0]=="-h":
    print("TempConverter is a CLI tool for converting the temperature between different scales!")
    print("Flags:")
    print("-c [Temperature] Temperature in Celsius")
    print("-k [Temperature] Temperature in Kelvin")
    print("-f [Temperature] Temperature in Fahrenheit")
    exit()

print("Cº:", round(TimeC))
print("Fº:", round(TimeF))
print("K:", round(TimeK))