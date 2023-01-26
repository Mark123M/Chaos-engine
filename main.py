import pygame
import pygame_gui
import random
import sys
import math
import colorsys
import tkinter as tk

root = tk.Tk()
pygame.init()

WIDTH, HEIGHT = root.winfo_screenwidth() - 50, root.winfo_screenheight() - 50
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CANVAS = pygame.Surface((WIDTH-300, HEIGHT))

pygame.display.set_caption("Chaos engine")
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
clock = pygame.time.Clock()

GAME_STATE = {
    "points": ["select a point","a", "banana", "orange"] 
}

points_dropdown = pygame_gui.elements.UIDropDownMenu(
    options_list= GAME_STATE["points"], 
    relative_rect=pygame.Rect((WIDTH-240, 50), (200, 40)), 
    starting_option = "select a point", 
    manager = MANAGER,
    object_id="menu",
)

def show_user_name(user_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        new_text = pygame.font.SysFont("bahnschrift", 100).render(f"Hello, {user_name}", True, "black")
        new_text_rect = new_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(new_text, new_text_rect)

        clock.tick(60)

        pygame.display.update()

def update_selection(option, dropdown):
   # SCREEN.fill("white")
    pygame.display.update()
    new_text = pygame.font.SysFont("bahnschrift", 100).render(f"Hello, {option}", True, "black")
    new_text_rect = new_text.get_rect(center=(WIDTH/2, HEIGHT/2))
    SCREEN.blit(new_text, new_text_rect)

def add_point(pos):
    print(pos)
    pygame.draw.circle(CANVAS, 'White', pos, 5)
    GAME_STATE["points"].append(str(pos))


def main():

    #text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                             #  object_id='#main_text_entry')
    #menu = pygame_gui.elements.UIScrollingContainer(relative_rect = pygame.Rect((10, 10), (900, 300)), manager = manager, object_id="main_menu_containter", visible=True, anchors={text_input})



    CANVAS.fill('Black')

    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000

        for event in pygame.event.get(): #handle events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                show_user_name(event.text)
            if(event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED):
                update_selection(event.text, points_dropdown)
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] < CANVAS.get_rect().width:
                #+print(CANVAS.get_rect().width)
                add_point(pygame.mouse.get_pos())
            
            MANAGER.process_events(event)

        #clear screen
        SCREEN.fill('White')
        clock.tick(60)
        MANAGER.draw_ui(SCREEN)

        #draw objects
        SCREEN.blit(CANVAS,(0, 0)) 


        #update rendering
        MANAGER.update(UI_REFRESH_RATE)
        pygame.display.update()
         
        
        
    
main()