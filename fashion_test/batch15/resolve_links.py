import json, re, urllib.parse
from curl_cffi import requests

links = [
 ("01_zipper", "https://vt.tokopedia.com/t/ZS9fQ4E2wY1NS-4HREi/"),
 ("02", "https://vt.tokopedia.com/t/ZS9fQg8G63srt-fzieY/"),
 ("03", "https://vt.tokopedia.com/t/ZS9fQg61vwAf6-ggOaF/"),
 ("04", "https://vt.tokopedia.com/t/ZS9fQgrHy3b16-u4DH0/"),
 ("05", "https://vt.tokopedia.com/t/ZS9fQgBHhqK3x-f3y31/"),
 ("06_dup05", "https://vt.tokopedia.com/t/ZS9fQgBHhqK3x-f3y31/"),
 ("07", "https://vt.tokopedia.com/t/ZS9fQg5tHesuy-LOtUG/"),
 ("08", "https://vt.tokopedia.com/t/ZS9fQg9YNQMmy-LXMkS/"),
 ("09", "https://vt.tokopedia.com/t/ZS9fQgXtqkSyQ-IeFbU/"),
 ("10", "https://vt.tokopedia.com/t/ZS9fQgc1c5aKm-x5BuH/"),
 ("11_kiyana", "https://vt.tokopedia.com/t/ZS9fQK5a5wHX3-qezMB/"),
 ("12_sweater_kotak", "https://vt.tokopedia.com/t/ZS9fQKgq9WJUo-P0jjo/"),
 ("13_aqila", "https://vt.tokopedia.com/t/ZS9fQEFxjqtye-vBSXa/"),
 ("14_kickchick", "https://vt.tokopedia.com/t/ZS9fQEpBys3yN-7BQR4/"),
 ("15_chicmore_garis", "https://vt.tokopedia.com/t/ZS9fQETQhj4J2-5Ue2d/"),
 ("16_kemeja_anak", "https://vt.tokopedia.com/t/ZS9fQoFCxo5fU-jgdfr/"),
 ("17_chicmore_pita", "https://vt.tokopedia.com/t/ZS9fQoDEquovF-wgGCD/"),
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
        # also try og tags in html
        if not title:
            m2 = re.search(r'<meta property="og:title" content="([^"]+)"', r.text)
            if m2: title = m2.group(1)
        if not img:
            m3 = re.search(r'<meta property="og:image" content="([^"]+)"', r.text)
            if m3: img = m3.group(1)
        pid = re.search(r'/product/(\d+)', final)
        out[tag] = {"short": url, "final": final, "product_id": pid.group(1) if pid else None, "title": title, "image": img, "status": r.status_code}
        print(tag, "|", pid.group(1) if pid else "?", "|", (title or "?")[:90])
    except Exception as e:
        out[tag] = {"short": url, "error": str(e)}
        print(tag, "| ERROR:", e)

json.dump(out, open('/home/hatch/workspace/fashion_test/batch15/products.json','w'), indent=1, ensure_ascii=False)
print("saved products.json")
