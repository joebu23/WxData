import helpers
import forecastDay
import textHelper
import datetime
from datetime import timedelta 

def getData(startYear, startMonth, startDay, dayDuration):
    year = startYear
    month = startMonth
    day = startDay
    daysToGet = dayDuration

    startDate = datetime.datetime(year, month, day)

    f = open("weatherData.csv","w+")
    weeksData = []

    for nDay in range(0,daysToGet):
        dateToGet = startDate + timedelta(days=nDay)  

        url_to_get = helpers.getUrl(dateToGet.year, str(dateToGet.month).zfill(2), str(dateToGet.day).zfill(2))

        data = helpers.getForecastData(url_to_get)   #dateToGet.year, str(dateToGet.month).zfill(2), str(dateToGet.day).zfill(2))

        if len(data) > 1:
            dateData, forecastData, tempData, preciptData = textHelper.getLinesWithPertinentData(data)

        try:
            # if forecastData is not None:
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
            
                newObject = forecastDay.ForecastDay(date, high, low, preciptPM, preciptAM, forecast, dateToGet)
                weeksData.append(newObject)
        except:
            newObject = forecastDay.ForecastDay(dateToGet, 999, 999, 999, 999, 'NA', datetime.datetime(1,1,1))
            weeksData.append(newObject)

    for data in weeksData:
        f.write(str(data.date) + ',' + str((data.date - data.forecastDate).days) + ',' + str(data.high) + ',' + str(data.low) + '\n')