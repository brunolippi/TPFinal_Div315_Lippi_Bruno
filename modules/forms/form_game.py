import pygame as pg
import modules.forms.form_base as form_base
import modules.variables as var
import modules.card as card_mod
import modules.level as level
from modules.player import init_player
from utn_fra.pygame_widgets import ( Label, ButtonImage )

def init_form_game(dict_form_data: dict, player: dict):
    form = form_base.create_base_form(dict_form_data)

    form['player'] = player
    form['game_loaded'] = False
    form['level'] = level.init_level(player=form['player'], enemy=init_player('Enemy'), screen=form.get('screen'), level_number=form.get('level_number'))
    form['clock'] = pg.time.Clock()
    form['last_tick'] = pg.time.get_ticks()

    form['heal_used'] = False
    form['shield_used'] = False

    form['lbl_time_left'] = Label(x=160, y=var.GAME_DIMENSIONS[1]//2, text=f"Time left: {form.get("level").get("level_timer")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=30)
    form['lbl_score'] = Label(x=var.GAME_DIMENSIONS[0]//2, y=25, text=f"Score: {form.get("player").get("score")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=40, color=var.COLOR_BLANCO)

    form['lbl_hp_enemy'] = Label(x=220, y=165, text=f"HP: {form.get('level').get("enemy").get("hp")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=25, color=var.COLOR_BLANCO)
    form['lbl_atk_enemy'] = Label(x=155, y=197, text=f"ATK: {form.get('level').get("enemy").get("attack")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=25, color=var.COLOR_BLANCO)
    form['lbl_def_enemy'] = Label(x=155, y=230, text=f"DEF: {form.get('level').get("enemy").get("defense")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=25, color=var.COLOR_BLANCO)

    form['lbl_hp_player'] = Label(x=220, y=495, text=f"HP: {form.get('level').get("player").get("hp")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=25, color=var.COLOR_BLANCO)
    form['lbl_atk_player'] = Label(x=155, y=527, text=f"ATK: {form.get('level').get("player").get("attack")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=25, color=var.COLOR_BLANCO)
    form['lbl_def_player'] = Label(x=155, y=560, text=f"DEF: {form.get('level').get("player").get("defense")}", screen=form.get('screen'), font_path=var.FONT_ALAGARD, font_size=25, color=var.COLOR_BLANCO)


    form['btn_back'] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 85, y=35, text="Back", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/forms/back.png', font_size=50, on_click_param="form_menu", on_click=on_exit)
    form['btn_play'] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 82, y=385, text="Play", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/buttons_image/btn_play_hand.png', font_size=50, on_click_param=form, on_click=on_play)
    
    form['btn_bonus_1'] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 78, y=575, text="Heal", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/buttons_image/heal.png', font_size=50, on_click_param={"bonus":"heal", "form": form}, on_click=on_bonus)
    form['btn_bonus_2'] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 78, y=630, text="Shield", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/buttons_image/shield.png', font_size=50, on_click_param={"bonus":"shield", "form": form}, on_click=on_bonus)
    form['btn_active_bonus_2'] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 82, y=210, text="Shield", width=126, height=45, screen=form.get('screen'), image_path='./assets/img/buttons_image/shield.png', font_size=50, on_click_param={"bonus":"shield", "form": form}, on_click=on_bonus)

    form['widgets_list'] = [
        form.get('lbl_time_left'),
        form.get('lbl_score'),
        form.get('lbl_hp_enemy'),
        form.get('lbl_atk_enemy'),
        form.get('lbl_def_enemy'),
        form.get('lbl_hp_player'),
        form.get('lbl_atk_player'),
        form.get('lbl_def_player'),
        form.get('btn_back'), 
        form.get('btn_play'), 
        form.get('btn_bonus_1'), 
        form.get('btn_bonus_2'),
    ]

    form_base.forms_dict[dict_form_data.get('name')] = form

    return form

def on_play(form: dict):
    level.handle_play(form['level'])

def on_bonus(form_and_bonus: dict):
    print(form_and_bonus['bonus'])
    if form_and_bonus['bonus'] == 'heal' and not form_and_bonus['form']['heal_used']:
        form_and_bonus['form']['player']['active_bonus'] = 'heal'
        form_and_bonus['form']['heal_used'] = True
        form_and_bonus['form']['widgets_list'][-2] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 78, y=575, text="Heal", width=126, height=45, screen=form_and_bonus['form'].get('screen'), image_path='./assets/img/buttons_image/heal_used.png', font_size=50, on_click_param={}, on_click=())

    elif form_and_bonus['bonus'] == 'shield' and not form_and_bonus['form']['shield_used']:
        form_and_bonus['form']['player']['active_bonus'] = 'shield'
        form_and_bonus['form']['shield_used'] = True
        form_and_bonus['form']['widgets_list'][-1] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 78, y=630, text="Shield", width=126, height=45, screen=form_and_bonus['form'].get('screen'), image_path='./assets/img/buttons_image/shield_used.png', font_size=50, on_click_param={}, on_click=())

def on_exit(param: str):
    form_base.forms_dict['form_game']['heal_used'] = False
    form_base.forms_dict['form_game']['shield_used'] = False

    form_base.forms_dict['form_game']['widgets_list'][-2] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 78, y=575, text="Heal", width=126, height=45, screen=form_base.forms_dict['form_game'].get('screen'), image_path='./assets/img/buttons_image/heal.png', font_size=50, on_click_param={"bonus":"heal", "form": form_base.forms_dict['form_game']}, on_click=on_bonus)
    form_base.forms_dict['form_game']['widgets_list'][-1] = ButtonImage(x=var.GAME_DIMENSIONS[0] - 78, y=630, text="Shield", width=126, height=45, screen=form_base.forms_dict['form_game'].get('screen'), image_path='./assets/img/buttons_image/shield.png', font_size=50, on_click_param={"bonus":"shield", "form": form_base.forms_dict['form_game']}, on_click=on_bonus)


    form_base.stop_music()
    form_base.play_music(form_base.forms_dict[param])
    form_base.set_active(param)


def update_timer(form_data: dict):
    if form_data.get('level').get('level_timer') > 0 and not form_data.get('level').get('game_over'):
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - form_data.get('last_tick') > 1000:
            form_data['last_tick'] = tiempo_actual
            form_data.get('level')['level_timer'] -= 1

            form_data['lbl_time_left'].update_text(f"Time left: {form_data.get("level").get("level_timer")}", var.COLOR_BLANCO)

def update_stats(form_data: dict):
    form_data['lbl_hp_enemy'].update_text(f"HP: {form_data.get('level').get("enemy").get("hp")}", var.COLOR_BLANCO)
    form_data['lbl_atk_enemy'].update_text(f"atk: {form_data.get('level').get("enemy").get("attack")}", var.COLOR_BLANCO)
    form_data['lbl_def_enemy'].update_text(f"def: {form_data.get('level').get("enemy").get("defense")}", var.COLOR_BLANCO)
    
    form_data['lbl_hp_player'].update_text(f"HP: {form_data.get('level').get("player").get("hp")}", var.COLOR_BLANCO)
    form_data['lbl_atk_player'].update_text(f"atk: {form_data.get('level').get("player").get("attack")}", var.COLOR_BLANCO)
    form_data['lbl_def_player'].update_text(f"def: {form_data.get('level').get("player").get("defense")}", var.COLOR_BLANCO)

    if form_data['level']['game_over']:
        form_data['lbl_score'].update_text(f"GAME OVER - {form_data['level']['winner']} WON", var.COLOR_BLANCO)
    else:
        form_data['lbl_score'].update_text(f"Score: {form_data.get("player").get("score")}", var.COLOR_BLANCO)
    
def update_bonus_btn(form_data: dict):
    if  form_data['player']['active_bonus'] == 'shield':
        form_data['widgets_list'].append(form_data["btn_active_bonus_2"])

    if form_data['player']['active_bonus'] != 'shield':
        if form_data["btn_active_bonus_2"] in form_data['widgets_list']:
            # Pareciera ser que `del` es mas rapido que .pop()
            del form_data['widgets_list'][form_data['widgets_list'].index(form_data["btn_active_bonus_2"])]

def draw(form_data: dict):
    form_base.draw(form_data)
    form_base.draw_widgets(form_data)
    
    level.draw(form_data.get('level'))

def update(form_data: dict, event_queue: list[pg.event.Event]):
    update_timer(form_data)
    update_stats(form_data)
    update_bonus_btn(form_data)

    level.update(form_data.get('level'), event_queue)

    if form_data.get('level').get('game_over'):
        form_base.stop_music()
        form_base.play_music(form_base.forms_dict['form_enter_name'])
        form_base.set_active('form_enter_name')

    form_base.update(form_data)