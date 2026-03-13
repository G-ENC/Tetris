import pygame
import numpy 
import math

def checker_pattern():
  for y in range(w//4):
    for x in range(h//4):
      test_surf = pygame.Surface((15,15)).convert_alpha()
      if((x)+(y))%2 == 1:
        test_surf.fill("red")
      else:
        test_surf.fill((0, 0, 0))
      screen.blit(test_surf,(15*x,y*15))

def drawgrid():
  for row in range(14):
    pygame.draw.line(screen,"#662C91",(0,row*h/14),(w,row*h/14),5)
  for column in range(0,11):
    pygame.draw.line(screen,"#662C91",(column*w/10,0),(column*w/10,h),5)

def is_game_active(tetris_array):
  game_active = False
  for y in range(19,5,-1):
    if (1 in tetris_array[y]):
      game_active = True
  return game_active  

def draw_10x14_tetris_array(tetris_array):
  for y in range(19,5,-1):
    for x in range(10):
      if(tetris_array[y][x]==1):
        # print(f'x: {w/10*x} y: {h/10*y}')
        pygame.draw.rect(screen,"#17A398",pygame.Rect(w/10*x, h/14*y, w/10 + 1 ,h/14 + 1))
      elif tetris_array[y][x] == 2:
        pygame.draw.rect(screen,"#EE6C4D",pygame.Rect(w/10*x, h/14*y, w/10 + 1 ,h/14 + 1))

def falling_logic_from_array(tetris_array):
      #spawing tetromino
  #idea: there is a bacg of random tetromino 
  #but a single teromno will be spawed with its whole pasted direct at the center of the board
  #if there could not be a viable spot then then gemo over ---- later

  #if there is 1 in the whole array the dont let another block to drop
  #we will controll the tetromino by keydown then shifting the array at that instant

  first_x_pos, x_length = 0, 1
  fuckass_flag = 0

  # determines the surface of the tetromino based on its position to the array
  if(not fuckass_flag):
    for y in range(19,5,-1):
      for x in range(10):
        if tetris_array[y][x] == 1 and not fuckass_flag:
          first_x_pos = x
          fuckass_flag = 1
          for x_sub in range(10-x):
            if(tetris_array[y][x+x_sub] == 1):
              x_length += 1

  for y in range(13,-1,-1):
    for x in range(10):

      if tetris_array[y][x]==1 :
        #if touched bottom freeze
        if y+1 == 14 :
          tetris_array[y][x] = 2

          #freeze the same column
          #idea: search if until the adjascent top of the block is 1 unless LEAVE TGHE FUCK OUT 
          #result: KUDOS
          for sub_y in range(12,0,-1):
            if tetris_array[sub_y][x] == 2:
              if tetris_array[sub_y+1][x] == 1:
                tetris_array[sub_y][x] = 2

        #freeze if there is a block beneath that is frozen
        elif (2 in tetris_array[y+1][first_x_pos:first_x_pos+x_length-1]) :
          for sub_y in range(13,-1,-1):
            for sub_x in range(10):

              if(tetris_array[sub_y][sub_x]==1):
                tetris_array[sub_y][sub_x] = 2

        #drop square
        else:
          tetris_array[y][x] = 0
          tetris_array[y+1][x] = 1

def spawn_teromino_from_array(tetris_array,I_tetromino):
  if(is_game_active(tetris_array) == False):
    for y in range(4):
        for x in range(3,7):
          if(tetris_array[y][x] == 0):
            tetris_array[y][x] = I_tetromino[0][y][x-3]

def eliminate_and_drop_row(tetris_array):
  #travers each row if it doesnt have a 1 or 0 then make it all 0
  #drop every index by 1 height
  for y in range(13,-1,-1):
    if( 0 in tetris_array[y] or 1 in tetris_array[y]) == False:
      tetris_array[y] = [0,0,0,0,0,0,0,0,0,0]
    #shift array down by 1
      for sub_y in range(y,0,-1):
        for sub_x in range(10):
          if(tetris_array[sub_y-1][sub_x] != 1):
            tetris_array[sub_y][sub_x] = tetris_array[sub_y-1][sub_x] 
          else:
            tetris_array[sub_y][sub_x] = 0 

I_tetromino = [
   [1,1,1,1],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
],[[0,0,1,0],
   [0,0,1,0],
   [0,0,1,0],
   [0,0,1,0]]





tetromino_array = []

pygame.init()
screen = pygame.display.set_mode((1600,1200),pygame.RESIZABLE)
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/PixelEmulator-xq08.ttf",30)

#screen dimens text


new_array =          [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0,0],
                      [1,1,1,0,0,0,0,1,1,1],
                      [1,1,1,0,0,0,0,1,1,1],
                      [1,1,1,0,1,1,1,1,1,1],
                      [0,0,0,0,0,1,0,0,0,1],]


cooldown = 0
delay = 5

key_cooldown = 0
key_delay = 1

while True:



#drawscreen
  w, h = pygame.display.get_surface().get_size()
  
  screen_dimension_text_surf = text_font.render(f"width: {w} height: {h}",False,(128,233,0))
  screen_dimension_text_rect = screen_dimension_text_surf.get_rect(center=(w/2,h/2))
  screen.blit(screen_dimension_text_surf,screen_dimension_text_rect)

#event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
   
   # drop one block on click 
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        mouse_x_array = math.floor(event.pos[0]/(w/10))
        mouse_y_array = math.floor(event.pos[1]/(h/14))
        new_array[mouse_y_array][mouse_x_array] = 1
  
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 3:
        mouse_x_array = math.floor(event.pos[0]/(w/10))
        mouse_y_array = math.floor(event.pos[1]/(h/14))
        new_array[mouse_y_array] = [1,1,1,1,1,1,1,1,1,1]

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        pygame.quit()
        exit() 
  # move tetris block by one when down arrow is clicked

 
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_DOWN:
      print("click")
      cooldown -= 1

      
                

  screen.fill("white")

  
  drawgrid()

  draw_10x14_tetris_array(new_array)

  spawn_teromino_from_array(new_array,I_tetromino)
  
  delta = clock.tick() / 5
  cooldown -= delta

  # print(cooldown)

  if(cooldown<=0):

    cooldown = delay

    falling_logic_from_array(new_array)    


    eliminate_and_drop_row(new_array)


    
 




  print(numpy.array(new_array))
  

  pygame.display.update()
  clock.tick(60)



#example syntaxs:-------------------------------------------
  # to make a square 
  # pygame.draw.rect(screen,"orange",pygame.Rect(coordinate x,coordinate y,box x,box y))

  #numpy 2d array pretty in print
  # a = numpy.array(test_tetris_array2)
  # b = numpy.array(new_array)


#idea 1
  #make a second array from the first array looking at the positions of the 1 values and make them go 
  #1 unit in the y direction ([y+1][x]) and if the 1 is at bottom or touches another 2 make that cell a 2
  #make the ones fall


#idea 2 

  #make the squares an acutal exntity that can colide
  #how to mkae custom hitboxes are issue for another day


#notes:
  # maybe drawing the array based on the position isnt suitable since 
  # the game will be jittry and skip[ the interavls of steps it take 
  # gonna retry with a rectangel object that falss based on its y value
  # and checking for collsions taht way will resolve my issue ig
  #scratch this original tetris is jittry too 
