import tkinter as tk
from tkinter import font

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Pythor")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#b88c2f")
        
        # Variables para la expresión y el resultado
        self.expresion = ""
        self.resultado_var = tk.StringVar()
        self.expresion_var = tk.StringVar()
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame para la pantalla
        pantalla_frame = tk.Frame(self.root, bg="#1a1a2e", pady=20)
        pantalla_frame.pack(fill="both")
        
        # Fuentes personalizadas
        fuente_expresion = font.Font(family="Arial", size=14)
        fuente_resultado = font.Font(family="Arial", size=32, weight="bold")
        
        # Pantalla de expresión (arriba)
        pantalla_expresion = tk.Label(
            pantalla_frame,
            textvariable=self.expresion_var,
            font=fuente_expresion,
            bg="#1a1a2e",
            fg="#a8a8a8",
            anchor="e",
            padx=20
        )
        pantalla_expresion.pack(fill="both")
        
        # Pantalla de resultado (abajo)
        pantalla_resultado = tk.Label(
            pantalla_frame,
            textvariable=self.resultado_var,
            font=fuente_resultado,
            bg="#1a1a2e",
            fg="#ffffff",
            anchor="e",
            padx=20,
            height=2
        )
        pantalla_resultado.pack(fill="both")
        
        # Frame para los botones
        botones_frame = tk.Frame(self.root, bg="#1a1a2e")
        botones_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Definir botones
        botones = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        # Crear botones
        for i, fila in enumerate(botones):
            for j, boton in enumerate(fila):
                if boton == '=':
                    # Botón igual más grande
                    btn = tk.Button(
                        botones_frame,
                        text=boton,
                        font=("Arial", 20, "bold"),
                        bg="#00d9ff",
                        fg="#1a1a2e",
                        activebackground="#00b8d4",
                        activeforeground="#1a1a2e",
                        border=0,
                        cursor="hand2",
                        command=lambda: self.calcular()
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=3, pady=3)
                elif boton in ['C', '⌫']:
                    # Botones de control
                    btn = tk.Button(
                        botones_frame,
                        text=boton,
                        font=("Arial", 18, "bold"),
                        bg="#ff6b6b",
                        fg="#ffffff",
                        activebackground="#ff5252",
                        activeforeground="#ffffff",
                        border=0,
                        cursor="hand2",
                        command=lambda b=boton: self.limpiar() if b == 'C' else self.borrar()
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                elif boton in ['/', '*', '-', '+', '%']:
                    # Botones de operadores
                    btn = tk.Button(
                        botones_frame,
                        text=boton,
                        font=("Arial", 20, "bold"),
                        bg="#16213e",
                        fg="#00d9ff",
                        activebackground="#0f1626",
                        activeforeground="#00d9ff",
                        border=0,
                        cursor="hand2",
                        command=lambda b=boton: self.agregar_caracter(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                else:
                    # Botones numéricos
                    btn = tk.Button(
                        botones_frame,
                        text=boton,
                        font=("Arial", 20),
                        bg="#0f3460",
                        fg="#ffffff",
                        activebackground="#16213e",
                        activeforeground="#ffffff",
                        border=0,
                        cursor="hand2",
                        command=lambda b=boton: self.agregar_caracter(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
        
        # Configurar el grid para que los botones se expandan
        for i in range(5):
            botones_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            botones_frame.grid_columnconfigure(j, weight=1)
    
    def agregar_caracter(self, caracter):
        self.expresion += str(caracter)
        self.expresion_var.set(self.expresion)
        self.resultado_var.set(self.expresion)
    
    def limpiar(self):
        self.expresion = ""
        self.expresion_var.set("")
        self.resultado_var.set("0")
    
    def borrar(self):
        self.expresion = self.expresion[:-1]
        self.expresion_var.set(self.expresion)
        self.resultado_var.set(self.expresion if self.expresion else "0")
    
    def calcular(self):
        try:
            # Reemplazar % por /100 para porcentajes
            expresion_eval = self.expresion.replace('%', '/100')
            resultado = eval(expresion_eval)
            
            # Formatear el resultado
            if isinstance(resultado, float):
                if resultado.is_integer():
                    resultado = int(resultado)
                else:
                    resultado = round(resultado, 8)
            
            self.resultado_var.set(str(resultado))
            self.expresion = str(resultado)
            self.expresion_var.set("")
        except:
            self.resultado_var.set("Error")
            self.expresion = ""
            self.expresion_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
