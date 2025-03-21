import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Health Assessment Tracker")

# Labels and Entries
labels = ["Name:", "Age:", "Height (cm):", "Weight (kg):", "Steps walked per day:"]
entries = {}

for i, label in enumerate(labels):
    ttk.Label(root, text=label).grid(row=i, column=0, sticky='W', padx=10, pady=3)
    entry = ttk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=3)
    entries[label] = entry

# Results display
result_label = ttk.Label(root, text="", justify="left")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Canvas for histogram
canvas = tk.Canvas(root, width=200, height=150, bg="white")
canvas.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Calculate function
def calculate():
    try:
        name = entries["Name:"].get()
        age = int(entries["Age:"].get())
        height_cm = float(entries["Height (cm):"].get())
        weight = float(entries["Weight (kg):"].get())
        steps = int(entries["Steps walked per day:"].get())

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            bmi_category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            bmi_category = "Normal Weight"
        elif 25 <= bmi <= 29.9:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        if steps < 5000:
            activity_level = "Sedentary"
        elif 5000 <= steps <= 9999:
            activity_level = "Lightly Active"
        else:
            activity_level = "Active"

        result_text = f"Name: {name}\nAge: {age}\nBMI Category: {bmi_category}\nActivity Level: {activity_level}"
        result_label.config(text=result_text)

        canvas.delete("all")
        bar_height = (steps / 10000) * 100
        bar_height = min(bar_height, 100)

        canvas.create_rectangle(50, 120 - bar_height, 150, 120, fill="blue")
        canvas.create_text(100, 130, text="Steps")

    except ValueError:
        result_label.config(text="Please enter valid numeric inputs.")

# Calculate Button
ttk.Button(root, text="Calculate", command=calculate).grid(row=5, column=0, columnspan=2, pady=10)

# Run GUI
root.mainloop()