import glob
import re

new_footer = """    <!-- Footer Start -->
    <div class="container-fluid bg-dark footer mt-5 pt-5 pb-3 wow fadeIn" data-wow-delay="0.1s">
        <div class="container py-4">
            <div class="row g-5">
                <div class="col-lg-3 col-md-6">
                    <h5 class="text-white mb-4">Sun Tech Precision</h5>
                    <div class="d-flex mb-3">
                        <i class="fa fa-map-marker-alt me-3 mt-1 text-primary"></i>
                        <span class="small">#685, 5&amp;6 Thigalarapalya Main Rd, Peenya 2nd Stage, Bengaluru, Karnataka 560058</span>
                    </div>
                    <div class="d-flex mb-3">
                        <i class="fa fa-phone-alt me-3 mt-1 text-primary"></i>
                        <a href="tel:+919964537822" class="text-white small">+91 9964537822</a>
                    </div>
                    <div class="d-flex mb-3">
                        <i class="fa fa-envelope me-3 mt-1 text-primary"></i>
                        <a href="mailto:sales@suntechprecision.com" class="text-white small text-break">sales@suntechprecision.com</a>
                    </div>
                    <div class="d-flex pt-2">
                        <a class="btn btn-square btn-primary rounded-circle me-2" href="https://wa.me/919964537822" target="_blank" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
                        <a class="btn btn-square btn-primary rounded-circle me-2" href="mailto:sales@suntechprecision.com" title="Email Us"><i class="fa fa-envelope"></i></a>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h5 class="text-white mb-4">Quick Links</h5>
                    <a class="btn btn-link" href="about.html">About Us</a>
                    <a class="btn btn-link" href="service.html">Capabilities</a>
                    <a class="btn btn-link" href="quality.html">Quality</a>
                    <a class="btn btn-link" href="gallery.html">Gallery</a>
                    <a class="btn btn-link" href="contact.html">Contact Us</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h5 class="text-white mb-4">Legal &amp; Policies</h5>
                    <a class="btn btn-link" href="supply-terms.html">Supply terms &amp; conditions</a>
                    <a class="btn btn-link" href="privacy-policy.html">Privacy policy</a>
                    <a class="btn btn-link" href="media-relations.html">Media relations</a>
                    <a class="btn btn-link" href="dpdp-policy.html">DPDP Act policy</a>
                    <a class="btn btn-link" href="terms-of-use.html">Terms Of Use</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h5 class="text-white mb-4">Quality &amp; Certification</h5>
                    <a href="quality.html" class="footer-cert-badge d-inline-block mb-3" title="AS9100D Certified">
                        <img src="img/as9100d-certified.png" alt="AS9100D Certified" class="img-fluid">
                    </a>
                    <p class="small text-light mb-0" style="line-height: 1.6;">ISO 9001:2015 &amp; AS9100D Certified Organization providing high-precision CNC machining, inspection, and finishing for demanding engineering applications.</p>
                </div>
            </div>
            <div class="row pt-4 mt-4 border-top border-secondary align-items-center justify-content-center text-center">
                <div class="col-12">
                    <a href="contact.html#quote" class="btn btn-primary py-3 px-5 rounded-pill fw-bold shadow-sm">Get A Quote <i class="fa fa-arrow-right ms-2"></i></a>
                </div>
            </div>
        </div>
    </div>
    <!-- Footer End -->"""

html_files = sorted(glob.glob("*.html"))
print(f"Found {len(html_files)} HTML files.")

for fname in html_files:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "<!-- Footer Start -->" not in content or "<!-- Footer End -->" not in content:
        print(f"ERROR: Missing footer comments in {fname}")
        continue
        
    updated_content = re.sub(
        r"<!-- Footer Start -->.*?<!-- Footer End -->",
        new_footer,
        content,
        flags=re.DOTALL
    )
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Updated {fname}")

print("All files updated successfully.")
