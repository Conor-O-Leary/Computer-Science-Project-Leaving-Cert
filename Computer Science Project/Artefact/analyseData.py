import csv
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import statistics

#Collect sleep data
sleepDataFile = open("sleepData.csv", "r")

sleepDataReader = csv.reader(sleepDataFile)

next(sleepDataReader)

sleepLength = []
airQuality = []

for line in sleepDataReader:
    sleepLength.append(float(line[0]))
    
    airQualityTemp = line[1]
    
    airQualityTemp = airQualityTemp.replace("[", "")
    airQualityTemp = airQualityTemp.replace("]", "")
    
    airQualityTemp = airQualityTemp.split(",")
    
    for i in range(len(airQualityTemp)):
        airQualityTemp[i] = float(airQualityTemp[i])
    
    airQuality.append(airQualityTemp)

sleepDataFile.close()

#print(sleepLength)
#print()
#print(airQuality[0])

#Collect heart rate data
heartRateDataFile = open("heartRateData.csv", "r")

heartRateDataReader = csv.reader(heartRateDataFile)

next(heartRateDataReader)

heartRate = []

for line in heartRateDataReader:
    if len(line) > 0:
        heartRate.append(int(line[0]))

heartRateDataFile.close()

#print(heartRate)

#Collect memory level data
memoryDataFile = open("memoryData.csv", "r")

memoryDataReader = csv.reader(memoryDataFile)

next(memoryDataReader)

memory = []

for line in memoryDataReader:
    memory.append(int(line[0]))

memoryDataFile.close()

#print(memory)

#Collect perceived happiness data
perceivedHappinessDataFile = open("perceivedHappinessData.csv", "r")

perceivedHappinessDataReader = csv.reader(perceivedHappinessDataFile)

next(perceivedHappinessDataReader)

perceivedHappiness = []

for line in perceivedHappinessDataReader:
    if line[0] == "True":
        perceivedHappiness.append(True)
    else:
        perceivedHappiness.append(False)

perceivedHappinessDataFile.close()

#Collect have meditated data
haveMeditatedDataFile = open("haveMeditatedData.csv", "r")

haveMeditatedDataReader = csv.reader(haveMeditatedDataFile)

next(haveMeditatedDataReader)

haveMeditated = []

for line in haveMeditatedDataReader:
    if line[0] == "True":
        haveMeditated.append(True)
    else:
        haveMeditated.append(False)

haveMeditatedDataFile.close()

#print(perceivedHappiness)

#print()
'''
for i in range(len(haveMeditated)):
    if haveMeditated 
'''
#Create Graphs
def addGraphToPlot(figure, xvar, xlabel, yvar, ylabel, index, boolX, boolY):
    ax = figure.add_subplot(5, 1, index)
    
    ax.scatter(xvar, yvar, color = 'black')
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    #ax.set_yticklabels = ["False", "True"]
    
    ax.set_xlim(min(xvar), max(xvar))
    ax.set_ylim(min(yvar), max(yvar))
    
    if boolX:
        plt.xticks([1.0, 0.0], ["True", "False"])
    
    if boolY:
        plt.yticks([1.0, 0.0], ["True", "False"])
    
    z = np.polyfit(xvar, yvar, 1)
    p = np.poly1d(z)
    #print(p[0]) # c
    #print(p[1]) # m
    
    ax.plot(xvar, p(xvar))

#Convert sleepLength from seconds to hours
for i in range(len(sleepLength)):
    sleepLength[i] = sleepLength[i] / (60 * 60)

#Get average of airQuality
airQualityAverage = []
for i in range(len(airQuality)):
    airQualityAverage.append(sum(airQuality[i]) / len(airQuality[i]))

def showSleepLengthGraphs():
    fig1 = plt.figure(figsize = (10, 8))
    
    addGraphToPlot(fig1, sleepLength, "sleepLength (hours)", heartRate, "heartRate (bpm)", 1, False, False)
    addGraphToPlot(fig1, sleepLength, "sleepLength (hours)", memory, "memory", 3, False, False)
    addGraphToPlot(fig1, sleepLength, "sleepLength (hours)", perceivedHappiness, "perceivedHappiness", 5, False, True)
    
    plt.show()

def showAirQualityGraphs():
    fig2 = plt.figure(figsize = (10, 8))
    
    addGraphToPlot(fig2, airQualityAverage, "airQualityAverage (0 = very good, 500 = very bad)", heartRate, "heartRate (bpm)", 1, False, False)
    addGraphToPlot(fig2, airQualityAverage, "airQualityAverage (0 = very good, 500 = very bad)", memory, "memory", 3, False, False)
    addGraphToPlot(fig2, airQualityAverage, "airQualityAverage (0 = very good, 500 = very bad)", perceivedHappiness, "perceivedHappiness", 5, False, True)
    
    plt.show()

def showHaveMeditatedGraphs():
    fig3 = plt.figure(figsize = (10, 8))
    
    addGraphToPlot(fig3, haveMeditated, "haveMeditated", heartRate, "heartRate (bpm)", 1, True, False)
    addGraphToPlot(fig3, haveMeditated, "haveMeditated", memory, "memory", 3, True, False)
    addGraphToPlot(fig3, haveMeditated, "haveMeditated", perceivedHappiness, "perceivedHappiness", 5, True, True)
    
    plt.show()

data = []
for i in range(len(sleepLength)):
    row = [sleepLength[i], airQualityAverage[i], haveMeditated[i]]
    
    data.append(row)

x = data

def predictHeartRate(sleepLengthInput, airQualityAverageInput, haveMeditatedInput):
    model = LinearRegression()
    
    y = heartRate
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
    
    model.fit(x_train, y_train)
    
    prediction = model.predict([[sleepLengthInput, airQualityAverageInput, haveMeditatedInput]])
    
    print("Predicted heart rate is", round(prediction[0]))
    
    return round(prediction[0])

def predictMemory(sleepLengthInput, airQualityAverageInput, haveMeditatedInput):
    model = LinearRegression()
    
    y = memory
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
    
    model.fit(x_train, y_train)
    
    prediction = model.predict([[sleepLengthInput, airQualityAverageInput, haveMeditatedInput]])
    
    print("Predicted memory is", round(prediction[0]))
    
    return round(prediction[0])

def predictPerceivedHappiness(sleepLengthInput, airQualityAverageInput, haveMeditatedInput):
    model = LinearRegression()
    
    y = perceivedHappiness
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
    
    model.fit(x_train, y_train)
    
    prediction = model.predict([[sleepLengthInput, airQualityAverageInput, haveMeditatedInput]])
    
    prediction[0] = round(prediction[0])
    
    if prediction[0] > 0:
        prediction[0] = True
    else:
        prediction[0] = False
    
    if prediction[0] == True:
        print("Predicted perceived happiness is True")
    else:
        print("Predicted perceived happiness is False")
    
    return prediction[0]

def addBarChart(figure, index, data1, title1, data2, title2, ylabel, title3, boolX, boolY):
    ax = figure.add_subplot(5, 1, index)
    
    ax.bar([title1, title2], [data1, data2])
    
    ax.set_ylabel(ylabel)
    ax.set_title(title3)
    
    if boolX:
        plt.xticks([1.0, 0.0], ["True", "False"])
    
    if boolY:
        plt.yticks([1.0, 0.0], ["True", "False"])

def displayBarCharts(data1, title1, data2, title2):
    fig4 = plt.figure(figsize = (10, 8))
    
    #Heart rate bar chart
    addBarChart(fig4, 1, data1[0], title1, data2[0], title2, "bpm", "Heart rate change", False, False)
    
    #Memory bar chart
    addBarChart(fig4, 3, data1[1], title1, data2[1], title2, "", "Memory change", False, False)
    
    #Perceived Happiness bar chart
    addBarChart(fig4, 5, data1[2], title1, data2[2], title2, "", "Perceived happiness change", False, True)
    
    plt.show()

#Model
while True:
    print("Menu")
    print("1) Graphs")
    print("2) Model")
    print("3) What if questions")
    print("4) Progress")
    print("5) Analyse data")
    print("6) End Program")
    
    option = input("Choose the number with corresponding action you wish to do: ")
    
    print()
    
    if option == "1":
        print("Menu")
        print("1) Sleep Length Graphs")
        print("2) Air Quality Graphs")
        print("3) Have Meditated Graphs")
        
        option = input("Choose the number with corresponding action you wish to do: ")
        
        if option == "1":
            showSleepLengthGraphs()
        elif option == "2":
            showAirQualityGraphs()
        elif option == "3":
            showHaveMeditatedGraphs()
    elif option == "2":
        sleepLengthInput = float(input("Enter a length of sleep in hours: "))
        airQualityAverageInput = float(input("Enter the air quality average while sleeping: "))
        haveMeditatedInput = input("Enter have meditated (Y/N): ")
        
        if haveMeditatedInput == "Y":
            haveMeditatedInput = True
        else:
            haveMeditatedInput = False
        
        print()
        
        predictHeartRate(sleepLengthInput, airQualityAverageInput, haveMeditatedInput)
        predictMemory(sleepLengthInput, airQualityAverageInput, haveMeditatedInput)
        predictPerceivedHappiness(sleepLengthInput, airQualityAverageInput, haveMeditatedInput)
    
    elif option == "3":
        print("What if questions!")
        print("------------------")
        
        #Calculate Baselines
        totalSleepLength = 0
        totalAirQualityAverage = 0
        totalHaveMeditatedBaseline = 0
        for i in range(len(sleepLength)):
            totalSleepLength += sleepLength[i]
            totalAirQualityAverage += airQualityAverage[i]
            totalHaveMeditatedBaseline += haveMeditated[i]
        sleepLengthBaseline = round(totalSleepLength / len(sleepLength), 2)
        airQualityAverageBaseline = round(totalAirQualityAverage / len(airQualityAverage), 2)
        haveMeditatedBaseline = round(totalHaveMeditatedBaseline / len(haveMeditated))
        
        print("Q1: What if my sleep length, air quality while sleeping and have I meditated that day is at baseline, what will my heart rate, memory level and perceived happiness be?")
        
        print("sleep length baseline:", sleepLengthBaseline, "hours")
        print("air quality average baseline:", airQualityAverageBaseline)
        
        if haveMeditatedBaseline == True:
            print("have meditated baseline: True")
        else:
            print("have meditated baseline: False")
        
        print()
        
        Q1PredictedHeartRate = predictHeartRate(sleepLengthBaseline, airQualityAverageBaseline, haveMeditatedBaseline)
        Q1PredictedMemory = predictMemory(sleepLengthBaseline, airQualityAverageBaseline, haveMeditatedBaseline)
        Q1PredictedPerceivedHappiness = predictPerceivedHappiness(sleepLengthBaseline, airQualityAverageBaseline, haveMeditatedBaseline)
        
        print()
        
        print("Q2: What if my sleep length and air quality while sleeping is at baseline and I have meditated that day, what will my heart rate, memory level and perceived happiness be?")
        
        print("sleep length baseline:", sleepLengthBaseline, "hours")
        print("air quality average baseline:", airQualityAverageBaseline)
        print("have meditated: True")
        
        print()
        
        Q2PredictedHeartRate = predictHeartRate(sleepLengthBaseline, airQualityAverageBaseline, True)
        Q2PredictedMemory = predictMemory(sleepLengthBaseline, airQualityAverageBaseline, True)
        Q2PredictedPerceivedHappiness = predictPerceivedHappiness(sleepLengthBaseline, airQualityAverageBaseline, True)
        
        print()
        
        print("Q3: What if my sleep length and have I meditated that day is at baseline and air quality while sleeping is 50% better than baseline, what will my heart rate, memory level and perceived happiness be?")
        
        print("sleep length baseline:", sleepLengthBaseline, "hours")
        print("air quality average 50% better than baseline:", airQualityAverageBaseline * 0.5)
        
        if haveMeditatedBaseline == True:
            print("have meditated baseline: True")
        else:
            print("have meditated baseline: False")
        
        print()
        
        Q3PredictedHeartRate = predictHeartRate(sleepLengthBaseline, airQualityAverageBaseline * 0.5, haveMeditatedBaseline)
        Q3PredictedMemory = predictMemory(sleepLengthBaseline, airQualityAverageBaseline * 0.5, haveMeditatedBaseline)
        Q3PredictedPerceivedHappiness = predictPerceivedHappiness(sleepLengthBaseline, airQualityAverageBaseline * 0.5, haveMeditatedBaseline)
        
        print()
        
        print("Q4: What if air quality while sleeping and have I meditated that day is at baseline and sleep length is 50% better than baseline, what will my heart rate, memory level and perceived happiness be?")
        
        print("sleep length 50% better than baseline:", sleepLengthBaseline * 1.5, "hours")
        print("air quality baseline:", airQualityAverageBaseline)
        
        if haveMeditatedBaseline == True:
            print("have meditated baseline: True")
        else:
            print("have meditated baseline: False")
        
        print()
        
        Q4PredictedHeartRate = predictHeartRate(sleepLengthBaseline * 1.5, airQualityAverageBaseline, haveMeditatedBaseline)
        Q4PredictedMemory = predictMemory(sleepLengthBaseline * 1.5, airQualityAverageBaseline, haveMeditatedBaseline)
        Q4PredictedPerceivedHappiness = predictPerceivedHappiness(sleepLengthBaseline * 1.5, airQualityAverageBaseline, haveMeditatedBaseline)
        
        print()
        
        #User Insights
        print("User Insights")
        print("-------------")
        
        print("'What if' Q1 and Q2 shown above show that meditating results in lower heart rate, higher memory level and higher perceived happiness")
        
        data1 = [Q1PredictedHeartRate, Q1PredictedMemory, Q1PredictedPerceivedHappiness]
        data2 = [Q2PredictedHeartRate, Q2PredictedMemory, Q2PredictedPerceivedHappiness]
        displayBarCharts(data1, "Has not meditated that day", data2, "Has meditated that day")
        
        print("'What if' Q1 and Q3 shown above show that a better air quality while sleeping results in lower heart rate, higher memory level and higher perceived happiness")
        
        data1 = [Q1PredictedHeartRate, Q1PredictedMemory, Q1PredictedPerceivedHappiness]
        data2 = [Q3PredictedHeartRate, Q3PredictedMemory, Q3PredictedPerceivedHappiness]
        displayBarCharts(data1, "Air quality at baseline", data2, "Air quality 50% better than baseline")
        
        print("'What if' Q1 and Q4 shown above show that a higher sleep length results in lower heart rate, higher memory level and higher perceived happiness")
        
        data1 = [Q1PredictedHeartRate, Q1PredictedMemory, Q1PredictedPerceivedHappiness]
        data2 = [Q4PredictedHeartRate, Q4PredictedMemory, Q4PredictedPerceivedHappiness]
        displayBarCharts(data1, "Sleep length at baseline", data2, "Sleep length 50% higher than baseline")
        
    elif option == "4":
        #General graph stuff
        dayNums = range(0, len(sleepLength))
        days = []
        for dayNum in dayNums:
            days.append("Day " + str(dayNum + 1))
        
        #Sleep length graph
        plt.plot(sleepLength)
        plt.ylabel("Hours of sleep")
        plt.title("sleep length over time")
        plt.subplots_adjust(bottom = 0.15)
        plt.xticks(dayNums, days, rotation = "vertical")
        
        plt.show()
        
        #Air quality graph
        plt.plot(airQualityAverage)
        plt.ylabel("Air quality average (0 = very good, 500 = very bad)")
        plt.title("Average air quality while sleeping over time")
        plt.subplots_adjust(bottom = 0.15)
        plt.xticks(dayNums, days, rotation = "vertical")
        
        plt.show()
        
        #Have meditated graph
        plt.plot(haveMeditated)
        plt.ylabel("have Meditated")
        plt.title("have Meditated over time")
        plt.subplots_adjust(bottom = 0.15)
        plt.xticks(dayNums, days, rotation = "vertical") 
        
        plt.yticks([1.0, 0.0], ["True", "False"])
        
        plt.show()
        
        #Heart rate graph
        plt.plot(heartRate)
        plt.ylabel("bpm")
        plt.title("Heart rate over time")
        plt.subplots_adjust(bottom = 0.15)  
        plt.xticks(dayNums, days, rotation = "vertical")
        
        plt.show()
        
        #Memory graph
        plt.plot(memory)
        plt.ylabel("memory level")
        plt.title("memory level over time")
        plt.subplots_adjust(bottom = 0.15)  
        plt.xticks(dayNums, days, rotation = "vertical") 
        
        plt.show()
        
        #Perceived happiness graph
        plt.plot(perceivedHappiness)
        plt.ylabel("perceived Happiness")
        plt.title("perceived Happiness over time")
        plt.subplots_adjust(bottom = 0.15)  
        plt.xticks(dayNums, days, rotation = "vertical") 
        
        plt.yticks([1.0, 0.0], ["True", "False"])
        
        plt.show()
    
    elif option == "5":
        #Mean
        sleepLengthMean = round(statistics.mean(sleepLength), 2)
        airQualityMean = round(statistics.mean(airQualityAverage), 2)
        haveMeditatedMean = round(statistics.mean(haveMeditated))
        
        heartRateMean = round(statistics.mean(heartRate), 2)
        memoryMean = round(statistics.mean(memory), 2)
        perceivedHappinessMean = round(statistics.mean(perceivedHappiness))
        
        #Find min
        sleepLengthMin = round(min(sleepLength), 2)
        airQualityAverageMin = round(min(airQualityAverage), 2)
        
        heartRateMin = round(min(heartRate), 2)
        memoryMin = round(min(memory), 2)
        
        #Find max
        sleepLengthMax = round(max(sleepLength), 2)
        airQualityAverageMax = round(max(airQualityAverage), 2)
        
        heartRateMax = round(max(heartRate), 2)
        memoryMax = round(max(memory), 2)
        
        #Inform user on sleep length
        print("sleep length")
        print("------------")
        print("Your sleep length mean is", sleepLengthMean, "hours.")
        if sleepLengthMean < 8:
            print("You need more sleep on average. Try limiting exposure to screens before bed and limiting caffeine close to bedtime.")
        elif sleepLengthMean < 12:
            print("You have a good amount of sleep on average. Great work!")
        else:
            print("You are having too much sleep. Try maintaing a consistent sleep routine and stay active.")
        
        print()
        sleepLengthDif = round(sleepLengthMax - sleepLengthMin, 2)
        print("The difference between your minimum and maximum sleep length is", sleepLengthDif, "hours.")
        if sleepLengthDif < 4:
            print("You don't have a high variation in sleep length. Good job!")
        else:
            print("You have a high variation in sleep length. Try maintaing a consistent sleep schedule.")
        
        print()
        #Inform user on average air quality when sleeping
        print("air quality")
        print("-----------")
        print("Your air quality mean is", airQualityMean)
        if airQualityMean < 40:
            print("Great! Your air quality is good on average!")
        else:
            print("Your air quality while sleeping needs to be improved. Try opening a window in your bedroom and keeping your bedroom clean.")
        
        print()
        print("Your air quality max is", airQualityAverageMax)
        if airQualityAverageMax > 80:
            print("This air quality is very high. This is a major hazard to your health and sleep quality. Try opening a window in your bedroom and keeping your bedroom clean.")
        else:
            print("Your maximum air quality is not bad. Good work!")
        
        print()
        #Inform user on meditation
        print("meditation")
        print("----------")
        if haveMeditated == True:
            print("You meditate most days.")
        else:
            print("You do not meditate most days. Try planning a time in the day to meditate.")
        
        print()
        #Inform user on heart rate
        print("heart rate")
        print("----------")
        print("Your heart rate mean is", heartRateMean, "bpm.")
        if heartRateMean < 40:
            print("Your heart rate mean is low. Please, ensure you have a good sleep length, air quality and meditate and also make sure you get daily exercise.")
        elif heartRateMean < 90:
            print("Your heart rate mean is good!")
        else:
            print("Your heart rate mean is high. Please, ensure you have a good sleep length, air quality and meditate and also make sure you get daily exercise.")
        
        print()
        heartRateDif = round(heartRateMax - heartRateMin, 2)
        print("The difference between your minimum and maximum heart rate is", heartRateDif, "bpm.")
        if heartRateDif < 40:
            print("You don't have a high variation in heart rate. Good job!")
        else:
            print("You have a high variation in heart rate. Please, ensure you have a good sleep length, air quality and meditate and also make sure you get daily exercise.")
        
        print()
        #Inform user on memory
        print("memory")
        print("------")
        print("Your memory level mean is", memoryMean)
        if memoryMean < 4:
            print("Your memory level mean is low. You must be very tired from lack of sleep. Please, ensure you have a good sleep length, air quality and meditate and also engage in activites that challenge your brain such as programming/reading.")
        else:
            print("Your memory level mean is good. Congrats!")
        
        print()
        memoryDif = round(memoryMax - memoryMin, 2)
        print("The difference between your minimum and maximum memory level is", memoryDif)
        if memoryDif < 5:
            print("You don't have a high variation in memory level. Good job!")
        else:
            print("You have a high variation in memory level. Please, ensure you have a good sleep length, air quality and meditate and also engage in activites that challenge your brain such as programming/reading.")
        
        print()
        #Inform user on perceivedHappiness
        print("perceived happiness")
        print("-------------------")
        
        if perceivedHappinessMean == True:
            print("You are happy most days.")
        else:
            print("You are not happy most days. Please, ensure you have a good sleep length, air quality and meditate and make sure you engage in hobbies you enjoy such as sport, reading, listening to music, etc.")
        
    elif option == "6":
        print("Thank you for using this program!")
        break
    else:
        print("Error: You may have mispelled your input")
    
    print()
