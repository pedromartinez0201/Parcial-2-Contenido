"""Genera los SVG de uml-*.puml con PlantUML y los incrusta en Simulador Parcial 2.html.

Uso: python3 armar-diagramas.py
La ruta del .jar se puede cambiar con la variable de entorno PLANTUML_JAR.
"""
import json, os, re, subprocess, tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
HTML = AQUI.parent / 'Simulador Parcial 2.html'
JAR = os.environ.get('PLANTUML_JAR', str(Path.home() / '.var/app/com.visualstudio.code/data/vscode/extensions/jebbs.plantuml-2.18.1/plantuml.jar'))

fuentes = sorted(AQUI.glob('uml-*.puml'))
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(['java', '-Djava.awt.headless=true', '-jar', JAR, '-tsvg', '-o', tmp, *map(str, fuentes)], check=True)
    diagramas = {}
    for f in fuentes:
        svg = (Path(tmp) / (f.stem + '.svg')).read_text(encoding='utf-8')
        svg = re.sub(r'<\?xml[^>]*\?>', '', svg).strip()
        ancho = re.search(r'viewBox="0 0 (\d+)', svg).group(1)
        # Ancho fluido hasta el tamaño natural, para que se lea en el celular con scroll horizontal.
        svg = re.sub(r'<svg [^>]*?(viewBox="[^"]*")[^>]*>',
                     lambda m: f'<svg xmlns="http://www.w3.org/2000/svg" {m.group(1)} role="img" style="display:block;width:100%;min-width:{min(int(ancho), 560)}px;max-width:{ancho}px;height:auto;margin:0 auto">',
                     svg, count=1)
        diagramas[f.stem.removeprefix('uml-')] = svg

html = HTML.read_text(encoding='utf-8')
bloque = '/*DIAGRAMS:BEGIN*/const DIAGRAMS=' + json.dumps(diagramas, ensure_ascii=False).replace('</', '<\\/') + ';/*DIAGRAMS:END*/'
html, n = re.subn(r'/\*DIAGRAMS:BEGIN\*/.*?/\*DIAGRAMS:END\*/', lambda _: bloque, html, flags=re.S)
if n != 1:
    raise SystemExit('No se encontró el marcador DIAGRAMS en el HTML')
HTML.write_text(html, encoding='utf-8')
print(f'{len(diagramas)} diagramas incrustados: {", ".join(diagramas)}')
