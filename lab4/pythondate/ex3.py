from datetime import datetime

def drop_microseconds(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def main():
    # Get current date and time
    current_datetime = datetime.now()

    # Drop microseconds
    result_datetime = drop_microseconds(current_datetime)

    print("Datetime with microseconds:", current_datetime)
    print("Datetime without microseconds:", result_datetime)

if __name__ == "__main__":
    main()