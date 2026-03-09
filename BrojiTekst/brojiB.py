def broji_slova(tekst):
    broj = {}
    for znak in tekst:
        if znak.isalpha():
            broj[znak] = broj.get(znak, 0) + 1
    return broj

tekst = "Ovo je primjer teksta!"
print(broji_slova(tekst))
