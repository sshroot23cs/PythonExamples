import time
from multiprocessing import Process
from threading import Thread

def cpu_bound_task():
    # Simulate a CPU-bound task
    count = 0
    for i in range(10**8):
        count += i

def io_bound_task():
    # Simulate an I/O-bound task
    time.sleep(1)

def run_in_parallel(task, num_tasks, use_multiprocessing):
    start_time = time.time()
    if use_multiprocessing:
        processes = [Process(target=task) for _ in range(num_tasks)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()
    else:
        threads = [Thread(target=task) for _ in range(num_tasks)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    # freeze_support()
    print("Running CPU-bound tasks with multiprocessing:")
    run_in_parallel(cpu_bound_task, 4, use_multiprocessing=True)

    print("Running CPU-bound tasks with threading:")
    run_in_parallel(cpu_bound_task, 4, use_multiprocessing=False)

    print("Running I/O-bound tasks with multiprocessing:")
    run_in_parallel(io_bound_task, 4, use_multiprocessing=True)

    print("Running I/O-bound tasks with threading:")
    run_in_parallel(io_bound_task, 4, use_multiprocessing=False)