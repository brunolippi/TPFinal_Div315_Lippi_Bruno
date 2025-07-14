import sys
import modules.forms.form_base as form_base
import modules.variables as var
import modules.level as level
from utn_fra.pygame_widgets import ( Label, ButtonImageSound )

def init_form_menu(dict_form_data: dict):
    form = form_base.create_base_form(dict_form_data)

    form['lbl_titulo'] = Label(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 - 250, text="Dragon Ball", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=75)
    form['lbl_subtitulo'] = Label(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 - 190, text="Podras vencer a la maquina?", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=25, color=var.COLOR_BLANCO)

    form['btn_start'] = ButtonImageSound(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 - 105, text="Start", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/forms/menu/start.png', sound_path=dict_form_data.get('btn_sound_path'), font_size=50, on_click_param="form_game", on_click=on_click)
    form['btn_ranking'] = ButtonImageSound(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 - 35, text="Ranking", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/forms/menu/ranking.png', sound_path=dict_form_data.get('btn_sound_path'), font_size=50, on_click_param="form_ranking", on_click=on_click)
    form['btn_options'] = ButtonImageSound(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 + 35, text="Options", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/forms/menu/options.png', sound_path=dict_form_data.get('btn_sound_path'), font_size=50, on_click_param="form_options", on_click=on_click)
    form['btn_exit'] = ButtonImageSound(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 + 105, text="Exit", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/forms/menu/exit.png', sound_path=dict_form_data.get('btn_sound_path'), font_size=50, on_click_param="form_exit", on_click=on_exit)
    
    form['lbl_alumno'] = Label(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1] - 30, text="Bruno Lippi", screen=form.get('screen'), color=var.COLOR_BLANCO, font_path=var.FONT_ALAGARD, font_size=35)
    
    form['widgets_list'] = [
        form.get('lbl_titulo'), form.get('lbl_subtitulo'), form.get('btn_start'), form.get('btn_options'), form.get('btn_ranking'), form.get('btn_exit'), form.get('lbl_alumno')
    ]

    form_base.forms_dict[dict_form_data.get('name')] = form

    return form

def on_click(param: str):
    print(param)

    if param == "form_game":
        form_start = form_base.forms_dict[param]
        form_start['level'] = level.reset_level(
            form_start.get('level'), form_start.get('player'),
            form_start.get('screen'), form_start.get('level_number')
        )
        level.init_data_level(form_start.get('level'))
    form_base.set_active(param)
    form_base.stop_music()
    form_base.play_music(form_base.forms_dict[param])

def on_exit(param: str):
    sys.exit()

def draw(form_data: dict):
    form_base.draw(form_data)
    form_base.draw_widgets(form_data)

def update(form_data: dict):
    form_base.update(form_data)