text = "Hola soy Juan Sebastian"
vocals = {c: c.upper() for c in text if c in 'aeiou'}
print(vocals)