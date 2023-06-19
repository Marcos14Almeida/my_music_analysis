
# =============================================================================
# ================================= Libraries =================================
# =============================================================================

import pandas as pd


# =============================================================================
#                                     Functions
# =============================================================================
def add_band(dict, column_name, n_songs):
    delete_genres = ["seen live", "covers", "palmeiras"]
    if column_name not in delete_genres:
        if (column_name not in dict.keys()):
            dict[column_name] = n_songs
        else:
            dict[column_name] += n_songs
    return dict
# =============================================================================


def analyse_genre(save_df_path):

    print()
    print("=" * 50)
    print("Analyse genres...")
    print()

    # Read the CSV file
    df = pd.read_csv(save_df_path + '/band_genres.csv')
    df['Artist'] = df['Artist'].apply(str.title)

    # Display the DataFrame
    print("\nReceived dataset:")
    print(df)

    genres_count = {}

    # Count genres
    print()
    for row in df.values:
        n_songs = row[1]
        genres_count = add_band(genres_count, row[2], n_songs)
        genres_count = add_band(genres_count, row[3], n_songs)
        genres_count = add_band(genres_count, row[4], n_songs)
        genres_count = add_band(genres_count, row[5], n_songs)
        genres_count = add_band(genres_count, row[6], n_songs)

    # Sort the dictionary by values in ascending order
    genres_count = dict(sorted(genres_count.items(), key=lambda x: x[1]))

    # Print
    print("\nFinal Dictionary counting genres:")

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(list(genres_count.items()), columns=['Genre', 'Count'])
    print(df)

    # Save the DataFrame to a CSV file
    save_df_path += '/genres.csv'
    df.to_csv(save_df_path, index=False)
    print(f"\nDataFrame saved to {save_df_path}")
# =============================================================================
