import pygame as pg
import modules.utils as utils

def init_carta(card_dict: dict, coords: tuple[int, int]) -> dict:
    card_final_dict = {}
    card_final_dict['id'] = card_dict.get('id')
    card_final_dict['nombre'] = card_dict.get('nombre')
    card_final_dict['frase'] = card_dict.get('frase')
    card_final_dict['hp'] = card_dict.get('hp')
    card_final_dict['attack'] = card_dict.get('attack')
    card_final_dict['defense'] = card_dict.get('defense')
    card_final_dict['bonus'] = card_dict.get('bonus')
    card_final_dict['path_imagen_frente'] = card_dict.get('path_imagen_frente')
    card_final_dict['path_imagen_reverso'] = card_dict.get('path_imagen_reverso')

    card_final_dict['visible'] =  False
    card_final_dict['imagen'] = utils.resize_image_card(card_final_dict.get('path_imagen_frente'), 0.65)
    card_final_dict['imagen_reverso'] = utils.resize_image_card(card_final_dict.get('path_imagen_reverso'), 0.65)

    card_final_dict['rect'] = card_final_dict.get('imagen').get_rect()
    card_final_dict['rect'].x = coords[0]
    card_final_dict['rect'].y = coords[1]

    card_final_dict['rect_reverso'] = card_final_dict.get('imagen_reverso').get_rect()
    card_final_dict['rect_reverso'].x = coords[0]
    card_final_dict['rect_reverso'].y = coords[1]

    return card_final_dict

def draw_card(card_data: dict, screen: pg.Surface):
    if card_data.get('visible'):
        screen.blit(card_data.get('imagen'), card_data.get('rect'))
    else:
        screen.blit(card_data.get('imagen_reverso'), card_data.get('rect_reverso'))

def assign_card_coords(carta_dict: dict, nueva_coordenada: tuple[int,int]):
    carta_dict['rect'].topleft = nueva_coordenada
    carta_dict['rect_reverso'].topleft = nueva_coordenada

def change_card_visibility(carta_dict: dict, visibilidad: bool):
    carta_dict['visible'] = visibilidad

def get_deck_stats(deck: list[dict]) -> tuple[int, int, int]:
    hp = 0
    attack = 0
    defense = 0

    for card in deck:
        hp += int(card['hp'])
        attack += int(card['attack'])
        defense += int(card['defense'])

    return hp, attack, defense

def get_card_stats_with_bonus(card: dict) -> tuple[int, int, int]: 
    bonus = int(card['bonus']) / 100

    hp = int(card['hp'])
    hp = round(hp + (hp * bonus))

    attack = int(card['attack'])
    attack = round(attack + (attack * bonus))
    
    defense = int(card['defense'])
    defense = round(defense + (defense * bonus))

    return hp, attack, defense

def check_loser_hand(enemy_card: dict, player_card: dict) -> str:
    bonus_enemy = int(enemy_card['bonus']) / 100
    attack_enemy = int(enemy_card['attack'])
    attack_enemy = attack_enemy + (attack_enemy * bonus_enemy)

    bonus_player = int(player_card['bonus']) / 100
    attack_player = int(player_card['attack'])
    attack_player = attack_player + (attack_player * bonus_player)

    if  attack_player > attack_enemy:
        print('Enemy lost')
        return "enemy"
    else:
        print("Player lost")
        return "player"