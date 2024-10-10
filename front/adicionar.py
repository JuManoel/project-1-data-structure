from ..front.ventanaBase import *


class adicionar(ventanaBase):
    def __init__(self):
        self.estado="agregar_producto"
        pg.init()

    def ventana_adicionar(self,screen):
        self.screen = screen
        self.input_box = InputBox(300,200,200,40)
        Azul=(0, 120, 215)
        self.font = pg.font.Font(None, 36)
        self.botones = self.crear_botones()
        self.corriendo = True
        
    def crear_botones(self):
        botones = []
        # Botón de "Guardar"
        guardar_rect = pg.Rect(300, 300, 100, 50)
        botones.append(("Guardar", guardar_rect))
        # Botón de "Cancelar"
        cancelar_rect = pg.Rect(450, 300, 100, 50)
        botones.append(("Cancelar", cancelar_rect))
        return botones

    def dibujar(self):
        self.screen.fill((30, 30, 30))  # Fondo oscuro
        self.input_box.update()  # Actualiza el recuadro de entrada
        self.input_box.draw(self.screen)  # Dibuja el recuadro de entrada

        # Dibuja los botones
        for texto, rect in self.botones:
            pg.draw.rect(self.screen, (0, 120, 215), rect)  # Dibuja el botón
            texto_renderizado = self.font.render(texto, True, (255, 255, 255))  # Renderiza el texto del botón
            self.screen.blit(texto_renderizado, (rect.x + 10, rect.y + 10))  # Dibuja el texto

    def ejecutar(self):
        while self.corriendo:
            self.manejar_eventos()
            self.dibujar()
            pg.display.flip()  # Actualiza la pantalla

        return False
    
    def run(self):
        # Configuración de la pantalla
        screen = pg.display.set_mode((1000, 600))  # 1000x600 px
        pg.display.set_caption("Adicionar un producto")

        corriendo = True
        while corriendo:
            if self.estado == "agregar_producto":#cambiar
                posiciones = self.menu(screen)
            # validar el button se fue volver al menu

            # Maneja eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    corriendo = False
                if event.type == pg.MOUSEBUTTONDOWN and self.estado == "agregar_producto":
                    mouse_pos = pg.mouse.get_pos()                   
                    self.validar_mouse(mouse_pos, posiciones)
            pg.display.flip()

        pg.quit()
