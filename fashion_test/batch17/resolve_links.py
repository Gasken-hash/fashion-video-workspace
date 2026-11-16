import json, re, time, urllib.parse
from curl_cffi import requests

links = [l.strip() for l in open('/home/hatch/workspace/fashion_test/batch17/links.txt') if l.strip()]

out = []
for i, url in enumerate(links, 1):
    tag = f"b17_{i:02d}"
    rec = {"tag": tag, "shortlink": url, "product_id": None, "name": None, "url": None}
    try:
        s = requests.Session(impersonate="chrome")
        r = s.get(url, timeout=30, allow_redirects=True)
        final = r.url
        rec["url"] = final
        title = None
        m = re.search(r'og_info=([^&]+)', final)
        if m:
            try:
                og = json.loads(urllib.parse.unquote(m.group(1)))
                title = og.get('title')
            except Exception:
                pass
        if not title:
            m2 = re.search(r'<meta property="og:title" content="([^"]+)"', r.text)
            if m2:
                title = m2.group(1)
        if not title:
            m2 = re.search(r'<title>([^<]+)</title>', r.text)
            if m2:
                title = m2.group(1).strip()
        pid = re.search(r'/product/(\d+)', final)
        if pid:
            rec["product_id"] = pid.group(1)
        rec["name"] = title
        rec["status"] = r.status_code
        if r.status_code != 200 or not pid:
            rec["error"] = f"status={r.status_code} pid={'found' if pid else 'missing'}"
        print(tag, "|", rec["product_id"] or "?", "|", (title or "?")[:100], flush=True)
    except Exception as e:
        rec["error"] = str(e)
        print(tag, "| ERROR:", e, flush=True)
    out.append(rec)
    time.sleep(0.6)

json.dump(out, open('/home/hatch/workspace/fashion_test/batch17/products.json', 'w'), indent=1, ensure_ascii=False)
ok = sum(1 for r in out if r.get("product_id"))
print(f"DONE ok={ok} fail={len(out)-ok}")
