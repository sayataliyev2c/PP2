from datetime import datetime, timedelta

def subtract_days(current_date, days):
    return current_date - timedelta(days=days)

def main():
    
    current_date = datetime.now().date()

    result_date = subtract_days(current_date, 5)

    print("Current date:", current_date)
    print("Date five days ago:", result_date)

if __name__ == "__main__":
    main()