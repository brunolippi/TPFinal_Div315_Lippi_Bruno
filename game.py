import sys
import pygame as pg
import modules.variables as var
import modules.player as player
import modules.utils as utils
import modules.forms.form_manager as form_manager

def dragon_ball():
    pg.init()
    pg.mixer.init()

    pg.display.set_caption(var.GAME_TITLE)
    pg.display.set_icon(var.game_icon)

    configs = utils.load_configs()
    volume = configs.get('sound_volume', 0.4)
    if configs.get('sound', True):
        pg.mixer.music.load(var.MENU_MUSIC_PATH)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(loops=-1, fade_ms=400)

    screen = pg.display.set_mode(var.GAME_DIMENSIONS)
    clock = pg.time.Clock()
    running = True

    player_data = player.init_player()

    f_manager = form_manager.create_form_manager(screen, player_data)


    while running:
        event_list = pg.event.get()

        clock.tick(var.GAME_FPS)

        for event in event_list:
            if event.type == pg.QUIT:
                running = False
        
        form_manager.update(f_manager, event_list)
        
        pg.display.flip()
    
    pg.quit()
    sys.exit()