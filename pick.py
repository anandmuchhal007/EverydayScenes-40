import os, shutil, re

os.makedirs("EverydayScenes-40", exist_ok=True)
chosen = set()

def pick(words1, words2, limit):
    count = 0
    with open("captions.txt", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = re.search(r'([^\s,]+\.jpg)', line)
            if not m:
                continue
            img = m.group(1)
            if img in chosen:
                continue
            text = line.lower()
            if any(re.search(rf'\b{w}\b', text) for w in words1) and any(re.search(rf'\b{w}\b', text) for w in words2):
                src = os.path.join("Images", img)
                if os.path.exists(src):
                    shutil.copy(src, os.path.join("EverydayScenes-40", img))
                    chosen.add(img)
                    count += 1
                    if count >= limit:
                        break

person = ["man", "woman", "boy", "girl", "child", "person", "people"]
pick(person, ["dog", "horse", "bird"], 15)
pick(person, ["car", "truck", "bus", "motorcycle"], 15)
pick(person, ["bicycle", "bike"], 10)
print("Done! Total copied:", len(chosen))