import pygame as pg 
import random as rd
import modules.card as card_mod
import modules.variables as var
import modules.utils as utils
from modules.player import init_player, set_stats as set_player_stats

def init_level(player: dict, enemy: dict, screen: pg.Surface, level_number: int) -> dict:
    level_data = {}
    
    level_data['level_number'] = level_number
    level_data['configs'] = {}
    
    level_data['decks_path'] = ''
    level_data['screen'] = screen
    level_data['player'] = player
    level_data['enemy'] = enemy
    
    level_data['game_over'] = False
    level_data['game_started'] = False
    level_data['saved_score'] = False
    level_data['level_timer'] = var.GAME_TIMER
    level_data['winner'] = None

    level_data['cards_deck'] = []

    level_data['player_deck'] = []
    level_data['player_deck_used'] = []

    level_data['enemy_deck'] = []
    level_data['enemy_deck_used'] = []
    
    level_data['data_loaded'] = False
    
    return level_data

def reset_level(level_data: dict, player: dict, screen: pg.Surface, level_number: int) -> dict:
    player['score'] = 0
    level_data = init_level(player, init_player("Enemy"), screen, level_number)

    return level_data

def init_data_level(level_data: dict):
    load_level_configs(level_data)
    load_card_decks(level_data)

    generate_final_decks(level_data)
    level_data['game_started'] = True

def load_level_configs(level_data: dict):
    if not level_data.get('game_over') and not level_data.get('data_loaded'):
        level_data['configs'] = utils.load_configs()

        level_data['decks_path'] = level_data.get('configs').get('decks_path')
        level_data['coords_iniciales'] = level_data.get('configs').get('coordenada_mazo_1')
        level_data['coords_finales'] = level_data.get('configs').get('coordenada_mazo_2')

        level_data['coords_enemy_deck'] = level_data.get('configs').get('coords_enemy_deck')
        level_data['coords_enemy_deck_used'] = level_data.get('configs').get('coords_enemy_deck_used')

        level_data['coords_player_deck'] = level_data.get('configs').get('coords_player_deck')
        level_data['coords_player_deck_used'] = level_data.get('configs').get('coords_player_deck_used')

        level_data['selected_enemy_deck'] = level_data.get('configs').get('selected_enemy_deck')
        level_data['selected_player_deck'] = level_data.get('configs').get('selected_player_deck')

        level_data['qty_cards_deck_player'] = level_data.get('configs').get('qty_cards_deck_player', 10)
        level_data['qty_cards_deck_enemy'] = level_data.get('configs').get('qty_cards_deck_enemy', 10)

        level_data['data_loaded'] = True

def load_card_decks(level_data: dict):
    if not level_data.get('game_over'):
        level_data['cards_deck'] = utils.generate_db(level_data.get('decks_path')).get('cards')

def generate_final_decks(level_data: dict):
    original_deck = level_data.get('cards_deck')
    
    level_data['player_deck'] = []
    level_data['enemy_deck'] = []

    for card in original_deck.get(level_data['selected_enemy_deck']):
        final_card = card_mod.init_carta(card, level_data.get('coords_enemy_deck'))
        level_data['enemy_deck'].append(final_card)

    rd.shuffle(level_data.get('enemy_deck'))

    for card in original_deck.get(level_data['selected_player_deck']):
        final_card = card_mod.init_carta(card, level_data.get('coords_player_deck'))
        level_data['player_deck'].append(final_card)
    
    rd.shuffle(level_data.get('player_deck'))

    qty_cards_deck_enemy = level_data['qty_cards_deck_enemy']
    level_data['enemy_deck'] = level_data['enemy_deck'][:qty_cards_deck_enemy]

    set_player_stats(level_data['enemy'], card_mod.get_deck_stats(level_data['enemy_deck']))
    print(f'stats enemy: {level_data['enemy']}')

    qty_cards_deck_player = level_data['qty_cards_deck_player']
    level_data['player_deck'] = level_data['player_deck'][:qty_cards_deck_player]
    
    set_player_stats(level_data['player'], card_mod.get_deck_stats(level_data['player_deck']))
    print(f'stats player: {level_data['player']}')

# Se encarga de revisar los eventos que ocurran buscando una interaccion del usuario
def handle_event(level_data: dict, event_queue: list[pg.event.Event]):
    if level_data.get('game_started') and not level_data.get('game_over'):
        if level_data['player']['active_bonus'] == 'heal':
            level_data['player']['hp'] = level_data['player']['hp_original']

        for event in event_queue:
            if event.type == pg.MOUSEBUTTONDOWN:
                    if level_data.get('player_deck')[-1]['rect'].collidepoint(event.pos):
                        handle_play(level_data)
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                    handle_play(level_data)

# Se encarga de gestionar la jugada
def handle_play(level_data: dict):
     if level_data.get('game_started') and not level_data.get('game_over'):

        # Carta del jugador
        if level_data.get('player_deck'):
            # Gestiona la carta, esta funcionalidad debe ser migrada a carta.py
            card_mod.assign_card_coords(level_data.get('player_deck')[-1], level_data.get('coords_player_deck_used'))
            card_mod.change_card_visibility(level_data.get('player_deck')[-1], True)

            player_card = level_data.get('player_deck').pop()
            level_data.get('player_deck_used').append(player_card)

        # Carta de la maquina
        if level_data.get('enemy_deck'):
            card_mod.assign_card_coords(level_data.get('enemy_deck')[-1], level_data.get('coords_enemy_deck_used'))
            card_mod.change_card_visibility(level_data.get('enemy_deck')[-1], True)

            enemy_card = level_data.get('enemy_deck').pop()
            level_data.get('enemy_deck_used').append(enemy_card)

        loser = card_mod.check_loser_hand(enemy_card, player_card)

        if loser == 'enemy':
            hp, attack, defense = card_mod.get_card_stats_with_bonus(player_card)
            points = calculate_points(player_card, enemy_card)
            level_data['player']['score'] += points
        else:
            hp, attack, defense = card_mod.get_card_stats_with_bonus(enemy_card)
            
            if level_data['player']['active_bonus'] == 'shield':
                print('used shield')
                loser = 'enemy'

        level_data['player']['active_bonus'] = ''
        level_data[loser]['hp'] -= hp
        level_data[loser]['attack'] -= attack
        level_data[loser]['defense'] -= defense

def calculate_points(winner_card: dict, loser_card: dict) -> int:
    return round((int(winner_card['attack']) - int(loser_card['defense'])) / 100)

def is_time_over(level_data: dict) -> bool:
    return level_data.get('level_timer') <= 0

def is_deck_empty(player_deck: list) -> bool:
    return len(player_deck) == 0

def has_anyone_lost(level_data: dict) -> bool:
    return level_data['player']['hp'] < 0 or level_data['enemy']['hp'] < 0

def is_game_over(level_data: dict) -> bool:
    return is_deck_empty(level_data['player_deck']) or\
        is_deck_empty(level_data['enemy_deck']) or\
        is_time_over(level_data) or\
        has_anyone_lost(level_data)

def get_level_winner(level_data: dict) -> str:
    if level_data['player']['hp'] < level_data['enemy']['hp']:
        return 'enemy'
    else:
        return 'player'

def draw(level_data: dict):
    if level_data.get('player_deck'):
        card_mod.draw_card(level_data.get('player_deck')[-1], level_data.get('screen'))
    if level_data.get('player_deck_used'):
        card_mod.draw_card(level_data.get('player_deck_used')[-1], level_data.get('screen'))
    
    if level_data.get('enemy_deck'):
        card_mod.draw_card(level_data.get('enemy_deck')[-1], level_data.get('screen'))
    if level_data.get('enemy_deck_used'):
        card_mod.draw_card(level_data.get('enemy_deck_used')[-1], level_data.get('screen'))

def update(level_data: dict, event_queue: list[pg.event.Event]):

    handle_event(level_data, event_queue)

    if is_game_over(level_data):
        level_data['game_over'] = True
        level_data['winner'] = get_level_winner(level_data)
        print(f'{level_data["winner"]} won the game')
