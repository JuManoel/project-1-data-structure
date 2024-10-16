import pygame as pg
from front.inicio import *
from back.controller.controller import Controller as ctrl
class agregar_Producto:
    def __init__(self):
        self.estado = "Agregar producto"
        pg.init()
        self.screen = pg.display.set_mode((1000,600))  # Inicializa la pantalla aquí, si es necesario

    def guardar(self, json): 
        con = ctrl()
        return con.insertarProducto(json)

    def formulario(self, screen):
        font = pg.font.Font(None, 32)
        title_font = pg.font.Font(None, 28)

        # Colores
        verde = (0, 200, 0)
        Color = (9, 12, 155)
        Rojo=(200, 0, 0)

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

            pg.draw.rect(screen, verde, button_save)  # Botón Guardar
            pg.draw.rect(screen, Rojo, button_cancel)  # Botón Cancelar

            save_surface = font.render('Guardar', True, (255, 255, 255))
            cancel_surface = font.render('Cancelar', True, (255, 255, 255))
            screen.blit(save_surface, (button_save.x + 10, button_save.y + 5))
            screen.blit(cancel_surface, (button_cancel.x + 10, button_cancel.y + 5))

            tree,estados=ctrl().service.getTree()
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
                        #agregar productos?
                        json = {
                            "nombre":None,
                            "precio":None,
                            "cantidad": None,
                            "categoria":None
                        }
                        for box in input_boxes:
                            if(box["text"] == 'categoría'):
                                json["categoria"] = box["text"]
                            else:
                                json[box["title"].lower()] = box["text"]
                        tree,estados = self.guardar(json)  # Aquí puedes guardar los datos
                        done = True  
                    elif button_cancel.collidepoint(event.pos):
                        done = True  
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
        return tree,estados
