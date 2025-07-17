import csv
import random

sleepDataFile = open("sleepData.csv", "a", newline = "")
sleepDataFileWrite = csv.writer(sleepDataFile)

memoryDataFile = open("memoryData.csv", "a", newline = "")
memoryDataFileWrite = csv.writer(memoryDataFile)

heartRateDataFile = open("heartRateData.csv", "a", newline = "")
heartRateDataFileWrite = csv.writer(heartRateDataFile)

perceivedHappinessDataFile = open("perceivedHappinessData.csv", "a", newline = "")
perceivedHappinessDataFileWrite = csv.writer(perceivedHappinessDataFile)

haveMeditatedDataFile = open("haveMeditatedData.csv", "a", newline = "")
haveMeditatedDataFileWrite = csv.writer(haveMeditatedDataFile)

#Generate Data
for i in range(30):
    sleepLength = random.randint(10800, 43200) #(60 * 60) * (3 + random.randint(0, 9))
    #print(sleepLength / (60 * 60))
    
    haveMeditatedNum = random.randint(0, 1)
    if haveMeditatedNum == 0:
        haveMeditated = False
    elif haveMeditatedNum == 1:
        haveMeditated = True
    
    baseAirQuality = random.randint(10, 80)
    airQuality = []
    for j in range(round(sleepLength / (60 * 10))):
       airQuality.append(baseAirQuality + random.randint(-5, 5)) 
    
    #print(airQuality)
    
    #print("sleepDif", ((sleepLength / (60 * 60)) * 2))
    #print("medDif", (haveMeditated * 15))
    #print("airDif", (baseAirQuality / 4))
    
    heartRate = round(100 - ((sleepLength / (60 * 60)) * 5) + (baseAirQuality / 2) - (haveMeditated * 15))# + random.randint(-5, 5)
    #print(heartRate)
    #print()
    #print(heartRate)
    
    #print("sleepDif", ((sleepLength / (60 * 60)) / 3))
    #print("medDif", (haveMeditated * 2))
    #print("airDif", (baseAirQuality / 20))
    memory = round(3 + ((sleepLength / (60 * 60)) / 3) - (baseAirQuality / 20) + (haveMeditated * 2))
    #print(memory)
    #print()
    
    #print("sleepDif", ((sleepLength / (60 * 60)) / 3))
    #print("medDif", (haveMeditated * 2))
    #print("airDif", (baseAirQuality / 20))
    perceivedHappiness = ((sleepLength / (60 * 60)) / 3) - (baseAirQuality / 20) + (haveMeditated * 2) - 1
    #print(perceivedHappiness)
    #print()
    
    if perceivedHappiness < 0:
        perceivedHappiness = False
    else:
        perceivedHappiness = True
    
    #print()
    
    sleepDataFileWrite.writerow([sleepLength, airQuality])
    heartRateDataFileWrite.writerow([heartRate])
    memoryDataFileWrite.writerow([memory])
    perceivedHappinessDataFileWrite.writerow([perceivedHappiness])
    haveMeditatedDataFileWrite.writerow([haveMeditated])

print("finished")

sleepDataFile.close()
memoryDataFile.close()
heartRateDataFile.close()
perceivedHappinessDataFile.close()
haveMeditatedDataFile.close()