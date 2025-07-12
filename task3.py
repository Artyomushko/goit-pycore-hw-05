import sys
import colorama


def parse_log_line(line: str) -> dict[str, str]:
    date, time, level, info = line.split(' ', 3)
    info = info.strip()
    return dict(date=date, time=time, level=level, info=info)


def load_logs(file_path: str) -> list[dict[str, str]]:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return list(map(parse_log_line, lines))
    except FileNotFoundError:
        print("File not found or not readable")


def filter_logs_by_level(logs: list[dict[str, str]], level: str) -> list[dict[str, str]]:
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))


def count_logs_by_level(logs: list) -> dict:
    # TODO: The list of levels should not be hardcoded but this is done to practice Comprehensions
    return {level: len(filter_logs_by_level(logs, level)) for level in ['INFO', 'ERROR', 'DEBUG', 'WARNING']}


def display_log_counts(counts: dict, user_level: str = None) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        color = colorama.Fore.GREEN if user_level and user_level.lower() == level.lower() else colorama.Fore.RESET
        print(f"{color}{level:<16} | {count}")


def display_filtered_logs(logs: list, user_level: str = None) -> None:
    if not user_level:
        return

    print(f'\nДеталі логів для рівня \'{user_level}\':')
    for log in filter_logs_by_level(logs, user_level):
        print(f'{log["date"]} {log["time"]} - {log["info"]}')


def main() -> None:
    logs = load_logs(sys.argv[1])

    level = None
    if (len(sys.argv) > 2):
        level = sys.argv[2]

    display_log_counts(count_logs_by_level(logs), level)
    display_filtered_logs(logs, level)


if __name__ == '__main__':
    main()
