#!/usr/bin/env python3
"""
Ejemplo de uso de la calculadora sin interfaz gráfica
Example usage of the calculator without GUI
"""


def test_calculator_operations():
    """
    Demuestra las operaciones que la calculadora puede realizar
    Demonstrates the operations that the calculator can perform
    """
    print("=" * 50)
    print("EJEMPLOS DE OPERACIONES / OPERATION EXAMPLES")
    print("=" * 50)
    
    # Ejemplos de operaciones
    operations = [
        ("5 + 3", "Suma / Addition"),
        ("10 - 4", "Resta / Subtraction"),
        ("6 * 7", "Multiplicación / Multiplication"),
        ("20 / 4", "División / Division"),
        ("10 % 3", "Módulo / Modulo"),
        ("(5 + 3) * 2", "Operación compuesta / Compound operation"),
        ("100 / (2 + 3)", "Operación con paréntesis / Operation with parentheses"),
    ]
    
    print("\nOperaciones soportadas / Supported operations:\n")
    
    for expression, description in operations:
        try:
            result = eval(expression)
            print(f"  {expression:20} = {result:8}  ({description})")
        except Exception as e:
            print(f"  {expression:20} = ERROR   ({description})")
    
    print("\n" + "=" * 50)
    print("Para usar la calculadora con interfaz gráfica:")
    print("To use the calculator with graphical interface:")
    print("  python3 calculator.py")
    print("=" * 50)


if __name__ == "__main__":
    test_calculator_operations()
