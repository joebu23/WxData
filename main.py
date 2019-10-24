import helpers
import forecastDay
import textHelper
import datetime
from datetime import timedelta 

rangeData = []

year = 2018
month = 10
day = 15

startDate = datetime.datetime(year, month, day)

daysToGet = 190

f = open("weatherData.csv","w+")

for nDay in range(0,daysToGet):
    # dateToGet = startDate + nDay
    dateToGet = startDate + timedelta(days=nDay)  

    data = helpers.getForecastData(dateToGet.year, str(dateToGet.month).zfill(2), str(dateToGet.day).zfill(2))
    counter = 0
    cityCounter = 0
    dateCounter = 0

    weeksData = []
    # forecasts = []
    # days = []
    highs = []
    lows = []

    if data != '':
        dateData, forecastData, tempData, preciptData = textHelper.getLinesWithPertinentData(data)

    if forecastData is not None:
        forecasts = textHelper.generateForecastData(forecastData)
        days = textHelper.generateDayparts(dateData, year)
        temps = textHelper.generateForecastData(tempData)
        precipt = textHelper.generateForecastData(preciptData)

        for n in range(7):
            forecast = forecasts[n]
            date = days[n]

            if temps[n].split('/')[1] != 'MM':
                high = int(temps[n].split('/')[1])
            else:
                high = 9999

            if temps[n].split('/')[0] != 'MM':
                low = int(temps[n].split('/')[0])
            else:
                low = 9999

            if precipt[n].split('/')[0] != 'MM':
                preciptPM = int(precipt[n].split('/')[0])
            else:
                preciptPM = 9999

            if precipt[n].split('/')[1] != 'MM':
                preciptAM = int(precipt[n].split('/')[1])
            else:
                preciptAM = 9999
            
            forecastDate = datetime.datetime(year, int(month), int(day))
    
            newObject = forecastDay.ForecastDay(date, high, low, preciptPM, preciptAM, forecast, forecastDate)
            # print('date: ' + str(date) + ' high: ' + str(high) + ' low: ' + str(low) + ' forecast: ' + str(forecast) + ' fdate: ' + str(forecastDate))
            # print('pm preceipt: ' + str(preciptPM) + ' am: ' + str(preciptAM))
            # print((date - forecastDate).days)
            # print(newObject)
            weeksData.append(newObject)


for data in weeksData:
    f.write(str(data.date) + ',' + str((data.date - data.forecastDate).days) + ',' + str(data.high) + ',' + str(data.low))