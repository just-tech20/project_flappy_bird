# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:31:15 2019

@author: Jatin
"""

import pygame as pg
import random
import time

pg.init()


White = (255,255,255)
display_width = 650
display_height = 670
bgImg = pg.image.load('bg1.png')
up_pipeImg = pg.image.load('up_pipe.png')
down_pipeImg = pg.image.load('down_pipe.png')
birdImg = pg.image.load('Flappy_Bird.png')
score = pg.image.load('score.png')
intro_bg = pg.image.load('angry_bird.jpg')
gameOver = pg.image.load('gameover_birds.jpg')
play = pg.image.load('play.png')
retry = pg.image.load('retry.png')
quitImg = pg.image.load('quit.png')
jump = pg.mixer.Sound("salamisound_jump.wav")
collect = pg.mixer.Sound("collect.wav")
hit = pg.mixer.Sound("hit.wav")

font = pg.font.SysFont('Arial', 32)

birdx = birdy = 60
#up_pipex = 600
#up_pipey = 470       # Length of PIPE = 200
#down_pipex = 600
#down_pipey = -5
Score = 0
green = (0, 255, 0)  
x_pos1 = 0
x_pos2 = 0
start1_up = [400,550]                   #     [400,550]
start1_down = [400,-5]                    #     [400,-5] 
start2_up = [700,550]                   #       [750,550]
start2_down = [700,-5]                  #        [750,-5]
temp_start1_up = [400,550]
temp_start1_down = [400,-5] 
temp_start2_up = [700,550]
temp_start2_down = [700,-5] 
r1 = random.randrange(240,550)
r2 = -(560 - r1)
r3 = random.randrange(240,550)
r4 = -(560 - r3)

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('Flappy Bird')



class pipe():
	def first_pipe(self,up,up_dim,pos_up,down,down_dim,pos_down):
	#def updown_pipe(self,up,up_dim,pos_up,down,down_dim,pos_down):
		#global up_pipex,down_pipex,up_pipey,down_pipey  # To Acces the global variables up_pipex, down_pipex
		global r1,r2,x_pos2,x_pos1,Score
		up_pipex = pos_up[0]
		up_pipey = pos_up[1] = r1
		down_pipex = pos_down[0]
		down_pipey = pos_down[1] = r2
		up_pipImg = pg.transform.scale(up,up_dim)
		gameDisplay.blit(up_pipImg,(up_pipex,up_pipey))
		down_pipImg = pg.transform.scale(down,down_dim)
		gameDisplay.blit(down_pipImg,(down_pipex,down_pipey))
		pos_up[0] = pos_up[0] - 2
		pos_down[0] = pos_down[0] - 2
		x_pos1 = pos_up[0]

		if (pos_up[0] + 100 == 0):
			pg.mixer.Sound.play(collect)
			Score += 1
			global start1_up,start1_down
			pos_up[0] = pos_down[0] = x_pos2 + 300      
			#pos_down[0] = start1_down[0]
			r1 = random.randrange(240,550)
			r2 = -(560 - r1)

	def second_pipe(self,up,up_dim,pos_up,down,down_dim,pos_down):
		global r3,r4,x_pos1,x_pos2,Score
		up_pipex = pos_up[0]
		up_pipey = pos_up[1] = r3
		down_pipex = pos_down[0]
		down_pipey = pos_down[1] = r4
		up_pipImg = pg.transform.scale(up,up_dim)
		gameDisplay.blit(up_pipImg,(up_pipex,up_pipey))
		down_pipImg = pg.transform.scale(down,down_dim)
		gameDisplay.blit(down_pipImg,(down_pipex,down_pipey))
		pos_up[0] = pos_up[0] - 2
		pos_down[0] = pos_down[0] - 2
		x_pos2 = pos_up[0]

		if (pos_up[0] + 100 == 0):
			pg.mixer.Sound.play(collect)
			Score += 1 
			global start2_up,start2_down
			pos_up[0] = pos_down[0] = x_pos1 + 300
			#pos_down[0] = start2_down[0]
			r3 = random.randrange(240,550)
			r4 = -(560 - r3)


def crash():
	global Score
	pg.mixer.Sound.play(hit)
	time.sleep(1)
	pg.mixer.music.load('Loadingloop.wav')
	pg.mixer.music.play(-1)
	#print("You have been Crashed")
	clock = pg.time.Clock()
	intro = True
	#gameExit = True
	while intro:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				intro = False
				pg.quit()
				quit()


		gameDisplay.fill(White)
		gameOverImg = pg.transform.scale(gameOver,(display_width,display_height))
		gameDisplay.blit(gameOverImg,(-10,-5))
		gameDisplay.blit(score,(315,100))
		text = font.render(str(Score), True, green)
		textRect = text.get_rect() 
		textRect.center = (392,120) 
		gameDisplay.blit(text, textRect)
		gameDisplay.blit(retry,(80,470))
		gameDisplay.blit(quitImg,(420,460))

		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()
		if 80 < mouse[0] < 285 and 460 < mouse[1] < 539: 
			big_retry = pg.transform.scale(retry,(220,90))
			gameDisplay.blit(big_retry,(70,460))
			if click[0] == 1:
				Score = 0
				gameLoop()
		elif 420 < mouse[0] < 616 and 450 < mouse[1] < 541:
			big_quit = pg.transform.scale(quitImg,(210,90))
			gameDisplay.blit(big_quit,(410,455))
			if click[0] == 1:
				pg.quit()
				quit()

		pg.display.update()
		clock.tick()


def gameIntro():
	global gameDisplay
	clock = pg.time.Clock()
	pg.mixer.music.load('Dream.mp3')
	pg.mixer.music.play(-1)
	intro = True
	while intro:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				intro = False
				pg.quit()
				quit()

		gameDisplay.fill(White)
		intro_bfImg = pg.transform.scale(intro_bg,(display_width,display_height))
		gameDisplay.blit(intro_bfImg,(0,0))
		play_button = pg.transform.scale(play,(70,70))
		gameDisplay.blit(play_button,(280,280))

		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()
		if 294 < mouse[0] < 337 and 292 < mouse[1] < 339: 
			play_button = pg.transform.scale(play,(110,110))
			gameDisplay.blit(play_button,(270,270))
			if click[0] == 1:
				intro = False
		pg.display.update()
		clock.tick(100)
		

def gameLoop():
	global gameDisplay,birdy
	birdx = birdy = 60
	x_pos1 = 0
	x_pos2 = 0
	start1_up = [400,550]                   #     [400,550]
	start1_down = [400,-5]                    #     [400,-5] 
	start2_up = [700,550]                   #       [750,550]
	start2_down = [700,-5]                  #        [750,-5]
	temp_start1_up = [400,550]
	temp_start1_down = [400,-5] 
	temp_start2_up = [700,550]
	temp_start2_down = [700,-5] 
	r1 = random.randrange(240,550)
	r2 = -(560 - r1)
	r3 = random.randrange(240,550)
	r4 = -(560 - r3)
	clock = pg.time.Clock()

	pg.mixer.music.load('one.mp3')
	pg.mixer.music.play(-1)


	gameExit = False

	while not gameExit:
	    for event in pg.event.get():
	        if event.type == pg.QUIT:
	            gameExit = True
	        
	        if event.type == pg.KEYDOWN:
	            if event.key == pg.K_SPACE:
	            	pg.mixer.Sound.play(jump)
	            	birdy = birdy - 80
	                
	        if event.type == pg.KEYUP:
	            if event.key == pg.K_SPACE or event.key == pg.K_p:
	                pass
	            
	    gameDisplay.fill(White)
	    bgImgsize = pg.transform.scale(bgImg,(display_width,display_height))
	    gameDisplay.blit(bgImgsize,(0,0))
	    
	    pipe1 = pipe()
	    #pipe2 = pipe() 
	    #400, 550	400,-5          400,240	  400,-320
	    pipe1.first_pipe(up_pipeImg,(100,450),temp_start1_up,down_pipeImg,(100,450),temp_start1_down) # 300   335           450 450
	    pipe1.second_pipe(up_pipeImg,(100,450),temp_start2_up,down_pipeImg,(100,450),temp_start2_down)
	    
	    gameDisplay.blit(birdImg,(birdx,birdy))
	    gameDisplay.blit(score,(530,10))
	    text = font.render(str(Score), True, green) 
	    textRect = text.get_rect() 
	    textRect.center = (605,30) 
	    gameDisplay.blit(text, textRect) 
	    birdy = birdy + 3

	    if ( ((birdx+43 > temp_start1_up[0] and birdx+43 < (temp_start1_up[0] + 126)) and (birdy+26 > temp_start1_up[1] and birdy+26 < (temp_start1_up[1] + 430)))  or ((birdx+43 > temp_start1_down[0] and birdx+43 < (temp_start1_down[0] + 126)) and (birdy-30 > temp_start1_down[1] and birdy-30 < (temp_start1_down[1] + 390))) or (birdy+30 > display_height or birdy < 1) ):
	    	crash()
	    elif ( ((birdx+43 > temp_start2_up[0] and birdx+43 < (temp_start2_up[0] + 126)) and (birdy+26 > temp_start2_up[1] and birdy+26 < (temp_start2_up[1] + 430)))  or ((birdx+43 > temp_start2_down[0] and birdx+43 < (temp_start2_down[0] + 126)) and (birdy-30 > temp_start2_down[1] and birdy-30 < (temp_start2_down[1] + 390))) ):
	    	crash()


	    pg.display.update()
	    clock.tick(100)


gameIntro()  
gameLoop()

pg.quit()
quit()
