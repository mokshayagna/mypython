import math
import csv


def dump_data_from_csv_file(filename):
    data_list = []
    with open(filename, 'rt') as fd:
        fdata = csv.reader(fd)
        next(fdata)
        for i in fdata:
            points = (int(i[0]), int(i[1]))
            data_list.append(points)
    return (data_list)
            #print(point)


def calculating_distance(points):
    distances = []
    for i in range(0,len(points)):
        x1, y1 = points[i]
        #print(x1,y1)
        print('') 
        for j in range(i+1, len(points)):  
            x2, y2 = points[j]
           # print(x2 ,y2)
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distances.append((distance,points[i]))
            print(((x1,y1),(x2,y2)), distance)
    return(distances)

def find_nearest_points(distances):
    distances.sort()
    if (distances[0][0] == 0):
        distances.pop(0)
    print(distances)
    nearest_points = [distances[0][1],distances[1][1]]
    print(nearest_points)
    return nearest_points

                
def main():
    points = dump_data_from_csv_file("graphpoints.csv")
    distances = calculating_distance(points)
    find_nearest_points(distances) 

if(__name__ == "__main__"):
    main()