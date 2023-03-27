import loguru
import requests
import time


def req(url):
    response = requests.get(url=url)
    text = response.text
    url = response.url
    
    return text, response, url

def log(url):
    time1 = time.time()

    request = req(url)

    time2 = time.time()
    total_time = time2 - time1

    loguru.logger.success(f'{request[1]}, url: {request[2]} execution time: {total_time}')

if __name__ == '__main__':
    log(input('Enter url: '))
