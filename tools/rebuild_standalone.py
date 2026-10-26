#!/usr/bin/env python3
"""Reconstrói o HTML autônomo publicado em 18 segmentos. Sem dependências."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
parts = sorted((root / "payload").glob("part-*.txt"))
assert len(parts) == 18, f"Esperados 18 segmentos; encontrados {len(parts)}."
text = "".join(p.read_text(encoding="utf-8") for p in parts)
assert text.startswith("<!doctype html>") and text.endswith("</body></html>")
output = root / "Observatorio_Brasil_2026_Standalone.html"
output.write_text(text, encoding="utf-8")
print(f"Gerado: {output} ({output.stat().st_size:,} bytes)")
