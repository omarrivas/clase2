# Las dos líneas siguientes son necesaias para hacer
# compatible el interfaz Tkinter con los programas basados
# en versiones anteriores a la 8.5, con las más recientes.
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

class Sistema:

    def presionarBoton(self):
        print("hola")


    def __init__(self):
        # Define la ventana principal de la aplicación
        self.raiz = Tk()

        # Define las dimensiones de la ventana, que se ubicará en
        # el centro de la pantalla. Si se omite esta línea la
        # ventana se adaptará a los widgets que se coloquen en
        # ella.
        self.raiz.geometry('300x200') # anchura x altura

        # Asigna un color de fondo a la ventana. Si se omite
        # esta línea el fondo será gris
        self.raiz.configure(bg = 'beige')

        # Asigna un título a la ventana
        self.raiz.title('Aplicación')

        # Define un botón en la parte inferior de la ventana
        # que cuando sea presionado hará que termine el programa.
        # El primer parámetro indica el nombre de la ventana 'raiz'
        # donde se ubicará el botón
        self.botonInfo = ttk.Button(self.raiz, text='Presionar', command=self.presionarBoton).pack(side=BOTTOM)

        # Después de definir la ventana principal y un widget botón
        # la siguiente línea hará que cuando se ejecute el programa
        # construya y muestre la ventana, quedando a la espera de
        # que alguna persona interactúe con ella.

        # Si la persona presiona sobre el botón Cerrar 'X', o bien,
        # sobre el botón 'Salir' el programa llegará a su fin.

        self.raiz.mainloop()


def main():
    mi_app = Sistema()
    return 0

if __name__ == '__main__':
    main()
