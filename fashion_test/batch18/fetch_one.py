import json, re, os, html, sys
from curl_cffi import requests
tag = sys.argv[1]
d = json.load(open('/home/hatch/workspace/fashion_test/batch18/products.json'))
p = [x for x in d if x['tag']==tag][0]
out = f'/home/hatch/workspace/fashion_test/batch18/{tag}'
os.makedirs(out, exist_ok=True)
hdr = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
       "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
s = requests.Session(impersonate="chrome")
r = s.get(p['shortlink'], headers=hdr, timeout=60, allow_redirects=True)
page = r.text
print("page len:", len(page), "captcha:", ("captcha" in page.lower() or "Security Check" in page))
raw = sorted(set(re.findall(r'https://[a-z0-9\-]+\.ibyteimg\.com[^"\'\\ ]+', page)))
urls = [html.unescape(u) for u in raw]
def is_product(u):
    if "power_shop" in u: return False
    if "resize-jpeg:300:300" in u: return False
    if "resize-webp:260:260" in u: return False
    if "resize-webp:800:800" not in u: return False
    return True
prod = [u for u in urls if is_product(u)]
seen = {}
for u in prod:
    m = re.search(r'/([0-9a-f]{32})~', u)
    key = m.group(1) if m else u
    seen.setdefault(key, u)
prod = sorted(seen.values())
print("product imgs:", len(prod))
n = 0
for u in prod[:12]:
    try:
        rr = s.get(u, timeout=40)
        if rr.status_code == 200 and len(rr.content) > 8000:
            open(os.path.join(out, f'tok_{n:02d}.bin'), 'wb').write(rr.content)
            n += 1
    except Exception as e:
        print("dl err:", e)
print("downloaded:", n)
