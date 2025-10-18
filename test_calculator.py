#!/usr/bin/env python3
"""
Tests para la calculadora
Tests for the calculator
"""

import unittest
from unittest.mock import Mock, patch
import tkinter as tk


class TestCalculatorLogic(unittest.TestCase):
    """Pruebas para la lógica de la calculadora"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        # Mock the tkinter root to avoid GUI creation
        self.root = Mock(spec=tk.Tk)
        
        # Import calculator after mocking
        import calculator
        self.Calculator = calculator.Calculator
    
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculator_initialization(self, mock_button, mock_entry, mock_frame):
        """Prueba la inicialización de la calculadora"""
        calc = self.Calculator(self.root)
        self.assertEqual(calc.expression, "")
        self.root.title.assert_called_with("Calculadora")
        self.root.geometry.assert_called_with("400x600")
    
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_append_char(self, mock_button, mock_entry, mock_frame):
        """Prueba añadir caracteres a la expresión"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        
        calc.append_char('5')
        self.assertEqual(calc.expression, "5")
        
        calc.append_char('+')
        self.assertEqual(calc.expression, "5+")
        
        calc.append_char('3')
        self.assertEqual(calc.expression, "5+3")
    
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_clear(self, mock_button, mock_entry, mock_frame):
        """Prueba limpiar la expresión"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "5+3"
        
        calc.clear()
        self.assertEqual(calc.expression, "")
    
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_backspace(self, mock_button, mock_entry, mock_frame):
        """Prueba borrar el último carácter"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "5+3"
        
        calc.backspace()
        self.assertEqual(calc.expression, "5+")
        
        calc.backspace()
        self.assertEqual(calc.expression, "5")
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculate_addition(self, mock_button, mock_entry, mock_frame, mock_error):
        """Prueba la suma"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "5+3"
        
        calc.calculate()
        self.assertEqual(calc.expression, "8")
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculate_subtraction(self, mock_button, mock_entry, mock_frame, mock_error):
        """Prueba la resta"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "10-4"
        
        calc.calculate()
        self.assertEqual(calc.expression, "6")
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculate_multiplication(self, mock_button, mock_entry, mock_frame, mock_error):
        """Prueba la multiplicación"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "6*7"
        
        calc.calculate()
        self.assertEqual(calc.expression, "42")
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculate_division(self, mock_button, mock_entry, mock_frame, mock_error):
        """Prueba la división"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "20/4"
        
        calc.calculate()
        self.assertEqual(calc.expression, "5")
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculate_modulo(self, mock_button, mock_entry, mock_frame, mock_error):
        """Prueba el módulo"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "10%3"
        
        calc.calculate()
        self.assertEqual(calc.expression, "1")
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculate_division_by_zero(self, mock_button, mock_entry, mock_frame, mock_error):
        """Prueba la división por cero"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "5/0"
        
        calc.calculate()
        mock_error.assert_called_once()
        self.assertEqual(calc.expression, "")
    
    @patch('tkinter.messagebox.showerror')
    @patch('tkinter.Frame')
    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    def test_calculate_invalid_expression(self, mock_button, mock_entry, mock_frame, mock_error):
        """Prueba una expresión inválida"""
        calc = self.Calculator(self.root)
        calc.display = Mock()
        calc.expression = "5+"
        
        calc.calculate()
        mock_error.assert_called_once()
        self.assertEqual(calc.expression, "")


if __name__ == '__main__':
    unittest.main()
