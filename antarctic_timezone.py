from time import sleep

import requests_cache

TIME_API_URL = 'http://worldtimeapi.org/api/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    vostok_url = TIME_API_URL + 'timezone/Antarctica/Vostok'
    for iteration in range(5):
        if iteration > 2:
            session.cache.clear()
        response = session.get(vostok_url)
        data = response.json()
        result = data.get('datetime')
        print(iteration, result)
        sleep(1)
    utc_offset = data.get('utc_offset')
    print('Часовой пояс антарктической станции «Восток»:', utc_offset)
