import csv

def dump_data_from_csv_file(filename):
    data_list = []
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)
    for i in fdata:
       # print (i)
        data_list.append(i)
    
    fd.close()
    #print(data_list)
    return data_list

def counts(filename):
    count = 0
    rfd = open("web-req-data.csv")
    chd = csv.reader(rfd)
    for row in chd:
        if "200" in row:
            count = count + 1
    return count

def main():
    filename = "web-req-data.csv"
    dl= dump_data_from_csv_file(filename)
    count_200 = counts(filename)
    print(f'{count_200}')

    


if(__name__ == "__main__"):
    main()