import pygame as pg
from front.inicio import *
from back.controller.controller import Controller as ctrl

class modificar:
    def __init__(self):
        self.estado = "Modificar producto"
        pg.init()
        self.screen = pg.display.set_mode((1000,600))

    def modificar(self, id, producto):
        con = ctrl()
        return con.modificarProducto(int(id), producto)

    def modificacion(self, screen):
        font = pg.font.Font(None,32)
        title_font = pg.font.Font(None, 28)
        Color = (9, 12, 155)
        VERDE = (0, 200, 0)  # Color verde para el botón de "Buscar"
        ROJO = (200, 0, 0)  

        # Definir todos los cuadros de texto
        input_box_id = {"rect": pg.Rect(100, 50, 300, 32), "text": '', "active": False, "title": "ID del Producto"}
        input_box_name = {"rect": pg.Rect(100, 125, 300, 32), "text": '', "active": False, "title": "Nombre del Producto"}
        input_box_price = {"rect": pg.Rect(100, 200, 300, 32), "text": '', "active": False, "title": "Precio del Producto"}
        input_box_quantity = {"rect": pg.Rect(100, 275, 300, 32), "text": '', "active": False, "title": "Cantidad"}
        input_box_category = {"rect": pg.Rect(100, 350, 300, 32), "text": '', "active": False, "title": "Categoría"}

        # Colores de los cuadros de texto
        color_inactive = (128, 128, 128)
        color_active = pg.Color('dodgerblue2')

        # Botón de buscar y cancelar
        button_search = pg.Rect(100, 425, 120, 40)
        button_cancel = pg.Rect(230, 425, 120, 40)

        done = False
        tree,estados=ctrl().service.getTree()
        # Bucle principal del formulario
        while not done:
            screen.fill(Color)  # Limpia la pantalla

            # Dibuja todos los cuadros de texto
            for input_box in [input_box_id, input_box_name, input_box_price, input_box_quantity, input_box_category]:
                color = color_active if input_box["active"] else color_inactive
                txt_surface = font.render(input_box["text"], True, (0, 0, 0))
                width = max(300, txt_surface.get_width() + 10)
                input_box["rect"].w = width

                title_surface = title_font.render(input_box["title"], True, (0, 0, 0))
                screen.blit(title_surface, (input_box["rect"].x, input_box["rect"].y - 30))
                pg.draw.rect(screen, color, input_box["rect"], 2)
                screen.blit(txt_surface, (input_box["rect"].x + 5, input_box["rect"].y + 5))

            # Dibuja los botones de "Buscar" (Verde) y "Cancelar" (Rojo)
            pg.draw.rect(screen, VERDE, button_search)  # Botón Buscar en verde
            pg.draw.rect(screen, ROJO, button_cancel)   # Botón Cancelar en rojo

            # Texto en los botones, en blanco
            search_surface = font.render('Buscar', True, (255, 255, 255))  # Texto en blanco
            cancel_surface = font.render('Cancelar', True, (255, 255, 255))  # Texto en blanco

            screen.blit(search_surface, (button_search.x + 10, button_search.y + 5))
            screen.blit(cancel_surface, (button_cancel.x + 10, button_cancel.y + 5))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                if event.type == pg.MOUSEBUTTONDOWN:
                    # Verificar si se hace clic en alguno de los cuadros de texto
                    for input_box in [input_box_id, input_box_name, input_box_price, input_box_quantity, input_box_category]:
                        if input_box["rect"].collidepoint(event.pos):
                            input_box["active"] = not input_box["active"]
                        else:
                            input_box["active"] = False

                    # Verificar si se hace clic en el botón de "Buscar"
                    if button_search.collidepoint(event.pos):
                        json = {
                            "nombre":input_box_name["text"],
                            "precio":float(input_box_price["text"]),
                            "cantidad":int(input_box_quantity["text"]),
                            "categoria":input_box_category["text"]
                        }
                        tree,estados = self.modificar(input_box_id["text"],json)
                        done = True

                    # Verificar si se hace clic en el botón de "Cancelar"
                    if button_cancel.collidepoint(event.pos):
                        print("Operación cancelada")
                        done = True  # Termina el bucle para volver al menú o cerrar

                if event.type == pg.KEYDOWN:
                    # Verificar si se está escribiendo en el cuadro activo
                    for input_box in [input_box_id, input_box_name, input_box_price, input_box_quantity, input_box_category]:
                        if input_box["active"]:
                            if event.key == pg.K_RETURN:
                                print(f'Buscando producto con ID: {input_box_id["text"]}')
                            elif event.key == pg.K_BACKSPACE:
                                input_box["text"] = input_box["text"][:-1]
                            else:
                                input_box["text"] += event.unicode

            pg.display.flip()
        return tree,estados
