from PIL import Image

src = Image.open("walk_grid_src.png").convert("RGB")
W, H = src.size
COLS, ROWS = 4, 2
N = COLS*ROWS

def alpha_of(cell):
    g = cell.convert("L")
    # branco -> transparente; tinta preta -> opaca (com corte do quase-branco)
    a = g.point(lambda v: 0 if v > 228 else min(255, int((255 - v - 22) * 1.7)))
    return a

figs = []
for r in range(ROWS):
    for c in range(COLS):
        x0 = round(c * W / COLS); x1 = round((c+1) * W / COLS)
        y0 = round(r * H / ROWS); y1 = round((r+1) * H / ROWS)
        # ignora 4px de borda da célula (evita linha/sujeira de borda)
        cell = src.crop((x0+4, y0+4, x1-4, y1-4))
        a = alpha_of(cell)
        bbox = a.getbbox()
        if bbox is None:
            continue
        rgba = cell.convert("RGBA"); rgba.putalpha(a)
        fig = rgba.crop(bbox)
        figs.append(fig)

assert len(figs) == N, f"esperava {N} figuras, achei {len(figs)}"

maxW = max(f.width for f in figs)
maxH = max(f.height for f in figs)
padX, padTop, padBot = 16, 10, 3
fw = maxW + 2*padX
fh = maxH + padTop + padBot

strip = Image.new("RGBA", (fw*N, fh), (0,0,0,0))
for i, fig in enumerate(figs):
    x = i*fw + (fw - fig.width)//2          # centraliza horizontal
    y = fh - padBot - fig.height            # alinha os pés na base
    strip.paste(fig, (x, y), fig)

strip.save("walk.png")
print(f"FRAMES={N} FW={fw} FH={fh}  (folha {strip.width}x{strip.height})")
