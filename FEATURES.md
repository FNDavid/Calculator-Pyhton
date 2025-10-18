# Características de la Calculadora / Calculator Features

## Interfaz Gráfica / Graphical Interface

La calculadora presenta una interfaz moderna y fácil de usar con los siguientes elementos:

### Display
- Pantalla grande (400x600 píxeles) para visualizar operaciones y resultados
- Fuente Arial de tamaño 24 en negrita
- Texto alineado a la derecha (como una calculadora tradicional)
- Fondo claro (#ECF0F1) con texto oscuro (#2C3E50)

### Botones / Buttons

#### Números (0-9)
- Color: Gris claro (#ECF0F1)
- Texto oscuro (#2C3E50)
- Disposición estándar de calculadora

#### Punto Decimal (.)
- Permite operaciones con decimales
- Mismo estilo que los números

#### Operadores (+, -, *, /, %)
- Color: Naranja (#E67E22)
- Texto blanco
- Fácilmente distinguibles de los números

#### Botones Especiales
- **C (Clear)**: Azul (#3498DB) - Limpia toda la expresión
- **← (Backspace)**: Azul (#3498DB) - Borra el último carácter
- **= (Igual)**: Verde (#27AE60) - Calcula el resultado

### Diseño de Botones / Button Layout

```
┌─────────────────────────────────────┐
│         [Display Area]              │
├──────────┬──────────┬──────────┬───┤
│    C     │    ←     │    %     │ / │
├──────────┼──────────┼──────────┼───┤
│    7     │    8     │    9     │ * │
├──────────┼──────────┼──────────┼───┤
│    4     │    5     │    6     │ - │
├──────────┼──────────┼──────────┼───┤
│    1     │    2     │    3     │ + │
├──────────┴──────────┼──────────┼───┤
│         0           │    .     │ = │
└─────────────────────┴──────────┴───┘
```

## Operaciones Soportadas / Supported Operations

1. **Suma (+)**: Ejemplo: 5 + 3 = 8
2. **Resta (-)**: Ejemplo: 10 - 4 = 6
3. **Multiplicación (*)**: Ejemplo: 6 * 7 = 42
4. **División (/)**: Ejemplo: 20 / 4 = 5
5. **Módulo (%)**: Ejemplo: 10 % 3 = 1

## Manejo de Errores / Error Handling

La calculadora maneja los siguientes casos de error:

1. **División por cero**: Muestra un mensaje de error y limpia la expresión
2. **Expresiones inválidas**: Detecta sintaxis incorrecta y muestra un mensaje de error
3. **Limpieza automática**: Después de un error, la expresión se limpia automáticamente

## Características Adicionales / Additional Features

- **Interfaz responsive**: Los botones se adaptan al tamaño de la ventana
- **Colores diferenciados**: Facilita la identificación de funciones
- **Cursor de mano**: Indica elementos clickeables
- **Resultados enteros**: Si el resultado es un número entero, se muestra sin decimales
- **Expresiones compuestas**: Permite múltiples operaciones en una sola línea

## Uso del Teclado / Keyboard Usage

Actualmente, la calculadora está optimizada para uso con mouse. Se puede extender para incluir:
- Teclas numéricas (0-9)
- Teclas de operadores (+, -, *, /)
- Enter para calcular
- Backspace para borrar
- Escape para limpiar

## Arquitectura del Código / Code Architecture

### Clase Calculator
- `__init__(root)`: Inicializa la calculadora
- `create_widgets()`: Crea la interfaz gráfica
- `on_button_click(char)`: Maneja los clicks en botones
- `append_char(char)`: Añade caracteres a la expresión
- `clear()`: Limpia la expresión
- `backspace()`: Borra el último carácter
- `calculate()`: Calcula el resultado
- `update_display()`: Actualiza el display

### Tests Unitarios / Unit Tests
- 11 pruebas que cubren:
  - Inicialización
  - Añadir caracteres
  - Operaciones básicas
  - Manejo de errores
  - Funciones especiales

## Requisitos Técnicos / Technical Requirements

- **Python**: 3.x
- **Tkinter**: 8.6 o superior
- **Sistema Operativo**: Windows, macOS, Linux

## Personalización / Customization

El código está diseñado para ser fácilmente personalizable:
- Colores definidos en variables
- Tamaño de ventana configurable
- Layout de botones modificable
- Fuentes y estilos ajustables

## Rendimiento / Performance

- Inicio rápido (< 1 segundo)
- Respuesta inmediata a clicks
- Sin lag en operaciones
- Bajo consumo de recursos
