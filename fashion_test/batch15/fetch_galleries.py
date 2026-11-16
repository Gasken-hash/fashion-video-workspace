import json, re, os, html
from curl_cffi import requests

prods = json.load(open('/home/hatch/workspace/fashion_test/batch15/products.json'))
tags = ["02","03","04","05","07","08","09","10","11_kiyana","12_sweater_kotak","13_aqila","14_kickchick","15_chicmore_garis","17_chicmore_pita"]
base = '/home/hatch/workspace/fashion_test/batch15'
hdr = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
       "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
for tag in tags:
    p = prods[tag]
    d = os.path.join(base, tag)
    os.makedirs(d, exist_ok=True)
    short = p['short']
    try:
        s = requests.Session(impersonate="chrome")
        r = s.get(short, headers=hdr, timeout=60, allow_redirects=True)
        page = r.text
        if "captcha" in page.lower() or "Security Check" in page:
            print(tag, "| BLOCKED/CAPTCHA len", len(page), flush=True)
            continue
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
        print(tag, "|", (p.get('title') or '?')[:45], "| product imgs:", len(prod), "| page len:", len(page), flush=True)
        n = 0
        for u in prod[:12]:
            try:
                rr = s.get(u, timeout=40)
                if rr.status_code == 200 and len(rr.content) > 8000:
                    open(os.path.join(d, f'tok_{n:02d}.bin'), 'wb').write(rr.content)
                    n += 1
            except Exception:
                pass
        print(tag, "| downloaded:", n, flush=True)
    except Exception as e:
        print(tag, "| ERROR:", e, flush=True)
print("DONE")
