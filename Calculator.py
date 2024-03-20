import tkinter as tk

def calculate():
    num_1 = float(entry1.get())
    num_2 = float(entry2.get())
    selection = selection_var.get()
    
    print("Selection:", selection)

    Output = None

    if selection == "Addition":
        Output = num_1 + num_2
        print("This add up to: ", Output)
    elif selection == "Subtraction":
        Output = num_1 - num_2
        print("Subtraction of the numbers is: ", Output)
    elif selection == "Multiplication":
        Output = num_1 * num_2
        print("The result of this multiplication is: ", Output )
    elif selection == "Division":
        if num_2 != 0:
            Output = num_1 / num_2
            print("The result of this division is: ", Output)
        else:
             print("Error! Division by zero ")
    
    else:
        print("Please check and try again")
        Output = "Invalid operation"
    
    Output_label.config(text = "Output: " + str(Output))
    
print("CALCULATOR")


    

    
window = tk.Tk()
window.title("CALCULATOR")
    
frame = tk.Frame(window)
frame.pack(padx=12, pady=12)
    
entry1 = tk.Entry(frame, width=12)
entry1.grid(row=0, column=0, padx=6, pady=6)
entry2 = tk.Entry(frame, width=12)
entry2.grid(row=0, column=1, padx=6, pady=6)
    
selection = ["Addition", "Subtraction", "Multiplication", "Division"]
selection_var = tk.StringVar()
selection_var.set(selection[0])
selection_dropdown = tk.OptionMenu(frame, selection_var,  *selection)
selection_dropdown.grid(row=0, column=2, padx=5, pady=6)
    
calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=6, pady=6)
Output_label = tk.Label(frame, text="Outcome: ")
Output_label.grid(row=2, column=0, columnspan=3, padx=5, pady=6)

window.mainloop()    
    
    

