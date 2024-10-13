import pygame as pg


class borrar:
    def __init__(self):
        self.estado = "Borrar producto"
        pg.init()

    def borrar_elemento(self, screen):
        font = pg.font.Font(None, 32)
        title_font = pg.font.Font(None, 28)

        # Colores
        VERDE = (0, 200, 0)  # Color verde para el botón de "Buscar"
        ROJO = (200, 0, 0)   # Color rojo para el botón de "Cancelar"
        Color = (9, 12, 155) # Fondo azul oscuro
        screen.fill(Color)

        # Input box para el ID del producto
        input_box_id = {"rect": pg.Rect(100, 50, 300, 32), "text": '', "active": False, "title": "ID del Producto"}

        # Colores de los cuadros de texto
        color_inactive = (128, 128, 128)
        color_active = pg.Color('dodgerblue2')

        # Botones de buscar y cancelar
        button_search = pg.Rect(100, 120, 120, 40)
        button_cancel = pg.Rect(230, 120, 120, 40)

        done = False

        # Bucle principal del formulario
        while not done:
            screen.fill(Color)  # Limpia la pantalla

            # Dibuja el cuadro de texto para el ID
            color = color_active if input_box_id["active"] else color_inactive
            txt_surface = font.render(input_box_id["text"], True, (0, 0, 0))
            width = max(300, txt_surface.get_width() + 10)
            input_box_id["rect"].w = width

            title_surface = title_font.render(input_box_id["title"], True, (0, 0, 0))
            screen.blit(title_surface, (input_box_id["rect"].x, input_box_id["rect"].y - 30))
            pg.draw.rect(screen, color, input_box_id["rect"], 2)
            screen.blit(txt_surface, (input_box_id["rect"].x + 5, input_box_id["rect"].y + 5))

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
                    # Verificar si se hace clic en el cuadro de texto
                    if input_box_id["rect"].collidepoint(event.pos):
                        input_box_id["active"] = not input_box_id["active"]
                    else:
                        input_box_id["active"] = False

                    # Verificar si se hace clic en el botón de "Buscar"
                    if button_search.collidepoint(event.pos):
                        print(f'Buscando producto con ID: {input_box_id["text"]}')
                        # Aquí puedes agregar la lógica de búsqueda

                    # Verificar si se hace clic en el botón de "Cancelar"
                    if button_cancel.collidepoint(event.pos):
                        print("Operación cancelada")
                        done = True  # Termina el bucle para volver al menú o cerrar

                if event.type == pg.KEYDOWN:
                    if input_box_id["active"]:
                        if event.key == pg.K_RETURN:
                            print(f'Buscando producto con ID: {input_box_id["text"]}')
                        elif event.key == pg.K_BACKSPACE:
                            input_box_id["text"] = input_box_id["text"][:-1]
                        else:
                            input_box_id["text"] += event.unicode

            pg.display.flip()