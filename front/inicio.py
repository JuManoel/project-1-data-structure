from ..front.ventanaBase import *

class Inicio(ventanaBase):
    def __init__(self):
        self.estado = "menu"  # Estado inicial: menú principal
        pg.init()

    def menu(self, screen):
        # Colores
        BLANCO = (255, 255, 255)
        AZUL = (0, 120, 215)
        NEGRO = (0, 0, 0)
        margen = 5

        # Divide la pantalla en dos
        divider_position = screen.get_width() // 2
        pg.draw.rect(screen, AZUL, (divider_position, 0, divider_position, screen.get_height()))
        pg.draw.rect(screen, BLANCO, (0, 0, divider_position, screen.get_height()))
        pg.draw.line(screen, (0, 0, 0), (divider_position, 0), (divider_position, screen.get_height()), 3)

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
            (screen.get_width() - cuadro_ancho - 160, 50),  # Cuadro 1
            (screen.get_width() - cuadro_ancho - 160, 50 + cuadro_alto + espaciado),  # Cuadro 2
            (screen.get_width() - cuadro_ancho - 160, 50 + 2 * (cuadro_alto + espaciado)),  # Cuadro 3
            (screen.get_width() - cuadro_ancho - 160, 50 + 3 * (cuadro_alto + espaciado))  # Cuadro 4
        ]

        # Dibuja los cuadros y el texto
        for i, pos in enumerate(posiciones):
            pg.draw.rect(screen, NEGRO, (pos[0] - margen, pos[1] - margen, cuadro_ancho + 2 * margen, cuadro_alto + 2 * margen))

            # Dibuja el cuadro
            pg.draw.rect(screen, AZUL, (pos[0], pos[1], cuadro_ancho, cuadro_alto))
            
            # Renderiza el texto
            texto_renderizado = fuente.render(textos[i], True, BLANCO)  # Texto en blanco
            
            # Calcula la posición para centrar el texto en el cuadro
            texto_rect = texto_renderizado.get_rect(center=(pos[0] + cuadro_ancho // 2, pos[1] + cuadro_alto // 2))
            
            # Dibuja el texto
            screen.blit(texto_renderizado, texto_rect)

        return posiciones

    
    def run(self):
        # Configuración de la pantalla
        screen = pg.display.set_mode((1000, 600))  # 1000x600 px
        pg.display.set_caption("Menu")

        corriendo = True
        while corriendo:
            if self.estado == "menu":
                posiciones = self.menu(screen)
            elif self.estado == "agregar_producto":
                self.agregar_producto(screen)
            elif self.estado == "Modificar elemento":
                self.ventana_Modificar(screen)

            # Maneja eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    corriendo = False
                if event.type == pg.MOUSEBUTTONDOWN and self.estado == "menu":
                    mouse_pos = pg.mouse.get_pos()                   
                    self.validar_mouse(mouse_pos, posiciones)

                

            pg.display.flip()

        pg.quit()


