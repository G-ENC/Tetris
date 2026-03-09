import pygame

def drawgrid():
  for row in range(14):
    pygame.draw.line(screen,"black",(0,row*h/14),(w,row*h/14),5)
  for column in range(0,11):
    pygame.draw.line(screen,"black",(column*w/10,0),(column*w/10,h),5)

pygame.init()
screen = pygame.display.set_mode((1600,1200),pygame.RESIZABLE)
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/PixelEmulator-xq08.ttf",30)

#screen dimens text

while True:

  w, h = pygame.display.get_surface().get_size()
  
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
  drawgrid()

  #take 14x10 array --> colors that specific part of the array which is 1 in grid 
  tetris_array = [[0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,1,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],]
  for row in range(14):
    for column in range(10):
      if(tetris_array[row][column]==1):
        temp_surface = pygame.Surface((15,15))
        starting_pos = (column*w/row, row*h/column)
        ending_pos = ((column+1)*w/row, (row+1)*h/column)
        pygame.draw.rect(screen,"orange",column*w/row, row*h/column, 2 ,2)

  

  screen_dimension_text_surf = text_font.render(f"width: {w} height: {h}",False,(128,233,0))
  screen_dimension_text_rect = screen_dimension_text_surf.get_rect(center=(w/2,h/2))
  screen.blit(screen_dimension_text_surf,screen_dimension_text_rect)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()



  pygame.display.update()
  clock.tick(30)