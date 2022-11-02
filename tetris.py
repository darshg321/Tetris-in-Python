import pygame, random, sys
pygame.init()
pygame.mixer.init()

fps = pygame.time.Clock()
screen = pygame.display.set_mode([1280, 720])

WHITE = (255, 255, 255)

btn_img = pygame.image.load("assets\images\\button.png")
btn_img = pygame.transform.scale(btn_img, (300, 90))

def get_font(size):
    return pygame.font.Font("assets\\font\hundin.ttf", size)

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
    
    bgnum = random.randint(1, 5)
    bg = pygame.image.load(f'assets\images\\bg{bgnum}.png')
    bg = pygame.transform.scale(bg, (1280, 720))
    grid = pygame.image.load(f'assets\images\\grid.png')
    grid = pygame.transform.scale(grid, (350, 720))
    
    while True:
        screen.blit(bg, (0,0))
        screen.blit(grid, (465, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        pygame.display.update()
        fps.tick(60)
    
def game_over():
    pygame.display.set_caption("Game Over!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        pygame.display.update()
        fps.tick(60)

def main_menu():
    pygame.display.set_caption("Main Menu")
    
    bgnum = random.randint(1, 5)
    bg = pygame.image.load(f'assets\images\\bg{bgnum}.png')
    bg = pygame.transform.scale(bg, (1280, 720))
    
    title_font = pygame.font.Font("assets\\font\\hundin.ttf", 100)
    title = title_font.render('Tetris!', True, WHITE)
    title_rect = title.get_rect(center= (640, 100))
    
    while True:
        screen.blit(bg, (0,0))
        screen.blit(title, title_rect)
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        play_btn = Button(image=btn_img, pos=(640, 300), text_input="Play",
                            font=get_font(65), base_color="White", hovering_color="#00d9ff")
        quit_btn = Button(image=btn_img, pos=(640, 500), text_input="Quit",
                            font=get_font(65), base_color="White", hovering_color="#00d9ff")
        
        for button in [play_btn, quit_btn]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                if quit_btn.checkForInput(MENU_MOUSE_POS):
                    sys.exit(0)
        
        pygame.display.update()
        fps.tick(60)

main_menu()