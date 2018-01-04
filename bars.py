import json
import argparse
import os


def create_parser():
    parser = argparse.ArgumentParser(description='Поиск бара')
    parser.add_argument(
        'longitude',
        type=float,
        help='It is your coordinates'
    )
    parser.add_argument(
        'latitude',
        type=float,
        help='It is your coordinates'
    )
    parser.add_argument(
        'filepath',
        type=str,
        help='Way to json file with data'
    )
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


def get_distance(user_lon, user_lat, longitude, latitude):
    distance = abs(user_lon - longitude) + abs(user_lat - latitude)
    return distance


def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min(
        bars_data,
        key=lambda bar:
        get_distance(
            bar['geometry']['coordinates'][0],
            bar['geometry']['coordinates'][1],
            longitude,
            latitude
        )
    )
    return closest_bar


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if os.path.exists(args.filepath):
        try:
            json_data = load_json_data_from_file(args.filepath)
            bars = json_data['features']
            print(
                'Наименьший бар',
                get_smallest_bar(bars)['properties']['Attributes']['Name']
            )
            print(
                'Наибольший бар',
                get_biggest_bar(bars)['properties']['Attributes']['Name']
            )
            print(
                'Ближайший бар',
                get_closest_bar(
                    bars,
                    args.longitude,
                    args.latitude
                    )['properties']['Attributes']['Name']
            )
        except ValueError:
                print('Ошибка переобразования JSON файла')
    else:
        print('Файла {} не найдено!'.format(args.filepath))
