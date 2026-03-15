        if tetris_array[y][x] == 1:
          if y+1 == 20:
            freeze_the_board(tetris_array)
        
          elif tetris_array[y+1][x] == 2:
            freeze_the_board(tetris_array)

          else:
            tetris_array[y][x] = 0
            tetris_array[y+1][x] = 1