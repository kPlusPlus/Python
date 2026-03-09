from collections import Counter

def broji_slova(tekst):
    return Counter(c for c in tekst if c.isalpha())

tekst = "Ovo je primjer teksta!"
print(broji_slova(tekst))
