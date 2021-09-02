x = {"Continental": "****", "Big street": "**", "Cornar": "**", "Trashviews": "*",
     "Hazbins": "****", "Hazbins Deluxe": "*****"}
val = input("stars")
for key in x:
    if x[key] == val:
        print(key)
