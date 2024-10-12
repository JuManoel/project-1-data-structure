import pygame as pg
from front.inicio import *

class agregar_Producto:
    def __init__(self):
        self.estado = "Agregar producto"
        pg.init()
        self.screen = pg.display.set_mode((1000,600))  # Inicializa la pantalla aquí, si es necesario

    def formulario(self, screen):
        font = pg.font.Font(None, 32)
        title_font = pg.font.Font(None, 28)

        # Colores
        AZUL = (0, 120, 215)
        Color = (9, 12, 155)

        input_boxes = [
            {"rect": pg.Rect(100, 50, 300, 32), "text": '', "active": False, "title": "Nombre"},
            {"rect": pg.Rect(100, 120, 300, 32), "text": '', "active": False, "title": "Precio"},
            {"rect": pg.Rect(100, 190, 300, 32), "text": '', "active": False, "title": "Cantidad"},
            {"rect": pg.Rect(100, 260, 300, 32), "text": '', "active": False, "title": "Categoría"}
        ]

        color_inactive = (128, 128, 128)
        color_active = pg.Color('dodgerblue2')

        button_save = pg.Rect(100, 320, 115, 40)
        button_cancel = pg.Rect(220, 320, 120, 40)

        done = False

        while not done:
            screen.fill(Color)  # Limpia la pantalla

            # Dibuja los cuadros de texto y botones
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

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                if event.type == pg.MOUSEBUTTONDOWN:
                    for box in input_boxes:
                        if box["rect"].collidepoint(event.pos):
                            box["active"] = not box["active"]
                        else:
                            box["active"] = False
                    if button_save.collidepoint(event.pos):
                        for box in input_boxes:
                            print(f'{box["title"]} agregado: {box["text"]}')  # Aquí puedes guardar los datos
                        done = True  # Termina el bucle para volver al menú
                    elif button_cancel.collidepoint(event.pos):
                        done = True  # Termina el bucle para volver al menú
                if event.type == pg.KEYDOWN:
                    for box in input_boxes:
                        if box["active"]:
                            if event.key == pg.K_RETURN:
                                for box in input_boxes:
                                    print(f'{box["title"]} agregado: {box["text"]}')
                                done = True  # Termina el bucle para volver al menú
                            elif event.key == pg.K_BACKSPACE:
                                box["text"] = box["text"][:-1]  # Borra el último carácter
                            else:
                                box["text"] += event.unicode  # Agrega el carácter

            pg.display.flip()  # Actualiza la pantalla
