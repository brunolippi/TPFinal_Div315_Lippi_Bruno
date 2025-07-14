import modules.forms.form_base as form_base
import modules.variables as var
import modules.utils as utils
from utn_fra.pygame_widgets import (
    ButtonImage, Label
)

img_checked_btn = './assets/img/forms/checked_box.png'
img_unchecked_btn = './assets/img/forms/unchecked_box.png'

def init_form_options(dict_form_data: dict, player: dict):
    form = form_base.create_base_form(dict_form_data)
    form['player'] = player
    form['score'] = player['score']

    form['configs'] = utils.load_configs()

    form['lbl_title'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1]//2 - 250,
        text="Dragon Ball", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=75
    )

    form['lbl_subtitle'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 180,
        text="Opciones", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=55, color=var.COLOR_AZUL
    )

    form['lbl_sound'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 100,
        text=f'Activar sonido', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=30, color=var.COLOR_BLANCO
    )

    form['btn_sound'] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 55,
         text="Enter", width=32, height=30, 
         screen=form.get('screen'), image_path=(img_checked_btn if form['configs']['sound'] else img_unchecked_btn), 
         font_size=50, on_click_param="original", on_click=handle_sound_change)
    

    form['lbl_sound_lvl'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2,
        text=f'Nivel de sonido', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=30, color=var.COLOR_BLANCO
    )

    form['btn_sound_lvl_25'] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2 - 70, y=var.GAME_DIMENSIONS[1] // 2 + 40,
         text="Enter", width=32, height=30, 
         screen=form.get('screen'), image_path=(img_checked_btn if form['configs']['sound_volume'] == 0.25 else img_unchecked_btn), 
         font_size=50, on_click_param=0.25, on_click=handle_sound_level_change)
    
    form['lbl_sound_lvl_25'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2 - 70, y=var.GAME_DIMENSIONS[1] // 2 + 70,
        text=f'25%', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=15, color=var.COLOR_NEGRO
    )
    
    form['btn_sound_lvl_50'] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2 - 20, y=var.GAME_DIMENSIONS[1] // 2 + 40,
         text="Enter", width=32, height=30, 
         screen=form.get('screen'), image_path=(img_checked_btn if form['configs']['sound_volume'] == 0.5 else img_unchecked_btn), 
         font_size=50, on_click_param=0.5, on_click=handle_sound_level_change)
    
    form['lbl_sound_lvl_50'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2 - 20, y=var.GAME_DIMENSIONS[1] // 2 + 70,
        text=f'50%', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=15, color=var.COLOR_NEGRO
    )

    form['btn_sound_lvl_75'] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2 + 30, y=var.GAME_DIMENSIONS[1] // 2 + 40,
         text="Enter", width=32, height=30, 
         screen=form.get('screen'), image_path=(img_checked_btn if form['configs']['sound_volume'] == 0.75 else img_unchecked_btn), 
         font_size=50, on_click_param=0.75, on_click=handle_sound_level_change)
    
    form['lbl_sound_lvl_75'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2 + 30, y=var.GAME_DIMENSIONS[1] // 2 + 70,
        text=f'75%', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=15, color=var.COLOR_NEGRO
    )

    form['btn_sound_lvl_100'] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2 + 80, y=var.GAME_DIMENSIONS[1] // 2 + 40,
         text="Enter", width=32, height=30, 
         screen=form.get('screen'), image_path=(img_checked_btn if form['configs']['sound_volume'] == 1 else img_unchecked_btn), 
         font_size=50, on_click_param=1, on_click=handle_sound_level_change)
    
    form['lbl_sound_lvl_100'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2 + 80, y=var.GAME_DIMENSIONS[1] // 2 + 70,
        text=f'100%', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=15, color=var.COLOR_NEGRO
    )

    form['btn_back'] = ButtonImage(x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 + 150, text="Back", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/forms/back.png', font_size=50, on_click_param="form_menu", on_click=on_exit)
    
    form['widgets_list'] = [
        form.get('lbl_title'), form.get('lbl_subtitle'), form.get('lbl_sound'),
        form.get('btn_sound'), form.get('lbl_sound_lvl'), form.get('btn_sound_lvl_25'),
        form.get('lbl_sound_lvl_25'), form.get('btn_sound_lvl_50'), form.get('lbl_sound_lvl_50'),
        form.get('btn_sound_lvl_75'), form.get('lbl_sound_lvl_75'), form.get('btn_sound_lvl_100'), 
        form.get('lbl_sound_lvl_100'), form.get('btn_back')
    ]
    
    form_base.forms_dict[dict_form_data.get('name')] = form

    return form

def on_exit(param: str):
    form_base.stop_music()
    form_base.play_music(form_base.forms_dict[param])
    form_base.set_active(param)

def handle_sound_change(form_and_sound_dict: bool):
    print(f'change sound option: {form_and_sound_dict}')
    form_and_sound_dict['form']['configs']['sound'] = form_and_sound_dict['sound']
    utils.save_configs('sound', form_and_sound_dict['sound'])

    if form_and_sound_dict['sound']:
        form_base.play_music(form_and_sound_dict['form'])
    else:
        form_base.stop_music()

def handle_sound_level_change(level: int):
    print(f'change sound volume: {level}')
    utils.save_configs('sound_volume', level)
    form_base.set_music_level(level)
    form_base.forms_dict['form_options']['configs']['sound_volume'] = level

def update_buttons(form_data: dict):
    if form_data.get('configs').get('sound') == False:
        form_data['widgets_list'][3] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 55,
         text="Enter", width=32, height=30, 
         screen=form_data.get('screen'), image_path=(img_checked_btn if form_data['configs']['sound'] else img_unchecked_btn), 
         font_size=50, on_click_param={"form": form_data, "sound": True}, on_click=handle_sound_change)
    elif form_data.get('configs').get('sound') == True:
        form_data['widgets_list'][3] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 55,
         text="Enter", width=32, height=30, 
         screen=form_data.get('screen'), image_path=(img_checked_btn if form_data['configs']['sound'] else img_unchecked_btn), 
         font_size=50, on_click_param={"form": form_data, "sound": False}, on_click=handle_sound_change)
    
    form_data['widgets_list'][5] = ButtonImage(
        x=var.GAME_DIMENSIONS[0] // 2 - 70, y=var.GAME_DIMENSIONS[1] // 2 + 40,
        text="Enter", width=32, height=30, 
        screen=form_data.get('screen'), image_path=(img_checked_btn if form_data['configs']['sound_volume'] == 0.25 else img_unchecked_btn), 
        font_size=50, on_click_param=0.25, on_click=handle_sound_level_change)
    
    form_data['widgets_list'][7] = ButtonImage(
        x=var.GAME_DIMENSIONS[0] // 2 - 20, y=var.GAME_DIMENSIONS[1] // 2 + 40,
        text="Enter", width=32, height=30, 
        screen=form_data.get('screen'), image_path=(img_checked_btn if form_data['configs']['sound_volume'] == 0.5 else img_unchecked_btn), 
        font_size=50, on_click_param=0.5, on_click=handle_sound_level_change)
    
    form_data['widgets_list'][9] = ButtonImage(
        x=var.GAME_DIMENSIONS[0] // 2 + 30, y=var.GAME_DIMENSIONS[1] // 2 + 40,
        text="Enter", width=32, height=30, 
        screen=form_data.get('screen'), image_path=(img_checked_btn if form_data['configs']['sound_volume'] == 0.75 else img_unchecked_btn), 
        font_size=50, on_click_param=0.75, on_click=handle_sound_level_change)
    
    form_data['widgets_list'][11] = ButtonImage(
        x=var.GAME_DIMENSIONS[0] // 2 + 80, y=var.GAME_DIMENSIONS[1] // 2 + 40,
        text="Enter", width=32, height=30, 
        screen=form_data.get('screen'), image_path=(img_checked_btn if form_data['configs']['sound_volume'] == 1 else img_unchecked_btn), 
        font_size=50, on_click_param=1, on_click=handle_sound_level_change)
    
def draw(form_dict: dict):
    form_base.draw(form_dict)
    form_base.draw_widgets(form_dict)
    
def update(form_dict: dict):
    update_buttons(form_dict)

    form_base.update(form_dict)