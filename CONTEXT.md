# 📖 CONTEXTO DEL PROYECTO: PINTABLES CATÓLICOS

> **Documento de Contexto Vivo**: Este archivo registra la intención original, el alcance, las especificaciones funcionales, la arquitectura técnica y la evolución de la aplicación. Se mantendrá actualizado con cada nueva funcionalidad.

---

## 1. Identificación y Propósito

* **Nombre del Proyecto:** Pintables Católicos (*Taller de Libros y Cuadernillos de Dibujo para Imprimir*)
* **Propósito Principal:** Proporcionar una herramienta visual y práctica para que catequistas, familias, parroquias y colegios puedan generar, diagramar e imprimir cuadernillos y libros de dibujos católicos para colorear, adaptados milimétricamente al formato de documentos estándar (Word / Carta).
* **Filosofía de Implementación:** 
  1. **Cero fricción:** La aplicación principal debe funcionar como un archivo HTML autocontenido que se abre con un simple doble clic en cualquier navegador, sin requerir instalación de programas, Node.js, terminales ni servidores.
  2. **Calidad de impresión física:** Cada hoja se calcula con dimensiones físicas reales (mm) y reglas de corte para maximizar el uso del papel y garantizar nitidez en impresoras domésticas e institucionales.

---

## 2. Intención y Casos de Uso

1. **Ajuste a documentos estilo Word:**
   * La hoja por defecto es **Carta (Letter: 8.5 × 11 pulgadas / 215.9 × 279.4 mm)**.
   * Cuenta con márgenes estándar de documentos (Normal 2.54 cm, Estrecho 1.27 cm, Moderado y Mínimo de impresora).
   * Los dibujos se escalan proporcionalmente dentro del área imprimible sin deformarse jamás.

2. **Aprovechamiento del papel y corte guiado:**
   * Las imágenes se catalogan en **Verticales** y **Horizontales**.
   * **Imagen horizontal solitaria:** Se ajusta al ancho máximo permitido por los márgenes de la hoja Carta.
   * **Dos imágenes horizontales en una hoja:** En una hoja Carta vertical, dos dibujos horizontales caben perfectamente apilados (uno arriba y otro abajo), aprovechando el 100% del ancho útil.
   * **Línea punteada de corte (✂️):** Activada **por defecto**. Indica con claridad la mitad exacta de la hoja para recortar con tijera o guillotina y obtener dos medias hojas prolijas.
   * **Cuatro imágenes por hoja (2×2):** Dispone de líneas de corte en cruz para generar mini-estampas o flashcards.

3. **Generación flexible de libros y cuadernillos:**
   * Permite crear cuadernillos de diferentes tamaños: libros de **4, 8, 12, 16, 20 páginas** o de **todas las páginas necesarias** según las ilustraciones seleccionadas en la biblioteca.
   * Incluye **portada para colorear** personalizable con título, dedicatoria (*"Este libro pertenece con cariño a: _______"*), nombre de la comunidad o parroquia y año.
   * Incluye pie de página con numeración consecutiva (*Página X de Y*).

4. **Impresión y Exportación:**
   * **Impresión Directa (`window.print`):** Estilos CSS calibrados con `@page { size: letter portrait; margin: 0; }` que limpian la interfaz de la web y mandan solo las hojas a escala 1:1 a la impresora física o al convertidor a PDF del navegador.
   * **Descarga a PDF:** Opción para descargar el documento listo para enviar por correo o a un centro de copiado.

---

## 3. Catálogo y Biblioteca de Dibujos

La aplicación clasifica cada recurso en dos orientaciones fundamentales y por temáticas catequéticas:

### Orientación y Detección Automática
* **Vertical (Retrato):** Proporción donde la altura es mayor que el ancho (aprox. 3:4). Típico de figuras individuales de santos, Cristo o la Virgen.
* **Horizontal (Paisaje):** Proporción donde el ancho es mayor que la altura (aprox. 16:10 / 16:11). Típico de escenas bíblicas panorámicas.
* **Subida de Dibujos Propios (PNG, JPG, SVG, WebP):** El usuario puede arrastrar o seleccionar cualquier imagen de su equipo. El sistema lee sus dimensiones (`width` y `height`), calcula la relación de aspecto y le asigna automáticamente la etiqueta **Vertical** u **Horizontal**.

### Colección Inicial Integrada (16 Obras Vectoriales SVG)
* **Verticales:**
  1. *La Sagrada Familia* (San José, María y el Niño)
  2. *Jesús el Buen Pastor* (con la ovejita sobre los hombros y báculo)
  3. *Virgen María Reina de la Paz* (manto de gracia y estrellas)
  4. *San Francisco de Asís* (hábito franciscano, pajarito y lobo bueno)
  5. *San Miguel Arcángel* (alas, armadura de fe y espada victoriosa)
  6. *Ángel de la Guarda* (custodiando a los niños en el camino)
  7. *La Santa Cruz y la Eucaristía* (Cáliz sagrado, Hostia con JHS, uvas y trigo)
  8. *El Sagrado Corazón de Jesús* (corazón ardiente, cruz y bendición)
* **Horizontales:**
  9. *El Arca de Noé y el Arcoíris* (animales asomándose y paloma de la paz)
  10. *Nacimiento en Belén / El Pesebre* (José, María, Niño, buey y estrella)
  11. *La Creación del Mundo* ("Y vio Dios que era bueno": sol, luna, río, flores)
  12. *La Última Cena* (Jesús bendiciendo el pan y el vino con los apóstoles)
  13. *Domingo de Ramos* (Jesús sobre el burrito y niños con palmas)
  14. *La Resurrección del Señor* (tumba vacía, el ángel y flores pascuales)
  15. *Milagro de los Panes y los Peces* (las canastas y la multitud)
  16. *La Iglesia Parroquial y las Familias* (campanario, atrio y comunidad)

---

## 4. Configuración y Parámetros del Documento

| Parámetro | Opciones | Valor por Defecto |
| :--- | :--- | :--- |
| **Tamaño de Hoja** | Carta (215.9 × 279.4 mm), A4 (210 × 297 mm), Oficio (215.9 × 355.6 mm) | **Carta (Letter)** |
| **Márgenes Word** | Normal (2.54 cm), Estrecho (1.27 cm), Moderado, Mínimo (1.0 cm) | **Normal (2.54 cm)** |
| **Distribución** | Inteligente (Smart), 1 por página, 2 por página, 4 por página | **Inteligente** |
| **Línea de Corte** | Activada (con tijera ✂️) / Desactivada | **Activada** |
| **Portada** | Activada / Desactivada (editable) | **Activada** |
| **Cantidad de Páginas**| Todas las necesarias, 4, 8, 12, 16, 20 páginas | **Todas** |
| **Guía de Márgenes** | Visible / Oculta (línea punteada azul para inspección) | **Oculta** |

---

## 5. Estructura de Archivos del Proyecto

El repositorio cuenta con dos modalidades complementarias:

### Modalidad A: Archivo Autónomo (Producción directa con un clic)
* [`index.html`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/index.html) y [`PintablesCatolicos.html`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/PintablesCatolicos.html):
  * **No requiere instalación ni comandos.** Se abre con doble clic.
  * Contiene todo el CSS, motor de renderizado, biblioteca de dibujos y lógica de corte en un único archivo autónomo.

### Modalidad B: Entorno Modular para Desarrollo (React + Tailwind CSS)
* [`src/App.jsx`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/App.jsx): Componente principal, manejo de estado y vistas.
* [`src/data/svgDrawings.js`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/data/svgDrawings.js): Catálogo de dibujos iniciales en formato SVG escalable.
* [`src/utils/paginationEngine.js`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/utils/paginationEngine.js): Algoritmo de diagramación de páginas, ranuras y líneas de corte.
* [`src/utils/pdfExport.js`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/utils/pdfExport.js): Generador de PDF en 300 DPI con `jsPDF`.
* [`src/components/PageSheetView.jsx`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/components/PageSheetView.jsx): Renderizado WYSIWYG de cada hoja física de papel.
* [`src/components/LibraryModal.jsx`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/components/LibraryModal.jsx): Galería con buscador, filtros y carga de imágenes.
* [`src/components/SettingsBar.jsx`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/components/SettingsBar.jsx): Controles de márgenes, papel y distribución.
* [`src/components/CoverEditModal.jsx`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/components/CoverEditModal.jsx): Editor del texto de la portada.

---

## 6. Historial de Versiones y Bitácora de Decisiones

* **v1.0.0 (03-11-2026):**
  * Definición de requisitos: ajuste a hojas de documento (Word), tamaño Carta por defecto, clasificación en vertical/horizontal.
  * Implementación de la distribución de dos imágenes horizontales apiladas en hoja vertical con línea punteada de corte central (✂️).
  * Creación de la biblioteca inicial de 16 dibujos vectoriales católicos de alta calidad.
  * Creación de la versión autónoma en un solo archivo `index.html` para abrir con un clic sin requerir configuración de entorno.
  * Creación de este documento de contexto (`CONTEXT.md`).
* **v1.1.0 (03-11-2026):**
  * **Eliminación de bordes y marcos:** Se eliminaron los rectángulos y marcos envolventes internos de las ilustraciones vectoriales para dejar únicamente los trazos limpios de los dibujos.
  * **Ajuste total a los márgenes de impresión:** Los dibujos ahora se expanden hasta tocar exactamente los límites de los márgenes de documento configurados (2.54 cm Normal, 1.27 cm Estrecho, etc.), que son los márgenes de seguridad que los procesadores de texto y las impresoras resguardan para no salirse de la página.
  * **Aprovechamiento 100% del área útil:** En el modo de 2 horizontales por página, cada ilustración se extiende de margen a margen y hasta la línea de corte central sin paddings innecesarios.
* **v1.2.0 (03-11-2026):**
  * **Rediseño artístico y anatómico:** Se eliminaron los trazos poligonales y esquemáticos, reemplazándolos por curvas Bézier continuas, orgánicas y elegantes propias de libros clásicos de colorear.
  * **Rostros humanos y serenos:** Ojos almendrados con párpados definidos y puntos de brillo, cejas proporcionadas, puente nasal suave y labios esculpidos con expresión dulce y compasiva.
  * **Figuras y contornos 100% cerrados:** Todos los elementos (vestimentas, manos, cabello, aureolas, animales, mantos) están construidos con trazados cerrados (`Z`), garantizando áreas delimitadas fáciles de colorear con lápices, ceras o digitalmente.
* **v1.4.0 (03-11-2026):**
  * **Integración de Ilustraciones con Nano Banana y Grabados Históricos Clásicos:** Sustitución completa de los dibujos programáticos vectoriales por auténticas obras maestras de arte sacro para colorear de alta definición, combinando la generación de imágenes con el modelo **Nano Banana** (Gemini Image Generation / Imagen) y grabados originales en xilografía de **Gustave Doré** (*La Grande Bible de Tours*).
  * **Almacenamiento Local:** Las imágenes en alta resolución se guardan en la carpeta local [`images/`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/images/) y [`public/images/`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/public/images/), cargándose de forma instantánea y nativa tanto en [`index.html`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/index.html) (con doble clic) como en el entorno Vite.
* **v1.5.0 (03-11-2026):**
  * **Estilo Intermedio Redondeado (Fácil de pintar completo con 8 colores en 40 minutos):**
    * **Eliminación del exceso de detalle:** Se eliminaron las micro-tramas y el sombreado denso que impedían colorear las láminas en una sesión normal de 30-40 minutos.
    * **Formas más redondeadas y simpáticas:** Rostros dulces con grandes ojos almendrados y brillo, mejillas suaves, sonrisas pacíficas, rizos esponjosos y pliegues amplios y fluidos que resultan entrañables y atractivos tanto para niños en catequesis como para adultos en oración y talleres.
    * **Optimizado para una caja básica de 8 lápices de colores:** Cada dibujo consta de entre 15 y 30 zonas amplias bien definidas, pensadas para combinar armoniosamente: Amarillo/Dorado (aureolas, sol), Azul (manto de María, cielos), Rojo (túnicas, corazones), Verde (árboles, prados, palmas), Marrón (madera, arca, cabellos), Piel/Durazno (rostros y manos), Blanco (corderito, lirios) y Gris/Negro (adoquines, detalles).
    * **Selector de Estilo de Dibujo:** Se incorporó un control directo en la barra superior para alternar instantáneamente entre el **Estilo Intermedio Amigable (predeterminado)** y el **Estilo Grabado Clásico (detallado)** según la preferencia del usuario o la edad del grupo.

* **v1.6.0 (04-11-2026):**
  * **Restauración de las Ilustraciones Originales y Reducción Quirúrgica de Líneas:**
    * **Restablecimiento del catálogo de Arte Sacro:** Se restauraron como colección principal y predeterminada en [`index.html`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/index.html) y [`PintablesCatolicos.html`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/PintablesCatolicos.html) las 16 composiciones admiradas por el usuario (*La Sagrada Familia, Buen Pastor, San Miguel, Virgen María, Arca de Noé, etc.*).
    * **Reducción de micro-líneas y sombreado pesado:** Mediante un pipeline de procesamiento con Python PIL (filtros medianos de eliminación de micro-tramas, suavizado gaussiano de bordes y curvas de umbral anti-aliased), se suprimieron los millones de trazos densos y rayados de sombreado cruzado (*cross-hatching*).
    * **Espacio en blanco para colorear del 87% al 98.5%:** Las láminas históricas (Doré) y de Nano Banana pasaron de tener fondos oscuros y sombreados recargados a amplios campos en blanco puro delimitados por líneas de contorno redondeadas, suaves y continuas.
    * **Fácil de pintar con 8 colores en 40 minutos:** Las figuras sagradas, rostros, mantos, aureolas, animales y arquitectura conservan toda su nobleza, simpatía y belleza visual, pero ahora cualquier niño o adulto puede completarlas en 40 minutos con una caja básica de 8 lápices o ceras.
    * **Selector visual en la barra de ajustes:** Permite alternar entre la colección de *Arte Sacro Limpio* y *Trazos Básicos SVG*.

* **v1.7.0 (04-11-2026):**
  * **Estandarización Vectorial Rigurosa: Trazos Cerrados, Líneas Continuas y Cero Artefactos de Imagen:**
    * **100% de Trazos Cerrados:** Cada uno de los 286 caminos vectoriales de la colección termina en el comando de cierre `Z` (o es un `<circle>`, `<ellipse>`, `<rect>`, `<polygon>`), garantizando que todas las áreas sean polígonos cerrados ideales para pintar sin "fugas" de color.
    * **Líneas Unidas y Continuas:** Las líneas convergen en intersecciones exactas de coordenadas. No existen segmentos flotantes, extremos sueltos ni elementos `<line>` desconectados.
    * **Espesor Definido y Coherente:** Grosor calibrado con exactitud (`stroke-width="3.5"` en contornos principales, `stroke-width="4.0"` en siluetas y arcos, y `stroke-width="2.5"` en rasgos faciales y detalles interiores), con `stroke-linecap="round"` y `stroke-linejoin="round"`.
    * **Líneas Delimitadas a lo Básico:** Eliminación de cualquier trama, micro-línea o sombreado; solo los contornos esenciales de las figuras, ropajes, aureolas y paisajes sagrados.
    * **Cero Puntos o Líneas de Imagen:** Se erradicaron completamente los artefactos rasterizados de mapa de bits (píxeles, ruido de dithering, puntos sueltos). Los ojos son trazados vectoriales limpios con iris en contorno abierto, listos para colorear.
    * **Actualización en toda la suite:** Integrado de forma predeterminada en [`index.html`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/index.html), [`PintablesCatolicos.html`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/PintablesCatolicos.html) y [`src/data/cleanVectorDrawings.js`](file:///C:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/src/data/cleanVectorDrawings.js).

* **v2.0.0 (04-11-2026):**
  * **El Gestor Completo de Carpetas e Imágenes para Imprimir (Funcionalidad Central):**
    * **Carga de Carpetas Completas (`webkitdirectory`):** Nuevo botón principal destacado **"📁 Cargar Carpeta"** en la barra superior y en el modal. Permite seleccionar con un solo clic cualquier carpeta del equipo, importando y procesando recursivamente todas las imágenes soportadas (PNG, JPG, WEBP, SVG, GIF, BMP).
    * **Soporte Drag & Drop Universal:** Arrastrar una carpeta o conjunto de archivos desde el explorador de Windows directamente a la ventana del navegador muestra un overlay interactivo y los importa de inmediato.
    * **Detección Automática de Orientación y Relación de Aspecto:** El motor calcula instantáneamente las proporciones (`naturalWidth` y `naturalHeight`). Si `aspecto > 1.05`, se etiqueta automáticamente como **Horizontal (↔ 2 por hoja)**; si es menor o igual, como **Vertical (↕ 1 por hoja completa)**.
    * **Herramientas de Gestión por Imagen:**
      * **Girar 90° (`↻ Girar`):** Rotación física de la imagen en un lienzo `<canvas>` interno, recalculando dimensiones y orientación automáticamente.
      * **Cambiar Orientación (`↔ / ↕`):** Botón directo para alternar manualmente entre formato horizontal y vertical.
      * **Reordenar Páginas (`⬆ / ⬇`):** Permite mover imágenes hacia adelante o atrás para definir con exactitud el orden en que se imprimirán las páginas del libro.
      * **Eliminar (`🗑`):** Quitar imágenes individuales o vaciar la carpeta completa.
    * **Persistencia Local en IndexedDB:** Las imágenes importadas se guardan en la base de datos interna del navegador (`PintablesCatolicosDB`). Al refrescar o reabrir el archivo con doble clic, la carpeta cargada sigue disponible sin tener que reimportar.
    * **Barra de Estado en Tiempo Real:** Muestra el nombre de la carpeta activa, cantidad de dibujos (verticales y horizontales) y el total exacto de páginas físicas que se generarán para impresión en tamaño Carta con márgenes Word (2.54 cm) y líneas de corte (✂️).

* **v2.1.0 (04-11-2026):**
  * **Menú de Ajustes Compacto y Plegable (Siempre Plegado por Defecto):**
    * **Ahorro Radical de Espacio Vertical:** Se eliminaron las 3 a 4 filas densas de controles y botones de configuración que ocupaban más de 200px de altura en la pantalla, despejando el área de trabajo para que las hojas simuladas de tamaño Carta sean visibles y protagonistas de forma inmediata.
    * **Siempre Plegado por Defecto:** Al abrir la aplicación o recargar la página, el panel de configuración arranca **100% plegado/oculto** (`display: none;`).
    * **Barra Resumen Slim (32px):** Una cinta compacta e interactiva situada bajo la cabecera que muestra en tiempo real las opciones activas mediante mini-etiquetas dinámicas:
      * `📄 Carta (Letter)` | `📐 Word 2.54cm` | `⚡ Inteligente` | `✂️ Corte ON` | `📖 Portada ON` | `📁 X dibujos selec.`
    * **Desplegable con un Solo Clic:** Al hacer clic en cualquier lugar de la cinta o en el botón `[ ⚙️ Ajustes ▾ ]` de la cabecera, el panel completo de ajustes de hoja, márgenes Word, distribución, portada y plantillas rápidas se despliega con fluidez.
    * **Cierre Inmediato:** Se puede volver a plegar haciendo clic en la cinta, en el botón de la cabecera o mediante el enlace inferior `[ ▴ Plegar y Ocultar Menú de Ajustes ]`.
    * **Actualización Reactiva de Badges:** Cualquier modificación de márgenes, tipo de hoja o plantilla rápida actualiza al instante las etiquetas de la cinta plegada.
    * **Sin Interferencia en Impresión:** Todas las barras de ajustes y cintas plegables se ocultan automáticamente en `@media print` y exportación a PDF.

* **v2.2.0 (04-11-2026):**
  * **Integración del Benchmark Referencial de Trazos y Composición (Colección Oficial):**
    * **Fuente Original:** Imágenes maestras aportadas en `uploadimages` (`pintar.pptx`), estableciendo el estándar absoluto de estilo y diagramación.
    * **Extracción y Optimización de 10 Láminas Verticales Oficiales:** Se procesaron y recortaron en formato vertical puro (3:4), reduciendo su peso en un 60% mediante escala de grises limpia optimizada para impresión física en blanco y negro:
      1. *Jesús Nació* (`JESUS NACIO`) — Belén, San José con báculo, María orando, Niño en pesebre, ovejita, burrito y estrella.
      2. *Espíritu Santo Guíame* (`ESPIRITU SANTO GUIAME`) — Paloma celestial con destellos de gracia, nubes y corazones.
      3. *María Acompáñame* (`MARIA ACOMPAÑAME`) — Virgen orando enmarcada en un Santo Rosario completo con su cruz.
      4. *Jesús es mi Pastor* (`JESUS ES MI PASTOR`) — Buen Pastor con cayado y tierna ovejita en prado de flores.
      5. *Gracias Dios Mío* (`GRACIAS DIOS MIO`) — Niño de rodillas orando con manos juntas, cruz, estrellas y corazones.
      6. *Vamos a Misa* (`VAMOS A MISA`) — Niños con mochilitas caminando alegres a la parroquia bajo un sol sonriente.
      7. *Angelito de mi Guarda* (`ANGELITO DE MI GUARDA`) — Ángel custodio alado protegiendo con dulzura a un niño rezando.
      8. *Jesús te Ama* (`JESUS TE AMA`) — Jesús sentado abrazando con amor a dos niños ("Dejad que los niños vengan a mí").
      9. *Virgencita de mi Corazón* (`VIRGENCITA DE MI CORAZON`) — Virgen María con brazos acogedores abiertos, túnica y flores.
      10. *San José Cuida a Jesús* (`SAN JOSE CUIDA A JESUS`) — San José sosteniendo al Niño Jesús en brazos con mirada bondadosa.
    * **Colección Activa por Defecto:** Al iniciar la aplicación, las 10 láminas oficiales se cargan y seleccionan automáticamente, listas para imprimir en hoja Carta o cuadernillo 2 por hoja.

* **v2.3.0 (04-11-2026):**
  * **Resguardo y Copia de Seguridad Íntegra (`uploadimages_copia`):**
    * Se creó una copia exacta y preservada intacta de la carpeta de referencia `uploadimages/` en [`uploadimages_copia/`](file:///c:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/uploadimages_copia/) con todos sus archivos originales sin modificar.
  * **Reparación Quirúrgica del Trazo Abierto en el Título ("JESUS NACIO"):**
    * En la lámina 2 de referencia (`pintar.pptx_20260711_191631_0000.png`), el borde derecho cortaba la letra `'O'` del título en `x=463, y=104..144`.
    * Se reconstruyó el arco faltante mediante una curva de Bézier de grosor exacto de 4.0px idéntica a la tipografía original.
    * Se ejecutó un test de relleno por inundación (*flood-fill*) con Python PIL en todos los caracteres y elementos, certificando el sellado hermético al 100% con cero fugas de pintura o color.
    * La corrección se propagó a todas las versiones: `uploadimages/`, `images/oficiales/`, `public/images/oficiales/` y `dist/images/oficiales/`.
  * **Generación de las 10 Láminas Complementarias al Estilo Pastoral Benchmark:**
    * Para completar los temas canónicos manteniendo la fidelidad visual de `uploadimages`, se crearon 10 nuevas ilustraciones maestras para colorear:
      1. *San Miguel Arcángel* (`SAN MIGUEL ARCANGEL`) — Armadura tierna, alas extendidas, espada de luz y escudo con cruz.
      2. *San Francisco de Asís* (`SAN FRANCISCO DE ASIS`) — Hábito franciscano, conejito en brazos, paloma y pajarillos en prado.
      3. *El Arca de Noé* (`EL ARCA DE NOE`, Horizontal) — Arca sobre el mar, parejitas de jirafas, leoncitos y arcoíris sonriente.
      4. *La Última Cena* (`LA ULTIMA CENA`, Horizontal) — Jesús en el centro con apóstoles chibi, cáliz y pan sobre la mesa.
      5. *Domingo de Ramos* (`DOMINGO DE RAMOS`, Horizontal) — Jesús montado en burrito entrando a Jerusalén entre niños agitando palmas.
      6. *Jesús Resucitado* (`JESÚS RESUCITADO`) — Túnica blanca radiante, estandarte de la victoria, sepulcro abierto y lirios.
      7. *El Santo Sacramento* (`EL SANTO SACRAMENTO`) — Custodia dorada con la Sagrada Eucaristía, ángeles adorando e incienso.
      8. *Panes y Peces* (`PANES Y PECES`, Horizontal) — Cesta con panes, peces saltando y sol alegre junto a las olas.
      9. *La Creación de Dios* (`LA CREACION DE DIOS`, Horizontal) — Sol, luna, estrellas, árboles frutales y mar rebosante de peces.
      10. *Sagrado Corazón de Jesús* (`SAGRADO CORAZON DE JESUS`) — Jesús con túnica y manto, corazón encendido con cruz y rayos suaves.
    * **Fórmula Estilística Unificada:** Título superior en letra globito hueca sin relleno, anatomía chibi/pastoral dulce y expresiva con ojos almendrados y doble brillo blanco, líneas de contorno continuas de 4px 100% cerradas, fondo enriquecido con corazones, estrellas de 5 puntas, nubes y margaritas, optimizadas para pintar con 8 colores en 30-40 minutos.
  * **Unificación de la Colección Maestra (20 Dibujos):**
    * Ambas modalidades (`index.html` autónomo y Vite React) incluyen los 20 dibujos en alta resolución.
    * Los 6 dibujos horizontales se emparejan automáticamente de 2 en 2 en hojas tamaño Carta con línea de corte central (✂️), y los 14 verticales ocupan una hoja completa ajustada a los márgenes Word.
  * **Inicialización Inmediata y Robusta:** Se implementó una verificación síncrona de `document.readyState` en `index.html` para garantizar que la aplicación y la biblioteca se muestren al instante sin depender de la temporización del evento `DOMContentLoaded`.
  * **Menú Siempre Plegado por Defecto:** La cabecera se mantiene en formato ultra-compacto con la cinta slim interactiva, preservando el 100% del área de pantalla para la visualización del libro y la gestión de carpetas e imágenes.

* **v2.3.1 (04-11-2026):**
  * **Simplificación Radical de Trazos y Líneas (Fidelidad Absoluta al Benchmark):**
    * **Eliminación de la densidad de líneas:** Se detectó que las versiones anteriores de las 10 láminas complementarias tenían demasiados pliegues de ropa, alas recargadas con decenas de plumas y fondos saturados.
    * **Rediseño Minimalista según las Referencias (`uploadimages`):** Se rehicieron las 10 láminas (*Sagrado Corazón, San Miguel, San Francisco, El Arca de Noé, La Última Cena, Domingo de Ramos, Jesús Resucitado, El Santo Sacramento, Panes y Peces, La Creación*) aplicando la regla de mínima cantidad de líneas:
      * **Ropajes:** Solamente 2 a 3 líneas suaves para pliegues esenciales, sin drapeados ni sombras.
      * **Alas y plumaje:** Contorno exterior limpio con 4 a 5 ondas redondeadas simples (idéntico al ángel de *Angelito de mi guarda*).
      * **Cabellos y rostros:** Bloques suaves con 2 a 3 ondulaciones, ojos redondos con brillo blanco y sonrisas dulces abiertas.
      * **Fondos aireados:** Máximo 2 nubes simples de 3 lóbulos, 4 corazones y 4 estrellas flotantes, dejando grandes extensiones de blanco puro para colorear fácilmente.
    * **Despliegue y Sincronización:** Actualizado en [`images/pastoral/`](file:///c:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/images/pastoral/), [`public/images/pastoral/`](file:///c:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/public/images/pastoral/), [`dist/images/pastoral/`](file:///c:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/dist/images/pastoral/), [`index.html`](file:///c:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/index.html) y [`PintablesCatolicos.html`](file:///c:/Users/ThinkPad/Desktop/NewCode/PintablesCatolicos/PintablesCatolicos.html).

* **v2.4.0 (05-11-2026) — Revisión de calidad y correcciones:**
  * **Logo y nombre enlazados:** el área de marca de la cabecera es un enlace que recarga la aplicación.
  * **Diseño responsive:** la cabecera y las barras se adaptan a pantallas estrechas (sin desplazamiento horizontal); las barras fijas se ubican bajo la cabecera según su altura real.
  * **Impresión fiel al papel elegido:** `@page` y el tamaño físico de hoja se ajustan dinámicamente a Carta, A4 u Oficio (antes siempre se imprimía en Carta).
  * **Distribución inteligente respeta el orden del libro:** las verticales ya no quedan siempre al final; cada horizontal se empareja con la siguiente horizontal de la lista.
  * **Aviso de páginas recortadas:** si el límite de páginas del libro deja dibujos fuera, se indica cuántas hojas se omitieron.
  * **Ajustes y portada persistentes:** colección, hoja, márgenes, distribución, corte, portada y textos se guardan en `localStorage` (con tolerancia a fallos).
  * **Correcciones de errores:** importación duplicada al soltar en el recuadro del gestor; carpetas de más de 100 imágenes se leían incompletas; imágenes repetidas (mismo nombre y tamaño) se omiten; cambiar de colección ya no borra las imágenes importadas; «Restaurar Ejemplos» usa la colección activa; ordenamiento estable; guardado en IndexedDB espera la transacción y conserva el orden; el estado vacío se muestra aunque la portada esté activa; estimación exacta de hojas en el gestor.
  * **Seguridad:** los SVG importados se muestran como imagen (`data:` URL), sin ejecutar scripts ni chocar ids.
  * **Usabilidad:** cerrar modales con Escape o clic fuera; Enter guarda la portada; tarjetas de la biblioteca accesibles por teclado; año de portada automático; «Guardar PDF» indica elegir «Guardar como PDF»; se eliminó la dependencia CDN de jsPDF (no se usaba), así la app funciona sin conexión.

* **v2.5.0 (05-11-2026) — Biblioteca de vectores con línea central y ancho único:**
  * Las 20 láminas de la colección principal se vectorizaron a SVG en `biblioteca_vectores/svg/` con `herramientas/vectorizar.py`, trabajando sobre una copia en `biblioteca_vectores/fuente/` (los originales de `images/` no se tocan).
  * **Ancho de línea único y sin zonas negras:** cada trazo se reduce a su línea central (esqueleto) y se dibuja con un solo `stroke-width`, sin rellenos. Las zonas negras macizas y compactas (pupilas, manchas) se convierten en su contorno para que se puedan colorear. Tinta: similar al original en las láminas de referencia y entre 18 % y 48 % menos en las pastoral.
  * **Líneas cerradas:** cierre morfológico que une huecos entre trazos; verificado con mapas de zonas en `biblioteca_vectores/revision/`.
  * **Simplificación:** se eliminan manchas sueltas y ramitas cortas del esqueleto, los huecos diminutos se funden en la línea y los trazos se suavizan (Bézier).
  * **Líneas limpias:** cada trazo se ajusta con rectas y curvas Bézier por mínimos cuadrados (Schneider) en `herramientas/curvas.py`, conservando esquinas nítidas; sin temblor. Grosor único de 6 px, igual al medido en las láminas de referencia de `uploadimages/` (mediana 6,0 px en las 10 oficiales).
  * **Ojos de la referencia en todos los personajes:** pupila ovalada negra con brillo blanco, como en las láminas de `uploadimages/`; tamaño uniforme por personaje (también los que tenían los ojos cerrados); párpados y cejas originales conservados. Posiciones revisadas lámina por lámina en `biblioteca_vectores/ojos.json`.
  * Marco redondeado opcional (`MARCO` en el script, desactivado por decisión del usuario): cerraría las figuras recortadas por el borde y las líneas de suelo/río. Sin marco, esas zonas quedan abiertas hacia el fondo. Tinta: similar al original en las 10 láminas de referencia (mismo grosor) y entre 18 % y 48 % menos en las 10 pastoral.
  * Márgenes vacíos recortados: los dibujos aprovechan mejor la hoja. Catálogo con métricas (zonas, tinta antes/después) en `catalogo.json` y comparación en `vista_previa.html`.
  * Limpieza: se eliminaron el prototipo React/Vite (`src/`, `public/`, `dist/`, `package.json`…) y `scratch/` (enviados a la Papelera).

* **v3.0.0 (07-11-2026) — Biblioteca en carpeta; se elimina la generación de imágenes:**
  * **Decisión del usuario:** se abandona la generación/vectorización automática de dibujos. Se enviaron a la Papelera `herramientas/`, `biblioteca_vectores/`, `.venv-vectores/`, `generate_clean_vectors.py`, `generate_pastoral_benchmark_vectors.py`, `images/`, `images_cleaned/` e `images_original/`, y se quitaron de la app las 3 colecciones incluidas (Oficial Pastoral, Trazos Vectoriales, Grabados). Se conservan las referencias `uploadimages/` y `uploadimages_copia/`.
  * **Biblioteca = carpeta `biblioteca/` del proyecto:** el usuario copia allí sus imágenes (PNG, JPG, WEBP, GIF, BMP, SVG; las subcarpetas son categorías) y ejecuta `actualizar_biblioteca.bat` (llama a `actualizar_biblioteca.py`, solo biblioteca estándar de Python), que genera `biblioteca/biblioteca.js` (`window.BIBLIOTECA`). La app lo carga con `<script src>`, así funciona con doble clic (`file://`) y con Live Server. Botón «🔄 Actualizar» para releer.
  * **Gestión para imprimir (sin cambios en el motor):** selección, orden, giro 90° (por CSS con unidades de contenedor, sin canvas para que funcione en `file://`), orientación manual, distribución 1/2/4 por hoja con corte, portada, impresión y PDF.
  * **Preferencias por imagen en `localStorage`** (`pintablesCatolicos.biblioteca.v1`), con la ruta del archivo como id: orden, giros, orientación, selección y ocultas. «Quitar» solo oculta el dibujo del libro (recuperable con «Mostrar ocultas»); nunca borra archivos. Las imágenes nuevas se añaden al final y seleccionadas.
  * Se eliminó la importación por navegador (cargar carpeta/archivos, arrastrar y soltar, IndexedDB): la carpeta `biblioteca/` es la única fuente.

* **v3.1.0 (07-11-2026) — Modo oscuro, mínimo 2 dibujos por hoja y giro automático:**
  * **Modo oscuro por defecto** en la interfaz (botón ☀️/🌙 en la cabecera, se recuerda en `localStorage` como `pintablesCatolicos.tema`; se aplica en `<head>` antes de pintar). Las hojas, la portada y las vistas previas siguen en blanco porque representan el papel; la impresión no cambia.
  * **Distribución:** «2 dibujos por hoja» (por defecto) empareja todos los dibujos en orden, sean verticales u horizontales; si el total es impar, la última hoja se completa **repitiendo un dibujo** (por defecto el primero del libro; se elige en Ajustes con «🔁 Completar la última hoja con», que solo aparece cuando hace falta). Así todas las hojas llevan 2. «1 dibujo por hoja» es la única opción con uno por hoja. En «4 por hoja», si sobraría uno, la hoja anterior cede uno (3 + 2). Se eliminó la opción duplicada «2 por página».
  * **Giro automático (activado por defecto, interruptor en Ajustes):** cada dibujo se gira 90° en su hueco si así ocupa más superficie (umbral 8 %), sin deformar nunca su proporción. Ej.: un dibujo vertical en media hoja apaisada se ve un 79 % más grande.

* **v3.2.0 (07-11-2026) — Descarga en Word:**
  * Botón «📄 Descargar Word»: genera en el navegador (sin librerías) un `.docx` con las imágenes incrustadas, para revisar el libro en un procesador de texto. Reproduce lo que se ve en pantalla: portada, dibujos por hoja, línea de corte, giros (aplicados a los píxeles), tamaño de hoja, márgenes y pie «Página X de Y». Imágenes JPEG a ~200 ppp; las repetidas se incrustan una sola vez.
  * Requiere abrir la app con Live Server (http): con doble clic (`file://`) el navegador no permite leer las imágenes; la app lo avisa.
  * Validado: abre en LibreOffice y produce las mismas 7 páginas que la vista en pantalla con los 11 dibujos de prueba.

* **v3.3.0 (08-11-2026) — Márgenes de 2 cm por pieza de corte y recorte del blanco:**
  * Nuevo margen por defecto «Libro para recortar (2 cm)». Cada dibujo ocupa su celda física de la hoja (entera, mitad o cuarto) menos 2 cm por cada lado: 2 cm hasta los bordes del papel y 2 cm a cada lado de la línea de corte, que va en el centro exacto. Al cortar, cada media hoja queda con 2 cm de margen alrededor de su dibujo. Los ajustes guardados antes de este cambio pasan al nuevo margen (`ajustesVersion: 2`).
  * Misma geometría (`geometriaHoja`) en pantalla, impresión y Word. En Word se usan tablas con filas de alto exacto y la línea de corte es un borde discontinuo en el centro.
  * Se recorta automáticamente el blanco sobrante de cada imagen (en pantalla con `object-view-box`; en Word al dibujar en el canvas), para que sea el dibujo y no el blanco del archivo lo que llega a los 2 cm. Requiere Live Server; con doble clic se usa la imagen entera.
  * Medido en LibreOffice (Carta, 2 por hoja): dibujos a 20,4 / 20,6 mm (arriba / hasta el corte) y 19,9 / 20,7 mm (desde el corte / abajo). Con dibujos 4:3, el alto (99,7 mm por media hoja) limita el tamaño, por lo que a los lados quedan 34–46 mm.

* **v3.4.0 (08-11-2026) — Dibujos estirados a 1 cm, sin portada ni numeración:**
  * **Estirar a los márgenes** (activado por defecto, interruptor «↔️ Estirar a los márgenes» en Ajustes): cada dibujo llena todo su hueco, aunque cambie su proporción. Con el estiramiento, el giro automático elige la orientación que menos deforma.
  * Margen «Libro para recortar» bajado a **1 cm** (bordes del papel y a cada lado de la línea de corte). Medido en LibreOffice (Carta, 2 por hoja): dibujos de 195,5 × 118,9 mm a 10,2–10,7 mm de los bordes y a 9,9–10,6 mm del corte.
  * Se quitó la numeración de página (pantalla, impresión y Word) y los símbolos ✂️/«Cortar»: solo queda la línea punteada.
  * Portada desactivada por defecto (`ajustesVersion: 3` la desactiva también en ajustes guardados); el interruptor «Portada» sigue disponible.

* **v3.5.0 (08-11-2026) — Marco negro en cada dibujo:**
  * Cada dibujo lleva un marco de línea negra de 0,5 mm (`GROSOR_MARCO_MM`) que lo rodea exactamente, también si se desactiva «Estirar» y el dibujo conserva su proporción. Interruptor «🖼️ Marco» en Ajustes (activado por defecto).
  * En pantalla/impresión es un `outline` escalado al papel con unidades de contenedor; en Word es el contorno de la imagen (`a:ln`). Verificado en LibreOffice.

* **v3.6.0 (11-11-2026) — Orden de carpetas: referencias y bandeja de imágenes nuevas:**
  * `uploadimages/` y `uploadimages_copia/` (20 archivos, solo 6 imágenes distintas) se reemplazan por `referencias/` con las 5 hojas de `pintar.pptx` con nombres claros («Hoja 1 - Jesús nació y Espíritu Santo guíame.png»…); se conserva la versión corregida de la Hoja 1. Las copias se enviaron a la Papelera.
  * Nueva carpeta `imagenes_nuevas/`: bandeja donde el usuario deja imágenes para que Claude las clasifique, quite duplicados, renombre e integre en `biblioteca/`. Su contenido está en `.gitignore` (solo se sube su `LEEME.txt`).

---

## 8. Guía Estilística Oficial de Trazos y Composiciones (Benchmark Referencial)

A partir de las láminas oficiales proporcionadas en `uploadimages`, se establecen las directrices obligatorias de diseño para todo el arte del proyecto:

### 8.1. Reglas de Trazo (Line Art)
1. **Grosor Definido y Continuo:**
   - Contornos principales con línea gruesa y uniforme (~3.5 pt a 4.5 pt).
   - Detalles internos (pliegues de túnicas, rasgos, destellos) con línea media (~2.0 pt a 2.5 pt).
   - Cero líneas "peludas", trazos temblorosos o bocetos inconclusos; cada línea debe ser firme y nítida.
2. **Formas 100% Cerradas y Redondeadas:**
   - Todos los caminos vectoriales cierran en sí mismos (polígonos cerrados).
   - Ausencia total de fugas: cualquier área debe poder rellenarse con la herramienta cubo de pintura digital sin desbordarse.
   - Esquinas y empalmes redondeados (`stroke-linecap="round"`, `stroke-linejoin="round"`).
3. **Rostros Humanos, Tiernos y Expresivos (Estilo Chibi / Pastoral Infantil):**
   - **Ojos:** Grandes, circulares u ovalados, pupilas negras con 1 o 2 brillos circulares blancos interiores.
   - **Cejas:** Arcos suaves y relajados que denotan paz, dulzura, alegría o recogimiento espiritual.
   - **Boca:** Sonrisa dulce arqueada hacia arriba o boca abierta sonriente con lengüita.
   - **Manos:** Dedos redondeados y claramente diferenciados en gestos naturales (oración, abrazo, bendición).
4. **Cero Tramas ni Texturas de Sombreado:**
   - Ningún dibujo debe contener achurados, líneas de sombreado, punteados de dithering ni medios tonos.
   - El 100% del interior de las figuras debe ser blanco puro `#FFFFFF` para colorear fácilmente con 8 colores en 30-40 minutos.

### 8.2. Reglas de Composición y Diagramación
1. **Título Superior en Letras Huecas ("Bubble Letters"):**
   - Cada lámina debe coronarse con un lema breve (1 o 2 líneas) en mayúsculas contorneadas huecas con interior blanco.
   - Las letras deben ser gruesas y redondeadas para que el niño también pueda colorearlas como parte de la actividad catequética.
2. **Distribución del Espacio:**
   - **Personaje o escena principal:** Ocupa el tercio central e inferior (65% al 75% del área total).
   - **Espacios negativos equilibrados:** Los huecos libres a los costados y en la parte superior se armonizan con motivos complementarios:
     - Celestes: Corazones flotantes (`♡`), estrellitas de 5 puntas (`★`), nubes mullidas (`☁`), rayos de luz rectos simples.
     - Terrestres: Flores tipo margarita de 5 pétalos (`✿`), pequeños mechones de hierba (`m`) en el suelo.
3. **Proporción de Lámina:**
   - Proporción vertical aproximada de 3:4 o 2:3 (ancho entre 480 y 512 px, alto entre 640 y 700 px).
   - Diseñadas para llenar exactamente los márgenes de una hoja Carta en vertical, o emparejarse en 2 láminas por hoja con línea de corte central.

---

## 9. Próximas Mejoras Planificadas (Roadmap)

- [ ] Modo Folleto / Cuadernillo con plegado central (imposición de páginas para engrapar en el lomo tipo revista).
- [ ] Opciones de estilos de marco para los dibujos (marcos barrocos, florales, sencillos, esquinas góticas).
- [ ] Exportación directa a documento Word (`.docx`) además de PDF e impresión.
- [ ] Más colecciones temáticas (Adviento y Navidad, Cuaresma y Pascua, Santos Patronos de América y España).

