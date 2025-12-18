import sys
from pathlib import Path

nombre = sys.argv[1] if len(sys.argv) > 1 else "Miriam Arias"
fichero = sys.argv[2] if len(sys.argv) > 2 else ""

print(f"Hola mundo soy {nombre}")

if fichero:
    p = Path(fichero)
    if p.exists():
        texto = p.read_text(encoding="utf-8", errors="replace")
        print(f"Archivo leído: {p.name}")
        print(f"Caracteres: {len(texto)}")
        print("Primeras líneas:")
        for line in texto.splitlines()[:5]:
            print(line)
    else:
        print(f"ERROR: no existe el archivo '{fichero}'")
        sys.exit(2)
else:
    print("No se ha subido ningún archivo.")
