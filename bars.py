import json
import sys
from math import sqrt


def get_distance(user_lon, user_lat, bar_lon, bar_lat):
    return sqrt(
        (float(user_lon) - float(bar_lon)) ** 2 +
        (float(user_lat) - float(bar_lat)) ** 2
        )


def seat_counter(bars):
    seats_count = []
    for bar in bars['features']:
        seats_count.append(
            [bar.get('properties').get('Attributes').get('SeatsCount'),
             bar.get('properties').get('Attributes').get('Name')]
        )
    return seats_count


def load_json_data_from_file(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as json_file:
                json_data = json.loads(json_file.read())
            return json_data
        except ValueError:
            print('Ошибка переобразования JSON файла')
            return None
    else:
        print('Файла {} не найдено!'.format(filepath))


def get_biggest_bar(bars_data):
    seats_count = seat_counter(bars_data)
    biggest_bar = max(seats_count)
    biggest_bar_name = biggest_bar[1]
    print(biggest_bar_name)


def get_smallest_bar(bars_data):
    seats_count = seat_counter(bars_data)
    smallest_bar = min(seats_count)
    smallest_bar_name = smallest_bar[1]
    print(smallest_bar_name)


def get_closest_bar(bars_data, longitude, latitude):
    distance_to_bars = []
    for bar in bars_data['features']:
        lon2 = bar.get('geometry').get('coordinates')[0]
        lat2 = bar.get('geometry').get('coordinates')[1]
        distance_to_bars.append(
            [get_distance(longitude, latitude, lon2, lat2),
             bar.get('properties').get('Attributes').get('Name')])
    closest_bar = min(distance_to_bars)
    closest_bar_name = closest_bar[1]
    print(closest_bar_name)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        json_data = load_json_data_from_file('bars.json')
        get_closest_bar(json_data, sys.argv[1], sys.argv[2])
        get_biggest_bar(json_data)
        get_smallest_bar(json_data)
    else:
        print('Укажите верный путь к файлу')
