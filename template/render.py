"""Crea le slide dei post (1080x1350, formato Instagram 4:5) con lo stile approvato.

Uso:  python3 template/render.py post.json
Il file JSON descrive il post, per esempio:

{
  "nome": "2026-11-19-camere",
  "slide": [
    {"tipo": "copertina", "foto": "foto/camere/camera-letto-finestra-palazzo-01.jpg",
     "posizione": "60% 50%", "titolo": "Your room, our care", "sottotitolo": "La tua camera, la nostra cura."},
    {"tipo": "interna", "foto": "foto/camere/camera-letto-scrivania-poltrona-01.jpg",
     "posizione": "55% 50%", "titolo": "Your room",
     "testo_en": "Soft fabrics, warm light ...", "testo_it": "Tessuti morbidi, luce calda ..."}
  ]
}

"posizione" sposta il ritaglio della foto (come object-position in CSS: "orizzontale verticale").
Le immagini escono in grafiche/<nome>-<n>.jpg. Le regole di stile sono in BRAND.md.
"""
import html
import json
import pathlib
import shutil
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "template" / "fonts"
LOGO = ROOT / "brand" / "logo-scuro.svg"
HEART = ('<svg width="36" height="33" viewBox="0 0 24 22" style="position:relative;top:2px">'
         '<path fill="#D4A600" d="M12 21.6 10.3 20C4.2 14.5 0 10.7 0 6.1 0 2.5 2.8 0 6.3 0c2 0 3.9.9 5.7 2.6'
         'C13.8.9 15.7 0 17.7 0 21.2 0 24 2.5 24 6.1c0 4.6-4.2 8.4-10.3 13.9z"/></svg>')

CSS = f"""
@font-face{{font-family:'Cormorant Garamond';src:url('{(FONTS / "CormorantGaramond[wght].ttf").as_uri()}');font-weight:300 700}}
@font-face{{font-family:'Cormorant Garamond';src:url('{(FONTS / "CormorantGaramond-Italic[wght].ttf").as_uri()}');font-weight:300 700;font-style:italic}}
@font-face{{font-family:'Jost';src:url('{(FONTS / "Jost[wght].ttf").as_uri()}');font-weight:100 900}}
body{{margin:0}}
.p{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#2A2018;font-family:'Jost',sans-serif}}
.p>img.f{{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}}
.banda{{position:absolute;left:0;top:44px;width:1080px;height:200px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center;background:rgba(250,246,239,0.58)}}
.banda .n{{font-weight:500;font-size:22px;letter-spacing:.3em;margin-left:.3em;color:#2B1D13;margin-top:14px}}
.banda .r{{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:25px;letter-spacing:.05em;color:#2B1D13;margin-top:4px}}
.scuro{{position:absolute;left:0;bottom:0;width:1080px;background:linear-gradient(0deg,rgba(34,25,17,.80) 0%,rgba(34,25,17,.5) 55%,rgba(34,25,17,0) 100%)}}
.giu{{position:absolute;left:110px;bottom:84px;width:860px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.tit{{display:flex;align-items:baseline;gap:16px;font-family:'Cormorant Garamond',serif;font-weight:500;line-height:1.05;color:#FAF6EF}}
.it{{font-family:'Cormorant Garamond',serif;font-style:italic;color:#E8D5A3}}
.en{{font-size:26px;line-height:1.45;color:#FAF6EF;margin-top:22px}}
"""


def esc(t):
    return html.escape(t or "")


def slide_html(s):
    foto = (ROOT / s["foto"]).as_uri()
    pos = esc(s.get("posizione", "50% 50%"))
    if s["tipo"] == "copertina":
        return f"""<div class="p"><img class="f" src="{foto}" style="object-position:{pos}">
<div class="banda"><img src="{LOGO.as_uri()}" style="width:64px;height:70px">
<div class="n">LES CHAMBRES D'OR</div><div class="r">Hotel • Suite • Apartament</div></div>
<div class="scuro" style="height:520px"></div>
<div class="giu" style="left:0;width:1080px"><div class="tit" style="font-size:78px">{esc(s['titolo'])}{HEART}</div>
<div class="it" style="font-size:40px;margin-top:10px">{esc(s.get('sottotitolo'))}</div></div></div>"""
    return f"""<div class="p"><img class="f" src="{foto}" style="object-position:{pos}">
<div class="scuro" style="height:640px"></div>
<div class="giu"><div class="tit" style="font-size:84px">{esc(s['titolo'])}{HEART}</div>
<div class="en">{esc(s.get('testo_en'))}</div>
<div class="it" style="font-size:31px;line-height:1.35;margin-top:18px">{esc(s.get('testo_it'))}</div></div></div>"""


def main(spec_path):
    spec = json.loads(pathlib.Path(spec_path).read_text())
    out_dir = ROOT / "grafiche"
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    outs = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=chrome, args=["--allow-file-access-from-files"]) if chrome \
            else pw.chromium.launch(args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        tmp = ROOT / "template" / ".slide.html"
        for i, s in enumerate(spec["slide"], 1):
            tmp.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
                           f"<body>{slide_html(s)}</body></html>")
            pg.goto(tmp.as_uri())
            pg.wait_for_load_state("networkidle")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(300)
            png = out_dir / f".{spec['nome']}-{i}.png"
            pg.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            from PIL import Image
            jpg = out_dir / f"{spec['nome']}-{i}.jpg"
            Image.open(png).convert("RGB").save(jpg, quality=92, optimize=True)
            png.unlink()
            outs.append(str(jpg.relative_to(ROOT)))
        tmp.unlink(missing_ok=True)
        b.close()
    print("\n".join(outs))


if __name__ == "__main__":
    main(sys.argv[1])
