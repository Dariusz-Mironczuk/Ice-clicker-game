#Importing libraries
import pygame
import  sys
#Initializing pygame
pygame.init()


#WINDOW SETTINGS
WINDOW_NAME = 'Ice breakerz'
WINDOW_ICON = pygame.image.load('assets/Game_icon.png')
WINDOW_SIZE = [640, 480]
#INITIALIZING WINDOW
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption(WINDOW_NAME)
pygame.display.set_icon(WINDOW_ICON)

#GAME CLOCK
FPS = 60
clock = pygame.time.Clock()

#GAME LOGIC
GAME_RUNNING = True


#Rectangle for clicking
clicking_rect = pygame.Rect(30, 30, 300, 230)

#STATISTIC
Breaking_ability = 1
Money = 0
Ice_broken = 0
Money_per_sec = 0
Money_per_sec_stat = 0


#Drawing money to the screen
pygame.font.init()
Title_screen_counter = 300
Money_font = pygame.font.Font('assets/orange_juice.ttf', 30)
TITLE_font = pygame.font.Font('assets/orange_juice.ttf', 45)
TITLE_SURFACE = TITLE_font.render(f'ICE BREAKERZ', False, (60, 114, 170))

#Drwing title screen
Title_screen_done = False
Transperancy = 255
Title_screen = pygame.image.load('assets/Title_screen.png').convert_alpha()
Title_screen.set_alpha(Transperancy)

#Drawing Image to click
backgound_choice = 1
Cold_level_background = [pygame.image.load('assets/Cold_level_background.png'),
                            pygame.image.load('assets/Cold_level_background_second.png')]
Cold_level_background_boarder = pygame.image.load('assets/Cold_level_background_border.png')

#Drawing pixckaxe digging
x = 0
player = [pygame.image.load('assets/breaking blocks/Wooden pickaxe hit1.png'),
        pygame.image.load('assets/breaking blocks/Wooden pickaxe hit2.png'),
          pygame.image.load('assets/breaking blocks/Stone pickaxe hit1.png'),
          pygame.image.load('assets/breaking blocks/Stone pickaxe hit2.png'),
          pygame.image.load('assets/breaking blocks/Iron pickaxe hit1.png'),
          pygame.image.load('assets/breaking blocks/Iron pickaxe hit2.png'),
          pygame.image.load('assets/breaking blocks/Diamond pickaxe hit1.png'),
          pygame.image.load('assets/breaking blocks/Diamond pickaxe hit2.png')]


#Drawing boarder icons for nice little animation
Corner_animaton_sek = FPS
Wood_Corner_animation_img = [pygame.image.load('assets/Corner boarder/Corner_boarder_wood_1.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_wood_2.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_wood_3.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_wood_4.png')]
Stone_Corner_animation_img = [pygame.image.load('assets/Corner boarder/Corner_boarder_stone_1.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_stone_2.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_stone_3.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_stone_4.png')]
Iron_Corner_animation_img = [pygame.image.load('assets/Corner boarder/Corner_boarder_Iron_1.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_Iron_2.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_Iron_3.png'),
                        pygame.image.load('assets/Corner boarder/Corner_boarder_Iron_4.png')]
Diamond_corner_animation_img = [pygame.image.load('assets/Corner boarder/Diamond_boarder_iron_1.png'),
                        pygame.image.load('assets/Corner boarder/Diamond_boarder_iron_2.png'),
                        pygame.image.load('assets/Corner boarder/Diamond_boarder_iron_3.png'),
                        pygame.image.load('assets/Corner boarder/Diamond_boarder_iron_4.png')]

#Stone pickaxe button
Stone_pickaxe_button = [pygame.image.load('assets/Stone pickaxe for buy.png'),
                        pygame.image.load('assets/Stone pickaxe bought.png')]
Stone_pickaxe_button_rect = Stone_pickaxe_button[1].get_rect()
Stone_pickaxe_button_rect.topleft = (20, 280)
Stone_pickaxe_button_bought = False
#Iron pickaxe button
Iron_pickaxe_button = [pygame.image.load('assets/Iron pickaxe for buy.png'),
                        pygame.image.load('assets/Iron pickaxe bought.png')]
Iron_pickaxe_button_rect = Iron_pickaxe_button[1].get_rect()
Iron_pickaxe_button_rect.topleft = (20, 365)
Iron_pickaxe_button_bought = False
#Factory button
Factory_button = [pygame.image.load('assets/Ice factory for buy.png'),
                  pygame.image.load('assets/Ice factory bought.png')]
Factory_button_rect = Factory_button[1].get_rect()
Factory_button_rect.topleft = (220, 280)
Factory_button_bought = False
Factory_money = False
#Stock button
Stock_button = [pygame.image.load('assets/Ice stock marcket for buy.png'),
                  pygame.image.load('assets/Ice stock marcket bought.png')]
Stock_button_rect = Stock_button[1].get_rect()
Stock_button_rect.topleft = (220, 365)
Stock_button_bought = False
Stock_money = False
#Diamond button
Diamond_pickaxe_button = [pygame.image.load('assets/Diamond pickaxe for buy.png'),
                         pygame.image.load('assets/Diamond pickaxe bought.png')]
Diamond_pickaxe_button_rect = Diamond_pickaxe_button[1].get_rect()
Diamond_pickaxe_button_rect.topleft = (420, 320)
Diamond_pickaxe_button_bought = False
Diamond_pickaxe_money = False



#GAME LOOP
while GAME_RUNNING:

    #Filling display anti-ghost efect
    DISPLAY.fill((173, 216, 230))


    #Drawing clicking rectangle to the screen
    pygame.draw.rect(DISPLAY, (60, 114, 170), clicking_rect)
    #Drawing the Money to the display
    Money_Surface = Money_font.render(f'Money                    {Money}', False, (0, 0, 0))
    ICE_BROKEN_Surface = Money_font.render(f'Ice broken               {Ice_broken}', False, (0, 0, 0))
    Money_font_per_sec = Money_font.render(f'Money/per sec       {Money_per_sec_stat}', False, (0,0,0))
    DISPLAY.blit(TITLE_SURFACE, (350, 40))
    DISPLAY.blit(Money_Surface, (390, 110))
    DISPLAY.blit(ICE_BROKEN_Surface, (372, 150))
    DISPLAY.blit(Money_font_per_sec, (350, 190))
    #Drawing to clickable screen
    if backgound_choice == 0:
        DISPLAY.blit(Cold_level_background[0], (30, 30))
    elif backgound_choice == 1:
        DISPLAY.blit(Cold_level_background[1], (30, 30))
    if Diamond_pickaxe_button_bought:
        DISPLAY.blit(player[x], (30, 30))
        x = 6
    elif Iron_pickaxe_button_bought:
        DISPLAY.blit(player[x], (30, 30))
        x = 4
    elif Stone_pickaxe_button_bought:
        DISPLAY.blit(player[x], (30, 30))
        x = 2
    else:
        DISPLAY.blit(player[x], (30, 30))
        x = 0
    DISPLAY.blit(Cold_level_background_boarder, (23, 23))


    #Drawing clickable buttons
    if Stone_pickaxe_button_bought == False:
        DISPLAY.blit(Stone_pickaxe_button[0], Stone_pickaxe_button_rect)
    else:
        DISPLAY.blit(Stone_pickaxe_button[1], Stone_pickaxe_button_rect)
        Breaking_ability = 2
    if Iron_pickaxe_button_bought == False:
        DISPLAY.blit(Iron_pickaxe_button[0], Iron_pickaxe_button_rect)
    else:
        DISPLAY.blit(Iron_pickaxe_button[1], Iron_pickaxe_button_rect)
        Breaking_ability = 5
    if Factory_button_bought == False:
        DISPLAY.blit(Factory_button[0], Factory_button_rect)
    else:
        DISPLAY.blit(Factory_button[1], Factory_button_rect)
        Factory_money = True
    if Stock_button_bought == False:
        DISPLAY.blit(Stock_button[0], Stock_button_rect)
    else:
        DISPLAY.blit(Stock_button[1], Stock_button_rect)
        Stock_money = True
    if Stone_pickaxe_button_bought and Iron_pickaxe_button_bought and Factory_button_bought and Stock_button_bought and Diamond_pickaxe_button_bought == False:
        DISPLAY.blit(Diamond_pickaxe_button[0], Diamond_pickaxe_button_rect)
    elif Diamond_pickaxe_button_bought:
        DISPLAY.blit(Diamond_pickaxe_button[1], Diamond_pickaxe_button_rect)
        Breaking_ability = 20

    #Corner animation
    if Diamond_pickaxe_button_bought:
        if Corner_animaton_sek >= 45:
            DISPLAY.blit(Diamond_corner_animation_img[0], (0, 0))
        elif Corner_animaton_sek >= 30:
            DISPLAY.blit(Diamond_corner_animation_img[1], (0, 0))
        elif Corner_animaton_sek >= 15:
            DISPLAY.blit(Diamond_corner_animation_img[2], (0, 0))
        else:
            DISPLAY.blit(Diamond_corner_animation_img[3], (0, 0))
    elif Iron_pickaxe_button_bought:
        if Corner_animaton_sek >= 45:
            DISPLAY.blit(Iron_Corner_animation_img[0], (0, 0))
        elif Corner_animaton_sek >= 30:
            DISPLAY.blit(Iron_Corner_animation_img[1], (0, 0))
        elif Corner_animaton_sek >= 15:
            DISPLAY.blit(Iron_Corner_animation_img[2], (0, 0))
        else:
            DISPLAY.blit(Iron_Corner_animation_img[3], (0, 0))
    elif Iron_pickaxe_button_bought == False and Stone_pickaxe_button_bought:
        if Corner_animaton_sek >= 45:
            DISPLAY.blit(Stone_Corner_animation_img[0], (0,0))
        elif Corner_animaton_sek >= 30:
            DISPLAY.blit(Stone_Corner_animation_img[1], (0,0))
        elif Corner_animaton_sek >= 15:
            DISPLAY.blit(Stone_Corner_animation_img[2], (0,0))
        else:
            DISPLAY.blit(Stone_Corner_animation_img[3], (0, 0))
    else:
        if Corner_animaton_sek >= 45:
            DISPLAY.blit(Wood_Corner_animation_img[0], (0,0))
        elif Corner_animaton_sek >= 30:
            DISPLAY.blit(Wood_Corner_animation_img[1], (0,0))
        elif Corner_animaton_sek >= 15:
            DISPLAY.blit(Wood_Corner_animation_img[2], (0,0))
        else:
            DISPLAY.blit(Wood_Corner_animation_img[3], (0, 0))



    #EVENT HANDLER
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            GAME_RUNNING = False
            pygame.quit()
            sys.exit()



        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if clicking_rect.collidepoint(event.pos):
                    if Diamond_pickaxe_button_bought:
                        x = 7
                    elif Iron_pickaxe_button_bought:
                        x = 5
                    elif Stone_pickaxe_button_bought:
                        x = 3
                    else:
                        x = 1
                    Money += Breaking_ability
                    Ice_broken += 1


            if Stone_pickaxe_button_rect.collidepoint(event.pos) and Money >= 20 and Stone_pickaxe_button_bought == False:
                Money -= 20
                Stone_pickaxe_button_bought = True
            if Iron_pickaxe_button_rect.collidepoint(event.pos) and Money >= 30 and Iron_pickaxe_button_bought == False:
                Money -= 30
                Iron_pickaxe_button_bought = True
            if Factory_button_rect.collidepoint(event.pos) and Money >= 100 and Factory_button_bought == False:
                Money -= 100
                Factory_button_bought = True
            if Stock_button_rect.collidepoint(event.pos) and Money >= 120 and Stock_button_bought == False:
                Money -= 120
                Stock_button_bought = True
            if Diamond_pickaxe_button_rect.collidepoint(event.pos) and Money >= 200 and Diamond_pickaxe_button_bought == False:
                Money -= 200
                Diamond_pickaxe_button_bought = True





    #Money per sec
    if Corner_animaton_sek == 1 and Factory_money and Stock_money:
        Money_per_sec = 3
        Money += Money_per_sec
    elif Corner_animaton_sek == 1 and Stock_money:
        Money_per_sec = 2
        Money += Money_per_sec
    elif Corner_animaton_sek == 1 and Factory_money:
        Money_per_sec = 1
        Money += Money_per_sec
    else:
        Money_per_sec = 0
        Money += Money_per_sec
    if Factory_money and Stock_money:
        Money_per_sec_stat = 3
    elif Stock_money:
        Money_per_sec_stat = 2
    elif Factory_money:
        Money_per_sec_stat = 1
    else:
        Money_per_sec_stat = 0

    # Corner animation timer
    Corner_animaton_sek -= 1
    if Corner_animaton_sek == 0:
        Corner_animaton_sek = FPS


    if Title_screen_done == False:
        DISPLAY.blit(Title_screen, (0,0))
        if Transperancy >= 200:
            Transperancy -= 1
        else:
            Transperancy -= 15
        Title_screen.set_alpha(Transperancy)
        if Title_screen_counter == 0:
            Title_screen_done = True


    #UPDATING THE DISPLAY
    pygame.display.update()

    #SETTING FPS LIMIT
    clock.tick(FPS)


#ENDING AND CLOSING THE GAME
pygame.quit()
sys.exit()