from PIL import Image
import os

SCALE = 4   # 4x upscale: 558 -> ~2232, 542 -> ~2168 (near 4K width)

fnames = [
    'certificate-iso-9001.png',
    'certificate-as9100d.png',
]

img_dir = 'img'

for fname in fnames:
    in_path = os.path.join(img_dir, fname)
    img = Image.open(in_path).convert('RGBA')
    w, h = img.size
    new_w = w * SCALE
    new_h = h * SCALE
    print(f"Upscaling {fname}: {w}x{h} -> {new_w}x{new_h} ...")
    upscaled = img.resize((new_w, new_h), Image.LANCZOS)
    out_path = os.path.join(img_dir, fname)
    upscaled.save(out_path, 'PNG', optimize=False, compress_level=1)
    new_size = os.path.getsize(out_path)
    print(f"  Saved {out_path}: {new_size/1024:.0f} KB")

print("Done.")
