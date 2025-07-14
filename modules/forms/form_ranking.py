import modules.forms.form_base as form_base
import modules.variables as var
import modules.utils as utils
from utn_fra.pygame_widgets import ( Label, ButtonImage )

def init_form_ranking(dict_form_data: dict, player: dict):
    form = form_base.create_base_form(dict_form_data)

    form['player'] = player
    form['data_loaded'] = False

    form['ranking_screen'] = []
    form['ranking_list'] = []

    form['lbl_titulo'] = Label(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 - 250, text="Dragon Ball", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=75)
    form['lbl_subtitulo'] = Label(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 - 175, text="Ranking", screen=form.get('screen'), font_path=var.FONT_ALAGARD, color=var.COLOR_AZUL, font_size=50)

    form['btn_back'] = ButtonImage(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2 +250, text="Back", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/forms/back.png', font_size=50, on_click_param="form_menu", on_click=on_exit)
    
    form['widgets_list'] = [
        form.get('lbl_titulo'), form.get('lbl_subtitulo'), form.get('btn_back')
    ]

    form_base.forms_dict[dict_form_data.get('name')] = form

    return form

def on_exit(param: str):
    print(param)

    form_base.set_active(param)
    form_base.forms_dict['form_ranking']['data_loaded'] = False

    form_base.stop_music()
    form_base.play_music(form_base.forms_dict[param])

def init_ranking(form_data: dict):
    if not form_data.get('data_loaded'):
        form_data['ranking_list'] = utils.load_ranking()[:10]
        form_data['ranking_screen'] = []
        matrix = form_data.get('ranking_list')

        for index in range(len(matrix)):
            row = matrix[index]

            # Numero
            form_data['ranking_screen'].append(
                Label(x=var.GAME_DIMENSIONS[0]//2 - 220, y=var.GAME_DIMENSIONS[1]//2.9 + index * 31, text=f"{index + 1}", screen=form_data.get('screen'), font_path=var.FONT_ALAGARD, color=var.COLOR_NEGRO, font_size=40)
            )
            # Nombre
            form_data['ranking_screen'].append(
                Label(x=var.GAME_DIMENSIONS[0]//2, y=var.GAME_DIMENSIONS[1]//2.9 + index * 31, text=f"{row[0]}", screen=form_data.get('screen'), font_path=var.FONT_ALAGARD, color=var.COLOR_NEGRO, font_size=40)
            )
            # Score
            form_data['ranking_screen'].append(
                Label(x=var.GAME_DIMENSIONS[0]//2 + 220, y=var.GAME_DIMENSIONS[1]//2.9 + index * 31, text=f"{row[1]}", screen=form_data.get('screen'), font_path=var.FONT_ALAGARD, color=var.COLOR_NEGRO, font_size=40)
            )
        
        form_data['data_loaded'] = True


def draw(form_data: dict):
    form_base.draw(form_data)
    form_base.draw_widgets(form_data)

    for label in form_data.get('ranking_screen'):
        label.draw()

def update(form_data: dict):
    if form_data.get('active'):
        init_ranking(form_data)
    form_base.update(form_data)