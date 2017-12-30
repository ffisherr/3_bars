import json
import argparse
import os
from math import sqrt


def create_parser():
    parser = argparse.ArgumentParser(description='Поиск бара')
    parser.add_argument('longitude',
                        type=float, nargs='+', help='It is your coordinates')
    parser.add_argument('latitude',
                        type=float, nargs='+', help='It is your coordinates')
    parser.add_argument('filepath',
                        type=str, nargs='+', help='Way to json file with data')
    return parser


def get_distance(user_lon, user_lat, bar_lon, bar_lat):
    return sqrt(
        (float(user_lon) - float(bar_lon)) ** 2 +
        (float(user_lat) - float(bar_lat)) ** 2
        )


def seat_counter(bars):
    seats_count = []
    for bar in bars:
        seats_count.append(
            bar['properties']['Attributes']['SeatsCount']
        )
    return seats_count


def load_json_data_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        json_data = json.loads(json_file.read())
    return json_data


def looking_the_same(bars_data, this_bar):
    bars = []
    for bar in bars_data:
        seats = bar['properties']['Attributes']['SeatsCount']
        if this_bar == seats:
            bars.append(bar)
    return bars


def get_biggest_bar(bars_data):
    seats_count = seat_counter(bars_data)
    biggest_bar = max(bars_data, key = seat_counter)
    return looking_the_same(bars_data, biggest_bar)


def get_smallest_bar(bars_data):
    seats_count = seat_counter(bars_data)
    smallest_bar = min(seats_count)
    return looking_the_same(bars_data, smallest_bar)


def get_closest_bar(bars_data, longitude, latitude):
    distance_to_bars = []
    for bar in bars_data:
        lon2 = bar['geometry']['coordinates'][0]
        lat2 = bar['geometry']['coordinates'][1]
        distance_to_bars.append(
            get_distance(longitude, latitude, lon2, lat2))
    closest_bar = min(distance_to_bars)
    bars = []
    for bar in bars_data:
        lon2 = bar['geometry']['coordinates'][0]
        lat2 = bar['geometry']['coordinates'][1]
        distance = get_distance(longitude, latitude, lon2, lat2)
        if distance == closest_bar:
            bars.append(bar)
    return bars


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if os.path.exists(args.filepath[0]):
        try:
            json_data = load_json_data_from_file(args.filepath[0])
            print(get_closest_bar(
                json_data['features'],
                args.longitude[0],
                args.latitude[0])
            )
            print(get_biggest_bar(json_data['features']))
            print(get_smallest_bar(json_data['features']))
        except ValueError:
                print('Ошибка переобразования JSON файла')
    else:
        print('Файла {} не найдено!'.format(args.filepath[0]))
