thisdict = {
    "firma" : "ford",
    "modelis" : "focus",
    "izlaiduma gads" : "2022.gads",
    "krasa" : "zila",

}
print(thisdict)

thisdict ["atrumkarba"] = "automats"
print(thisdict)
thisdict.pop("izlaiduma gads")
print(thisdict)
thisdict["krasa"] = "sarkans"

print(thisdict)

