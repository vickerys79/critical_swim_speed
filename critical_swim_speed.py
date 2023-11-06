import tkinter as tk
from datetime import timedelta
from tkinter import messagebox, filedialog
import pandas as pd


class CSSCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CSS Test Calculator")

        self.data = []

        self.table_frame = tk.Frame(self.root)
        self.table_frame.grid(row=0, column=0)

        self.create_table()

        button_frame = tk.Frame(root)
        button_frame.grid(row=len(self.table) + 1, column=0, padx=5, pady=5)

        self.add_button = tk.Button(button_frame, text="Add Row", command=self.add_row)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.calculate_button = tk.Button(button_frame, text="Calculate CSS", command=self.calculate_css)
        self.calculate_button.grid(row=0, column=1, padx=5, pady=5)

        self.export_button = tk.Button(button_frame, text="Export Data", command=self.export_data)
        self.export_button.grid(row=0, column=2, padx=5, pady=5)

    def create_table(self):
        columns = ["Name", "400m Time (mm:ss)", "200m Time (mm:ss)", "CSS"]
        self.table = []
        # Create header row
        for i, column in enumerate(columns):
            label = tk.Label(self.table_frame, text=column, padx=20)
            label.grid(row=0, column=i, padx=5, pady=5)

        # Create an empty initial row
        self.add_row()

    def add_row(self):
        new_row = []
        for i in range(4):
            entry = tk.Entry(self.table_frame)
            entry.grid(row=len(self.table) + 1, column=i, padx=5, pady=5)
            new_row.append(entry)
        self.table.append(new_row)

    def calculate_css(self):
        for row in self.table:
            time_400_str = row[1].get()
            time_200_str = row[2].get()

            try:
                time_400 = self.parse_time(time_400_str)
                time_200 = self.parse_time(time_200_str)

                # Calculate CSS and round to the nearest second
                css = (time_400 - time_200) / 2
                css_seconds = round(css.total_seconds())
                row[3].delete(0, tk.END)
                row[3].insert(0, f"{css_seconds // 60:02}:{css_seconds % 60:02}")
            except (ValueError, TypeError):
                messagebox.showerror("Error", "Invalid input. Make sure times are in the format 'mm:ss'.")

    def parse_time(self, time_str):
        # Custom time string parsing
        minutes, seconds = map(int, time_str.split(':'))
        return timedelta(minutes=minutes, seconds=seconds)

    def export_data(self):
        if not self.table:
            messagebox.showwarning("Warning", "No data to export.")
            return
        self.calculate_css()
        export_format = "XLSX"
        filename = filedialog.asksaveasfilename(defaultextension=f".{export_format.lower()}",
                                                filetypes=[(f"{export_format} files", f".{export_format.lower()}",)],
                                                title="Save As")
        if filename:
            data = []
            for row in self.table:
                data.append({
                    "Name": row[0].get(),
                    "400 Time": row[1].get(),
                    "200 Time": row[2].get(),
                    "CSS": row[3].get()
                })

            df = pd.DataFrame(data)
            df.to_excel(filename, index=False)
            messagebox.showinfo("Export Success", f"Data exported as {filename}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CSSCalculator(root)
    root.mainloop()
