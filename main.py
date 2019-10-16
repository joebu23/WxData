import helpers
import forecastDay
import textHelper
import datetime

rangeData = []

year = 2019
month = '01'
day = '27'

data = helpers.getForecastData(year, month, day)
counter = 0
cityCounter = 0
dateCounter = 0

weeksData = []
# forecasts = []
# days = []
highs = []
lows = []

dateData, forecastData = textHelper.getLinesWithPertinentData(data)

forecasts = textHelper.generateForecastData(forecastData)
days = textHelper.generateDayparts(dateData, year)

for n in range(7):
    forecast = forecasts[n]
    date = days[n]
    high = 89
    low = 9
    forecastDate = datetime.datetime(year, int(month), int(day))
    
    newObject = forecastDay.ForecastDay(date, high, low, forecast, forecastDate)
    weeksData.append(newObject)

print(weeksData)
