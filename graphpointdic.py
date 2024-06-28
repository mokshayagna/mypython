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
    distances = {}
    for i in range(0,len(points)):
        x1, y1 = points[i]
        #print(x1,y1)
        print('') 
        for j in range(i+1, len(points)):  
            x2, y2 = points[j]
           # print(x2 ,y2)
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distances[((x1, y1), (x2, y2))] = distance
           # print(((x1,y1),(x2,y2)), distance)
    return(distances)


def find_nearest_points(distances):
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])
    nearest_points = sorted_distances[0][0] 
    return nearest_points

def distance_between_points(distances, point1, point2):
    if (point1, point2) in distances:
        return distances[(point1, point2)]
    elif (point2, point1) in distances:
        return distances[(point2, point1)]
    else:
        return None 
    
                
def main():
    points = dump_data_from_csv_file("graphpoints.csv")
    distances = calculating_distance(points)
    nearest_points = find_nearest_points(distances)
    print("The nearest points are:", nearest_points)

    # Example usage of get_distance_between_points function
    point1 = (1, 2)
    point2 = (4, 6)
    distance = distance_between_points(distances, point1, point2)
    if distance is not None:
        print(f"The distance between {point1} and {point2} is: {distance}")
    else:
        print(f"No distance found between {point1} and {point2}")
    
    

if(__name__ == "__main__"):
    main()