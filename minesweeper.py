import random
import numpy as np
import pygame , sys

n,k = 5 , 5
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700

class Board():
	"""docstring for Board"""
	def __init__(self,n,k):
		self.n = n
		self.k = k
		self.boxes = []

	def drawGrid(self):
		blockSize = WINDOW_WIDTH // self.n 
		for x in range(0, WINDOW_WIDTH, blockSize):
			for y in range(0, WINDOW_HEIGHT, blockSize):
				rect = pygame.Rect(x, y, blockSize, blockSize)
				pygame.draw.rect(SCREEN, WHITE, rect, 1)

				self.boxes.append([rect,(x//blockSize,y//blockSize)])


	def CreateBoard(self):
		arr = np.full((self.n, self.n), 0, dtype=int)
		return arr
	
	def PlaceBombs(self):
		arr = self.CreateBoard()
		n=self.n
		k=self.k
		for num in range(k):
			x = random.randint(0,n-1)
			y = random.randint(0,n-1)
			arr[y][x] = -1

			if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
				if arr[y][x+1] != -1:
					arr[y][x+1] += 1

			if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
				if arr[y][x-1] != -1:
					arr[y][x-1] += 1

			if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
				if arr[y-1][x-1] != -1:
					arr[y-1][x-1]+= 1

			if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
				if arr[y-1][x+1] != -1:
					arr[y-1][x+1] += 1

			if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
				if arr[y-1][x] != -1:
					arr[y-1][x] += 1

			if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
				if arr[y+1][x+1]!= -1:
					arr[y+1][x+1] += 1      

	
			if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
				if arr[y+1][x-1] != -1:
					arr[y+1][x-1] += 1 

			if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
				if arr[y+1][x] != -1:
					arr[y+1][x] += 1 
		return arr
		
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()

        	


def main():
	over=False
	board = Board(n, k)
	answer = board.PlaceBombs()
	print(answer)
	pygame.init()
	
	SCREEN.fill(BLACK)
    
	
	while True:
		board.drawGrid()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN and over==False:
				for box in board.boxes:
					if(box[0].collidepoint(pygame.mouse.get_pos())):
						(y,x) = box[1]
						print(box[1])
						if(answer[x][y]==-1):
							print("GAME OVER")
							font = pygame.font.Font(None, 150)
							text = font.render("GAME OVER", True, WHITE)
							text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
							SCREEN.blit(text,text_rect)
							over=True

						else:
							print(answer[x][y])

							font = pygame.font.Font(None, 100)
							text = font.render(str(answer[x][y]), True, WHITE)


							SCREEN.blit(text,box[0].center)





						break
				 


				


		pygame.display.update()
		CLOCK.tick(30)


		




main()