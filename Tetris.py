import pygame


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/PixelEmulator-xq08.ttf",30)

#screen dimens text

while True:

  w, h = pygame.display.get_surface().get_size()
  
  screen.fill("white")

  #draw checker pattern
  # for y in range(w//2):
  #   for x in range(h//2):
  #     test_surf = pygame.Surface((80,80))
  #     if((x)+(y))%2 == 1:
  #       test_surf.fill("red")
  #     else:
  #       test_surf.fill((0, 0, 0))
  #     screen.blit(test_surf,(80*x,y*80))
  
  #grid



  screen_dimension_text_surf = text_font.render(f"width: {w} height: {h}",False,(128,233,0))
  screen_dimension_text_rect = screen_dimension_text_surf.get_rect(center=(w/2,h/2))
  screen.blit(screen_dimension_text_surf,screen_dimension_text_rect)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()



  pygame.display.update()
  clock.tick(30)