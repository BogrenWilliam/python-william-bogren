def temperatur (tal): # Defenierar tempteraturen
    fahrenheit = float(tal) # Variabel
    celcius = (fahrenheit-32) * 5 / 9
    return celcius

celcius = temperatur(40) # Bestämmer att celcius har temperaturen 40 c*
print(type(celcius))
print("40 grader fahrenheit är " + str(celcius)) # Skriver ut vad fahrenheit (40) är i celcius 

