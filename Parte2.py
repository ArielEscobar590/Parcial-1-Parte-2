while (True):
    #try:
        print("\n--- MENU ---")
        print("1. Calcular MCD de dos números")
        print("2. Crear una cadena repetidad N veces")
        print("3. Conteo de veces que aparece una letra en una cadena")
        print("4. Convertir un número decimal a Binario")
        print("5. Conteo de dígitos en un número")
        print("6. Salir")
        op = int(input("Ingrese una opción para continuar:  "))

        if op == 1:
          def CalculoMCD(num1, num2):
              residuo = num1 % num2
              if residuo == 0:
                  return print(f"El maximo común divisor es: {num2}")
              else:
                  return CalculoMCD(num2, residuo)

          print("\nCalculo de MCD")
          num1 = int(input("Ingrese el primer Número:  "))
          num2 = int(input("Ingrese el segundo Número:  "))
          CalculoMCD(num1, num2)
        #elif op == 2:


        #elif op == 3:



        elif op == 4:


       # elif op == 5:

       # elif op == 6:
            break



        def Conteodigi(conteo):
            if conteo==0:
                return 0
        def Convertir(num):
            if num == 0:
                return 0
            else:
                return num
        def Cadena(palabra, veces):
            if veces == 0:
                return 0
            else:
                print(Cadena(palabra, veces - 1))
        def Conteoletra(num):
            if num == 0:
                return 0


    #except:
       # print("Ha ocurrido un error")
