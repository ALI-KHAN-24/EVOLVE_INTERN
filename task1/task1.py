import tkinter as tk
import time
import winsound
from tkinter import filedialog
import threading
from tkinter import *

# Create the main window
window = tk.Tk()
window.title("Wake UP Clock")

# Set the window background color
window.config(bg='black')

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%D')
    current_month = time.strftime('%B')
    current_year = time.strftime('%Y')

    clock_label.config(text=current_time)
    date_label.config(text="Date: "+ current_date)
    month_label.config(text="Month: "+ current_month)
    year_label.config(text="Year: " + current_year)

    clock_label.after(1000, update_time)



# Function to set the alarm time and sound file
def set_alarm():
    alarm_time = alarm_entry.get()
    alarm_sound = alarm_sound_var.get()
    alarm_label.config(text="Alarm set for: " + alarm_time)

    # Start a separate thread for checking and triggering the alarm
    alarm_thread = threading.Thread(target=check_alarm, args=(alarm_time, alarm_sound))
    alarm_thread.daemon = True
    alarm_thread.start()

def check_alarm(alarm_time, alarm_sound):
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == alarm_time:
            play_alarm_sound(alarm_sound)
            break
        time.sleep(1)

def play_alarm_sound(alarm_sound):
    try:
        winsound.PlaySound(alarm_sound, winsound.SND_FILENAME)
    except Exception as e:
        print("Error playing sound:", e)

# Function to select an alarm sound file
def browse_sound_file():
    file_path = filedialog.askopenfilename(filetypes=[("Sound files", "*.wav")])
    alarm_sound_var.set(file_path)



# Create a label for displaying the time
clock_label = tk.Label(window, font=("Arial", 80),background='black',foreground='cyan')
clock_label.pack(pady=10)

# Create labels for displaying the date, month, and year
date_label = tk.Label(window, font=("cooper black", 24))
date_label.pack(pady=9)
month_label = tk.Label(window, font=("cooper black", 24))
month_label.pack(pady=9)
year_label = tk.Label(window, font=("cooper black", 24))
year_label.pack()

# Start updating the time
update_time()




# Create a label for setting the alarm
alarm_label = tk.Label(window, text="Set Alarm:", font=("cooper black", 20))
alarm_label.pack(pady=5)

# Create an entry for setting the alarm time
alarm_entry = tk.Entry(window, font=("Arial", 20))
alarm_entry.pack(pady=5)

# Create a button to browse and select the alarm sound file
alarm_sound_var = tk.StringVar()
alarm_sound_button = tk.Button(window, text="Select Alarm Sound", command=browse_sound_file)
alarm_sound_button.pack(pady=5)

# Create a button to set the alarm
set_alarm_button = tk.Button(window, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=5)


# Run the main event loop
window.mainloop()
