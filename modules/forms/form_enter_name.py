import pygame as pg
import modules.forms.form_base as form_base
import modules.player as player_mod
import modules.variables as var
import modules.utils as utils
from utn_fra.pygame_widgets import (
    Button, ButtonImage, Label, TextBox
)

def init_form_enter_name(dict_form_data: dict, player: dict):
    form = form_base.create_base_form(dict_form_data)
    form['player'] = player
    form['score'] = player['score']
    form['confirm_name'] = False

    form['lbl_title'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1]//2 - 250,
        text="Dragon Ball", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=75
    )

    form['lbl_subtitle'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 180,
        text="Le ganaste a la maquina del mal!", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=55, color=var.COLOR_AZUL
    )

    form['lbl_score'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 130,
        text=f'Score: {form.get("score")}', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=30, color=var.COLOR_BLANCO
    )

    form['lbl_ask_name'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 - 20,
        text='ESCRIBE TU NOMBRE', screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=40, color=var.COLOR_NEGRO
    )

    form['text_box'] = TextBox(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 + 40,
        text='__________' ,screen=form.get('screen'), font_path=var.FONT_ALAGARD,
        font_size=25, color=var.COLOR_BLANCO
    )
    
    form['btn_confirm_name'] = ButtonImage(
         x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 + 100,
         text="Enter", width=126, height=45, 
         screen=form.get('screen'), image_path='./assets/img/forms/enter.png', 
         font_size=50, on_click_param=form, on_click=click_confirm_name)
    
    
    form['widgets_list'] = [
        form.get('lbl_title'),form.get('lbl_subtitle'),form.get('lbl_ask_name'),form.get('lbl_score'),
        form.get('btn_confirm_name')
    ]
    
    form_base.forms_dict[dict_form_data.get('name')] = form

    return form

def click_confirm_name(form_dict: dict):
    form_dict['confirm_name'] = True
    form_dict['player']['name'] = form_dict.get('writing_text').text

    utils.save_ranking(form_dict.get('player'))

    form_base.set_active('form_ranking')

def draw(form_dict: dict):
    form_base.draw(form_dict)
    form_base.draw_widgets(form_dict)
    
    form_dict.get('text_box').draw()
    
    form_dict['writing_text'] = Label(
        x=var.GAME_DIMENSIONS[0] // 2, y=var.GAME_DIMENSIONS[1] // 2 + 30,
        text=f'{form_dict.get("text_box").writing.upper()}',
        screen=form_dict.get('screen'), font_path=var.FONT_ALAGARD,
        font_size=30, color=var.COLOR_VERDE
    )
    
    form_dict.get('writing_text').draw()

def update(form_dict: dict, event_queue: list[pg.event.Event]):
    form_dict['score'] = form_dict['player']['score']
    form_dict['winner'] = form_base.forms_dict['form_game']['level']['winner']

    if form_dict['winner'] == 'enemy': 
        form_dict.get('widgets_list')[1].update_text("Has sido derrotado por la IA <emocion></triste>", var.COLOR_AZUL)

    form_dict.get('widgets_list')[3].update_text(f'SCORE: {form_dict.get("score")}', var.COLOR_AZUL)

    for event in event_queue:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    click_confirm_name(form_dict)

    form_dict.get('text_box').update(event_queue)
    form_base.update(form_dict)