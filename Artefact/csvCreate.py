import csv

#Create sleep data CSV file
sleepDataFile = open("sleepData.csv", "a", newline = "")

sleepDataFileWrite = csv.writer(sleepDataFile)

header = ["sleepLength", "airQuality"]
sleepDataFileWrite.writerow(header)

sleepDataFile.close()

#Create heart rate tracker CSV file
heartRateDataFile = open("heartRateData.csv", "a", newline = "")

heartRateDataFileWrite = csv.writer(heartRateDataFile)

header = ["heartRate"]
heartRateDataFileWrite.writerow(header)

heartRateDataFile.close()

#Create memory tracker CSV file
memoryDataFile = open("memoryData.csv", "a", newline = "")

memoryDataFileWrite = csv.writer(memoryDataFile)

header = ["memoryLevel"]
memoryDataFileWrite.writerow(header)

memoryDataFile.close()

#Create perceived happiness CSV file
perceivedHappinessDataFile = open("perceivedHappinessData.csv", "a", newline = "")

perceivedHappinessDataFileWrite = csv.writer(perceivedHappinessDataFile)

header = ["perceivedHappiness"]
perceivedHappinessDataFileWrite.writerow(header)

perceivedHappinessDataFile.close()

#Create have meditated CSV file
haveMeditatedDataFile = open("haveMeditatedData.csv", "a", newline = "")

haveMeditatedDataFileWrite = csv.writer(haveMeditatedDataFile)

header = ["haveMeditated"]
haveMeditatedDataFileWrite.writerow(header)

haveMeditatedDataFile.close()

print("finished")