n = int(raw_input("Ingresar la Cantidad de Trabajadores: "))
c = 1
while c <= n:
    nombre = raw_input("Ingrese Nombre del Trabajador: ")
    opcion = int(raw_input("\n Menu\n\t" + "1.Barnizado\n\t 2.Laqueado\n\t 3.Pintado\n\t" + "Ingresar Cargo: "))
    hora1 = int(raw_input("Ingresar Horas Trabajadas Durante la Semana: "))
    hora = 40
    hora_x_opcion = {1:10,2:12,3:14}
    valido = False
    i = 1
    while not valido:
    	if opcion > 0 and opcion < 4:
            HE = 0
            JE = 0
            sueldo = hora_x_opcion[opcion] * hora
            if hora1 > hora:
                HE = (hora1 - 40) * 0.3
                JE = hora_x_opcion[opcion] * HE
                sueldo = hora_x_opcion[opcion] * hora1 + JE 
            valido = True
            break
        else:
            print "Ingresar Opciones Validas"
            opcion = int(raw_input("\n Menu\n\t" + "1.Barnizado\n\t 2.Laqueado\n\t 3.Pintado\n\t" + "Ingresar Cargo: "))
            hora1 = int(raw_input("Ingresar Horas Trabajadas Durante la Semana: "))
    c += 1
    print "El Nombre es: " + str(nombre) + "\n La Hora Extra es: " + str(HE) + "\n El Jornal Extra es: " + str(JE) + "\n El Jornal Semanal es: " + str(sueldo)
