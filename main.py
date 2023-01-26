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
manager = pygame_gui.UIManager((1600, 900))

clock = pygame.time.Clock()

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
    print(option)
    pygame.display.update()

    new_text = pygame.font.SysFont("bahnschrift", 100).render(f"Hello, {option}", True, "black")
    new_text_rect = new_text.get_rect(center=(WIDTH/2, HEIGHT/2))
    SCREEN.blit(new_text, new_text_rect)


def main():

    #text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                             #  object_id='#main_text_entry')
    #menu = pygame_gui.elements.UIScrollingContainer(relative_rect = pygame.Rect((10, 10), (900, 300)), manager = manager, object_id="main_menu_containter", visible=True, anchors={text_input})
    
    dropdown = pygame_gui.elements.UIDropDownMenu(
        options_list=["select a point", "apple", "banana", "orange"], 
        relative_rect=pygame.Rect((WIDTH-240, 50), (200, 30)), 
        starting_option = "select a point", 
        manager = manager,
        object_id="menu",
        
    )

    CANVAS.fill('Black')
    SCREEN.fill('White')

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
                update_selection(event.text, dropdown)
            
            manager.process_events(event)

        #clear screen
        SCREEN.fill((54,57,63))
        clock.tick(60)
        manager.draw_ui(SCREEN)

        #draw objects
        SCREEN.blit(CANVAS,(0, 0)) 

        #update rendering
        manager.update(UI_REFRESH_RATE)
        pygame.display.update()
         
        
        
    
main()