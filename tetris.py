import pygame, random, sys
pygame.init()
pygame.mixer.init()

fps = pygame.time.Clock()
screen = pygame.display.set_mode([1280, 720])

WHITE = (255, 255, 255)

def drawStyleRect(surface):
    pygame.draw.rect(surface, (30, 29, 45), (400, 300, 880, 90), 0)
    
    for i in range(4):
        pygame.draw.rect(surface, (0, 0, 0), (400-i, 300-i, 880, 90), 1)

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def game_loop():
    pygame.display.set_caption("Tetris")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        pygame.display.update
        fps.tick(60)
    
def game_over():
    pygame.display.set_caption("Game Over!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        pygame.display.update
        fps.tick(60)

def main_menu():
    pygame.display.set_caption("Main Menu")
    
    bgnum = random.randint(1, 5)
    bg = pygame.image.load(f'assets\images\\bg{bgnum}.png')
    bg = pygame.transform.scale(bg, (1280, 720))
    
    while True:
        screen.blit(bg, (0,0))
        
        # pygame.draw.rect(screen, (30, 29, 45), (400, 300, 880, 70))
        
        drawStyleRect(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        
        pygame.display.update()
        fps.tick(60)

main_menu()