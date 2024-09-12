
def main():
    lift=int(input("agregue la altitud inicial del satélite (km): "))
    drag=float(input("agregue el coeficiente de arrastre: "))
    alt_m=int(input("altura minima en la que el satelite entra en la atmosfera (km): "))
    contador= 0
    while lift<alt_m:
        print("la altitud inicial es menor que la altitud minima, agregue otra vez estos datos:")
        lift=int(input("agregue la altitud inicial del satélite (km): "))
        alt_m=int(input("altura minima en la que el satelite entra en la atmosfera (km): "))
    print ("calculando las órbitas...")
    while drag<lift or lift<= alt_m:
        alt_perdida=drag*lift
        lift-= alt_perdida
        drag+= 0.0001
        contador+= 1
        print (f"órbita {contador}: altitud = {lift} Km, coeficiente de arrastre= {drag}")
    print (f"el satélite ha ingresado a la atmosfera despues de {contador} órbitas")


if __name__ == "__main__":
    main()
