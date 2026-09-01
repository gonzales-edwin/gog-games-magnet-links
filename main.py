import requests
import json
import os

#out os 6390 games only 2130 have torrents, 4260 don't have torrent links

MAIN_URL = "https://gog-games.to/"
ALL_GAMES_API_URL = MAIN_URL + "api/web/all-games"
MAGNET_PROTOCOL = "magnet:?xt=urn:btih:"
TRACKERS = ("&tr=udp://tracker.opentrackr.org:1337/announce"
            "&tr=udp://exodus.desync.com:6969/announce"
            "&tr=udp://open.stealth.si:80/announce"
            "&tr=udp://tracker-udp.gbitt.info:80/announce")

def generate_games_json(url, filename='all-games.json'):
    if not filename:
        print('No filename provided, default all-games.json will be used.')
    print(f'Grabbing file from: {url}')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            print('Data loaded successfully.')
            with open(filename, 'w') as file:
                json.dump(response_json, file, indent=4)
            print('Json file created successfully.')
            return filename
    except requests.exceptions.RequestException as e:
        print(f'An error occurred while getting file: {e}')

def generate_magnet_links(json_file='torrents.json'):
    with open(json_file, 'r') as file:
        content = json.load(file)
        games_with_torrent = []
        for i, game in enumerate(content):
            infohash = game['infohash']
            if infohash is not None:
                magnet_link = MAGNET_PROTOCOL + infohash + TRACKERS
                game['torrent'] = magnet_link
                games_with_torrent.append(game)
    new_file = 'torrents.json'
    with open(new_file, 'w') as file:
        json.dump(games_with_torrent, file, indent=4)
    print(f'{json_file} was created successfully.')

if __name__ == '__main__':
    dump_file = generate_games_json(ALL_GAMES_API_URL)
    generate_magnet_links(dump_file)
