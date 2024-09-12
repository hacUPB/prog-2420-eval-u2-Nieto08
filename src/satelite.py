
def main():
    lift=int(input("agregue la altitud inicial del satélte (km): "))
    drag=float(input("agregue el coeficiente de arrastre: "))
    alt_m=int(input("altura en la que el satelite se desintregra (km): "))
    while drag<lift or lift<= alt_m:
        alt_perdida=drag*lift
        lift=lift-alt_perdida
        drag+=0.0001
    print 


if __name__ == "__main__":
    main()
