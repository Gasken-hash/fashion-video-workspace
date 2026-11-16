"""Extract Tokopedia product gallery from the fetched HTML (curl-cffi).
Downloads the 800x800 product images, deduped by image hash."""
import re, os, html
from curl_cffi import requests

OUT = os.path.expanduser("~/workspace/fashion_test/korean_style/zipper_leather/tokopedia")
os.makedirs(OUT, exist_ok=True)

page = open("/tmp/tokopedia_cffi.html", encoding="utf-8", errors="ignore").read()
print("page bytes:", len(page))

# all ibyteimg urls, unescape &amp;
raw = sorted(set(re.findall(r'https://[a-z0-9\-]+\.ibyteimg\.com[^"\'\\ ]+', page)))
urls = [html.unescape(u) for u in raw]
print("total ibyteimg:", len(urls))

# product gallery = 800x800 webp in the product buckets, skip badges/avatars
def is_product(u):
    if "power_shop" in u: return False
    if "resize-jpeg:300:300" in u: return False
    if "resize-webp:260:260" in u: return False
    if "resize-webp:800:800" not in u: return False
    return True

prod = [u for u in urls if is_product(u)]
# dedupe by image hash (the hex id before ~tplv)
seen = {}
for u in prod:
    m = re.search(r'/([0-9a-f]{32})~', u)
    key = m.group(1) if m else u
    seen.setdefault(key, u)
prod = sorted(seen.values())
print("product images (unique hashes):", len(prod))
for u in prod:
    print("P:", u[:160])

# download each at 800x800
s = requests.Session(impersonate="chrome")
for i, u in enumerate(prod):
    m = re.search(r'/([0-9a-f]{32})~', u)
    h = m.group(1)[:12] if m else f"img{i}"
    fn = os.path.join(OUT, f"tok_{i:02d}_{h}.jpg")
    r = s.get(u, timeout=60)
    open(fn, "wb").write(r.content)
    print("saved", fn, len(r.content), "bytes", r.status_code)

# also try to find variant / color names in the page
for pat in [r'"variant[^"]*"\s*:', r'Warna', r'warna', r'"color[^"]*"\s*:']:
    hits = re.findall(pat, page)
    print(pat, "->", len(hits))
# print a snippet around 'variant' if present
idx = page.lower().find("varian")
print("varian idx:", idx)
if idx > 0:
    print(page[max(0, idx-200):idx+800][:1000])
