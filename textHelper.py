import helpers

def getLinesWithPertinentData(data):
    if data != '':
        counter = 0
        dateCounter = 0
        cityCounter = 0

        for d in data:
            if d.strip()[:4] == 'FCST':
                dateCounter = counter

            if d.strip().lower() == 'grand rapids':
                cityCounter = counter
    
            counter = counter + 1
    
        return data[dateCounter+2], data[cityCounter+1], data[cityCounter+2], data[cityCounter+3]

# day data = print(data[dateCounter+2].strip())

def generateDayparts(dataline, year):
    dayList = []
    dayData = dataline.strip().split('  ')
    for d in dayData:
        dayList.append(helpers.getDateObject(d.strip(), year))

    return dayList

def generateForecastData(dataline):
    forecastList = []
    forecastData = dataline.strip().split(' ')
    for f in forecastData:
        if f:
            forecastList.append(helpers.getForecast(f))

    return forecastList
