import pygame

def drawgrid():
  for row in range(14):
    pygame.draw.line(screen,"black",(0,row*h/14),(w,row*h/14),5)
  for column in range(0,11):
    pygame.draw.line(screen,"black",(column*w/10,0),(column*w/10,h),5)

#draws screen based on array
def draw_10x14_tetris_array(tetris_array):
  for y in range(13,0,-1):
    for x in range(10):
      if(tetris_array[y][x]==1):
        # print(f'x: {w/10*x} y: {h/10*y}')
        pygame.draw.rect(screen,"orange",pygame.Rect(w/10*x, h/14*y, w/10 + 1 ,h/14 + 1))
      elif tetris_array[y][x] == 2:
        pygame.draw.rect(screen,"dark orange",pygame.Rect(w/10*x, h/14*y, w/10 + 1 ,h/14 + 1))


pygame.init()
screen = pygame.display.set_mode((1600,1200),pygame.RESIZABLE)
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/PixelEmulator-xq08.ttf",30)

#screen dimens text


test_tetris_array =  [[0,0,1,0,0,0,0,0,0,0],
                      [0,0,1,0,0,0,0,0,0,0],
                      [0,0,1,1,0,0,0,0,0,0],
                      [0,1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,1],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,0,1,0,0,0,0,0],
                      [0,0,0,0,0,1,0,0,0,0],
                      [0,0,0,0,0,1,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,1,0,0,0,0],
                      [1,0,0,0,0,0,0,0,0,0],]

test_tetris_array2 = [[0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],]


new_array =         [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],]


while True:

  w, h = pygame.display.get_surface().get_size()

  screen_dimension_text_surf = text_font.render(f"width: {w} height: {h}",False,(128,233,0))
  screen_dimension_text_rect = screen_dimension_text_surf.get_rect(center=(w/2,h/2))
  screen.blit(screen_dimension_text_surf,screen_dimension_text_rect)


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  
  screen.fill("white")

#draw checker pattern
  # for y in range(w//4):
  #   for x in range(h//4):
  #     test_surf = pygame.Surface((15,15))
  #     if((x)+(y))%2 == 1:
  #       test_surf.fill("red")
  #     else:
  #       test_surf.fill((0, 0, 0))
  #     screen.blit(test_surf,(15*x,y*15))
  
  #line grid
  # drawgrid()

  #take 14x10 array --> colors that specific part of the array which is 1 in grid 

  draw_10x14_tetris_array(test_tetris_array2)

  #example syntaxs
    # to make a square 
    # pygame.draw.rect(screen,"orange",pygame.Rect(coordinate x,coordinate y,box x,box y))

  # traverse every cell if value equals 1 put a square beneath it and delete the current cell in the original
  # make the first array equal to the second array
  # after every time we put all squares in to their new position print the array

  for y in range(13,0,-1):
    for x in range(10):
      
      if(test_tetris_array2[y][x]==1):
        
        if y+1 == 14 :
          test_tetris_array2[y][x] = 0
          new_array[y][x] = 2
          for sub_y in range(12,0,-1):
            if test_tetris_array2[sub_y][x] == 1 or new_array[sub_y][x] == 1:
              print("asfsafasf")
              new_array[sub_y][x] = 2
              test_tetris_array2[sub_y][x] = 2

        elif (test_tetris_array2[y+1][x] == 2 or new_array[y+1][x] == 2):
          print("runing!")
          test_tetris_array2[y][x] = 0
          new_array[y][x] = 2
          for sub_y in range(13,0,-1):
            if test_tetris_array2[sub_y][x] == 1 or new_array[sub_y][x] == 1:
              print("asfsafasf")
              new_array[sub_y][x] = 2
              test_tetris_array2[sub_y][x] = 2


        else:
          # print("muah")
          new_array[y+1][x] = 1
          test_tetris_array2[y][x] = 0
          
      # elif test_tetris_array2[y][x] == 2:
      #      for sub_y in range(14):
      #       if(test_tetris_array2[sub_y][x] == 1 or new_array[sub_y][x]==1):
      #         print("ahh")
      #         new_array[sub_y][x] = 2

  temp_array = test_tetris_array2
  test_tetris_array2 = new_array
  new_array = temp_array
  
  


  draw_10x14_tetris_array(test_tetris_array2)







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

  #scratch this 

  pygame.display.update()
  clock.tick(0.7)