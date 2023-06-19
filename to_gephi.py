
# Get File with artists, songs and genres. Generate a new file to use on gephi

# =============================================================================
# ================================= Libraries =================================
# =============================================================================

import os
import pandas as pd

# =============================================================================
#                                     Functions
# =============================================================================


def to_gephi(save_df_path, filter_best):

    print()
    print("=" * 50)
    print("Bands-Genres dataframe to use on Gephi")
    print()
    # =============================================================================
    # Read the CSV file

    # Construct the path to the band_genres.csv file
    csv_path = os.path.join(save_df_path, 'band_genres.csv')

    df = pd.read_csv(csv_path)

    # =============================================================================
    # Drop songs column and remove bands non-relevant
    # Count the occurrences of each value in the column
    if filter_best:
        df = df[df['Songs'] >= 1]
    df = df.drop("Songs", axis=1)
    print("\nReceived dataset:")
    print(df)

    # =============================================================================
    # Transform the dataset format
    # Reshape the data from wide to long format
    df_long = pd.melt(
                        df,
                        id_vars=['Artist'],
                        value_vars=['Genre 1', 'Genre 2', 'Genre 3', 'Genre 4', 'Genre 5'],
                        var_name='Genre_ID',
                        value_name='Genre'
                    )
    # Drop unnecessary columns
    df_long = df_long.drop(['Genre_ID'], axis=1)
    # Reset the index of the DataFrame
    df_long = df_long.reset_index(drop=True)

    # =============================================================================
    # Drop rows where there is no genre
    # Exclude rows with empty values
    df_long = df_long.dropna()

    # =============================================================================
    # Delete rows where 'seen live' genre is present in any column
    df_long = df_long[~df_long.astype(str).apply(lambda x: x.str.contains('seen live')).any(axis=1)]

    # =============================================================================
    # Let just the relevant genres that appear more than once
    # Count the occurrences of each value in the column
    if filter_best:
        value_counts = df_long['Genre'].value_counts()

        # Filter the DataFrame to exclude values that appear only once
        df_long = df_long[df_long['Genre'].isin(value_counts[value_counts > 1].index)]

    # =============================================================================
    # Save the dataframe
    # Print the resulting DataFrame
    print("\nFinal transformed dataset:")
    print(df_long)

    # Save dataframe
    save_df_path += '/gephi_bands.csv'
    df_long.to_csv(save_df_path, index=False)
    print(f"\nDataFrame saved to {save_df_path}")
