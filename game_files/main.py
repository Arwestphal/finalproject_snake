import pygame
import random as rnd
pygame.init()

WIDTH, HEIGHT = 1000, 1000
FPS = 60
PIXELSIZE = 100
SPEED = 1
LOOPING = PIXELSIZE // SPEED

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

BACKGROUND = pygame.image.load('game_files/graphics/snake_bg.png').convert_alpha()
HEAD_IMG = [
    pygame.image.load(f'game_files/graphics/snake/s{i}.png').convert_alpha()
    for i in range(24)
]
SAD_SNAKE = pygame.image.load('game_files/graphics/sad_snake.png').convert_alpha()
BODY = pygame.image.load('game_files/graphics/snake_body.png').convert_alpha()
FOOD = pygame.image.load('game_files/graphics/apple.png').convert_alpha()

pygame.mixer.music.load("game_files/audio/snake_music.mp3")
pygame.mixer.music.play(-1, 0.0)

font_1 = pygame.font.Font('game_files/font/Pixeltype.ttf', 300)
font_2 = pygame.font.Font('game_files/font/Pixeltype.ttf', 100)
font_3 = pygame.font.Font('game_files/font/Pixeltype.ttf', 70)
font_4 = pygame.font.Font('game_files/font/Pixeltype.ttf', 50)

text_1 = font_1.render("SNAKE", True, (0, 0, 0))
text_2 = font_2.render("Created by Andrew Westphal", True, (0, 0, 0))
text_3 = font_2.render("And Abdullah Malik", True, (0, 0, 0))
text_4 = font_3.render("Press any arrow key to start", True, (0, 0, 0))
victory_text = font_1.render("VICTORY", True, (0, 0, 0))
gameover_text = font_1.render("GAMEOVER", True, (0, 0, 0))
reset_text = font_3.render("Press SPACE to reset", True, (0, 0, 0))

text_1_rect = text_1.get_rect(center = (500, 230))
text_2_rect = text_2.get_rect(center = (500, 660))
text_3_rect = text_3.get_rect(center = (500, 760))
text_4_rect = text_4.get_rect(center = (500, 860))
gameover_rect = gameover_text.get_rect(center = (500, 530))
victory_rect = victory_text.get_rect(center = (500, 530))
reset_rect = reset_text.get_rect(center = (500, 660))

def titlescreen(head, head_img, food, score, highscore):
	WIN.fill((0, 0, 0))
	WIN.blit(BACKGROUND, (0, 0))
	WIN.blit(FOOD, (food.x, food.y))
	WIN.blit(head_img, (head.x, head.y))
	WIN.blit(text_1, text_1_rect)
	WIN.blit(text_2, text_2_rect)
	WIN.blit(text_3, text_3_rect)
	WIN.blit(text_4, text_4_rect)
	score_text = font_4.render(f"Score: {score}", True, (0, 0, 0))
	highscore_text = font_4.render(f"Highscore: {highscore}", True, (0, 0, 0))
	score_rect = score_text.get_rect(center = (80, 20))
	highscore_rect = highscore_text.get_rect(center = (880, 20))
	WIN.blit(score_text, score_rect)
	WIN.blit(highscore_text, highscore_rect)
	pygame.display.update()

def draw_window(head, head_img, food, body_x, body_y, score, highscore):
	WIN.fill((0, 0, 0))
	WIN.blit(BACKGROUND, (0, 0))
	if len(body_x) > 0:
		for i in range(len(body_x)):
			WIN.blit(BODY, (body_x[i], body_y[i]))
	WIN.blit(FOOD, (food.x, food.y))
	WIN.blit(head_img, (head.x, head.y))
	score_text = font_4.render(f"Score: {score}", True, (0, 0, 0))
	highscore_text = font_4.render(f"Highscore: {highscore}", True, (0, 0, 0))
	score_rect = score_text.get_rect(center = (80, 20))
	highscore_rect = highscore_text.get_rect(center = (880, 20))
	WIN.blit(score_text, score_rect)
	WIN.blit(highscore_text, highscore_rect)
	pygame.display.update()

def victoryscreen(head, head_img, food, body_x, body_y, score, highscore):
	WIN.fill((0, 0, 0))
	WIN.blit(BACKGROUND, (0, 0))
	if len(body_x) > 0:
		for i in range(len(body_x)):
			WIN.blit(BODY, (body_x[i], body_y[i]))
	WIN.blit(FOOD, (food.x, food.y))
	WIN.blit(head_img, (head.x, head.y))
	score_text = font_4.render(f"Score: {score}", True, (0, 0, 0))
	highscore_text = font_4.render(f"Highscore: {highscore}", True, (0, 0, 0))
	score_rect = score_text.get_rect(center = (80, 20))
	highscore_rect = highscore_text.get_rect(center = (880, 20))
	WIN.blit(score_text, score_rect)
	WIN.blit(highscore_text, highscore_rect)
	WIN.blit(victory_text, victory_rect)
	WIN.blit(reset_text, reset_rect)
	pygame.display.update()

def gameoverscreen(head, head_img, food, body_x, body_y, score, highscore):
	WIN.fill((0, 0, 0))
	WIN.blit(BACKGROUND, (0, 0))
	if len(body_x) > 0:
		for i in range(len(body_x)):
			WIN.blit(BODY, (body_x[i], body_y[i]))
	WIN.blit(FOOD, (food.x, food.y))
	WIN.blit(head_img, (head.x, head.y))
	score_text = font_4.render(f"Score: {score}", True, (0, 0, 0))
	highscore_text = font_4.render(f"Highscore: {highscore}", True, (0, 0, 0))
	score_rect = score_text.get_rect(center = (80, 20))
	highscore_rect = highscore_text.get_rect(center = (880, 20))
	WIN.blit(score_text, score_rect)
	WIN.blit(highscore_text, highscore_rect)
	WIN.blit(gameover_text, gameover_rect)
	WIN.blit(reset_text, reset_rect)
	pygame.display.update()

def getstart(queue):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				queue.append(1)
			elif event.key == pygame.K_DOWN:
				queue.append(3)
			elif event.key == pygame.K_LEFT:
				queue.append(4)
			elif event.key == pygame.K_RIGHT:
				queue.append(2)

def getkey(queue):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and queue[-1] != 3:
				queue.append(1)
			elif event.key == pygame.K_DOWN and queue[-1] != 1:
				queue.append(3)
			elif event.key == pygame.K_LEFT and queue[-1] != 2:
				queue.append(4)
			elif event.key == pygame.K_RIGHT and queue[-1] != 4:
				queue.append(2)

def newgame():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				return False
	return True

def main():
	game = True
	highscore = 0
	while game:
		head = pygame.Rect(200, 400, PIXELSIZE, PIXELSIZE)
		food = pygame.Rect(700, 400, PIXELSIZE, PIXELSIZE)
		head_img = pygame.transform.rotate(HEAD_IMG[0], 90)
		head_frame = 0
		animation_speed = 30
		frame_counter = 0
		clock = pygame.time.Clock()
		queue = []
		score = 0
		while not queue:
			getstart(queue)
			titlescreen(head, head_img, food, score, highscore)
		body_x = []
		body_y = []
		body_direction = []
		body_x.append(head.x)
		body_y.append(head.y)
		body_direction.append(queue[0])
		running = True
		victory = False
		gameover = False
		while running:
			clock.tick(FPS)
			getkey(queue)
			for i in range(LOOPING):
				if queue[0] == 1:
					head.y -= SPEED
					head_img = pygame.transform.rotate(HEAD_IMG[head_frame], 180)
				elif queue[0] == 3:
					head.y += SPEED
					head_img = pygame.transform.rotate(HEAD_IMG[head_frame], 0)
				elif queue[0] == 4:
					head.x -= SPEED
					head_img = pygame.transform.rotate(HEAD_IMG[head_frame], 270)
				elif queue[0] == 2:
					head.x += SPEED
					head_img = pygame.transform.rotate(HEAD_IMG[head_frame], 90)
				
				for b in range(len(body_direction)):
					if body_direction[b] == 1:
						body_y[b] -= SPEED
					elif body_direction[b] == 3:
						body_y[b] += SPEED
					elif body_direction[b] == 4:
						body_x[b] -= SPEED
					elif body_direction[b] == 2:
						body_x[b] += SPEED

				frame_counter += 1
				if frame_counter >= animation_speed:
					head_frame = (head_frame + 1) % len(HEAD_IMG)
					frame_counter = 0

				draw_window(head, head_img, food, body_x, body_y, score, highscore)
			
			if len(queue) > 1:
				del queue[0]
			body_direction.insert(0, queue[0])
			body_direction.pop()
			if head.x == food.x and head.y == food.y:
				score += 1
				if score > highscore:
					highscore = score
				food.x = rnd.randint(0, (WIDTH // PIXELSIZE) - 1) * PIXELSIZE
				food.y = rnd.randint(0, (HEIGHT // PIXELSIZE) - 1) * PIXELSIZE
				if len(body_direction) > 1:
					if body_direction[-1] == 1:
						body_x.append(body_x[-1])
						body_y.append(body_y[-1] + PIXELSIZE)
					elif body_direction[-1] == 3:
						body_x.append(body_x[-1])
						body_y.append(body_y[-1] - PIXELSIZE)
					elif body_direction[-1] == 4:
						body_x.append(body_x[-1] + PIXELSIZE)
						body_y.append(body_y[-1])
					elif body_direction[-1] == 2:
						body_x.append(body_x[-1] - PIXELSIZE)
						body_y.append(body_y[-1])
					body_direction.append(body_direction[-1])
				elif len(body_direction) > 0:
					if body_direction[0] == 1:
						body_x.append(body_x[0])
						body_y.append(body_y[0] + PIXELSIZE)
					elif body_direction[0] == 3:
						body_x.append(body_x[0])
						body_y.append(body_y[0] - PIXELSIZE)
					elif body_direction[0] == 4:
						body_x.append(body_x[0] + PIXELSIZE)
						body_y.append(body_y[0])
					elif body_direction[0] == 2:
						body_x.append(body_x[0] - PIXELSIZE)
						body_y.append(body_y[0])
					body_direction.append(body_direction[0])
			if score < 99:
				if (head.y == 0 and queue[0] == 1):
					running = False
					gameover = True
					head_img = pygame.transform.rotate(SAD_SNAKE, 180)
				elif head.y == HEIGHT - PIXELSIZE and queue[0] == 3:
					running = False
					gameover = True
					head_img = pygame.transform.rotate(SAD_SNAKE, 0)
				elif head.x == 0 and queue[0] == 4:
					running = False
					gameover = True
					head_img = pygame.transform.rotate(SAD_SNAKE, 270)
				elif head.x == WIDTH - PIXELSIZE and queue[0] == 2:
					running = False
					gameover = True
					head_img = pygame.transform.rotate(SAD_SNAKE, 90)
				for b in range(1, len(body_direction)-1, 1):
					if body_x[b] == head.x and body_y[b] == head.y:
						running = False
						gameover = True
					elif ((body_x[b] == head.x) and (body_y[b] == head.y - PIXELSIZE)) and queue[0] == 1:
						running = False
						gameover = True
						head_img = pygame.transform.rotate(SAD_SNAKE, 180)
					elif ((body_x[b] == head.x) and (body_y[b] == head.y + PIXELSIZE)) and queue[0] == 3:
						running = False
						gameover = True
						head_img = pygame.transform.rotate(SAD_SNAKE, 0)
					elif ((body_x[b] == head.x - PIXELSIZE) and (body_y[b] == head.y)) and queue[0] == 4:
						running = False
						gameover = True
						head_img = pygame.transform.rotate(SAD_SNAKE, 270)
					elif ((body_x[b] == head.x + PIXELSIZE) and (body_y[b] == head.y)) and queue[0] == 2:
						running = False
						gameover = True
						head_img = pygame.transform.rotate(SAD_SNAKE, 90)
			else:
				running = False
				victory = True
		while victory:
			victoryscreen(head, head_img, food, body_x, body_y, score, highscore)
			victory = newgame()
		while gameover:
			gameoverscreen(head, head_img, food, body_x, body_y, score, highscore)
			gameover = newgame()
	pygame.quit()

if __name__ == "__main__":
    main()