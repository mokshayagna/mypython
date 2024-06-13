import csv

def dump_data_from_csv(filename):
    data_dict = {}
    print(data_dict)
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  
        for row in csvreader:
            if len(row) == 3:  
                fruit_name = row[0]
                colour = int(row[1])
                sweet = int(row[2])
                data_dict[fruit_name] = (colour, sweet)
            
    return data_dict

def nearest_fruit(fruits_dict, given_fruit):
    if given_fruit in fruits_dict:
        print(f"Nearest fruit to {given_fruit}: Colour={fruits_dict[given_fruit][0]}, Sweet={fruits_dict[given_fruit][1]}")
    

def main():
    filename = 'fruits.csv'
    fruits_dict = dump_data_from_csv(filename)
    given_fruit = 'mango'
    
    for fruit, ratings in fruits_dict.items():
        print(f"Fruit: {fruit}, Colour: {ratings[0]}, Sweet: {ratings[1]}")
    
    nearest_fruit(fruits_dict, given_fruit)

if __name__ == "__main__":
    main()
