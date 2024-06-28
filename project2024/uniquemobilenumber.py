import csv

def dump_data_from_csv_file(filename):
    data_list = []
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)
    for i in fdata:
        # print (i)
        data_list.append(i)
    print ("")
    
    fd.close()
    #print(data_list)
    return data_list
def remove_space(dl):
     clean_data = []
     rfd1 = open("users-data.csv",'rt')
     chd1 = csv.reader(rfd1)
     for row in chd1:
        if len(row) > 4:
         row[4] = row[4].replace(' ','')  
        if len(row) > 5:
         row[5] = row[5].replace(' ','') 
        clean_data.append(row)
     return clean_data
     
     
def remove_duplicates(dl):
    new_data = []
    for i in range(len(dl)):
        if dl[i][4] == dl[i][5]:
            dl[i][5] = ''
        if any(dl[i]): 
            new_data.append(dl[i])
        for j in range(i + 1, len(dl)):
            if (dl[i][4] == dl[j][4] or
                dl[i][4] == dl[j][5] or
                dl[i][5] == dl[j][4] or
                dl[i][5] == dl[j][5]):
                dl[j] = [''] * len(dl[j])
    rfd2 = open("new_data.csv","w",newline='')
    for row in new_data:
        rfd2.write(','.join(row)+'\n')
    return new_data

    

def main():
    dl = dump_data_from_csv_file("users-data.csv")
    clean_data = remove_space(dl)
    unique_data = remove_duplicates(clean_data)
    for index,row in enumerate(clean_data, start=1):
            mobile = row[4]
            home = row[5]
           # print(f"{index}:{mobile}, {home}")
    for index,row in enumerate(unique_data, start=1):
            mobile = row[4]
            home = row[5]
            print(f"{index}:{mobile}, {home}")

    


if(__name__ == "__main__"):
    main()