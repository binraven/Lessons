def all_variants(text):
    i = 0
    x, y = 0, 1
    while i < len(text):
        yield text[i]
        i += 1
    while y < i:
        yield text[x] + text[y]
        x += 1
        y += 1
    yield text


a = all_variants("abc")
for i in a:
    print(i)

