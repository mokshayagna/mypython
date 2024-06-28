network_library = {
    "Total_books" : 15, 
    "books": { 
        "py_books" : 2,
        "c++_books" : 2,
        "perl_scripts" : 8,
        "os_books" : 3
    }
 }

embedded_library = {
    "Total_books" : 19, 
    "books": {
        "py_books" : 10,
        "c_books" : 5,
        "perl_scripts" : 2,
        "os_books" : 2
        }
    }

def main():
    combined_library = {}
   # print(network_library["books"])
   # print(embedded_library["books"])

    #if "py_books" in network_library["books"]:
    #    print("yes")
    #else:
     #   print("No")
    combined_library["Total_books"] = network_library["Total_books"] + embedded_library["Total_books"]
    for ele in network_library["books"]:
        if ele in embedded_library["books"]:
            combined_library[ele] = network_library["books"][ele] + embedded_library["books"][ele]
        else:
            combined_library[ele] = network_library["books"][ele]

    for ele in embedded_library["books"]:
        if ele not in combined_library:
            combined_library[ele] = embedded_library["books"][ele]
    print(combined_library)

    return

if __name__ == "__main__":
    main()
