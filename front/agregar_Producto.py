import pygame as pg
from front.inicio import Inicio  # Move the import statement inside the class

class agregar_Producto:
    def __init__(self):
        self.estado = "Agregar producto"
        pg.init()

    def formulario(self, screen):
        font = pg.font.Font(None, 32)
        title_font = pg.font.Font(None, 28)

        # Colores
        AZUL = (0, 120, 215)
        Color = (9, 12, 155)
        screen.fill(Color)
        
        input_boxes = [
            {"rect": pg.Rect(100, 50, 300, 32), "text": '', "active": False, "title": "Nombre"},
            {"rect": pg.Rect(100, 120, 300, 32), "text": '', "active": False, "title": "Precio"},
            {"rect": pg.Rect(100, 190, 300, 32), "text": '', "active": False, "title": "Cantidad"},
            {"rect": pg.Rect(100, 260, 300, 32), "text": '', "active": False, "title": "Categoría"}
        ]
        
        # Colores de los cuadros de texto
        color_inactive = (128, 128, 128)
        color_active = pg.Color('dodgerblue2')
        
        # Botones
        button_save = pg.Rect(100, 320, 115, 40)
        button_cancel = pg.Rect(220, 320, 120, 40)
        
        done = False
        
        # Dibujar en la pantalla
        for box in input_boxes:
            color = color_active if box["active"] else color_inactive
            txt_surface = font.render(box["text"], True, (0, 0, 0))
            width = max(300, txt_surface.get_width() + 10)
            box["rect"].w = width
            
            title_surface = title_font.render(box["title"], True, (0, 0, 0))
            screen.blit(title_surface, (box["rect"].x, box["rect"].y - 30))
            pg.draw.rect(screen, color, box["rect"], 2)
            screen.blit(txt_surface, (box["rect"].x + 5, box["rect"].y + 5))
        
        pg.draw.rect(screen, AZUL, button_save)  # Botón Guardar
        pg.draw.rect(screen, AZUL, button_cancel)  # Botón Cancelar
        
        save_surface = font.render('Guardar', True, (255, 255, 255))
        cancel_surface = font.render('Cancelar', True, (255, 255, 255))
        screen.blit(save_surface, (button_save.x + 10, button_save.y + 5))
        screen.blit(cancel_surface, (button_cancel.x + 10, button_cancel.y + 5))
        
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    for box in input_boxes:
                        if box["rect"].collidepoint(event.pos):
                            box["active"] = not box["active"]
                        else:
                            box["active"] = False
                    if button_save.collidepoint(event.pos):
                        for box in input_boxes:
                            print(f'{box["title"]} agregado: {box["text"]}')  # Puedes guardar los datos aquí
                        self.estado = "menu"  # Cambiar el estado a menú
                        done = True
                    elif button_cancel.collidepoint(event.pos):
                        self.estado = "menu"  # Cambiar el estado a menú
                        done = True   
                if event.type == pg.KEYDOWN:
                    for box in input_boxes:
                        if box["active"]:
                            if event.key == pg.K_RETURN:
                                for box in input_boxes:
                                    print(f'{box["title"]} agregado: {box["text"]}')
                                self.estado = "menu"
                                done = True
                            elif event.key == pg.K_BACKSPACE:
                                box["text"] = box["text"][:-1]  # Borra el último carácter
                            else:
                                box["text"] += event.unicode  # Agrega el carácter
                self.screen=screen
                corriendo=True
                while corriendo:
                    if self.estado == "agregar_producto":
                        self.formulario(screen)
                    if self.estado == "menu":
                        pg.quit()
                        ventana = Inicio()
                        ventana.run()
                pg.display.flip()
                pg.quit()

            

   