from PIL import Image

fnames = ['certificate-iso-9001.png', 'certificate-as9100d.png']
for fname in fnames:
    img = Image.open('img/' + fname)
    dpi = img.info.get('dpi', 'N/A')
    print(f"{fname}: size={img.size} mode={img.mode} dpi={dpi}")
