"""
Render the article markdown to a clean, readable HTML (images embedded as base64),
ready to print to PDF via headless Chromium. Strips the HTML front-matter comment.
"""
import base64
import mimetypes
import re
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent.parent  # article dir
MD = HERE / "dev-workflow-blueprint.md"
OUT_HTML = HERE / "dev-workflow-blueprint.print.html"

text = MD.read_text(encoding="utf-8")

# drop the leading <!-- ... --> front-matter block (metadata, not body)
text = re.sub(r"^<!--.*?-->\s*", "", text, count=1, flags=re.DOTALL)

# convert markdown -> html body
html_body = markdown.markdown(
    text, extensions=["extra", "sane_lists", "tables", "smarty"]
)


# inline every local image as base64 so the PDF is self-contained
def embed(match):
    alt, src = match.group(1), match.group(2)
    p = (HERE / src).resolve()
    if not p.exists():
        return match.group(0)
    mime = mimetypes.guess_type(str(p))[0] or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f'<img alt="{alt}" src="data:{mime};base64,{b64}">'


html_body = re.sub(r'<img alt="([^"]*)" src="([^"]+)"\s*/?>', embed, html_body)

CSS = """
@page { size: A4; margin: 22mm 20mm; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 11.5pt; line-height: 1.62; color: #1a1a1a;
  max-width: 100%; margin: 0;
}
h1 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 23pt;
     line-height: 1.2; margin: 0 0 6pt; color: #0f1a2b; }
h2 { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 15pt;
     margin: 24pt 0 6pt; color: #0f1a2b; border-bottom: 1px solid #e3e8ef;
     padding-bottom: 4pt; }
h1 + p em, body > p:first-of-type em { color: #55627a; }
p { margin: 0 0 10pt; }
em { color: #55627a; }
img { max-width: 100%; max-height: 150mm; height: auto; width: auto;
      display: block; margin: 14pt auto 4pt; border: 1px solid #eaedf2;
      border-radius: 4px; page-break-inside: avoid; }
img + em, p > em:only-child { display: block; text-align: center;
      font-size: 9.5pt; color: #77839b; margin-bottom: 12pt; }
blockquote { margin: 12pt 0; padding: 6pt 0 6pt 14pt;
      border-left: 3px solid #9aa544; color: #33404f; background: #fafbf5; }
blockquote p { margin: 4pt 0; }
code { font-family: "SF Mono", Consolas, monospace; font-size: 10pt;
      background: #f3f5f8; padding: 1px 4px; border-radius: 3px; color: #b34; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; margin: 12pt 0; }
th, td { border: 1px solid #dfe4ec; padding: 6px 9px; text-align: left;
      vertical-align: top; }
th { background: #f3f5f8; font-family: "Helvetica Neue", Arial, sans-serif; }
ul, ol { margin: 0 0 10pt; padding-left: 20pt; }
li { margin: 3pt 0; }
h2 { page-break-after: avoid; }
img { page-break-inside: avoid; }
a { color: #245a80; text-decoration: none; }
"""

doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>A Simple Blueprint for Building Software with AI Agents</title>
<style>{CSS}</style></head><body>
{html_body}
</body></html>"""

OUT_HTML.write_text(doc, encoding="utf-8")
print(f"wrote {OUT_HTML}")
