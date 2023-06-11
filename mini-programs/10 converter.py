import tkinter as tk

class Converter:
    def __init__(self, master):
        self.master = master
        self.master.title("Unit Converter")

        # Create labels for input and output units
        self.input_label = tk.Label(master, text="Input unit:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.output_label = tk.Label(master, text="Output unit:")
        self.output_label.grid(row=1, column=0, padx=10, pady=10)

        # Create dropdown menus for input and output units
        self.input_unit = tk.StringVar()
        self.input_unit.set("Celsius")
        self.input_dropdown = tk.OptionMenu(master, self.input_unit, "Celsius", "Fahrenheit", "Kelvin")
        self.input_dropdown.grid(row=0, column=1)

        self.output_unit = tk.StringVar()
        self.output_unit.set("Fahrenheit")
        self.output_dropdown = tk.OptionMenu(master, self.output_unit, "Celsius", "Fahrenheit", "Kelvin")
        self.output_dropdown.grid(row=1, column=1)

        # Create entry fields for input and output values
        self.input_value = tk.Entry(master)
        self.input_value.grid(row=0, column=2)

        self.output_value = tk.Entry(master)
        self.output_value.grid(row=1, column=2)

        # Create a button to perform the conversion
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=2, column=1, pady=10)

    def convert(self):
        try:
            # Get the input value and unit
            value = float(self.input_value.get())
            input_unit = self.input_unit.get()

            # Convert to base unit (Kelvin)
            if input_unit == "Celsius":
                base_value = value + 273.15
            elif input_unit == "Fahrenheit":
                base_value = (value - 32) * 5/9 + 273.15
            else:
                base_value = value

            # Convert from base unit to output unit
            output_unit = self.output_unit.get()
            if output_unit == "Celsius":
                output_value = base_value - 273.15
            elif output_unit == "Fahrenheit":
                output_value = (base_value - 273.15) * 9/5 + 32
            else:
                output_value = base_value

            # Update the output value
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, str(round(output_value, 2)))
        except ValueError:
            # Handle invalid input values
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, "Invalid input")

root = tk.Tk()
converter = Converter(root)
root.mainloop()
