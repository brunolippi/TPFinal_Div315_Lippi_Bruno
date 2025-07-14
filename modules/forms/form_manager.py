import pygame as pg
import modules.forms.form_menu as form_menu
import modules.forms.form_options as form_options
import modules.forms.form_ranking as form_ranking
import modules.forms.form_game as form_game
import modules.forms.form_enter_name as form_enter_name
import modules.variables as var

def create_form_manager(screen: pg.Surface, player_data: dict):
    form = {}
    form['main_screen'] = screen
    form['player'] = None
    form['enemy'] = None

    form['player_data'] = player_data

    form['form_list'] = [
        form_menu.init_form_menu(
            dict_form_data={
                "name": "form_menu",
                "screen": form.get('main_screen'),
                "active": True,
                "coords": (0, 0),
                "stage_number": 1,
                "screen_dimentions": var.GAME_DIMENSIONS,
                "music_path": var.MENU_MUSIC_PATH,
                "background_path": var.MENU_BG_PATH,
                "btn_sound_path": './assets/audio/music/select.mp3'
            }
        ),
        form_game.init_form_game(dict_form_data={
                "name": "form_game",
                "screen": form.get('main_screen'),
                "active": False,
                "coords": (0, 0),
                "stage_number": 1,
                "screen_dimentions": var.GAME_DIMENSIONS,
                "music_path": var.GAME_MUSIC_PATH,
                "background_path": var.GAME_BG_PATH,
            }, player=form.get('player_data')
        ),
        form_enter_name.init_form_enter_name(
            dict_form_data={
                "name":'form_enter_name', 
                "screen":form.get('main_screen'), 
                "active":False, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RANKING_MUSIC_PATH,
                "background_path": var.RANKING_BG_PATH,
                "screen_dimentions": var.GAME_DIMENSIONS
            },player=form.get('player_data')
        ),
        form_ranking.init_form_ranking(
            dict_form_data={
                "name": "form_ranking",
                "screen": form.get('main_screen'),
                "active": False,
                "coords": (0, 0),
                "stage_number": 1,
                "screen_dimentions": var.GAME_DIMENSIONS,
                "music_path": var.RANKING_MUSIC_PATH,
                "background_path": var.RANKING_BG_PATH,
            }, player=form.get('player_data')
        ),
        form_options.init_form_options(
            dict_form_data={
                "name": "form_options",
                "screen": form.get('main_screen'),
                "active": False,
                "coords": (0, 0),
                "stage_number": 1,
                "screen_dimentions": var.GAME_DIMENSIONS,
                "music_path": var.RANKING_MUSIC_PATH,
                "background_path": var.OPTIONS_BG_PATH,
            }, player=form.get('player_data')
        )
    ]

    return form

def update(form_manager: dict, event_queue: list[pg.event.Event]):
    # Menu
    if form_manager.get('form_list')[0].get('active'):
       form_data = form_manager.get("form_list")[0]

       form_menu.update(form_data)
       form_menu.draw(form_data)

    # Game
    elif form_manager.get('form_list')[1].get('active'):
       form_data = form_manager.get("form_list")[1]

       form_game.update(form_data, event_queue)
       form_game.draw(form_data)

    # Game
    elif form_manager.get('form_list')[2].get('active'):
       form_data = form_manager.get("form_list")[2]

       form_enter_name.update(form_data, event_queue)
       form_enter_name.draw(form_data)
       
    # Ranking
    elif form_manager.get('form_list')[3].get('active'):
       form_data = form_manager.get('form_list')[3]

       form_ranking.update(form_data)
       form_ranking.draw(form_data)
       
    # Options
    elif form_manager.get('form_list')[4].get('active'):
       form_data = form_manager.get('form_list')[4]

       form_options.update(form_data)
       form_options.draw(form_data)