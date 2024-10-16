import pygame as pg
from back.controller.controller import Controller as ctrl

class BusquedaAvanzada:
    def __init__(self):
        self.estado = "Busqueda Avanzada"
        pg.init()

    def buscar(self, nombre=None, categoria=None, precio_min=None, precio_max=None):
        con = ctrl()
        # Aquí deberías agregar la lógica de búsqueda avanzada
        if nombre:
            resultados = con.buscarProductoPorNombre(nombre)
        elif categoria:
            resultados = con.buscarProductoPorCategoria(categoria)
        elif precio_min is not None and precio_max is not None:
            resultados = con.buscarProductoPorRangoPrecio(precio_min, precio_max)
        
        for producto in resultados:
            print(producto)  # Muestra los resultados (luego se mostrará en pantalla)

    def busqueda(self, screen):
        font = pg.font.Font(None, 32)
        title_font = pg.font.Font(None, 28)

        # Colores
        VERDE = (0, 200, 0)  # Color verde para el botón de "Buscar"
        ROJO = (200, 0, 0)   # Color rojo para el botón de "Cancelar"
        Color = (9, 12, 155) # Fondo azul oscuro

        # Input boxes para los criterios de búsqueda
        # Ajusta las posiciones de las cajas de entrada para mayor separación
        input_box_nombre = {"rect": pg.Rect(100, 50, 300, 30), "text": '', "active": False, "title": "Nombre del Producto"}
        input_box_categoria = {"rect": pg.Rect(100, 110, 300, 30), "text": '', "active": False, "title": "Categoría"}
        input_box_precio_min = {"rect": pg.Rect(100, 180, 140, 30), "text": '', "active": False, "title": "Precio Mínimo"}  # Aumentar el espacio entre las cajas
        input_box_precio_max = {"rect": pg.Rect(260, 180, 140, 30), "text": '', "active": False, "title": "Precio Máximo"}  # Aumentar el espacio entre las cajas


        # Colores de los cuadros de texto
        color_inactive = (128, 128, 128)
        color_active = pg.Color('dodgerblue2')

        # Botones
        button_search = pg.Rect(100, 220, 120, 40)
        button_cancel = pg.Rect(250, 220, 120, 40)

        done = False

        # Bucle principal del formulario
        while not done:
            screen.fill(Color)  # Limpia la pantalla

            # Dibuja los cuadros de texto para los criterios de búsqueda
            for input_box in [input_box_nombre, input_box_categoria, input_box_precio_min, input_box_precio_max]:
                color = color_active if input_box["active"] else color_inactive
                txt_surface = font.render(input_box["text"], True, (0, 0, 0))
                width = max(140 if "precio" in input_box["title"].lower() else 300, txt_surface.get_width() + 10)
                input_box["rect"].w = width

                title_surface = title_font.render(input_box["title"], True, (255, 255, 255))
                screen.blit(title_surface, (input_box["rect"].x, input_box["rect"].y - 30))
                pg.draw.rect(screen, color, input_box["rect"], 2)
                screen.blit(txt_surface, (input_box["rect"].x + 5, input_box["rect"].y + 10))

            # Dibuja los botones de "Buscar" y "Cancelar"
            pg.draw.rect(screen, VERDE, button_search)  # Botón Buscar en verde
            pg.draw.rect(screen, ROJO, button_cancel)   # Botón Cancelar en rojo

            # Texto en los botones
            search_surface = font.render('Buscar', True, (255, 255, 255))
            cancel_surface = font.render('Cancelar', True, (255, 255, 255))
            screen.blit(search_surface, (button_search.x + 10, button_search.y + 5))
            screen.blit(cancel_surface, (button_cancel.x + 10, button_cancel.y + 5))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                if event.type == pg.MOUSEBUTTONDOWN:
                    # Verificar si se hace clic en alguna caja de texto
                    for input_box in [input_box_nombre, input_box_categoria, input_box_precio_min, input_box_precio_max]:
                        if input_box["rect"].collidepoint(event.pos):
                            input_box["active"] = not input_box["active"]
                        else:
                            input_box["active"] = False

                    # Verificar si se hace clic en el botón de "Buscar" o "Cancelar"
                    if button_search.collidepoint(event.pos):
                        nombre = input_box_nombre["text"] if input_box_nombre["text"] else None
                        categoria = input_box_categoria["text"] if input_box_categoria["text"] else None
                        precio_min = float(input_box_precio_min["text"]) if input_box_precio_min["text"] else None
                        precio_max = float(input_box_precio_max["text"]) if input_box_precio_max["text"] else None
                        self.buscar(nombre, categoria, precio_min, precio_max)
                        done = True

                    if button_cancel.collidepoint(event.pos):
                        done = True

                if event.type == pg.KEYDOWN:
                    # Si una de las cajas está activa, escribe el texto en ella
                    for input_box in [input_box_nombre, input_box_categoria, input_box_precio_min, input_box_precio_max]:
                        if input_box["active"]:
                            if event.key == pg.K_BACKSPACE:
                                input_box["text"] = input_box["text"][:-1]
                            else:
                                input_box["text"] += event.unicode

            pg.display.flip()
