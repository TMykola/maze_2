from data import *

class Human(pygame.Rect):
    def __init__(self, x,y, width, height, image_list, step):
        super().__init__(x, y ,width, height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_now = self.image
        self.image_count = 0

    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count % 10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count += 1

class Hero(Human):
    def __init__(self, x, y, width, height, image_list, step):
        super().__init__(x, y, width, height, image_list, step)
        self.step = step
        self.walk = {"up": False, "down": False, "left": False, "right": False} 
        self.side = False

    def move(self, window): 
        if self.walk ["up"] and self.y > 0: 
            self.y -= self.step 
            if self.collidelist(wall_list) != -1: 
                self.y += self.step 
        if self.walk["down"] and self.y + self.height < size_window[1]: 
            self.y += self.step 
            if self.collidelist(wall_list) != -1: 
                self.y -= self.step 
        if self.walk ["left"] and self.x > 0: 
            self.x -= self.step 
            if self.collidelist(wall_list) != -1: 
                self.x += self.step 
            self.side = True 
        if self.walk["right"] and self.x + self.width < size_window[0]: 
            self.x += self.step 
            if self.collidelist(wall_list) != -1: 
                self.x -= self.step 
                self.side = False 
        for value in list(self.walk.values()): 
            if value: 
                self.move_image() 
                break 
        else: 
            self.image = self.image_list[0] 
        if self.side: 
            self.image_now = pygame.transform.flip(self.image, True, False) 
        else: 
            self.image_now = self.image
        
        window.blit(self.image_now, (self.x, self.y))


class Bot(Human):
    def __init__(self, x, y, width, height, image_list, step):
        super().__init__(x, y, width, height, image_list, step)

class Wall(pygame.Rect):
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width, height)
        self.color = color

def create_wall(new_map):
    x,y = 0,0
    width, height = 15, 15
    for line in new_map:
        for element in line:
            if element == "1":
                wall_list.append(Wall(x,y,width,height,BLACK))
            x += width
        x = 0
        y += height

create_wall(maps["LVL1"]["map"])