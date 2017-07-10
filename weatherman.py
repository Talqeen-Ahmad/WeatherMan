import os
import re
import calendar

    #Global Variables

path = "/home/talqeen/Downloads/weatherdata/"
index = 0
completeDate = ""
fileNames = []
MaxTempMonthWise = []
LowTempMonthWise = []
dateMonthWise = []
Humid = []

    # Getting a specific year's data

def getFiles(year):
    for files in os.listdir(path):
        if re.match('.*'+year+'.*',files):
            fileNames.append(files)

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

        # Converting MaxTempMonthWise into integer list

def templistConversion():
    global MaxTempMonthWise
    global LowTempMonthWise
    global Humid
    MaxTempMonthWise = list(map(int, MaxTempMonthWise))
    LowTempMonthWise = list(map(int, LowTempMonthWise))
    Humid = list(map(int, Humid))


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


     # Main Method

year = str(input("Enter the year you want to get information: "))
getFiles(year)
readFromFiles()
removingElements()
templistConversion()
#dateConversion()
printData()










