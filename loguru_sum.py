import loguru
import time


def sum(a, b):
    try:
        sum = float(a+b)
    except:
        sum = 'Enter number please'
    return sum, a, b

def log():
    time1 = time.time()
    
    result = sum(int(input('Enter first num: ')), int(input('Enter second num: ')))

    time2 = time.time()
    total_time = time2 - time1

    loguru.logger.success(f'result: {result[1]} + {result[2]} = {result[0]}, execution time: {total_time}')


if __name__ == '__main__':
    log()