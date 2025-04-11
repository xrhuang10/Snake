import pygame as pg

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))
running = True
turn = 0
font = pg.font.SysFont("Arial", 100)

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

pg.draw.rect(surface = screen, color="white", rect=(0, 0, 600, 600))
pg.draw.line(surface = screen, color="black", start_pos=(200, 0), end_pos=(200, 600), width=5)
pg.draw.line(surface = screen, color="black", start_pos=(400, 0), end_pos=(400, 600), width=5)
pg.draw.line(surface = screen, color="black", start_pos=(0, 200), end_pos=(600, 200), width=5)
pg.draw.line(surface = screen, color="black", start_pos=(0, 400), end_pos=(600, 400), width=5)

while running:

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200
            if board[row][col] == "" and turn%2 == 0:
                board[row][col] = 'X'  
                screen.blit(font.render('X', True, (0, 0, 0)), (col*200 + 50, row*200 + 50))
                turn += 1
            elif board[row][col] == "" and turn%2 == 1:
                board[row][col] = 'O'
                screen.blit(font.render('O', True, (0, 0, 0)), (col*200 + 50, row*200 + 50))
                turn += 1
            else:
                print("Invalid move")  
        
        if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
            print(f"Player {-1*((turn%2) - 1) + 1} wins!")
            running = False
        
        if board[0][0] == board[0][1] == board[0][2] != "" or board[1][0] == board[1][1] == board[1][2] != "" or board[2][0] == board[2][1] == board[2][2] != "":
            print(f"Player {-1*((turn%2) - 1) + 1} wins!")
            running = False
        
        if board[0][0] == board[1][0] == board[2][0] != "" or board[0][1] == board[1][1] == board[2][1] != "" or board[0][2] == board[1][2] == board[2][2] != "":
            print(f"Player {-1*((turn%2) - 1) + 1} wins!")
            running = False
        
        if turn == 9:
            print("It's a draw!")
            running = False

    clock.tick(10)

    pg.display.flip()
    print(board)

pg.quit()