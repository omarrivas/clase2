import calendar

sueldobasico = {'maestranza A':27311, 'maestranza B':27414, 'maestranza C':27777, 'administracion A': 27699}

################################################
#VARIABLES
antiguedad= 0.1
jubilacion= 0.11
ley19032= 0.03
obrasocial= 0.03
SEC= 0.02
FAEC= 0.05

#################################################
#MES A LIQUIDAR
mes= 9
anio= 2020
feriados_mes= 2

##################################################
#DATOS TRABAJADOR
nombre= "Omar Rivas"
tipo_empleado= 'administracion A'
dias_trabajados= 28
dias_feriados_trabajado = 1


###################################################
#CALCULOS
cantidadDiasMes = calendar.monthrange(anio,mes)

sueldo_basico = sueldobasico[tipo_empleado]

sueldo_por_antiguedad= sueldo_basico * antiguedad
asistencia_y_puntualidad= (sueldo_basico + sueldo_por_antiguedad) / 12

valor_dia_normal= (sueldo_basico + sueldo_por_antiguedad + asistencia_y_puntualidad) / cantidadDiasMes[1]

menos_feriados = valor_dia_normal * feriados_mes

pago_feriado=(sueldo_basico + sueldo_por_antiguedad + asistencia_y_puntualidad) / 25

pago_feriado_trabajado= (pago_feriado + valor_dia_normal) * dias_feriados_trabajado
pago_feriado_notrabajado= pago_feriado * (feriados_mes-dias_feriados_trabajado)

pago_jubilacion= (sueldo_basico + sueldo_por_antiguedad + asistencia_y_puntualidad) * jubilacion
pago_ley19032= (sueldo_basico + sueldo_por_antiguedad + asistencia_y_puntualidad) * ley19032
pago_obrasocial= (sueldo_basico + sueldo_por_antiguedad + asistencia_y_puntualidad) * obrasocial

print("BASICO           " + str(cantidadDiasMes[1]) + "          " + str(sueldo_basico))
print("ANTIGUEDAD       " + str(antiguedad) + "         " + str(sueldo_por_antiguedad))
print("ASIST. Y PUNT.               " + str(asistencia_y_puntualidad))
print("DIA FERIADO      " + str(feriados_mes) + "         -" + str(menos_feriados))
print("PAGO FER NO TRAB " + str(feriados_mes) + "          " + str(pago_feriado_notrabajado))
print("PAGO FER TRAB    " + str(feriados_mes) + "          " + str(pago_feriado_trabajado))
print("")
print("                 11%               " + str(pago_jubilacion))
print("                  3%               " + str(pago_ley19032))
print("                  3%               " + str(pago_obrasocial))