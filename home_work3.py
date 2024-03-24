import sys


def parse_log_line(line):
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }


def load_logs(file_path):
    try:
        with open(file_path, 'r') as file:
            return [parse_log_line(line) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(2)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(3)

def filter_logs_by_level(logs, level):
    return list(filter(lambda log: log['level'] == level.upper(), logs))

def count_logs_by_level(logs):
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        counts = count_logs_by_level(filtered_logs)
        display_log_counts(counts)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
