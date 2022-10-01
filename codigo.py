ciudadA=3500000
ciudadD=5000000
años=1980
while ciudadA < ciudadD:
    ciudadA=(ciudadA*7/100)+ciudadA
    ciudadD=(ciudadD*5/100)+ciudadD
    años=años+1
print("la cantidad de años necesarios para que la ciudadA supere la ciudad D son : "+str(años))