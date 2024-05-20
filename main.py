
import pygame as pg



def main():
    
    pg.init()
    
    pg.mixer.init()
    pg.display.
    run = True
    
    
    
    while run:
        
        
        
        
        for event in pg.event.get():
            
            if event.type == pg.K_QUIT:
                run = False


if __name__ == "__main__":
    main()
    pg.quit()