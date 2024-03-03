def all_true(tuple_data):
    return all(tuple_data)

def main():
    tuple_data = (True, True, True, True)  

    if all_true(tuple_data):
        print("All elements of the tuple are True.")
    else:
        print("Not all elements of the tuple are True.")

if __name__ == "__main__":
    main()