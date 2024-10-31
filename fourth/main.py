from datetime import datetime
from task import Task

def main() -> int:
    task: Task = Task("banana", datetime.now(), datetime(2022, 12, 1), True)

    print(task)

if(__name__ == "__main__"):
    main()