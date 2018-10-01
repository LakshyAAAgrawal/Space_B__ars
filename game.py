#!/usr/bin/python3
#Space_B__ars
#IGS Team Name GH-76
#Made by Lakshya A Agrawal, Shrikant Garg, Rahul Kukreja, Nitish Gupta
import input_keyb as pygame_textinput
import pygame
from give_char import givechar as gc
import pickle
import cons_keyb
pygame.init()

#variable definitions
screen_max_x=1024
screen_max_y=760
screen_bgcolor=(0,0,0)
keyb_scaling_y=2.4
keyb_scaling_x=1.1
slow_count=0
new_game=False
save_state=False
save_counter=0

speed=50
dirn=True
dirn_change=False
dirn_change_counter=0
split_mode_on=False
split_mode_counter=0
slow_used=False
slow_start=0
str_to_disp=''
game_start=True

displayfont = pygame.font.SysFont(None, (screen_max_y)//20)

class char_text:
    r=None
    textrect=None
    text=None
    def __init__(self, rep):
        self.r = '_' if rep==' ' else rep
        basicfont = pygame.font.SysFont(None, (screen_max_y)//10)
        self.text = basicfont.render(self.r, True, (0, 255, 250))
        self.textrect = self.text.get_rect()
        self.textrect.centerx = -50 if dirn else (screen_max_x+50)
        self.textrect.centery = screen_max_y//4 + screen_max_y//8
    
    def update_screen(self, screen):
        screen.blit(self.text, self.textrect)
        
    def update_pos(self):
        self.textrect.centerx=self.textrect.centerx+7 if dirn else (self.textrect.centerx-7)

    def __del__(self):
        self.textrect=None
        self.r=None
        self.text=None

def update_marquee(cap_char, screen):
    i=0
    if dirn:
        while i<len(list_of_chars):
            if list_of_chars[i].textrect.centerx>screen_max_x+50:
                list_of_chars.pop(i)
                i=i-1
            else:
                list_of_chars[i].update_pos()
                list_of_chars[i].update_screen(screen)
            i=i+1
        if list_of_chars[-1].textrect.centerx>50:
            if not dirn_change:
                list_of_chars.append(char_text(gc(cap_char)))
    else:
        while i<len(list_of_chars):
            if list_of_chars[i].textrect.centerx<-50:
                list_of_chars.pop(i)
                i=i-1
            else:
                list_of_chars[i].update_pos()
                list_of_chars[i].update_screen(screen)
            i=i+1
        if list_of_chars[-1].textrect.centerx<screen_max_x-50:
            if not dirn_change:
                list_of_chars.append(char_text(gc(cap_char)))
                
def game():
    global slow_count, slow_flag, dirn, dirn_change_counter, dirn_change, speed, gameplay, split_mode_on, split_mode_counter, save_counter, save_state, slow_start, slow_used, str_to_disp
    screen.fill(screen_bgcolor)
    events = pygame.event.get()
    displayText = displayfont.render(str_to_disp, True, (0, 255, 0), (0,0,0))
    displaytextrect = displayText.get_rect()
    displaytextrect.centerx = screen_max_x//2
    displaytextrect.centery = screen_max_y//10
    screen.blit(displayText, displaytextrect)
    if "_" in captured_char:
        gameplay=not gameplay
        return()
    for i in ['!','@','#','$','%','^','&','(',')']:
        if i in captured_char:
            str_to_disp="Oops, you didn't want that"
            split_mode_on=True
            split_mode_counter=pygame.time.get_ticks()
            captured_char.remove(i)
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    # Feed it with events every frame
    ret_status=textinput.update(events, captured_char, list_of_chars, screen_max_x, screen_max_y, split_mode_on)
    if ret_status==True:
        if textinput.get_text() == "slow":
            if not slow_used:
                if not slow_flag:
                    print("slow")
                    speed=20
                    slow_flag=True
                    slow_count=pygame.time.get_ticks()
                    slow_start=slow_count
                    slow_used=True
                    print("block slow")
                    str_to_disp="Slowed!!"
            else:
                print("Can't use slow")
                str_to_disp="Can't slow right now"
        elif (textinput.get_text() == "><") or (textinput.get_text() == "reverse"):
            dirn_change=True
            dirn=not dirn
        elif textinput.get_text() == "save":
            if not save_state:
                with open('savefile_char', 'wb') as fp:
                    pickle.dump(captured_char, fp)
                with open('savefile_split', 'wb') as fp:
                    pickle.dump(split_mode_on, fp)
                save_state=True
                save_counter=pygame.time.get_ticks()
                str_to_disp="Game Saved"
            else:
                print("Can't save")
                str_to_disp="Game Cannot be saved"
        textinput.clear_text()
        
    if pygame.time.get_ticks()<=4000:
        str_to_disp="Welcome to Space_Bar! Use IT, but Avoid IT"
    elif 4000<pygame.time.get_ticks()<=8000:
        str_to_disp="Collect all alphabets.. Catch'em All!!"
    elif 8000<pygame.time.get_ticks()<=12000:
        str_to_disp="Use keys you collect, for commands"
    elif 12000<pygame.time.get_ticks()<=16000:
        str_to_disp="Command + Enter = Magic!!"
    elif 16000<pygame.time.get_ticks()<=20000:
        str_to_disp="Use command for everything( yes, even save, reverse, slow )"
    elif 20000<pygame.time.get_ticks()<=22000:
        str_to_disp="Rem : 1+1=0"
    elif 22000<pygame.time.get_ticks()<=24000:
        str_to_disp="Some characters are good, some(*MOST*) deceptive"
    if slow_flag:
        if abs(pygame.time.get_ticks()-slow_count)>=10000:
            print("slow over")
            str_to_disp="Slow over"
            slow_flag=False
            slow_count=0
            speed=30
    if slow_used:
        if abs(pygame.time.get_ticks()-slow_start)>=60000:
            slow_used=not slow_used
            slow_start=0
            print("Allowed to use slow")
            str_to_disp="Allowed to use slow"
    if split_mode_on:
        if abs(pygame.time.get_ticks()-split_mode_counter)>=30000:
            split_mode_on=False
            split_mode_counter=0
    if save_state:
        if abs(pygame.time.get_ticks()-save_counter)>=90000:
            save_state=False
            save_counter=0
    if dirn_change_counter==10:
        dirn_change=False
        dirn_change_counter=0
    if dirn_change:
        dirn_change_counter=dirn_change_counter+1

    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (screen_max_x//6, (screen_max_y//2)//2.7))
    #display_keyboard(captured_char, screen, (screen_max_x-(screen_max_x//keyb_scaling_x))//2, screen_max_y//2 + (((screen_max_y//2)-(screen_max_y//keyb_scaling_y))//2))
    cons_keyb.cons_keyb(screen, captured_char)
    
    
    if not split_mode_on:
        screen.blit(selector, (screen_max_x//2-30,screen_max_y//4+screen_max_y//11.5))
    else:
        screen.blit(selector, (screen_max_x//4-30,screen_max_y//4+screen_max_y//11.5))
        screen.blit(selector, (3*screen_max_x//4 -30,screen_max_y//4+screen_max_y//11.5))
    speed=90 if speed+0.05>80 else speed + 0.05
    update_marquee(captured_char, screen)
    pygame.display.update()
    clock.tick(speed)

def show_menu():
    global new_game, captured_char, gameplay, list_of_chars, split_mode_on, str_to_disp, game_start
    game_start=True
    screen.fill(screen_bgcolor)
    events = pygame.event.get()
    str_to_disp=''
    split_mode_on=False
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_game=not new_game
            elif event.key==pygame.K_RETURN:
                if new_game:
                    captured_char=[]
                else:
                    try:
                        fp = open("savefile_char", "rb")
                        captured_char = pickle.load(fp)
                        fp.close()
                    except:
                        captured_char=[]
                        
                    try:
                        fp = open("savefile_split", "rb")
                        split_mode_on = pickle.load(fp)
                        fp.close()
                    except:
                        split_mode_on=False
                    captured_char=['s','a','v','e','l','o','w','>','<']
                gameplay=not gameplay
                list_of_chars=[char_text(gc(captured_char))]
                return()
    titlebasicfont = pygame.font.SysFont(None, (screen_max_y)//5)
    titleText = titlebasicfont.render('Space _ B___ars', True, (0,255,250))
    titleTextrect = titleText.get_rect()
    titleTextrect.centerx = screen_max_x//2
    titleTextrect.centery = screen_max_y//4
    screen.blit(titleText, titleTextrect)
    menubasicfont = pygame.font.SysFont(None, (screen_max_y)//10)
    menuText1 = menubasicfont.render('New Game', True, (101, 115, 126))
    menuText1rect = menuText1.get_rect()
    menuText1rect.centerx = screen_max_x//2
    menuText1rect.centery = screen_max_y//2 + screen_max_y//5
    screen.blit(menuText1,menuText1rect)
    menuText2 = menubasicfont.render('Load Game', True, (101, 115, 126))
    menuText2rect = menuText2.get_rect()
    menuText2rect.centerx = screen_max_x//2
    menuText2rect.centery = screen_max_y//2 + (3*screen_max_y)//10
    screen.blit(menuText2,menuText2rect)
    
    selector_menu = pygame.Surface((screen_max_x//2, screen_max_y//10), pygame.SRCALPHA)   # per-pixel alpha
    selector_menu.fill((255,255,255,50))                         # notice the alpha value in the color
    if new_game:
        screen.blit(selector_menu, (screen_max_x//4,screen_max_y//2 + screen_max_y//7))
    else:
        screen.blit(selector_menu, (screen_max_x//4,screen_max_y//2 + (2*screen_max_y)//8))
    pygame.display.update()
# Create TextInput-object
textinput = pygame_textinput.TextInput()
screen = pygame.display.set_mode((screen_max_x, screen_max_y))
clock = pygame.time.Clock()

selector = pygame.Surface((60,60), pygame.SRCALPHA)   # per-pixel alpha
selector.fill((255,255,255,50))
if not split_mode_on:
    screen.blit(selector, (screen_max_x//2,screen_max_y//2-screen_max_y//70))
else:
    screen.blit(selector, (screen_max_x//4,screen_max_y//2-screen_max_y//70))
    screen.blit(selector, (3*screen_max_x//4,screen_max_y//2-screen_max_y//70))

slow_flag=False
gameplay=False
while True:
    if gameplay:
        game()
    else:
        show_menu()
