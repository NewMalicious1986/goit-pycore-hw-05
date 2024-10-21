from collections import Counter
import sys

HEADERS = {"level": "Log Level", "count": "Count"}


def parse_log_line(line: str) -> dict:
    """
    Parses a single line of a log file into its components.
    Args:
        line (str): A single line from the log file, expected to be in the format "date time level message".
    Returns:
        dict: A dictionary with keys 'date', 'time', 'level', and 'message' containing the corresponding parts of the log line.
              Returns None if the line cannot be parsed.
    """

    try:
        date, time, level, message = line.split(" ", 3)
        return {"date": date, "time": time, "level": level, "message": message}
    except ValueError:
        print(f"Error: Unable to parse log line: {line}")
        return None


def load_logs(file_path: str) -> list:
    """
    Load and parse log entries from a specified file.
    Args:
        file_path (str): The path to the log file.
    Returns:
        list: A list of parsed log entries.
    Raises:
        SystemExit: If the file is not found or an IO error occurs.
    """

    logs = []
    try:
        with open(file_path) as file:
            while line := file.readline().strip():
                parsed_log = parse_log_line(line)
                if parsed_log:
                    logs.append(parsed_log)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: An IO error occurred while reading the file '{file_path}'.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters a list of log entries by a specified log level.
    Args:
        logs (list): A list of log entries, where each entry is a dictionary containing log details.
        level (str): The log level to filter by (e.g., 'INFO', 'ERROR').
    Returns:
        list: A list of log entries that match the specified log level.
    """

    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Count the number of log entries for each log level.
    Args:
        logs (list): A list of log entries, where each log entry is a dictionary
                     containing at least a "level" key.
    Returns:
        dict: A dictionary with log levels as keys and the count of log entries
              for each level as values.
    """

    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: dict) -> None:
    """
    Display the log counts in a formatted table.
    Args:
        counts (dict): A dictionary where the keys are log levels (e.g., 'INFO', 'ERROR')
                       and the values are the counts of each log level.
    Returns:
        None
    """

    print(f"{HEADERS['level']} | {HEADERS['count']}")
    print("-" * (len(HEADERS["level"]) + len(HEADERS["count"]) + 3))

    for level, count in counts.items():
        level_header_length_dif = len(HEADERS["level"]) - len(level)
        print(f'{level}{" " * level_header_length_dif} | {count}')


def display_filtered_logs(logs: list) -> None:
    """
    Display filtered log entries.
    Args:
        logs (list): A list of dictionaries, where each dictionary represents a log entry
                     with keys 'date', 'time', and 'message'.
    Returns:
        None
    """

    for log in logs:
        print(f'{log["date"]} {log["time"]} - {log["message"]}')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_parser.py <log_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(sys.argv[1])
    count_logs = count_logs_by_level(logs)

    display_log_counts(count_logs)

    if sys.argv[2:]:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)

        print(f"Filtered logs for {level}:")
        display_filtered_logs(filtered_logs)
