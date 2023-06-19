
# =============================================================================
# ================================= Libraries =================================
# =============================================================================

from scripts.functions import get_song_names, get_band_names, fill_band_df

# =============================================================================
#                                     Main
# =============================================================================

# Parameters

music_folder_path = "C:/Users/marco/Musics_all"
save_df_path = "datasets/band_genres.csv"

# =============================================================================

print()
print("Running...")
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

# Save DataFrame to CSV
df.to_csv(save_df_path, index=False)

print("\nDataFrame saved to datasets/band_genres.csv")

print()
print("My TOP 10 Bands")
df_sorted = df.sort_values('Songs', ascending=False)
df_sorted = df_sorted[['Artist', 'Songs']]
top_10_rows = df_sorted.head(10)
print(top_10_rows)
