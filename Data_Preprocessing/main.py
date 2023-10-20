import csv 

def putTheData(dataset: list, ref: str) -> list:
    with open(ref, encoding='utf-8') as r_file:
        reader = csv.reader(r_file)
        for row in reader:
            dataset.append(row)
    return dataset
    
def convertColumns(dataset: list) -> list:
    converted_array: list = []
    for sublist in dataset:
        converted_sublist: list = []
        for element in sublist:
            if isinstance(element, str) and element.replace(".", "", 1).isdigit():
                converted_sublist.append(int(float(element)))
            else:
                converted_sublist.append(element)
        converted_array.append(converted_sublist)

    return converted_array

def convertColumnsReverse(dataset: list) -> list:
    converted_array: list = []
    for sublist in dataset:
        converted_sublist: list = []
        for index, element in enumerate(sublist):
            if(index == 1 or index == 5 or index == 6):
                try:
                    converted_sublist.append(str(float(element)))
                except:
                    converted_sublist.append(element) 
            converted_sublist.append(str(element))
        converted_array.append(converted_sublist)
    return converted_array

if __name__ == '__main__':  
    dataset: list = []
    ref:     str  = '4.csv'

    putTheData(dataset, ref)
    convertColumns(dataset)
    print(dataset)
    # convertColumnsReverse(dataset)