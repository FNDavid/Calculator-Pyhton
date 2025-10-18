# Guía Visual de la Calculadora / Calculator Visual Guide

## Interfaz de Usuario / User Interface

La calculadora presenta la siguiente interfaz gráfica:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                               ┃
┃   ╔═══════════════════════════════════════╗  ┃
┃   ║                                       ║  ┃
┃   ║             [Display]                 ║  ┃
┃   ║        (Expresión/Resultado)          ║  ┃
┃   ║                                       ║  ┃
┃   ╚═══════════════════════════════════════╝  ┃
┃                                               ┃
┃   ┏━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┓         ┃
┃   ┃   C   ┃   ←   ┃   %   ┃   /   ┃         ┃
┃   ┃ (Azul)┃(Azul) ┃(Naranja)(Naranja)       ┃
┃   ┣━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫         ┃
┃   ┃   7   ┃   8   ┃   9   ┃   *   ┃         ┃
┃   ┃ (Gris)┃(Gris) ┃(Gris) ┃(Naranja)        ┃
┃   ┣━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫         ┃
┃   ┃   4   ┃   5   ┃   6   ┃   -   ┃         ┃
┃   ┃ (Gris)┃(Gris) ┃(Gris) ┃(Naranja)        ┃
┃   ┣━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫         ┃
┃   ┃   1   ┃   2   ┃   3   ┃   +   ┃         ┃
┃   ┃ (Gris)┃(Gris) ┃(Gris) ┃(Naranja)        ┃
┃   ┣━━━━━━━┻━━━━━━━╋━━━━━━━╋━━━━━━━┫         ┃
┃   ┃       0       ┃   .   ┃   =   ┃         ┃
┃   ┃    (Gris)     ┃(Gris) ┃(Verde)┃         ┃
┃   ┗━━━━━━━━━━━━━━━┻━━━━━━━┻━━━━━━━┛         ┃
┃                                               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Paleta de Colores / Color Palette

### Display
- **Fondo**: #ECF0F1 (Gris muy claro)
- **Texto**: #2C3E50 (Gris oscuro)
- **Fuente**: Arial 24pt Bold

### Botones Numéricos (0-9, .)
- **Fondo**: #ECF0F1 (Gris claro)
- **Texto**: #2C3E50 (Gris oscuro)
- **Fuente**: Arial 18pt Bold

### Botones de Operadores (+, -, *, /, %)
- **Fondo**: #E67E22 (Naranja)
- **Texto**: Blanco
- **Fuente**: Arial 18pt Bold

### Botones Especiales (C, ←)
- **Fondo**: #3498DB (Azul)
- **Texto**: Blanco
- **Fuente**: Arial 18pt Bold

### Botón Igual (=)
- **Fondo**: #27AE60 (Verde)
- **Texto**: Blanco
- **Fuente**: Arial 18pt Bold

### Fondo de Ventana
- **Color**: #2C3E50 (Gris oscuro)

## Ejemplos de Uso / Usage Examples

### Ejemplo 1: Suma Simple / Simple Addition

```
Estado inicial:
┌─────────────────────┐
│                     │  ← Display vacío
└─────────────────────┘

Después de presionar 5:
┌─────────────────────┐
│                   5 │
└─────────────────────┘

Después de presionar +:
┌─────────────────────┐
│                  5+ │
└─────────────────────┘

Después de presionar 3:
┌─────────────────────┐
│                 5+3 │
└─────────────────────┘

Después de presionar =:
┌─────────────────────┐
│                   8 │
└─────────────────────┘
```

### Ejemplo 2: Operación Compleja / Complex Operation

```
Expresión: (10 + 5) * 2

Paso 1: 10+5*2  (sin paréntesis en este momento)
Resultado: 20
```

### Ejemplo 3: Manejo de Errores / Error Handling

```
Expresión: 5/0

Resultado:
┌─────────────────────────────────┐
│ ⚠️ Error                         │
│ No se puede dividir por cero    │
└─────────────────────────────────┘

Display se limpia automáticamente
```

## Flujo de Interacción / Interaction Flow

```
   Usuario hace click en botón
            ↓
   ¿Qué tipo de botón?
      ↙         ↓        ↘
   Número    Operador   Especial
      ↓         ↓          ↓
   Agregar   Agregar    Ejecutar
   al display al display función
      ↓         ↓          ↓
   Actualizar display
```

## Tamaño y Disposición / Size and Layout

- **Ventana**: 400px (ancho) × 600px (alto)
- **Display**: Ocupa ~20% del alto total
- **Botones**: Ocupa ~80% del alto total
- **Filas de botones**: 5 filas
- **Columnas**: 4 columnas
- **Espaciado**: 2px entre botones

## Comportamiento de Botones / Button Behavior

### Botón 'C' (Clear)
- Limpia toda la expresión
- Reinicia el display a estado vacío

### Botón '←' (Backspace)
- Elimina el último carácter
- Si el display está vacío, no hace nada

### Botón '='
- Evalúa la expresión matemática
- Muestra el resultado
- Si hay error, muestra mensaje y limpia

### Botones Numéricos y Operadores
- Agregan el carácter al final de la expresión
- Actualizan el display inmediatamente

## Accesibilidad / Accessibility

✓ **Contraste alto** entre texto y fondo
✓ **Botones grandes** fáciles de presionar
✓ **Colores diferenciados** por función
✓ **Cursor interactivo** (mano) al pasar sobre botones
✓ **Mensajes de error claros** en español

## Responsive Design

La calculadora mantiene proporciones fijas:
- Ancho mínimo: 400px
- Alto mínimo: 600px
- No se puede redimensionar (por diseño)
- Botones se expanden proporcionalmente

---

**Nota**: La calculadora está diseñada para ser intuitiva y fácil de usar, 
siguiendo los principios de diseño de calculadoras tradicionales.
