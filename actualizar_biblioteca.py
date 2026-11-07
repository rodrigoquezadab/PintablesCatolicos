"""
Actualiza la lista de imágenes de la biblioteca de Pintables Católicos.

Recorre la carpeta  biblioteca/  (incluidas sus subcarpetas, que se usan como categorías)
y escribe  biblioteca/biblioteca.js , que la aplicación (index.html) lee al abrirse.

Uso: doble clic en  actualizar_biblioteca.bat   (o:  python actualizar_biblioteca.py)
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BIBLIOTECA = RAIZ / "biblioteca"
SALIDA = BIBLIOTECA / "biblioteca.js"
EXTENSIONES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".svg"}


def orden_natural(texto):
    """'lamina 2' antes que 'lamina 10'."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", texto)]


def titulo_desde_nombre(nombre):
    t = Path(nombre).stem
    t = re.sub(r"^\d+[\s._-]*", "", t) or Path(nombre).stem  # quita numeración inicial: "01_..."
    t = re.sub(r"_+", " ", t)
    t = re.sub(r"(?<! )-+(?! )", " ", t).strip()  # "dibujo-de-x" -> "dibujo de x"; " - " se conserva
    return t[:1].upper() + t[1:]


def main():
    BIBLIOTECA.mkdir(exist_ok=True)
    archivos = sorted(
        (p for p in BIBLIOTECA.rglob("*") if p.is_file() and p.suffix.lower() in EXTENSIONES),
        key=lambda p: orden_natural(str(p.relative_to(BIBLIOTECA))),
    )
    imagenes = []
    for p in archivos:
        rel = p.relative_to(RAIZ).as_posix()
        carpeta = p.parent.relative_to(BIBLIOTECA).as_posix()
        imagenes.append({
            "archivo": rel,
            "titulo": titulo_desde_nombre(p.name),
            "categoria": "" if carpeta == "." else carpeta.replace("/", " / "),
        })

    datos = {"generado": datetime.now().strftime("%d-%m-%Y %H:%M"), "imagenes": imagenes}
    SALIDA.write_text(
        "// Archivo generado por actualizar_biblioteca.py — no editar a mano.\n"
        "window.BIBLIOTECA = " + json.dumps(datos, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )
    categorias = sorted({i["categoria"] for i in imagenes if i["categoria"]})
    print(f"Biblioteca actualizada: {len(imagenes)} imagenes"
          + (f" en {len(categorias)} carpetas" if categorias else ""))
    print(f"Lista guardada en: {SALIDA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
