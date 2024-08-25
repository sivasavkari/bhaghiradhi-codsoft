import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import random

class TodoApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("To-Do List with Gradient Background")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        self.tasks = []
        self.task_var = tk.StringVar()

        # Set up the canvas for background image
        self.canvas = tk.Canvas(self.root, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind resize event to update background image
        self.root.bind("<Configure>", self.update_background_image)

        # Create gradient overlay
        self.gradient_image = None
        self.add_gradient_overlay()

        # Set up the to-do list section in the center
        self.center_frame = tk.Frame(self.canvas, bg='black', bd=5)
        self.center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.task_entry = tk.Entry(self.center_frame, textvariable=self.task_var, width=40, font=('Helvetica', 12))
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_task_button = tk.Button(self.center_frame, text="Add Task", command=self.add_task, bg='white', fg='black')
        self.add_task_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(self.center_frame, selectmode=tk.SINGLE, width=50, height=10, font=('Helvetica', 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.delete_task_button = tk.Button(self.center_frame, text="Delete Task", command=self.delete_task, bg='white', fg='black')
        self.delete_task_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Event binding for dynamic gradient change
        self.canvas.bind("<Enter>", self.change_gradient_on_hover)
        self.canvas.bind("<Leave>", self.reset_gradient)

        # Initial update of the background image
        self.update_background_image()

    def update_background_image(self, event=None):
        try:
            img = Image.open(image_path)
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            img_resized = img.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(img_resized)
            self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')
            self.canvas.tag_lower(self.background_image)  # Ensure image is behind other canvas items
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")


    def add_gradient_overlay(self, start_color=(50, 50, 100), end_color=(0, 0, 50)):
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        gradient = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(gradient)

        # Create a vertical gradient
        for i in range(height):
            r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / height))
            g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / height))
            b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / height))
            draw.line((0, i, width, i), fill=(r, g, b, 128))

        self.gradient_image = ImageTk.PhotoImage(gradient)
        self.canvas.create_image(0, 0, image=self.gradient_image, anchor='nw')
        self.canvas.tag_lower(self.gradient_image)  # Ensure gradient is behind other canvas items

    def change_gradient_on_hover(self, event=None):
        # Randomize colors for gradient
        start_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.add_gradient_overlay(start_color=start_color, end_color=end_color)

    def reset_gradient(self, event=None):
        # Reset to default gradient
        self.add_gradient_overlay()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            tk.messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task)
            self.task_listbox.delete(selected_task_index)
        else:
            tk.messagebox.showwarning("Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    image_path = r"c:\Users\kesam\Downloads\bg-pat.png"  # Path to the background image
    root = tk.Tk()
    app = TodoApp(root, image_path)
    root.mainloop()

