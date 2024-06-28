import csv

def dump_data_from_csv(filename):
    data_dict = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  
        for row in csvreader:
            if len(row) == 3:  
                fruit_name = row[0]
                colour = int(row[1])
                sweet = int(row[2])
                data_dict[fruit_name] = {'Colour': colour, 'Sweet': sweet}
            
    return data_dict


def nearest_fruits(data,given_fruit,attribute):
    if given_fruit in data:
        value = data[given_fruit][attribute]
        print(f"The attribute value of {given_fruit} is: {value}")
        targeted_value = value + 1
        for fruit, attributes in data.items():
            if attributes['Colour'] == targeted_value:
                print(f"The fruit with attribute value {targeted_value} is: {fruit}")
        targeted_value = value - 1
        for fruit, attributes in data.items():
            if attributes['Colour'] == targeted_value:
                print(f"The fruit with attribute value {targeted_value} is: {fruit}")


def main():
    filename = 'fruits.csv'  
    data = dump_data_from_csv(filename)
    print(data)
    given_fruit = 'Mango'
   # nearest_fruits(data,given_fruit,'Sweet')
    nearest_fruits(data,given_fruit,'Colour')


if __name__ == "__main__":
    main()
