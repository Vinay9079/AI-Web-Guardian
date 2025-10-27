def classify_content(text):
    keywords = ["porn", "xxx", "nsfw", "escort", "camgirl"]
    for k in keywords:
        if k in text:
            return "unsafe"
    return "safe"
