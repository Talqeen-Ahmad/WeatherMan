import calendar
import os
import re
from termcolor import colored

#Global Variables

path = "/home/talqeen/Downloads/weatherdata/"
index = 0
completeDate = ""
count = 0
fileNames = []
monthFiles = []
MaxTempMonthWise = []
LowTempMonthWise = []
dateMonthWise = []
Humid = []


    #Clear global variables after use

def clearVariables():
    global  index
    global count
    index = 0
    count = 0
    fileNames.clear()
    monthFiles.clear()
    MaxTempMonthWise.clear()
    LowTempMonthWise.clear()
    dateMonthWise.clear()
    Humid.clear()

   # Getting a specific year's data

def getFiles(year):
    for files in os.listdir(path):
        if re.match('.*'+year+'.*',files):
            fileNames.append(files)

    # Getting a specific Month data

def getFile(year,month):
    for files in os.listdir(path):
        if re.match('.*' + year + '.*', files):
            fileNames.append(files)

    for mon in fileNames:
        if re.match('.*'+month+'.*',mon):
            monthFiles.append(mon)

    # Read data from files

def readFromFiles():
    for myFile in fileNames:
        file1 = (open(path+myFile,"r"))
        for line in file1:
            if line == "\n" or re.match('.*!--.*',line):
                continue
            r = line.split(",")
            if r[1] == "":
                continue

            MaxTempMonthWise.append(r[1])
            LowTempMonthWise.append(r[3])
            Humid.append(r[7])
            dateMonthWise.append(r[0])


            # Read data from file for am month

def readFromFile():
    for myFile in monthFiles:
        file1 = (open(path+myFile,"r"))
        for line in file1:
            if line == "\n" or re.match('.*!--.*',line):
                continue
            r = line.split(",")
            if r[1] == "":
                continue

            global count
            count += 1
            MaxTempMonthWise.append(r[1])
            LowTempMonthWise.append(r[3])
            Humid.append(r[7])
            dateMonthWise.append(r[0])


    # Removing unnecessary elements

def removingElements():
    a = 0
    while a<12:
        MaxTempMonthWise.remove("Max TemperatureC")
        LowTempMonthWise.remove("Min TemperatureC")
        Humid.remove("Max Humidity")
        if "PKT" in dateMonthWise:
            dateMonthWise.remove("PKT")
        else:
            dateMonthWise.remove("PKST")
        a += 1

        # Removing unnecessary element from month file

def removingElement():
    global count
    count -= 1
    MaxTempMonthWise.remove("Max TemperatureC")
    LowTempMonthWise.remove("Min TemperatureC")
    Humid.remove("Max Humidity")
    if "PKT" in dateMonthWise:
        dateMonthWise.remove("PKT")
    else:
        dateMonthWise.remove("PKST")
    templistConversion()


        # Converting MaxTempMonthWise into integer list

def templistConversion():
    global MaxTempMonthWise
    global LowTempMonthWise
    global Humid
    MaxTempMonthWise = list(map(int, MaxTempMonthWise))
    LowTempMonthWise = list(map(int, LowTempMonthWise))
    Humid = list(map(int, Humid))

def showAverage():
    global MaxTempMonthWise
    global LowTempMonthWise
    global Humid
    global count
    sumMaxTemp = sum(MaxTempMonthWise)
    sumLowTemp = sum(LowTempMonthWise)
    sumHumid = sum(Humid)
    averageMaxTemp = int(sumMaxTemp/count)
    averageLowTemp = int(sumLowTemp/count)
    averageHumid = int(sumHumid/count)
    print("Highest Average: "+str(averageMaxTemp)+"C")
    print("Lowest Average: " + str(averageLowTemp) + "C")
    print("Average Humidity: " + str(averageHumid) + "%")



    # Date Conversion

def dateConversion():
    rawDate = (dateMonthWise[index])
    rawDate = rawDate.split("-")
    global completeDate
    completeDate = calendar.month_name[int(rawDate[1])]
    completeDate = completeDate+" "+rawDate[2]

    # Print

def printData():
    maxValue = max(MaxTempMonthWise)
    minValue = min(LowTempMonthWise)
    maxHumid = max(Humid)
    global index
    index = MaxTempMonthWise.index(maxValue)
    minIndex = LowTempMonthWise.index(minValue)
    humidIndex = Humid.index(maxHumid)
    print("Highest: " + str(MaxTempMonthWise[index]) + "C on " + dateMonthWise[index])
    print("Lowest: " +  str(LowTempMonthWise[minIndex]) + "C on " + dateMonthWise[minIndex])
    print("Humidity: " + str(Humid[humidIndex]) + "% on " + dateMonthWise[humidIndex])

def printChart():

     for a,b,c in zip(MaxTempMonthWise,LowTempMonthWise,dateMonthWise):
        print(c + colored("+"*a,"red") + str(a) + "C")
        print(c + colored("+"*b,"blue")+ str(b) + "C")


def printBarChart():
    for a, b, c in zip(MaxTempMonthWise, LowTempMonthWise, dateMonthWise):
        print(c + colored("+" * b, "blue") + colored("+" * a, "red") + str(b)+"C "+ str(a)+"C")


     # Main Method


while 1 == 1:
  try:
    choice = int(input("Press 1 for year base information\nPress 2 for Month base information\nPress 3 to print chart\nPress 4 to make horizontal bar chart for each day\nPress 5 exit: "))
    if choice == 1:
        year = str(input("Enter the year you want to get information: "))
        getFiles(year)
        readFromFiles()
        removingElements()
        templistConversion()
        printData()
    elif choice == 2:
        year = str(input("Enter the year you want to get information: "))
        month = str(input("Enter the month (i.e Jan): "))
        getFile(year,month)
        readFromFile()
        removingElement()
        showAverage()
    elif choice == 3:
        year = str(input("Enter the year you want to get information: "))
        month = str(input("Enter the month (i.e Jan): "))
        getFile(year, month)
        readFromFile()
        removingElement()
        printChart()

    elif choice == 4:
        year = str(input("Enter the year you want to get information: "))
        month = str(input("Enter the month (i.e Jan): "))
        getFile(year, month)
        readFromFile()
        removingElement()
        printBarChart()


    elif choice == 5:
        break


    else:
        print("Wrong choice")

    clearVariables()
    choice = 0
    print("\n")

  except:
      print("Unexpectd error!!!")
      clearVariables()
      choice = 0






