import json
import argparse
import os
from math import sqrt


def create_parser():
    parser = argparse.ArgumentParser(description='Поиск бара')
    parser.add_argument('longitude',
                        type=float, help='It is your coordinates')
    parser.add_argument('latitude',
                        type=float, help='It is your coordinates')
    parser.add_argument('filepath',
                        type=str, help='Way to json file with data')
    return parser


def get_distance(user_lon, user_lat, bar_lon, bar_lat):
    return sqrt(
        (float(user_lon) - float(bar_lon)) ** 2 +
        (float(user_lat) - float(bar_lat)) ** 2
        )


def load_json_data_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        json_data = json.loads(json_file.read())
    return json_data


def get_biggest_bar(bars_data):
    biggest_bar = max(
        bars_data,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return biggest_bar


def get_smallest_bar(bars_data):
    smallest_bar = min(
        bars_data,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return smallest_bar


def get_closest_bar(bars_data, longitude, latitude):
    distance_to_bars = []
    for bar in bars_data:
        lon2 = bar['geometry']['coordinates'][0]
        lat2 = bar['geometry']['coordinates'][1]
        distance_to_bars.append(
            get_distance(longitude, latitude, lon2, lat2)
        )
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
    if os.path.exists(args.filepath):
        try:
            json_data = load_json_data_from_file(args.filepath)
            json_dict = json_data['features']
            print('Наименьший бар', get_smallest_bar(json_dict))
            print('Наибольший бар', get_biggest_bar(json_dict))
            print(
                get_closest_bar(
                    json_dict,
                    args.longitude,
                    args.latitude
                    )
            )
        except ValueError:
                print('Ошибка переобразования JSON файла')
    else:
        print('Файла {} не найдено!'.format(args.filepath))
