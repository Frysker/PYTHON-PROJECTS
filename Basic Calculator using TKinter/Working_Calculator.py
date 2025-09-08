import tkinter as tk

calculation = ""

def display_to_calculator(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        calculation = result
    except Exception as e:
        clear_calculation()
        text_result.insert(1.0, "Error")

def clear_calculation():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

calc = tk.Tk()
calc.geometry("243x298")
calc.title("Calculator")
calc.resizable(False, False)
calc.config(bg="black")

text_result = tk.Text(calc, 
                      height=3, 
                      width=15, 
                      font=("Times New Roman", 24, "bold"),
                      fg="white",
                        bg="#424242")

text_result.grid(columnspan=4)

def create_button(text, 
                  row, 
                  column, 
                  command=None, 
                  width=5, 
                  columnspan=1):
    
    button = tk.Button(calc, 
                       text=text, 
                       command=command, 
                       width=width, 
                       font=("Times New Roman", 14), 
                       fg="white", 
                       bg="#424242")
    
    button.grid(row=row, 
                column=column, 
                columnspan=columnspan)
    return button

create_button("1", 2, 0, lambda: display_to_calculator("1"))
create_button("2", 2, 1, lambda: display_to_calculator("2"))
create_button("3", 2, 2, lambda: display_to_calculator("3"))
create_button("+", 2, 3, lambda: display_to_calculator("+"))

create_button("4", 3, 0, lambda: display_to_calculator("4"))
create_button("5", 3, 1, lambda: display_to_calculator("5"))
create_button("6", 3, 2, lambda: display_to_calculator("6"))
create_button("-", 3, 3, lambda: display_to_calculator("-"))

create_button("7", 4, 0, lambda: display_to_calculator("7"))
create_button("8", 4, 1, lambda: display_to_calculator("8"))
create_button("9", 4, 2, lambda: display_to_calculator("9"))
create_button("*", 4, 3, lambda: display_to_calculator("*"))

create_button("(", 5, 0, lambda: display_to_calculator("("))
create_button("0", 5, 1, lambda: display_to_calculator("0"))
create_button(")", 5, 2, lambda: display_to_calculator(")"))
create_button("/", 5, 3, lambda: display_to_calculator("/"))

create_button("=", 6, 2, evaluate_calculation, width=11, columnspan=2)
create_button("C", 6, 0, clear_calculation, width=11, columnspan=2)

calc.mainloop()
