from ..back.controller.controller import Controller as ctrl
import pygame as pg
from ..front.inicio import Inicio 

class ventanaBase():
    def __init__(self):
        self.controller = ctrl()

    def validar_mouse(self, mouse_pos,posiciones):
        if posiciones[0][0] <= mouse_pos[0] <= posiciones[0][0] + 200 and posiciones[0][1] <= mouse_pos[1] <= posiciones[0][1] + 100:
         self.estado = "agregar_producto"  # Cambia el estado a "agregar_producto" 
        if posiciones[1][0] <= mouse_pos[0] <= posiciones[1][0] + 200 and posiciones[1][1] <= mouse_pos[1] <= posiciones[1][1] + 100:
            self.estado="Modificar elemento"  # Aquí puedes cambiar el estado a una función específica
        if posiciones[2][0] <= mouse_pos[0] <= posiciones[2][0] + 200 and posiciones[2][1] <= mouse_pos[1] <= posiciones[2][1] + 100:
            print("Borrar elemento")  # Aquí puedes cambiar el estado a una función específica
        if posiciones[3][0] <= mouse_pos[0] <= posiciones[3][0] + 200 and posiciones[3][1] <= mouse_pos[1] <= posiciones[3][1] + 100:
            print("Buscar elemento")  # Aquí puedes cambiar el estado a una función específica
