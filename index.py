import tkinter as tk
import subprocess
import os
from tkinter import messagebox, PhotoImage
from PIL import Image

class ObjectDetectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Object Detection App")

        #self.master.configure(bg="lightblue")
        self.convert_webp_to_png("background.webp", "background.png")
        self.background_image = PhotoImage(file="background.png")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.run_button = tk.Button(master, text="Run Object Detection", fg="white", padx=30, pady=10, bg="black", command=self.run_detection)
        self.run_button.place(x=250,y=171)
        #self.run_button.pack()

        self.view_data_button = tk.Button(master, text="View Number Plate Data", padx=35, pady=10, bg="black", command=self.view_car_plate_data, fg="white")
        self.view_data_button.place(x=750,y=171)
    def convert_webp_to_png(self, webp_path, png_path):
        if os.path.exists(webp_path):
            image_webp = Image.open(webp_path)
            image_webp.save(png_path, "PNG")
    def run_detection(self):
        # Run main1.py as a subprocess
        subprocess.Popen(["python", "main1.py"])
    def view_car_plate_data(self):
        # Check if car_plate_data.txt exists
        if os.path.exists("car_plate_data.txt"):
            # Open the file in the default text editor
            with open("car_plate_data.txt", "r") as file:
                data = file.read()

            # Create a new window to display the content
            data_window = tk.Toplevel(self.master)
            data_window.title("Car Plate Data")

            # Create a text widget to display the content
            text_widget = tk.Text(data_window)
            text_widget.insert(tk.END, data)
            text_widget.pack(expand=True, fill="both")
        else:
            # Display a message if the file doesn't exist
            tk.messagebox.showinfo("No Data", "It has not detected any number plate yet.")

def main():
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
