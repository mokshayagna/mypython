import pandas as pd
import math
import logging
import whereami

# Logging configuration
# CRITICAL
# ERROR
# Warning 
# INFO
# DEBUG

logging.basicConfig(
    level=logging.INFO,
    # level=logging.CRITICAL,
    # format="%(asctime)s - %(levelname)s - %(message)s",
    # datefmt="%Y-%m-%d %H:%M:%S",

    format="%(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)

attributes = ["Red", "Yellow", "Green", "Sweet", "Sour", "Bitter"]

fruit_attributes = {
    "Apple": ["Red", "Sweet"],
    "Banana": ["Yellow"],
    "Cherry": ["Red", "Sweet", "Sour"],
    "Grapes": ["Green", "Sweet", "Sour"]
}

def generate_embeddings(fruits, attrs):
    whereami.whereami()
    embeddings = {}
    for fruit, attr_list in fruits.items():
        embedding = [1 if attr in attr_list else 0 for attr in attrs]
        embeddings[fruit] = embedding
        logger.info(f"fruit      :{fruit}")
        logger.info(f"embeddings :{embeddings}")
        logger.info("")
    return embeddings

def finding_fruit(embeddings, required_embdding):
    whereami.whereami()
    matching_fruits = []
    for fruit, embedding in embeddings.items():
        if embedding == required_embdding:
            matching_fruits.append(fruit)
    return matching_fruits

def finding_fruit_with_attribute(embedding, attrs, attribute):
    whereami.whereami()
    logger.info(f"embedding :{embedding}")
    logger.info(f"attrs     :{attrs}")
    logger.info(f"attribute :{attribute}")

    matching_fruit = []
    attribute_index = attrs.index(attribute)
    for fruit, embeddings in embeddings.items():
        if embedding[attribute_index] == 1:
            matching_fruit.append(fruit)
    logger.info(f"matching :{matching_fruit}")
    return matching_fruit

def euclidean_distance(embedding1, embedding2):
    whereami.whereami()
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
    whereami.whereami()
    distances = []
    for  fruit, embedding_value in embedding.items():
        dist = euclidean_distance(fixed_embedding, embedding_value)
        distances.append((dist, embedding_value, fruit))
    return distances

def nearest_fruits(distances):
    whereami.whereami()
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
    whereami.whereami()
    embeddings = generate_embeddings(fruit_attributes, attributes)
    logger.info(f"{whereami.whereami()}: Generated Embeddings DataFrame:")
    logger.critical(f"embeddings :{embeddings}")
    
   # required_fruit = "Apple"

    required_attributes = ["Sweet"]

    found_fruits = finding_fruit_with_attribute(embeddings, attributes, required_attributes)
    logger.info(f"found_fruits :{found_fruits}")
    if found_fruits:
        print(f"Fruits matching the required embedding {required_embedding}:")
        for fruit in found_fruits:
            logger.info(f"fruit :{fruit}")
            logger.info('\n')
    else:
        logger.info(f"No fruit matches the required embedding.\n")

    required_embedding = [1 if attr in required_attributes else 0 for attr in attributes]
    logger.info(f"Embedding for required attribute{required_attributes}: {required_embedding}\n")

    distances_for_fixed = calculate_distance_from_fixedpoint(embeddings, required_embedding)
    print("\nDistances from the fixed embedding:")
    for distance, embedding, fruit in distances_for_fixed:
        logger.info(f"Fruit      :{fruit}")
        logger.info(f"Embedding  :{embedding}")
        logger.info(f"Distance   :{distance}")
        logger.info("")  

    nearest_fruits(distances_for_fixed)
    
    
if __name__ == "__main__":
    main()
