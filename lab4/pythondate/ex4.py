from datetime import datetime

def date_difference_in_seconds(date1, date2):
    difference = abs(date2 - date1)  
    return difference.total_seconds()

def main():
    
    date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
    date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

   
    date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

    difference_seconds = date_difference_in_seconds(date1, date2)

    print("Difference between the two dates in seconds:", difference_seconds)

if __name__ == "__main__":
    main()