import threading, queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print('Working on:{}'.format(item))
        print('Finished:{}'.format(item))
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item)
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')
