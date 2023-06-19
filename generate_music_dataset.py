
# =============================================================================
# ================================= Libraries =================================
# =============================================================================

from scripts.functions import get_song_names, get_band_names, fill_band_df


# =============================================================================
#                                     Main
# =============================================================================
def top_10bands(df):
    print()
    print("My TOP 10 Bands")
    df_sorted = df.sort_values('Songs', ascending=False)
    df_sorted = df_sorted[['Artist', 'Songs']]
    top_10_rows = df_sorted.head(10)
    print(top_10_rows)


# =============================================================================
def generate_music_dataset(music_folder_path, save_df_path):
    print()
    print("Generating Music Dataset...")
    print()

    # Get all songs from my local files
    songs = get_song_names(music_folder_path)
    # Get the band name from the song name
    bands_dict = get_band_names(songs)

    # Bands
    # Bands and their corresponding genres
    bands_name_list = list(bands_dict.keys())
    # bands_name_list = bands_name_list[100:102]  # Test just a subsample of bands
    print("List of bands")
    print(bands_name_list)

    # Get genres for each band
    print()
    print("Getting Genres for each band from Last.fm API")
    df = fill_band_df(bands_dict, bands_name_list)

    print("\nFinal Dataframe:")
    print(df)

    print()
    print(f"N songs: {df['Songs'].sum()}")
    print(f"N bands: {len(df)}")

    top_10bands(df)

    # Save DataFrame to CSV
    save_df_path += "/band_genres.csv"
    df.to_csv(save_df_path, index=False)

    print(f"\nDataFrame saved to {save_df_path}")
