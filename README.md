# gog-games torrent magnet link generator - before it shuts down

This is a simple script to download all the games' metadata currently listed on gog-games.

If you would like to run this code to create a cope for yourself.
## Before you begin
- Have `Python3` installed
## Install dependencies
- In the terminal run:
```
pip install -r requirements.txt
```
## Run the script
```
python3 main.py
```
After the script is done you should see two files:
- `all-games.json` -> Contains all the games on gog-games database
- `torrents.json` -> Contains only the games that have a torrent file
  - Each game contains the magnet link which can be added to your preferred torrent client to get the torrent.
