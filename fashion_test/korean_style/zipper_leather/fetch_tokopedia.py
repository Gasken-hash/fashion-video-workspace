"""Fetch Tokopedia product page with Chrome impersonation (curl-cffi)
and extract all product image URLs. No browser used."""
import re, json, sys
from curl_cffi import requests

URL = "https://vt.tokopedia.com/t/ZS9fQ4E2wY1NS-4HREi/"
hdr = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}

s = requests.Session(impersonate="chrome")
r = s.get(URL, headers=hdr, timeout=60, allow_redirects=True)
print("final_url:", r.url[:200])
print("status:", r.status_code, "len:", len(r.text))
open("/tmp/tokopedia_cffi.html", "w").write(r.text)

html = r.text
# 1) look for captcha
if "captcha" in html.lower() or "Security Check" in html:
    print("CAPTCHA/BLOCKED: page is a security check")
# 2) find ibyteimg image urls
imgs = sorted(set(re.findall(r'https://[a-z0-9\-]+\.ibyteimg\.com[^"\'\\ ]+', html)))
print("ibyteimg urls found:", len(imgs))
for u in imgs[:40]:
    print("IMG:", u[:220])
# 3) find product-image-ish json blobs (tokopedia embeds data)
m = re.findall(r'"(imageUrl|image_url|thumbnail|original)"\s*:\s*"([^"]+)"', html)
print("json image fields:", len(m))
for k, v in m[:20]:
    print("JF:", k, v[:180])
# 4) title
t = re.search(r'<title>(.*?)</title>', html, re.S)
print("title:", t.group(1)[:150] if t else None)
