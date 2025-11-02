# main.py
# Program i syfte att demonstrera GitHub
# Genererat av Microsoft Copilot AI, kontrollerat av Nikodemus Karlsson

print("Välj operation:")
print("1. Addition")
print("2. Subtraktion")
print("3. Multiplikation")
print("4. Division")

val = input("Val: ")
tal1 = float(input("Ange första talet: "))
tal2 = float(input("Ange andra talet: "))

if val == "1":
    print("Resultat:", tal1 + tal2)
elif val == "2":
    print("Resultat:", tal1 - tal2)
elif val == "3":
    print("Resultat:", tal1 * tal2)
elif val == "4":
    print("Resultat:", tal1 / tal2)
else:
    print("Ogiltigt val.")

