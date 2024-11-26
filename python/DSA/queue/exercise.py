# git https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md

from collections import deque
import time
import threading

def taking_order(e):
    while e:  # This loop continues as long as the deque is not empty
        time.sleep(0.5)
        order = e.popleft()
        print('taking order of',order)


def serving_order(e):
    while e:
        time.sleep(1)
        order = e.popleft()
        print('serving order of',order)

orders = ['pizza','samosa','pasta','biryani','burger']

orders_taking_queue = deque(orders)
orders_serving_queue = deque(orders)

# taking_order(orders_taking_queue)
# serving_order(orders_serving_queue)

thread_1 = threading.Thread(target = taking_order, args = (orders_taking_queue,))
thread_2 = threading.Thread(target= serving_order, args=(orders_serving_queue,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()




