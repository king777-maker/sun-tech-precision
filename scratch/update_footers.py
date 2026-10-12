import glob
import os

target = '''                <div class="col-lg-3 col-md-6">
                    <h5 class="text-white mb-4">Quality &amp; Certification</h5>
                    <p class="small text-light mb-4" style="line-height: 1.6;">ISO 9001:2015 &amp; AS9100D Certified Organization providing high-precision CNC machining, inspection, and finishing for demanding engineering applications.</p>
                    <a href="contact.html#quote" class="btn btn-primary py-2 px-4">Get A Quote</a>
                </div>'''

replacement = '''                <div class="col-lg-3 col-md-6">
                    <h5 class="text-white mb-4">Quality &amp; Certification</h5>
                    <a href="quality.html" class="footer-cert-badge" title="View AS9100D Quality Certificate">
                        <img src="img/as9100d-logo.svg" alt="AS9100D Certified Logo">
                    </a>
                    <p class="small text-light mb-4" style="line-height: 1.6;">ISO 9001:2015 &amp; AS9100D Certified Organization providing high-precision CNC machining, inspection, and finishing for demanding engineering applications.</p>
                    <a href="contact.html#quote" class="btn btn-primary py-2 px-4">Get A Quote</a>
                </div>'''

html_files = glob.glob(r'c:\Users\ADMIN\Desktop\part-time\*.html')
count = 0

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {os.path.basename(file_path)}")
    else:
        print(f"Target not matched in {os.path.basename(file_path)}")

print(f"Total files updated: {count}")
