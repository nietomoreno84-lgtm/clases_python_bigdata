from data.trabajadores import trabajadores


def calcular_coste_hora_extra(trabajador):
    # dividimos el sueldo por las horas y sacamos el coste hora
    coste_hora_extra = trabajador['sueldo_base'] / trabajador['horas_contrato']
    # multiplicamos por las horas extra, y obtenemos el coste_horas_extra
    total_horas_extra = coste_hora_extra * trabajador['horas_extra']    
    # se lo añadimos al trabajo clave: valor
    trabajador['total_horas_extra'] = total_horas_extra
   


for trabajador in trabajadores:
    calcular_coste_hora_extra(trabajador)

## calcular los horas extra de todos los trabajadores.


## calcular la nomina de un trabajador

## calcular la nomina de todos los trabajadores.

from data.trabajadores import trabajadores

def calcular_coste_hora_extra(trabajador):
    # dividimos el sueldo por las horas y sacamos el coste hora
    coste_hora_extra = trabajador['sueldo_base'] / trabajador['horas_contrato']
    # multiplicamos por las horas extra, y obtenemos el coste_horas_extra
    total_horas_extra = coste_hora_extra * trabajador['horas_extra']    
    # se lo añadimos al trabajo clave: valor
    trabajador['total_horas_extra'] = total_horas_extra



## calcular la nomina de un trabajador

def calcular_nomina(trabajador):
    irpf = trabajador['sueldo_base'] * (trabajador['porcentaje_impuestos']/100)
    sueldo_neto_sin_extras = trabajador['sueldo_base'] - irpf
    sueldo_final = sueldo_neto_sin_extras + trabajador['total_horas_extra']
    trabajador['nomina'] = sueldo_final

# pintar todos los trabajadores de una lista

def listar_trabajadores(lista_trabajadores):
    print("          ###### lista de trabajadores ######")
    for trabajador in lista_trabajadores:
        print('-'*70)
        print(f"{trabajador['nombre']}  | departamento: {trabajador['departamento']}  | sueldo base: {trabajador['sueldo_base']}")
        print('-' * 70)

# filtrar los trabajadores y pintarlo por categoria

def filtrar_por_departamento(lista_trabajadores,departamento):
    lista_filtrada = []
    for trabajador in lista_trabajadores :
        if trabajador['departamento'] == departamento:
            lista_filtrada.append(trabajador)
    return lista_filtrada



lista_direccion = filtrar_por_departamento(trabajadores,'Dirección')
lista_marketing = filtrar_por_departamento(trabajadores,'Marketing')
listar_trabajadores(lista_marketing)

