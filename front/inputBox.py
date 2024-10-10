import pygame as pg
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color_inactive = (100, 100, 100)
        self.color_active = (0, 120, 215)
        self.color = self.color_inactive
        self.text = text
        self.font = pg.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
    def handle_event(self,event):
        if event.type ==pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active= not self.active
            else:
                self.active=False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True,(255,255,255))
        
    def update(self):
        width=max(200,self.txt_surface.get_width())+10
        self.rect.w=width

    def draw(self,screen):
        pg.draw.rect(screen,self.color,self.rect,2)
        screen.blit(self.txt_surface,(self.rect.x+5,self.rect.y+5))
        
