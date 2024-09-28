import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Import Pillow for image handling
import os
sys.path.append('/Users/noman/Documents/COURSES/SoftwareProject/DataAnonymization/DataProcessing')

output_directory = ""
def on__file_button_click():
    file_path = filedialog.askopenfilename(title="Select Data File ")
    if file_path:
        last_folder_name = os.path.basename(os.path.dirname(file_path))
        filename = os.path.basename(file_path)
        label_data_file.config(text=f"{last_folder_name} / {filename}")

def on_config_button_click():
    file_path = filedialog.askopenfilename(title="Select Config File")
    if file_path:
        last_folder_name = os.path.basename(os.path.dirname(file_path))
        filename = os.path.basename(file_path)
        label_config_file.config(text=f"{last_folder_name} / {filename}")

# Function to handle selecting the output location
def select_output_directory():
    
    output_directory = filedialog.askdirectory(title="Select Output Folder")
    if output_directory:
        label_output_directory.config(text=f"Output Folder: {output_directory}")

def Action():
    
    output_directory = filedialog.askdirectory(title="Select Output Folder")
    if output_directory:
        label_output_directory.config(text=f"Output Folder: {output_directory}")

root = tk.Tk()
root.title("Data Annonymazier")
root.geometry("600x400")

# Create frames for dividing the window
frame_left = tk.Frame(root, width=400, bg='gray25')  # Left frame
frame_left.pack(side='left', fill='both', expand = True)

frame_right = tk.Frame(root, width=200 )  # Right frame
frame_right.pack(side='right', fill='both', expand = True)


# Spacer to push buttons to the lower part of the window
spacer = tk.Label(frame_left,bg='gray25', text="", height=3)  # Empty label to create space
spacer.pack(expand=True)  # Allow the spacer to expand





label_data_file = tk.Label(frame_left, text="No Data File  selected", wraplength=200,bg='gray25')
label_data_file.pack(anchor='w', padx=10, pady=10)
button_file = tk.Button(frame_left, text="Upload Data File!", command=on__file_button_click)
button_file.pack(anchor='w', padx=1, pady=1)


# Add a spacer below the buttons to increase the distance from the root
spacer_bottom = tk.Label(frame_left, bg='gray25', height=2)  # Match the frame's background
spacer_bottom.pack( expand=True,padx=10, pady=(0, 20))  # Vertical space of 20 below the buttons

# Label and Button for File 2 upload
label_config_file = tk.Label(frame_left, text="No  Config File selected", wraplength=200,bg='gray25')
label_config_file.pack(anchor='w', padx=10, pady=10)
button_config = tk.Button(frame_left, text="Upload Config File!", command=on_config_button_click)
button_config.pack(anchor='w', padx=1, pady=1)

# Add a spacer below the buttons to increase the distance from the root
spacer_bottom = tk.Label(frame_left, bg='gray25', height=2)  # Match the frame's background
spacer_bottom.pack( expand=True,padx=10, pady=(0, 20))  # Vertical space of 20 below the buttons

# Add a label for output directory
label_output_directory = tk.Label(frame_left, text="No output folder selected", bg='gray25', wraplength=200)
label_output_directory.pack(anchor='w', padx=1, pady=10)

# Button to select output directory
button_output_directory = tk.Button(frame_left, text="Select Output Directory", command=select_output_directory)
button_output_directory.pack(anchor='w', padx=1, pady=5)


# Add a spacer below the buttons to increase the distance from the root
spacer_bottom = tk.Label(frame_left, bg='gray25', height=2)  # Match the frame's background
spacer_bottom.pack( expand=True,padx=10, pady=(0, 20))  # Vertical space of 20 below the buttons

# Load the logo image
logo_path = "/Users/noman/Documents/COURSES/SoftwareProject/DataAnonymization/UI/DA_logo.png"  # Update with the path to your logo
  # Update with the path to your logo
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((200, 200), Image.LANCZOS)  # Resize the image if needed
logo = ImageTk.PhotoImage(logo_image)

# Create a label for the logo and place it in the right quadrant
label_logo = tk.Label(frame_right, image=logo)
label_logo.image = logo  # Keep a reference to avoid garbage collection

# Pack the logo label to center it in the right frame
label_logo.pack(expand=True)  # This will center the logo vertically and horizontally

# Add a label to indicate the right frame
label_info = tk.Label(frame_right, text="Go Anonymous",font=("Helvetica", 16, "bold italic"))
label_info.pack(pady=20)


root.mainloop()
