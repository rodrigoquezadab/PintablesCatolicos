# PintablesCatolicos

Taller para armar e imprimir libros y cuadernillos de dibujos católicos para colorear, ajustados a hojas Carta, A4 u Oficio, con línea de corte punteada.

Es una aplicación web de un solo archivo (`index.html`): no requiere instalación ni servidor para usarla.

## Cómo usarla

1. Deja las imágenes nuevas en `imagenes_nuevas/` para clasificarlas, o cópialas ya ordenadas en la carpeta `biblioteca/` (PNG, JPG, WEBP, GIF, BMP o SVG). Las subcarpetas se muestran como temas (*Navidad*, *Santos*…).
2. Haz doble clic en `actualizar_biblioteca.bat` para actualizar la lista de dibujos (usa Python).
3. Abre `index.html` en el navegador (o con Live Server en `http://localhost:5500`) y pulsa **🔄 Actualizar**.

## Funciones

- **Biblioteca:** elegir, ordenar, girar y ocultar dibujos; filtro por tema y orientación. Los archivos de la carpeta nunca se modifican.
- **Distribución:** 2 dibujos por hoja (por defecto), 1 por hoja o 4 por hoja (2×2). Si el número es impar, la última hoja se completa repitiendo un dibujo.
- **Márgenes de 1 cm** hasta el borde del papel y a cada lado de la línea de corte, que va en el centro exacto: al cortar, cada pieza queda con su margen.
- **Ajuste de los dibujos:** se estiran hasta los márgenes (o se conserva la proporción), con giro automático y recorte del blanco sobrante.
- **Marco negro** alrededor de cada dibujo y **línea de corte** punteada.
- **Salida:** imprimir, guardar como PDF o **descargar en Word (.docx)** con las imágenes incrustadas (la descarga en Word requiere abrir la app con Live Server).
- **Modo oscuro** por defecto, con botón para cambiar a claro.

## Estructura

| Ruta | Contenido |
|---|---|
| `index.html` | La aplicación completa (HTML, CSS y JavaScript) |
| `PintablesCatolicos.html` | Copia idéntica de `index.html` |
| `biblioteca/` | Dibujos de la biblioteca y su lista `biblioteca.js` (generada) |
| `actualizar_biblioteca.py` / `.bat` | Actualizador de la lista de la biblioteca |
| `imagenes_nuevas/` | Bandeja para dejar imágenes nuevas antes de clasificarlas (su contenido no se sube a GitHub) |
| `referencias/` | Láminas de referencia originales de `pintar.pptx` (modelo de estilo; la app no las usa) |
| `CONTEXT.md` | Contexto del proyecto e historial de cambios |
