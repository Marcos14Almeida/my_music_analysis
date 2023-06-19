
# =============================================================================
# ================================= Libraries =================================
# =============================================================================

import os
import pandas as pd
import requests

# =============================================================================
#                                 Functions
# =============================================================================


def get_song_names(folder_path="C:/Users/marco/Musics_all"):

    # Get all file names in the folder
    song_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if ("mp3" in file):
                song_names.append(file)
    song_names.sort()

    return song_names


def get_band_names(song_names):

    bands = {}

    for song in song_names:
        if "-" in song:
            # Split the file name before and after the hyphen
            split_name = song.split(" - ")

            band_name = split_name[0].lower()
            band_name = band_name.replace("rhcp", "red hot chili peppers").replace("ratm", "rage against the machine")

            if (band_name not in bands.keys()):
                bands[band_name] = {"songs": 1, "genres": []}
            else:
                bands[band_name]["songs"] += 1

    return bands


def get_band_genres(band_name):

    api_key = "2b705394dcc816bc0773dc767d53ed29"  # Replace with your Last.fm API key

    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={band_name}&api_key={api_key}&format=json"

    response = requests.get(url)
    data = response.json()

    if "error" in data:
        print(f"Error retrieving genres for {band_name}")
        return []

    artist = data["artist"]
    if "tags" in artist and "tag" in artist["tags"]:
        tags = artist["tags"]["tag"]
        genres = [tag["name"] for tag in tags]
        for i in range(len(genres)):
            genres[i] = rename_genres(genres[i])
        return genres
    else:
        return []


def rename_system_files():

    folder_path = "C:/Users/marco/Musics_all"

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if ' - ' not in filename and "mp3" in filename:
                # Create the new filename by replacing '#' with another character or removing it
                # new_filename = filename.replace('—', '-')
                print(root)
                print(filename)
                # Rename the file
                # os.rename(os.path.join(root, filename), os.path.join(root, new_filename))


def fill_band_df(bands_dict, bands_name_list):
    max_columns = 0
    for band_name in bands_name_list:
        genres = get_band_genres(band_name)
        bands_dict[band_name]["genres"] = genres
        if len(genres) > max_columns:
            max_columns = len(genres)

    # Create an empty DataFrame with desired column names
    df = pd.DataFrame(columns=['Artist', 'Songs'] + [f'Genre {i+1}' for i in range(max_columns)])

    # Iterate over the data dictionary and populate the DataFrame
    for artist, info in bands_dict.items():
        genres = info['genres']
        row = [artist, info['songs']] + genres + [None] * (len(df.columns) - len(genres) - 2)
        df.loc[len(df)] = row

    # Drop where there is no genre
    df = df.dropna(subset=[df.columns[2]])
    return df


def rename_genres(word):
    dictionary = {
        "brasil": "brazil",
        "brazilian": "brazil",
        "brazilian rock": "brazil",
        "rio de janeiro": "brazil",
        "rock gaucho": "brazil",
        "paraense": "brazil",
        "Parana": "brazil",
        "fortaleza": "brazil",
        "rock nacional": "brazil",
        "rock brasileiro": "brazil",
        "Canadian": "canada",
        "Female Frontend metal": "female vocalist",
        "female vocalists": "female vocalist",
        "hip hop": "Hip-Hop",
        "Nu-Metal": "Nu Metal",
        "Pop-Rock": "pop rock",
        "powerpop": "Power pop",
        "Rock and Roll": "rock n roll",
        "rock´n´roll": "rock n roll",
        "russian rock": "russian",
        "seen live": "",
        "spainish": "spain",
        "USA": "american",
        "us": "american",
        "utah": "american",
        "new york": "american",
        "Cleveland": "american",
        "Drum n Bass": "Drum and bass",
        "electronica": "electronic",
        "hair metal": "Glam Metal",
        "metal cover": "metal",
    }

    if (word in dictionary.keys()):
        return dictionary[word]
    else:
        return word
