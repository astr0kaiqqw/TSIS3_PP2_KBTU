def grams_to_ounces(grams):
    ounces = grams * 28.3495231
    return ounces
    
grams = float(input("Enter the grams: "))
ounces = grams_to_ounces(grams)
print(f"{grams} грамм = {ounces:.2f} унций")