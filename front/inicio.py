import pygame as pg
from front.agregar_Producto import agregar_Producto
from front.modificar import modificar
from front.borrar import borrar
from front.buscar_elemento import buscar_Producto
class Inicio:
    def __init__(self):
        self.estado = "menu"  # Estado inicial: menú principal
        pg.init()  # Inicializa Pygame al inicio del programa
        self.screen = pg.display.set_mode((1000, 600))  # Configuración de la pantalla
        pg.display.set_caption("Menu")

    def menu(self):
        # Colores
        BLANCO = (255, 255, 255)
        AZUL = (0, 120, 215)
        NEGRO = (0, 0, 0)
        margen = 5

        # Divide la pantalla en dos
        divider_position = self.screen.get_width() // 2
        pg.draw.rect(self.screen, AZUL, (divider_position, 0, divider_position, self.screen.get_height()))
        pg.draw.rect(self.screen, BLANCO, (0, 0, divider_position, self.screen.get_height()))
        pg.draw.line(self.screen, (0, 0, 0), (divider_position, 0), (divider_position, self.screen.get_height()), 3)

        # Dimensiones y espaciado de los cuadros
        cuadro_ancho = 200
        cuadro_alto = 100
        espaciado = 20

        # Fuente para el texto
        fuente = pg.font.Font(None, 36)

        # Textos para los cuadros
        textos = ["Adicionar", "Modificar", "Borrar", "Buscar"]

        # Posiciones de los cuadros centrados a la derecha
        posiciones = [
            (self.screen.get_width() - cuadro_ancho - 160, 50 + i * (cuadro_alto + espaciado)) for i in range(len(textos))
        ]

        # Dibuja los cuadros y el texto
        for i, pos in enumerate(posiciones):
            pg.draw.rect(self.screen, NEGRO, (pos[0] - margen, pos[1] - margen, cuadro_ancho + 2 * margen, cuadro_alto + 2 * margen))
            pg.draw.rect(self.screen, AZUL, (pos[0], pos[1], cuadro_ancho, cuadro_alto))
            texto_renderizado = fuente.render(textos[i], True, BLANCO)  # Texto en blanco
            texto_rect = texto_renderizado.get_rect(center=(pos[0] + cuadro_ancho // 2, pos[1] + cuadro_alto // 2))
            self.screen.blit(texto_renderizado, texto_rect)

        return posiciones

    def validar_mouse(self, mouse_pos, posiciones):
        if posiciones[0][0] <= mouse_pos[0] <= posiciones[0][0] + 200 and posiciones[0][1] <= mouse_pos[1] <= posiciones[0][1] + 100:
            self.estado = "agregar_producto"  # Cambia el estado a "agregar_producto"
        elif posiciones[1][0] <= mouse_pos[0] <= posiciones[1][0] + 200 and posiciones[1][1] <= mouse_pos[1] <= posiciones[1][1] + 100:
            self.estado = "Modificar elemento"  # Cambia a una función específica
        elif posiciones[2][0] <= mouse_pos[0] <= posiciones[2][0] + 200 and posiciones[2][1] <= mouse_pos[1] <= posiciones[2][1] + 100:
            self.estado = "borrar" 
        elif posiciones[3][0] <= mouse_pos[0] <= posiciones[3][0] + 200 and posiciones[3][1] <= mouse_pos[1] <= posiciones[3][1] + 100:
           self.estado="Buscar elemento" 
    def run(self):
        corriendo = True
        while corriendo:
            if self.estado == "menu":
                posiciones = self.menu()
            if self.estado == "agregar_producto":
                ventana = agregar_Producto()  # Ahora obtiene el estado de vuelta
                ventana.formulario(self.screen)
                self.estado = "menu"  # Cambia el estado a "menu" cuando termine la ventana agregar_Producto
            if self.estado == "Modificar elemento":
               modi=modificar()
               modi.modificacion(self.screen)
               self.estado = "menu"
            if self.estado=="borrar":
                suprimir=borrar()
                suprimir.borrar_elemento(self.screen)
                self.estado="menu"
            if self.estado=="Buscar elemento":
                buscar=buscar_Producto()
                buscar.busqueda(self.screen)
                self.estado="menu"

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    corriendo = False
                if event.type == pg.MOUSEBUTTONDOWN and self.estado == "menu":
                    mouse_pos = pg.mouse.get_pos()
                    self.validar_mouse(mouse_pos, posiciones)

            pg.display.flip()

pg.quit()
