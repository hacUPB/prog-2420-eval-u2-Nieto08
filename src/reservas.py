
def main():
    import random 
    from random import choice, randint
    num_aleatorio= random.choice(range(1,30))   
    prefijo = input("¿cual prefijo lo define?, señor o señora: ").upper()
    while prefijo != "SEÑOR" or prefijo != "SEÑORA":
        print("por favor elija entre, señor o señora: ") 
        prefijo=input("").upper()
    nombre=input("por favor agregue su nombre y apellido: ")
    origen= int(input("seleccione el número de la ciudad de origen \n 1. Medellin \n 2. Bogotá \n 3. Cartagena \n")) 
    ciudad=origen
    precio=0 
    if ciudad ==1:
        ciudad1= ("Medellín")
    elif ciudad ==2:
        ciudad1= ("Bogotá")
    elif ciudad==3:
        ciudad1= ("Cartagena")
    destino= int(input("seleccione el número de la ciudad de destino \n 1. Medellin \n 2. Bogotá \n 3. Cartagena \n")) 
    if destino == origen:
        print("por favor elija un destino diferente al origen:")
        destino= int(input("seleccione el número de la ciudad de destino \n 1. Medellin \n 2. Bogotá \n 3. Cartagena \n")) 
        if destino ==1:
            destino1= ("Medellín")
        elif destino ==2:
            destino1= ("Bogotá")
        elif destino ==3:
            destino1= ("Cartagena")
    elif destino ==1:
        destino1= ("Medellín")
    elif destino ==2:
        destino1= ("Bogotá")
    elif destino ==3:
        destino1= ("Cartagena")
    dia=input("Que dia desea viajar \n 1.lunes \n 2.martes \n 3.miercoles \n 4.jueves \n 5.viernes \n 6.sabado \n 7.domingo \n ")
    num_mes=int(input("seleccione el numero de ese dia (1-30):"))
    if origen==1 and destino==2 or origen==2 and destino==1 and dia in range (1,4):
        precio=79900
    elif origen==1 and destino==2 or origen==2 and destino==1 and dia in range (5,7):
        precio=119900
    elif origen==1 and destino==3 or origen==3 and destino==1 and dia in range (1,4):
        precio=156900
    elif origen==2 and destino==3 or origen==3 and destino==2 and dia in range (5,7):
        precio=213000
    asiento=input("¿prefiere un asiento en: \n ventana \n pasillo \n sin preferencia \n ")
    if asiento == "ventana":
        num_asi=(f"{num_aleatorio}A")
    if asiento == "pasillo":
        num_asi=(f"{num_aleatorio}C")
    if asiento == "sin preferencia":
        num_asi=(f"{num_aleatorio}B")

    print (f"Bienvenido a cokeline airline {prefijo} {nombre}.  \n su vuelo de {ciudad1} a {destino1} el dia {dia} {num_mes} de agosto está reservado. \n El precio del voleto es de: {precio} pesos \n Su asiento es el {num_asi}")


if __name__ == "__main__":
    main()
