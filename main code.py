import pygame as pg
from sys import exit

class Base():
    
    def __init__(self):
        super().__init__()
        self.playboard_surf = pg.Surface((500,500),pg.SRCALPHA)
        self.playboard = self.playboard_surf.get_rect(center = (350,350))
        self.board = [[None,None,None],
                      [None,None,None],
                      [None,None,None]]
        
        self.cells = []
        self.current_player = "X"
        self.win = ""
        self.playerfont = pg.font.Font(r"C:\Users\chava\Desktop\python projects\TicTacToe\Fonts\PlayfairDisplay.ttf",30)
        self.current_player_display = self.playerfont.render("Current Player : {}".format(self.current_player),False,(0,0,0)).convert()
        self.current_player_rect = self.current_player_display.get_rect(bottomleft = (230,670))
        self.title_font = pg.font.Font(r"C:\Users\chava\Desktop\python projects\TicTacToe\Fonts\PlayfairDisplay.ttf",38)
        
        
        for row in range(3):
            self.row_list = []
            for col in range(3):
                self.rect = pg.Rect(self.playboard.left + col * 166, self.playboard.top + row * 166,166,166) #cell size is roughly 500/3
                self.row_list.append(self.rect)
            self.cells.append(self.row_list)
            
    def winner(self,board):
        self.board = board
        for col in range(3):
            if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
                self.win = board[0][col]
                return self.win
            
        if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
            self.win = board[0][0]
            return self.win
        
        if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
            self.win = board[0][2]
            return self.win
        
        for row in range(3):
            if board[row][0] is not None and board[row][0] == board[row][1] == board[row][2]:
                self.win = board[row][0]
                return self.win
        
        self.win = "Tie"
        return self.win
    

pg.init()
screen = pg.display.set_mode((700,700))
pg.display.set_caption("Tic Tac Toe")
clock = pg.time.Clock()
bg_music = pg.mixer.Sound(r"C:\Users\chava\Desktop\python projects\TicTacToe\Audio\music.mp3")
bg_music.set_volume(0.5)
bg_music.play(loops=-1)

click_sound = pg.mixer.Sound(r"C:\Users\chava\Desktop\python projects\TicTacToe\Audio\click.mp3")
win_sound = pg.mixer.Sound(r"C:\Users\chava\Desktop\python projects\TicTacToe\Audio\victory.mp3")
main_background = pg.image.load(r"C:\Users\chava\Desktop\python projects\TicTacToe\Graphics\main_background.png")
main_background = pg.transform.scale(main_background,(700,700))


base_ins = Base()
game_state = False

myfont = pg.font.Font(r"C:\Users\chava\Desktop\python projects\TicTacToe\Fonts\PlayfairDisplay.ttf",60)
title = myfont.render("Tic Tac Toe",False,(0,0,0),((190, 155, 123))).convert()
title_rect = title.get_rect(topleft = (205,10))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if game_state: 
            mouse_pos = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN and mouse_pos[0]<600 and mouse_pos[0]>=100 and mouse_pos[1]<600 and mouse_pos[1]>=100:
                for row in range(3):
                    for col in range(3):
                        if base_ins.cells[row][col].collidepoint(mouse_pos):
                            if base_ins.board[row][col] is None:
                                base_ins.board[row][col] = base_ins.current_player
                                bg_music.set_volume(0.2)
                                click_sound.play()
                                pg.time.wait(500)
                                bg_music.set_volume(0.5)
                            
                                if base_ins.current_player == "X":
                                    base_ins.current_player = "O"
                                else:
                                    base_ins.current_player = "X"
                        
                        base_ins.winner(base_ins.board)
                        
        if event.type == pg.MOUSEBUTTONDOWN:
            game_state = True
                        
    if game_state:
    
        screen.blit(main_background,(0,0))
        pg.draw.rect(screen,(255,255,255),title_rect)
        base_ins.playboard_surf.fill((255,255,255,0))
        
        #drawing the grid
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(166.66,0),(166.66,500),2)
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(333.32,0),(333.32,500),2)
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(0,166.66),(500,166.66),2)
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(0,333.32),(500,332.32),2)
        
        pg.draw.rect(screen,(0,0,0),base_ins.playboard,2)
        
        #making moves(redrawing,drawing x's and o's)
        
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(166.66,0),(166.66,500),2)
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(333.32,0),(333.32,500),2)
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(0,166.66),(500,166.66),2)
        pg.draw.line(base_ins.playboard_surf,(0,0,0),(0,333.32),(500,332.32),2)
        
        pg.draw.rect(screen,(0,0,0),base_ins.playboard,2)
        
        for row in range(3):
            for col in range(3):
                rect = base_ins.cells[row][col]
                if base_ins.board[row][col] == "X":
                    x,y,w,h = rect.x-base_ins.playboard.left,rect.y-base_ins.playboard.top,rect.width,rect.height
                    pg.draw.line(base_ins.playboard_surf,(255,0,0),(x,y),(x+w,y+h),2)
                    pg.draw.line(base_ins.playboard_surf,(255,0,0),(x+w,y),(x,y+h),2)
                    
                
                elif base_ins.board[row][col] == "O":
                    x_center,y_center = rect.center
                    x_center-=base_ins.playboard.left
                    y_center-=base_ins.playboard.top
                    rad = rect.width //2 -10
                    
                    pg.draw.circle(base_ins.playboard_surf,(0,0,255),(x_center,y_center),rad,2)
                    
        #display for current player
        
        if base_ins.win !="X" and base_ins.win !="O":
            base_ins.current_player_display = base_ins.playerfont.render("Current Player : {}".format(base_ins.current_player),False,(0,0,0)).convert()
        
        elif base_ins.win == "X":
            base_ins.current_player_display = base_ins.playerfont.render("Current Player : X",False,(0,0,0)).convert()
        
        elif base_ins.win == "O":
            base_ins.current_player_display = base_ins.playerfont.render("Current Player : O",False,(0,0,0)).convert()
            
        screen.blit(base_ins.current_player_display,base_ins.current_player_rect)
        
        screen.blit(title,title_rect)
        screen.blit(base_ins.playboard_surf,base_ins.playboard)
        
    else:
        img = pg.image.load(r"C:\Users\chava\Desktop\python projects\TicTacToe\Graphics\background.png").convert()
        img = pg.transform.scale(img,(700,700))
        screen.blit(img,(0,0))
        main_title = myfont.render("Tic Tac Toe",False,(0,0,0)).convert()
        main_title_rect = main_title.get_rect(topleft = (205,10))
        
        instructions = base_ins.title_font.render("Click anywhere to start a new game",False,(0,0,0)).convert()
        instructions_rect = instructions.get_rect(center = (350,650))
        
        screen.blit(main_title,main_title_rect)
        screen.blit(instructions,instructions_rect)

        
    
    pg.display.update()
    
    #checking for winners
    if base_ins.win == "X":
        bg_music.set_volume(0)
        win_sound.play()
        print(base_ins.win,"is winner")
        pg.time.wait(3000)
        
        game_state = False
        base_ins.board = [[None,None,None],[None,None,None],[None,None,None]]
        base_ins.current_player = "X"
        base_ins.win = ""
    
    elif base_ins.win == "O":
        bg_music.set_volume(0)
        win_sound.play()
        print(base_ins.win,"is winner")
        pg.time.wait(3000)
        game_state = False
        base_ins.board = [[None,None,None],[None,None,None],[None,None,None]]
        base_ins.current_player = "X"
        base_ins.win = ""
        
    tie = True   
    for row in base_ins.board:
        for col in row:
            if col is None:
                tie = False
                break
        if not tie:
            break
        
    if base_ins.win == "Tie" and tie:
        print("It's a tie")
        pg.time.wait(1000)
        game_state = False
        base_ins.board = [[None,None,None],[None,None,None],[None,None,None]]
        base_ins.current_player = "X"
        base_ins.win = ""

    clock.tick(60)