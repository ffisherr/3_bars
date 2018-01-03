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
    closest_bar = min(
        bars_data,
        key=lambda bar:
        abs(bar['geometry']['coordinates'][0] - longitude)
        + abs(bar['geometry']['coordinates'][1] - latitude)
    )
    return closest_bar


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if os.path.exists(args.filepath):
        try:
            json_data = load_json_data_from_file(args.filepath)
            bars = json_data['features']
            print('Наименьший бар', get_smallest_bar(bars))
            print('Наибольший бар', get_biggest_bar(bars))
            print(
                'Ближайший бар',
                get_closest_bar(
                    bars,
                    args.longitude,
                    args.latitude
                    )
            )
        except ValueError:
                print('Ошибка переобразования JSON файла')
    else:
        print('Файла {} не найдено!'.format(args.filepath))
