def mostrar_menu():
    print('1 - Calcular energia potencial.')
    print('2 - Calcular energia cinética.')
    print('3 - Sair do programa')
   
def calcular_ep(m,h):
    ep = m * 9.8 * h
    return ep

def calcular_ac(m,v):
    ec = (m*(v**2))/2
    return ec