import json, re, urllib.parse
from curl_cffi import requests

links = [
 ("01_tanktop", "https://vt.tokopedia.com/t/ZS9fqPBmffLDQ-l9Ac9/"),
 ("02_bianca", "https://vt.tokopedia.com/t/ZS9fq5YS9gamP-kJu0G/"),
 ("03_batik", "https://vt.tokopedia.com/t/ZS9fbwVs5Ct7o-ktzYB/"),
 ("04_lunelly", "https://vt.tokopedia.com/t/ZS9fbw3MSvYYx-KA1aa/"),
 ("05_kaos_hati", "https://vt.tokopedia.com/t/ZS9fbK6wTc9Pb-caiAZ/"),
 ("06_moka", "https://vt.tokopedia.com/t/ZS9fbKPfBe2We-lRuJu/"),
 ("07_yola", "https://vt.tokopedia.com/t/ZS9fbK4J1bFRg-gAhgh/"),
 ("08_rompi_rajut", "https://vt.tokopedia.com/t/ZS9fbE6bLQ7co-QJ3V5/"),
 ("09_lucy", "https://vt.tokopedia.com/t/ZS9fbEH24kAVt-ZuY22/"),
 ("10_hailey", "https://vt.tokopedia.com/t/ZS9fbEsoPXUHf-ZFkiz/"),
]

out = {}
for tag, url in links:
    try:
        s = requests.Session(impersonate="chrome")
        r = s.get(url, timeout=30, allow_redirects=True)
        final = r.url
        title = None; img = None
        m = re.search(r'og_info=([^&]+)', final)
        if m:
            try:
                og = json.loads(urllib.parse.unquote(m.group(1)))
                title = og.get('title')
                img = og.get('image')
            except Exception as e:
                title = f"og_parse_fail:{e}"
        if not title:
            m2 = re.search(r'<meta property="og:title" content="([^"]+)"', r.text)
            if m2: title = m2.group(1)
        if not img:
            m3 = re.search(r'<meta property="og:image" content="([^"]+)"', r.text)
            if m3: img = m3.group(1)
        pid = re.search(r'/product/(\d+)', final)
        out[tag] = {"short": url, "final": final, "product_id": pid.group(1) if pid else None, "title": title, "image": img, "status": r.status_code}
        print(tag, "|", pid.group(1) if pid else "?", "|", (title or "?")[:90], flush=True)
    except Exception as e:
        out[tag] = {"short": url, "error": str(e)}
        print(tag, "| ERROR:", e, flush=True)

json.dump(out, open('/home/hatch/workspace/fashion_test/batch16/products.json','w'), indent=1, ensure_ascii=False)
print("saved products.json")
