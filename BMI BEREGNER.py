# har laver et kode der beregner ens bmi og fortæller om du er fed eller ej ;)
# koden spørger om hvad du hedder? og indtroducere hvad den vil lave
navnet = input('Hvad hedder du?: ')
print('Hej, nu skal vi lave et bmi test til', navnet)

# her vil koden stille dig spørgsmål til hvor høj og hvor meget du vejer, også regner bmi ud
try:
    højde = float(input('Hvor høj er du (i cm)?: '))
    vægt = float(input('Hvor meget vejer du (i kg)?: '))
    bmi = vægt / ((højde / 100) ** 2)
    print("Dit BMI er: ", bmi)
    # lige pt den gøre cm om til meter, det har været en lille helvede at finde ud af det xD
except:
    print("Du indtastede ikke en gyldig værdi. Prøv igen.")

# udfra din bmi fortæller den dig om du har fedme eller ej
if bmi <= 18.5:
    print("du er undervægtig")
elif bmi>=18.5 and bmi<25:
    print("du er normalvægtig")
elif bmi >= 25 and bmi < 30:
    print("du er overvægtig")
else:
    print("du er meget overvægtig")