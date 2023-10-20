import requests
import sys
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

# Шаг 1 
def gettingDataFromTheSite(url:str):
    response = requests.get(url)
    # with open('Bitcoin_Analysis/test.html', 'w', encoding="utf-8") as output_file:
    #     output_file.write(response.text)
    return response.text

def htmlFileProcessing(html_file)->None:
    soup = BeautifulSoup(html_file)
    data_list = soup.find('table', {'class': 'TableRates'})
    items = data_list.find_all('td')

    sort_data_tag: list = []
    count: int = 0
    for item in items: 
        count += 1
        if(count == 2):
            sort_data_tag.append(str(item))
        if(count == 3): 
            count = 0

    sort_data: list = []
    for item in sort_data_tag: 
        sort_data.append(item[4:-5])

    with open("Bitcoin_Analysis/file.txt", "w", encoding="utf-8") as output:
        for item in sort_data: 
            output.write(f"{item}\n")
    
# Шаг 1.2 
def open_file(data:list)->list: 
    with open('Bitcoin_Analysis/file.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def variance(ls: list)-> int:
    '''Дисперсия числового ряда'''
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean)**2 for x in ls) / n
    std_dev = var ** 0.5
    return std_dev
    
def theSimplestStatistics(data:list)->None:
    result: dict = {}
    for number in data:
        if number in result:
            result[number] += 1
        else:
            result[number] = 1

    maxValue:int = max(result.values())
    maxValueKey:str = max(result, key=result.get)

    countElement:int = len(result) 

    data_element:list = []
    for item in result.values():
        data_element.append(int(item))
    mean = np.mean(data_element)

    __variance = variance(data_element)
    
    probabilityOfLoss = maxValue / countElement
    print("В данной последовательности число:", maxValueKey, "выпало больше всех остальных и имеет вероятность выпасть еще раз:", probabilityOfLoss, "\n")
    print("Частота вхождения данного числа:", maxValue, "/", countElement, "\n")
    print("Математическое ожидание" ,mean,"\n")
    print("Стандартное отклонение", __variance, "\n")

def commentsOnStatistics(data:list)->None: 
    print("Данная последовательность является статистически случайной.\n")
    theSimplestStatistics(data)
    print("Данная последовательность является дискретной.")

# Шаг 2 
def euroBitcoinParsing(url: str)->str:
    response = requests.get(url)
    return response.text

def gettingDataFromTheEuroBitcoin(html_file):
    soup = BeautifulSoup(html_file)
    data_list = soup.find('table', {'class': 'TableRates'})
    items = data_list.find_all('td')

    sort_data_tag: list = []
    count: int = 0
    for item in items: 
        count += 1
        if(count == 2):
            sort_data_tag.append(str(item))
        if(count == 3): 
            count = 0

    sort_data: list = []
    for item in sort_data_tag: 
        sort_data.append(item[4:-5])

    with open("Bitcoin_Analysis/file_bitcoin_euro.txt", "w", encoding="utf-8") as output:
        for item in sort_data: 
            output.write(f"{item}\n")

def open_file_two(data:list)->list: 
    with open('Bitcoin_Analysis/file_bitcoin_euro.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def buildAGraph(data_one: list, data_two: list):
    plt.title('euro bitcoin / ruble bitcoin')
    plt.plot(data_one)
    plt.plot(data_two)
    plt.show()

# Шаг 3 
def theNumberOfDataFromThePercentage(data:list, percent: int)->int: 
    n: int = len(data) 
    return n * percent / 100

def uploadingDataByACertainPercentage(data:list, data_60_percent:list, data_40_percent:list, percent: int)->None:
    numberOfData: int = theNumberOfDataFromThePercentage(data, percent) 
    count:int = 0
    with open('Bitcoin_Analysis/file.txt', 'r') as file:
        for line in file:
            count += 1
            if(count < int(numberOfData)): 
                data_60_percent.append(int(line.strip()))
            else:      
                data_40_percent.append(int(line.strip()))

def willTheNumberBeIncludedInTheSelection(item: int, mean: int)->bool:
    percent: int = item * 100 / int(mean)
    if abs(100 - percent) <= 5:
        return True
    return False

if __name__ == '__main__': 
    sys.stdout.reconfigure(encoding='utf-8')
    # Задание 1
    # Шаг 1 
    # url: str = 'https://cryptocharts.ru/bitcoin/'
    # html_file = gettingDataFromTheSite(url)
    # htmlFileProcessing(html_file)

    # Шаг 1.2 
    # data: list = []
    # open_file(data)
    # commentsOnStatistics(data)

    # Задание 2 
    # Шаг 2 
    # url: str = 'https://cryptocharts.ru/bitcoin-euro/'
    # html_file_two = euroBitcoinParsing(url)
    # gettingDataFromTheEuroBitcoin(html_file_two)
    # data_one: list = []
    # data_two: list = []
    # open_file(data_one)
    # open_file_two(data_two)
    # buildAGraph(data_one, data_two)
    # print("Зависимость линейна")

    # Заданиие 3 
    # Шаг 3 
    # data: list = []
    # open_file(data)
    # data_60_percent: list = []
    # data_40_percent: list = []
    # uploadingDataByACertainPercentage(data, data_60_percent, data_40_percent, 60)
    # mean: list = []
    # for item in range(1, len(data_60_percent)):
    #     mean.append(np.mean(data_60_percent))

    # plt.plot(data_60_percent, color = 'red')
    # plt.plot(mean, color='blue')
    # plt.show()

    # theProbabilityOfLossOfTheValue: list = []
    # for item in data_60_percent: 
    #     if willTheNumberBeIncludedInTheSelection(item, mean[0]):
    #         theProbabilityOfLossOfTheValue.append(item)
    
    # didTheForecastComeTrue:list = []
    # isFlag = False 
    # for itemOne in theProbabilityOfLossOfTheValue:
    #     for itemTwo in data_40_percent:
    #         if itemOne == itemTwo:
    #             isFlag = True
    #     if isFlag:
    #         didTheForecastComeTrue.append(isFlag)
    #         isFlag = False
    #     else: 
    #         didTheForecastComeTrue.append(isFlag)

    # print(didTheForecastComeTrue)        