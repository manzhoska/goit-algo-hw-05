import sys
from pathlib import Path

# This script reads a log file and counts the occurrences of a specified status.
# prompt sample: python3 log.py logs.txt debug

#---------------------First Part---------------------

# Transfer file lines into the list of lines
def load_logs(file_path: str) -> list:
    with open(file_path, 'r') as file:

        logs = []
        for line in file:
            logs.append(line.strip())

        return logs


# Filtering list of logs by the status_message 
def filter_logs_by_level(logs: list, level: str) -> list:
    level_list = []

    # Filtering by level
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        if level.upper() in log:
            print(log)
    print("\n")
            
       
    return level_list

# Defining information from the line
def parse_log_line(line: str) -> dict:
    # split received line 
    tmp_line = line.split(" ")
    
    #parce received line into the dictionary
    counts = {
        "date" : tmp_line[0],
        "time" : tmp_line[1],
        "level" : tmp_line[2],
        "message": " ".join(tmp_line[3:])
    }
    return counts



#---------------------Second part---------------------

# Showing table of status_messages and their total count in the log file
def count_logs_by_level(logs: list) -> dict:
    status_dict = {}
    for line in logs:
        line = line.split(' ')
        status = line[2]
        
        # adding the status to the dictionary and counting its occurrences
        if status in status_dict:
            status_dict[status] += 1
        else:
            status_dict[status] = 1

    #call function display_log_counts 
    display_log_counts(status_dict)



# Showing status messages and their counts in table view
def display_log_counts(counts: dict):
    print(f"\n{'Рівень логування':<20} {'| Кількість' :<10}")
    print("-" * 30)
    for key, value in counts.items():
        print(f"{key :<20} | {value :<10} ")







#---------------------Main function---------------------
def main():
    try:
        # setting prompted file path
        file_path = Path("./", sys.argv[1]).absolute()

        list_of_logs = load_logs(file_path)
        
        # Always show general table with count of status messages
        count_logs_by_level(list_of_logs)

        # If expected status received show respective logs
        if sys.argv[2]: 
            expected_status = sys.argv[2] # expected status
            status_messages = ['INFO', 'ERROR', 'DEBUG', 'WARNING']
            if expected_status.upper() in status_messages:
                
                filtered_logs = filter_logs_by_level(list_of_logs, expected_status)
                for l in filtered_logs:
                    parse_log_line(l)
            else: 
                print(f"\nPlease provide a status code from the next list: {status_messages}\n")

    except FileNotFoundError:
        print("\nFile not found. Please check the file path and try again.\n")
        sys.exit() 


if __name__ == "__main__":
    main()