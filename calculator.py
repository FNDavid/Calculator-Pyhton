#!/usr/bin/env python3
"""
Calculadora simple con interfaz gráfica usando Tkinter
Simple Calculator with GUI using Tkinter
"""

import tkinter as tk
from tkinter import messagebox


class Calculator:
    """Clase principal de la calculadora"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Variable para almacenar la expresión
        self.expression = ""
        
        # Crear la interfaz
        self.create_widgets()
        
    def create_widgets(self):
        """Crea los widgets de la calculadora"""
        # Frame para el display
        display_frame = tk.Frame(self.root, bg="#2C3E50", padx=10, pady=10)
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Display de la calculadora
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 24, "bold"),
            justify="right",
            bg="#ECF0F1",
            fg="#2C3E50",
            bd=0,
            insertwidth=4
        )
        self.display.pack(fill=tk.BOTH, expand=True, ipady=20)
        
        # Frame para los botones
        buttons_frame = tk.Frame(self.root, bg="#2C3E50")
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Definir los botones
        buttons = [
            ['C', '←', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        # Colores para los botones
        number_color = "#ECF0F1"
        operator_color = "#E67E22"
        special_color = "#3498DB"
        equal_color = "#27AE60"
        
        # Crear los botones
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                # Determinar el color del botón
                if button_text in ['=']:
                    bg_color = equal_color
                elif button_text in ['C', '←']:
                    bg_color = special_color
                elif button_text in ['+', '-', '*', '/', '%']:
                    bg_color = operator_color
                else:
                    bg_color = number_color
                
                # Configurar el span del botón
                if button_text == '0':
                    colspan = 2
                elif button_text == '=':
                    colspan = 1
                else:
                    colspan = 1
                
                button = tk.Button(
                    buttons_frame,
                    text=button_text,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg="white" if button_text not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'] else "#2C3E50",
                    activebackground=bg_color,
                    activeforeground="white",
                    bd=0,
                    cursor="hand2",
                    command=lambda x=button_text: self.on_button_click(x)
                )
                
                if button_text == '0':
                    button.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=2, pady=2)
                else:
                    button.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        
        # Configurar el peso de las filas y columnas para que se expandan
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        """Maneja los clicks en los botones"""
        if char == 'C':
            self.clear()
        elif char == '←':
            self.backspace()
        elif char == '=':
            self.calculate()
        else:
            self.append_char(char)
    
    def append_char(self, char):
        """Añade un carácter a la expresión"""
        self.expression += str(char)
        self.update_display()
    
    def clear(self):
        """Limpia la expresión"""
        self.expression = ""
        self.update_display()
    
    def backspace(self):
        """Borra el último carácter"""
        self.expression = self.expression[:-1]
        self.update_display()
    
    def calculate(self):
        """Calcula el resultado de la expresión"""
        try:
            # Evaluar la expresión
            result = eval(self.expression)
            # Formatear el resultado
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", "Expresión inválida")
            self.clear()
    
    def update_display(self):
        """Actualiza el display con la expresión actual"""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


def main():
    """Función principal"""
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
