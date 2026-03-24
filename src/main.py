import threading
import time
import logging

logger = logging.getLogger(__name__)

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.task_lock = threading.Lock()

    def add_task(self, task, interval):
        with self.task_lock:
            self.tasks.append((task, interval))

    def run(self):
        while True:
            for task, interval in self.tasks:
                try:
                    task()
                except Exception as e:
                    logger.error(f'Error executing task: {e}')
                time.sleep(interval)

def main():
    scheduler = TaskScheduler()

    def my_task():
        print('Executing task...')

    scheduler.add_task(my_task, 60)  # Execute 'my_task' every 60 seconds

    scheduler_thread = threading.Thread(target=scheduler.run, daemon=True)
    scheduler_thread.start()

    print('Press Ctrl+C to stop the program.')
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()