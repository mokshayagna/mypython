import pandas as pd
import math

attributes = ["Red", "Yellow", "Green", "Sweet", "Sour", "Bitter"]

fruit_attributes = {
    "Apple": ["Red", "Sweet"],
    "Banana": ["Yellow", "Sweet"],
    "Cherry": ["Red", "Sweet", "Sour"],
    "Grapes": ["Green", "Sweet", "Sour"]
}

def generate_embeddings(fruits, attrs):
    embeddings = {}
    for fruit, attr_list in fruits.items():
        embedding = [1 if attr in attr_list else 0 for attr in attrs]
        embeddings[fruit] = embedding
        print(fruit,embeddings)
    return embeddings

def finding_fruit(embeddings, required_fruit):
    matching_fruits = []
    for fruit, embedding in embeddings.items():
        if embedding == required_fruit:
            matching_fruits.append(fruit)
    return matching_fruits

def euclidean_distance(embedding1, embedding2):
    sum_of_difference = 0
    for i in range (len(embedding1)):
        sum_of_difference = sum_of_difference + (embedding1[i] - embedding2[i]) **2
    return math.sqrt(sum_of_difference)

#def calculate_distance(points):
    distances = []
    for i in range (0,len(points)):
        for j in range (i+1,len(points)):
            dist = euclidean_distance(points[i],points[j])
            distances.append((dist,points[i], points[j]))
    return distances

def calculate_distance_from_fixedpoint(embedding, fixed_embedding):
    distances = []
    for  fruit, embedding_value in embedding.items():
        dist = euclidean_distance(fixed_embedding, embedding_value)
        distances.append((dist, embedding_value, fruit))
    return distances

def nearest_fruits(distances):
    distances.sort()

    if (distances[0][0]  ==  0):
        distances.pop(0)
        for distance,embedding, fruit in distances [:3]:
            print(distance)
            print(embedding)
            print(fruit)

    else:
        for distance,embedding, fruit in distances [:3]:
            print(distance)
            print(embedding)
            print(fruit)

        
                




def main():
    embeddings = generate_embeddings(fruit_attributes, attributes)
    print("Generated Embeddings DataFrame:")
    print(embeddings)
    
    required_fruit = [1, 0, 0, 1, 0, 1] 
    distances_for_fixed = calculate_distance_from_fixedpoint(embeddings, required_fruit)
    print("\nDistances from the fixed embedding:")
    for distance, embedding, fruit in distances_for_fixed:
        print(f"Fruit: {fruit}")
        print(f"Embedding: {embedding}")
        print(f"Distance: {distance}")
        print("")  

    found_fruits = finding_fruit(embeddings, required_fruit)
    if found_fruits:
        print(f"Fruits matching the required embedding {required_fruit}:")
        for fruit in found_fruits:
            print(fruit)
    else:
        print(f"No fruit matches the required embedding.")
        print("")
    

    nearest_fruits(distances_for_fixed)
    
    
    

if __name__ == "__main__":
    main()
