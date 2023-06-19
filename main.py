
# =============================================================================
# ================================= Libraries =================================
# =============================================================================

import tkinter as tk
from tkinter import filedialog
from genres_count import analyse_genre
from generate_music_dataset import generate_music_dataset
from to_gephi import to_gephi

# ====================================================================

# Preferences

api_key = ""  # Replace with your Last.fm API key
music_folder_path = "C:/Users/marco/Musics_all"
save_df_path = "C:/Users/marco/OneDrive/Documentos/python/my_music_analysis/datasets"


# =============================================================================
#                                     Main
# =============================================================================

def get_music_folder():

    global music_folder_path
    file_path = filedialog.askdirectory(initialdir=music_folder_path)
    print("Selected folder:", file_path)
    # Update the label widget with the folder name
    music_folder_path = file_path
    label.config(text=f"Selected folder:\n{file_path}")


def save_folder():

    global save_df_path
    file_path = filedialog.askdirectory(initialdir=save_df_path)
    print("Selected folder:", file_path)
    # Update the label widget with the folder name
    save_df_path = file_path
    label0.config(text=f"Selected folder:\n{file_path}")


def close_window():
    root.destroy()


def button1():
    generate_music_dataset(music_folder_path, save_df_path, api_key)


def button2():
    analyse_genre(save_df_path)


def button3():
    to_gephi(save_df_path, filter_best=False)


# -------------------------------------------------------------------------------
root = tk.Tk()
root.title("My Music Analysis")

# Add padding to the whole window
root.configure(padx=20, pady=20)
canvas = tk.Canvas(root, width=300, height=100)
canvas.pack()

# Create a rectangle
rectangle = canvas.create_rectangle(50, 30, 270, 70, fill='lightblue')

# Add text inside the rectangle
text = canvas.create_text(160, 50, text="My Music Analysis", font=("Arial", 16, "bold"), fill='black')

# Create a label
label_title = tk.Label(root, text="First select the folder where you want to explore your .mp3 music files")
label_title.pack(pady=5)
button_select = tk.Button(root, text="Change Music Folder Path", command=get_music_folder)
button_select.pack()
# Folder selected
label = tk.Label(root, text=f"Selected folder:\n{music_folder_path}")
label.pack()

button_select = tk.Button(root, text="Save Path", command=save_folder)
button_select.pack()
# Folder selected
label0 = tk.Label(root, text=f"Selected folder:\n{save_df_path}")
label0.pack()

# Create a label
label1 = tk.Label(root, text="Create the music dataset containing music genres from last.fm")
label1.pack(pady=(25, 0))
button_1 = tk.Button(root, text="1. Create Dataset", command=button1)
button_1.pack()

label2 = tk.Label(root, text="Create and save a new dataframe counting the genres")
label2.pack(pady=(15, 0))
button_2 = tk.Button(root, text="2. Analyse Genres", command=button2)
button_2.pack()

label3 = tk.Label(root, text="Dataframe relating bands and genres")
label3.pack(pady=(15, 0))
button_3 = tk.Button(root, text="3. Save dataset to use on Gephi", command=button3)
button_3.pack()

cancel_var = tk.IntVar()
button_close = tk.Button(root, text="Close", command=close_window, fg="red")
button_close.pack(pady=25)

root.mainloop()
