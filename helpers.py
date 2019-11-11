import datetime
import requests
from bs4 import BeautifulSoup

def getDateObject(dayString, Year):
    # x = datetime.datetime(2020, 5, 17)
    parts = dayString.split(' ')
    monthNum = getMonth(parts[0].strip())
    dayNum = int(parts[1].strip())
    return datetime.datetime(Year, monthNum, dayNum)

def getMonth(monthCode):
    if monthCode.lower().strip() == 'jan':
        return 1
    if monthCode.lower().strip() == 'feb':
        return 2
    if monthCode.lower().strip() == 'mar':
        return 3
    if monthCode.lower().strip() == 'apr':
        return 4
    if monthCode.lower().strip() == 'may':
        return 5
    if monthCode.lower().strip() == 'jun':
        return 6
    if monthCode.lower().strip() == 'jul':
        return 7
    if monthCode.lower().strip() == 'aug':
        return 8
    if monthCode.lower().strip() == 'sep':
        return 9
    if monthCode.lower().strip() == 'oct':
        return 10
    if monthCode.lower().strip() == 'nov':
        return 11
    if monthCode.lower().strip() == 'dec':
        return 12

def getForecast(forecastString):
    if forecastString.strip() == 'Snoshwr':
        return 'Snow Showers'
    if forecastString.strip() == 'Ptcldy':
        return 'Partly Cloudy'
    if forecastString.strip() == 'Sunny':
        return 'Sunny'
    if forecastString.strip() == 'Mocldy':
        return 'Mostly Cloudy'
    if forecastString.strip() == 'Vrycld':
        return 'Very Cold'
    if forecastString.strip() == 'Fzdrzl':
        return 'Freezing Drizzle'
    return forecastString

def getForecastData(url): #year, month, day):
    # urlBase = 'https://mesonet.agron.iastate.edu/wx/afos/p.php?pil=SFTMI%20&e='

    # urlToOpen = urlBase + str(year) + str(month) + str(day) + '2115' # '201811182215'

    print(url)
    url_get = requests.get(url)

    soup = BeautifulSoup(url_get.content, 'html.parser')
    data_pre = soup.pre

    if (data_pre):
        return data_pre.prettify().splitlines()
    else:
        return ''

def getUrl(year, month, day):
    # https://mesonet.agron.iastate.edu/wx/afos/list.phtml?source=GRR&year=2012&month=4&day=21&view=grid&order=asc
    baseUrl = 'https://mesonet.agron.iastate.edu/wx/afos/list.phtml?source=GRR&year=' + str(year) + '&month=' + str(month) + '&day=' + str(day) + '&view=grid&order=asc'

    url_get = requests.get(baseUrl)

    soup = BeautifulSoup(url_get.content, 'html.parser')
    data_sftmi = soup.find("div", {"id": "sectSFTMI "})

    last_link = ''

    if (data_sftmi):
        children = data_sftmi.findChildren("a" , recursive=False)
        for child in children:
            last_link = child['href']

    return 'https://mesonet.agron.iastate.edu/wx/afos/' + last_link.replace(' ', '%20')