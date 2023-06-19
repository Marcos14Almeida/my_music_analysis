# My Music Analysis

## Project Description

Analysis of my songs filtering the data using Python. Obtaining genres from the Last.fm API and vizualing the results using Gephi, Tableau.


## How to use it

1- I select all my .mp3 files and list all the songs I have. File: `Generate_music_dataset.py`.

2- Filter the bands from the names of the songs. File: `Generate_music_dataset.py`.

3- I use the Last.fm API to get the musical genre of each band and save it in a .csv file. File: `Generate_music_dataset.py`.

4- I count the number of appearances of each genre. File: `genres_count.py`.

5- I create a .csv file to be used in Gephi. In Gephi I generate a visual map of the bands I listen to and their respective genres, saved in a .pdf. File: `to_gephi.py`. PDF: ()[https://github.com/Marcos14Almeida/my_music_analysis/blob/main/gephi/bands_graph_map.pdf]

6- I do a final exploratory analysis of the data using Tableau.

## Screenshot

<p align="center">
  <img src="https://github.com/Marcos14Almeida/my_music_analysis/blob/main/gephi/print_gephi.jpg" width="200" title="Screenshot">
</p> 
