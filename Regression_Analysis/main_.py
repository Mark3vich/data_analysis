import csv 
from dsmltf import *

def putTheData(dataset: list, ref: str) -> None:
    with open(ref, encoding='utf-8') as r_file:
        reader = csv.reader(r_file)
        for row in reader:
            dataset.append(row)
    dataset = dataset[1:]
    # print(dataset)

def convertColumns(dataset: list) -> list[list]:
    columns = [[d[i] for d in dataset] for i, _ in enumerate(dataset[0])]
    new_columns = []
    vdict = {}
    for i, col in enumerate(columns):
        new_columns.append([])
        vdict[i] = {}
        for v in col:
            try:
                new_columns[-1].append(int(v))
            except:
                if v not in vdict[i]:
                    vdict[i][v] = len(vdict[i])
                new_columns[-1].append(vdict[i][v])
    new_data = [[d[i] for d in new_columns] for i, _ in enumerate(new_columns[0])]
    return new_data

def predictionOfTheFirstExam(new_data: list[list])->None:
    train_data = new_data[:int(len(new_data) * 0.7)]
    x1 = [nd[:5] for nd in train_data]
    y1 = [nd[5] for nd in train_data] 
    xtl = [[d[i] for d in x1] for i, _ in enumerate(x1[0])]
    regression(xtl, y1)
    beta = regression(xtl, y1)
    r_sq = mult_r_squared(x1, y1,beta)
    print(beta, r_sq)

def predictionOfTheSecondExam(new_data: list[list])->None:
    train_data = new_data[:int(len(new_data) * 0.7)]
    x2 = [nd[:6] for nd in train_data]
    y2 = [nd[6] for nd in train_data] 
    xtl = [[d[i] for d in x2] for i, _ in enumerate(x2[0])]
    regression(xtl, y2)
    beta = regression(xtl, y2)
    r_sq = mult_r_squared(x2, y2,beta)
    print(beta, r_sq)

def predictionOfTheTreeExam(new_data: list[list])->None:
    train_data = new_data[:int(len(new_data) * 0.7)]
    x3 = [nd[:7] for nd in train_data]
    y3 = [nd[7] for nd in train_data] 
    xtl = [[d[i] for d in x3] for i, _ in enumerate(x3[0])]
    beta = regression(xtl, y3)
    r_sq = mult_r_squared(x3, y3,beta)
    print(beta, r_sq)

if __name__ == '__main__':  
    dataset: list = []
    ref:     str  = 'Regression_Analysis/exams_exams.csv' # Путь изменить под себя 

    putTheData(dataset, ref)
    new_data:list[list] = convertColumns(dataset)
    predictionOfTheFirstExam(new_data)
    print("\n")
    predictionOfTheSecondExam(new_data)
    print("\n")
    predictionOfTheTreeExam(new_data)
    