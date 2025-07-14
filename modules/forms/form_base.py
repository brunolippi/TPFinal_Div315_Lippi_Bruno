import pygame as pg 
import modules.utils as utils
import modules.variables as vars

forms_dict = {}

def create_base_form(dict_form_data: dict) -> dict:
    form = {}
    form['name'] = dict_form_data.get('name')

    form['screen'] = dict_form_data.get('screen')
    form['surface'] = pg.image.load(dict_form_data.get('background_path')).convert_alpha()
    form['surface'] = pg.transform.scale(form.get('surface'), dict_form_data.get('screen_dimentions'))
    form['x_coord'] = dict_form_data.get('coords')[0]
    form['y_coord'] = dict_form_data.get('coords')[1]

    form['level_number'] = dict_form_data.get('stage_number')
    form['music_path'] = dict_form_data.get('music_path')
    form['active'] = dict_form_data.get('active')
    
    form['rect'] = form.get('surface').get_rect()
    form['rect'].x = dict_form_data.get('coords')[0]
    form['rect'].y = dict_form_data.get('coords')[1]

    return form

def play_music(form_dict: dict):
    print(f'Nueva musica: {form_dict.get('music_path')}')
    configs = utils.load_configs()
    volume = configs.get('sound_volume', 0.4)

    if configs.get('sound', True):
        pg.mixer.music.load(form_dict.get('music_path'))
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(loops=-1, fade_ms=400)

def set_music_level(level: int):
    pg.mixer.music.set_volume(level)

def stop_music():
    pg.mixer.music.stop()

def set_active(name: str):
    print(f'Nuevo form: {name}')
    for form in forms_dict.values():
        form['active'] = False
        
    forms_dict[name]['active'] = True

def update_widgets(form_data: dict):
    for widget in form_data.get('widgets_list'):
        widget.update()

def draw_widgets(form_data: dict):
    for widget in form_data.get('widgets_list'):
        widget.draw()

def draw(form_data: dict):
    form_data['screen'].blit(form_data.get('surface'), form_data.get('rect'))

def update(form_data: dict):
    update_widgets(form_data)
    
    
