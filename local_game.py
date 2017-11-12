import random
import time
import pickle

run_time = 120
end_time = time.time() + run_time
answered = 0

history = []

def handle_question(a, b, connector, correct_answer):
    t0 = time.time()
    answer = int(input(f'{a} {connector} {b} = '))
    if answer == correct_answer:
        t1 = time.time()
        history.append([a, b, connector, correct_answer, t1-t0, 0])
        return
    else:
        handle_question(a, b, connector, correct_answer)
        history[-1][-1] += 1

while time.time() < end_time:
    print(f'{answered} {round(end_time-time.time(), 0)} s')
    calc_type = random.choice(['add', 'subtract', 'multiply', 'divide'])
    a = random.randint(2, 100)
    b = random.randint(2, 100)
    if calc_type == 'add':
        handle_question(a, b, '+', a+b)
    elif calc_type == 'subtract':
        handle_question(a+b, b, '-', a)
    elif calc_type == 'multiply':
        handle_question(a, b, '*', a*b)
    elif calc_type == 'divide':
        handle_question(a * b, b, '/', a)
    answered += 1

print(history)
