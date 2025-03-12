# nesting dictioanary in  a dictionary
traval_log = {
    "France":{"cities_visited":["Paris","Lille","Digon"]},
    "Germany": {"cities_visted":["Berlin", "Hamburg", "Stuttgrart"]}
}

print(traval_log)

#Nesting dictionary in a list

traval_log = [
    {
        "Country":"France",
        "cities_visited":["Paris","Lille","Digon"],
        "totel_visits": 12
    },
    {
        "Country":"Germany",
        "cities_visted":["Berlin", "Hamburg", "Stuttgrart"],
        "totel_visits": 15
    },
]

print(traval_log)