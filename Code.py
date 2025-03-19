'''
A structured product code could look like this:

Format: Category-Fabric-Color-Design-Number

Example:
	1.	MK-COT-BLU-PLN-001 → Men’s Cotton Blue Plain Kurta
	2.	MK-SLK-GRN-EMB-002 → Men’s Silk Green Embroidered Kurta
	3.	MK-LIN-WHT-PRT-003 → Men’s Linen White Printed Kurta

A product code typically includes important identifiers, such as:
	•	Category (Men’s Kurta = MK)
	•	Fabric Type (Cotton = COT, Silk = SLK)
	•	Color (Blue = BLU, Red = RED)
	•	Design Type (Plain = PLN, Embroidered = EMB, Printed = PRT)
	•	Unique Number (001, 002, etc.)

Steps to Create Product Codes

Step 1: Define Category Code
	•	Men’s Kurta → MK

Step 2: Define Fabric Code
	•	Cotton → COT
	•	Silk → SLK
	•	Linen → LIN
	•	Rayon → RYN
	•	Other → OTH

Step 3: Define Color Code
	•	Black → BLK
	•	White → WHT
	•	Blue → BLU
	•	Green → GRN
	•	Red → RED
	•	Yellow → YLW
	•	Maroon → MRN
	•	Custom → First 3 letters of the color

Step 4: Define Design Code
	•	Plain → PLN
	•	Embroidered → EMB
	•	Printed → PRT
	•	Striped → STR
	•	Checked → CHK

Step 5: Assign a Unique Number
	•	Start from 001 and increase sequentially.
 '''
 
import tkinter as tk
from tkinter import ttk

class ProductCodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Product Code Generator")
        self.geometry("400x300")

        # Define categories, fabrics, colors, designs
        self.categories = ["MK","OPJP","BLE","FPC","Test"]  # Men’s Kurta (MK)
        self.fabrics = ["COT", "SLK", "LIN", "RYN", "OTH"]
        self.colors = ["BLK", "WHT", "BLU", "GRN", "RED", "YLW", "MRN"]
        self.designs = ["PLN", "EMB", "PRT", "STR", "CHK"]

        # Initialize UI elements
        self.create_widgets()

    def create_widgets(self):
        # Category Dropdown
        self.category_label = tk.Label(self, text="Category")
        self.category_label.pack(pady=5)

        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(self, textvariable=self.category_var, values=self.categories, state="readonly")
        self.category_dropdown.pack(pady=5)
        self.category_dropdown.current(0)

        # Fabric Dropdown
        self.fabric_label = tk.Label(self, text="Fabric Type")
        self.fabric_label.pack(pady=5)

        self.fabric_var = tk.StringVar()
        self.fabric_dropdown = ttk.Combobox(self, textvariable=self.fabric_var, values=self.fabrics, state="readonly")
        self.fabric_dropdown.pack(pady=5)
        self.fabric_dropdown.current(0)

        # Color Dropdown
        self.color_label = tk.Label(self, text="Color")
        self.color_label.pack(pady=5)

        self.color_var = tk.StringVar()
        self.color_dropdown = ttk.Combobox(self, textvariable=self.color_var, values=self.colors, state="readonly")
        self.color_dropdown.pack(pady=5)
        self.color_dropdown.current(0)

        # Design Dropdown
        self.design_label = tk.Label(self, text="Design Type")
        self.design_label.pack(pady=5)

        self.design_var = tk.StringVar()
        self.design_dropdown = ttk.Combobox(self, textvariable=self.design_var, values=self.designs, state="readonly")
        self.design_dropdown.pack(pady=5)
        self.design_dropdown.current(0)

        # Unique Number Entry
        self.number_label = tk.Label(self, text="Unique Number (e.g. 001)")
        self.number_label.pack(pady=5)

        self.number_var = tk.StringVar()
        self.number_entry = tk.Entry(self, textvariable=self.number_var)
        self.number_entry.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(self, text="Generate Product Code", command=self.generate_code)
        self.generate_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self, text="Generated Product Code: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def generate_code(self):
        # Get selected values from dropdowns
        category = self.category_var.get()
        fabric = self.fabric_var.get()
        color = self.color_var.get()
        design = self.design_var.get()
        number = self.number_var.get().zfill(3)  # Ensure 3-digit formatting

        # Generate product code
        product_code = f"{category}-{fabric}-{color}-{design}-{number}"
        
        # Display the generated code
        self.result_label.config(text=f"Generated Product Code: {product_code}")

if __name__ == "__main__":
    app = ProductCodeGenerator()
    app.mainloop()
