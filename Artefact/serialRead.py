import serial
import time
import csv
import msvcrt

ser= serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.open()

airQualityList = []

print("Your heart rate, memory level, sleep length, air quality when sleeping and perceived happiness will be recorded and processed in this program")
print()

while True:
    microbitdata = (str(ser.readline()))
    microbitdata = microbitdata[2:-5]
    
    print(microbitdata)
    
    namePosition = microbitdata.find(":")
    
    dataName = microbitdata[:namePosition]
    dataValue = microbitdata[namePosition + 1:]
    
    print(dataName)
    print(dataValue)
    print()
    
    if dataName == "a":
        airQuality = float(dataValue)
        
        if airQuality >= 0 and airQuality <= 100:
            airQualityList.append(airQuality)
        else:
            print("Validation Error")
            print()
    elif dataName == "s":
        sleepLength = float(dataValue)
        
        if sleepLength > 0 and sleepLength <= 15 * (60 * 60):
            if sleepLength < 7 * (60 * 60):
                print("You are not having enough sleep")
            elif sleepLength > 11 * (60 * 60):
                print("You are having too much sleep")
            else:
                print("You are having a good amount of sleep")
            
            #Get average of air quality
            totalAirQuality = 0
            for airQuality in airQualityList:
                totalAirQuality += airQuality
            
            averageAirQuality = totalAirQuality / len(airQualityList)
            
            if averageAirQuality > 50:
                print("The air quality needs to be improved")
            elif averageAirQuality > 20:
                print("The air quality is good")
            else:
                print("The air quality is very good")
            
            sleepDataFile = open("sleepData.csv", "a", newline = "")
            
            sleepDataFileWrite = csv.writer(sleepDataFile)
            sleepDataFileWrite.writerow([sleepLength, airQualityList])
        else:
            print("Validation Error")
        print()
        
        sleepDataFile.close()
    elif dataName == "r":
        heartRate = int(dataValue)
        
        if heartRate >= 20 and heartRate <= 220:
            if heartRate >= 100:
                print("Your heart rate is too high")
            elif heartRate <= 50:
                print("Your heart rate is too low")
            else:
                print("Your heart rate is good")
            
            heartRateDataFile = open("heartRateData.csv", "a", newline = "")
            
            heartRateDataFileWrite = csv.writer(heartRateDataFile)
            heartRateDataFileWrite.writerow([heartRate])
            
            heartRateDataFile.close()
        else:
            print("Validation Error")
        print()
    elif dataName == "m":
        memoryLevel = int(dataValue)
        
        if memoryLevel >= 1 and memoryLevel <= 20:
            if memoryLevel <= 2:
                print("Your memory level is poor")
            elif memoryLevel >= 6:
                print("Your memory is very good")
            else:
                print("Your memory is good")
            
            memoryDataFile = open("memoryData.csv", "a", newline = "")
            
            memoryDataFileWrite = csv.writer(memoryDataFile)
            memoryDataFileWrite.writerow([memoryLevel])
            
            memoryDataFile.close()
        else:
            print("Validation Error")
        print()
    elif dataName == "h":
        perceivedHappiness = int(dataValue)
        if perceivedHappiness == 0:
            perceivedHappiness = False
            
            perceivedHappinessDataFile = open("perceivedHappinessData.csv", "a", newline = "")
            
            perceivedHappinessDataFileWrite = csv.writer(perceivedHappinessDataFile)
            perceivedHappinessDataFileWrite.writerow([perceivedHappiness])
            
            perceivedHappinessDataFile.close()
        elif perceivedHappiness == 1:
            perceivedHappiness = True
        
            perceivedHappinessDataFile = open("perceivedHappinessData.csv", "a", newline = "")
            
            perceivedHappinessDataFileWrite = csv.writer(perceivedHappinessDataFile)
            perceivedHappinessDataFileWrite.writerow([perceivedHappiness])
            
            perceivedHappinessDataFile.close()
        else:
            print("Validation Error")
            print()
    elif dataName == "d":
        haveMeditated = int(dataValue)
        if haveMeditated == 0:
            haveMeditated = False
            
            haveMeditatedDataFile = open("haveMeditatedData.csv", "a", newline = "")
            
            haveMeditatedDataFileWrite = csv.writer(haveMeditatedDataFile)
            haveMeditatedDataFileWrite.writerow([haveMeditated])
            
            haveMeditatedDataFile.close()
        elif haveMeditated == 1:
            haveMeditated = True
        
            haveMeditatedDataFile = open("haveMeditatedData.csv", "a", newline = "")
            
            haveMeditatedDataFileWrite = csv.writer(haveMeditatedDataFile)
            haveMeditatedDataFileWrite.writerow([haveMeditated])
            
            haveMeditatedDataFile.close()
        else:
            print("Validation Error")
            print()

print("finished")

ser.close()