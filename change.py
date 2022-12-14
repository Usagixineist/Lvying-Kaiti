import re
with open('characters base.md', encoding='utf-8', mode='r+') as base:
    doc = base.read()
    doc1 = re.sub(r'[*][*]([^*]+)[*][*]',
                  r'<span style="color:#ff0000">\1</span>', doc)
    doc2 = re.sub(r'[~][~]([^~]+)[~][~]',
                  r'<span style="color:#00000000">\1</span>', doc1)
    with open('characters.md', encoding='utf-8', mode='r+') as f:
        f.seek(0)
        f.truncate()
        f.write(doc2)
