import customtkinter as ctk

# Initialize main application window
root = ctk.CTk()
root.geometry("600x200")

# Create a frame to hold the OptionMenus
frame = ctk.CTkFrame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Configure columns to expand proportionally
frame.grid_columnconfigure((0, 1, 2), weight=1)  # Adjust based on number of widgets

# Add CTkOptionMenu widgets to the frame
options1 = ctk.CTkOptionMenu(frame, values=["Option 1", "Option 2", "Option 3"])
options1.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

options2 = ctk.CTkOptionMenu(frame, values=["Option A", "Option B", "Option C"])
options2.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

options3 = ctk.CTkOptionMenu(frame, values=["Option X", "Option Y", "Option Z"])
options3.grid(row=0, column=2, padx=5, pady=10, sticky="ew")

root.mainloop()