import pygame
from random import randint
import math
from sklearn.cluster import KMeans

def distance(p1,p2):
	return math.sqrt((p1[0] - p2[0])* (p1[0] - p2[0]) + (p1[1] - p2[1])* (p1[1] - p2[1]))
	
pygame.init()

screen = pygame.display.set_mode((1200,700)) # 1200 chiều ngang 700 chiều dọc

pygame.display.set_caption("Yon AI")

running = True

clock = pygame.time.Clock()

background = (214,214,214)
black = (0,0,0)
background_panal = (249, 255, 230)
white = (255,255,255)

red = (255, 0, 0)
green = (0, 255, 34)
blue = (0, 26, 255)
yellow = (255, 255, 0)
purple =(183, 0, 255)
sky = (0, 191, 255)
orange = (255, 145, 0)
grabe= (255, 0, 187)
grass = (255, 149, 0)
COLORS = [red,green,blue,yellow,purple,sky,orange,grabe,grass]

K = 0
error =0
points = []
clusters = []
labels =[]
X = 0
Y = 0


font_x_y = pygame.font.SysFont('sans',20)
font = pygame.font.SysFont('sans',40) # font chữ
text_plus = font.render('+',True,white) # viết ra
reset = font.render('reset',True,white)
run = font.render('run',True,white)
random = font.render('random',True,white)
algorithm = font.render('algorithm',True,white)
minus = font.render('-',True,white)
text_x = font.render('X',True,white)
text_y = font.render('Y',True,white)



while running:
	clock.tick(60) # fps vẽ 60 lần trên 1s
	screen.fill(background) # làm màu cho nền
	pygame.draw.rect(screen,black,(50,50,700,500)) # 50,50 tọa độ góc đầu tiên, 700 chiều ngang, 500 chiều dọc
	pygame.draw.rect(screen,background_panal,(52,52,696,496)) # draw panal
	


	pygame.draw.rect(screen,black,(850,50,50,50)) # draw button K -
	
	pygame.draw.rect(screen,black,(920,50,50,50)) # draw button k -

	pygame.draw.rect(screen,black,(850,200,150,50)) # draw button run
	
	pygame.draw.rect(screen,black,(850,400,150,50)) # draW button random
	
	pygame.draw.rect(screen,black,(850,500,150,50)) # draW button algorithm
	
	pygame.draw.rect(screen,black,(850,600,150,50)) # draW button reset

	pygame.draw.rect(screen,black,(50,600,100,50))

	pygame.draw.rect(screen,black,(200,600,100,50))

	
	
	text_k= font.render('K = ' + str(K), True, black)
	
	text_x = font.render('X =' + str(X),True,white)
	
	text_y = font.render('Y =' + str(X),True,white)
	
	screen.blit(text_plus,(860,60))
	
	screen.blit(minus,(930,60))
	
	screen.blit(run,(860,210))
	
	screen.blit(random,(860,410))
	
	screen.blit(algorithm,(860,510))
	
	screen.blit(reset,(860,610))
	
	
	
	screen.blit(text_k,(980,60))

	screen.blit(text_x,(50,600))

	screen.blit(text_y,(200,600))

	mouse_x, mouse_y = pygame.mouse.get_pos()

	if 52 < mouse_x < 748 and 52 < mouse_y < 548:
		mouse = font_x_y.render('('+ str(mouse_x - 52) + ","+ str(mouse_y - 52) + ')',True,black)
		screen.blit(mouse,(mouse_x + 10,mouse_y))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # so sánh khi nào bạn bấm nút tắt
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			# change k button +

				

			if 52 < mouse_x < 748 and 52 < mouse_y < 548:
				labels = []
				point = [mouse_x - 52, mouse_y - 52]
				points.append(point)
				print(points)
			if 850 < mouse_x < 900 and 50 < mouse_y < 100:
				if K<8:	
					K = K+1
				print("++")
			if 920 < mouse_x < 970 and 50 < mouse_y < 100:
				if K > 0:
					K = K-1
				print("--")
			if 850 < mouse_x < 1000 and 200 < mouse_y < 250:
				labels = []
				if clusters == []:
					continue
				for p in points:
					distances_to_cluster = []
					for c in clusters:
						dis = distance(p,c)
						distances_to_cluster.append(dis)
					
					min_distance = min(distances_to_cluster)
					label = distances_to_cluster.index(min_distance)
					labels.append(label)

				for i in range(K):
					sum_x = 0
					sum_y = 0
					count = 0
					for j in range(len(points)):
						if labels[j] == i:
							sum_x += points[j][0]
							sum_y += points[j][1]
							count += 1

					if count != 0:
						new_cluster_x = sum_x/count
						new_cluster_y = sum_y/count
						clusters[i] = [new_cluster_x, new_cluster_y]
				print("run")
			if 850 < mouse_x < 1000 and 400 < mouse_y < 450:
				clusters = []
				labels = []
				for i in range(K):
					random_point = [randint(0,700), randint(0,500)]
					clusters.append(random_point)
				print("random")
			if 850 < mouse_x < 1000 and 500 < mouse_y < 550:
				
				try:
					kmeans = KMeans(n_clusters=K).fit(points) 
					labels = kmeans.predict(points)
					clusters = kmeans.cluster_centers_
				except:
					print("error")
				print("Algorithm button pressed")

			if 850 < mouse_x < 1000 and 600 < mouse_y < 650:
				K = 0
				error = 0
				points = []
				clusters = []
				labels = []
				print("reset")
	for i in range(len(clusters)):
		pygame.draw.circle(screen,COLORS[i],(int(clusters[i][0]) + 52,int(clusters[i][1]) + 52),10)
	for i in range(len(points)):
		pygame.draw.circle(screen,black,(points[i][0] + 52,points[i][1] + 52),7)
		if labels == []:
			pygame.draw.circle(screen,white,(points[i][0] + 52,points[i][1] + 52),6)
		else:
			pygame.draw.circle(screen,COLORS[labels[i]],(points[i][0] + 52,points[i][1] + 52),6)
	error = 0
	if clusters != [] and labels != []:
		for i in range(len(points)):
			error += distance(points[i], clusters[labels[i]])

	text_error = font.render("Error = " + str(int(error)), True,black)
	screen.blit(text_error,(860,300))

	pygame.display.flip() # tất cả những thứ vẽ ở trên sẽ có hiệu lực
pygame.quit() # thoát toàn bộ pygame khi kết thúc vòng lặp while