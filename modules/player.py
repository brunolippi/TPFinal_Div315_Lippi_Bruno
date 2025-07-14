import modules.card as card_mod

def init_player(name = 'Player'):
    return {
        "name": name,
        'score': 0,
        'hp': 0,
        'attack': 0,
        'defense': 0,
        'active_bonus': ''
    }

def set_stats(player_dict: dict, stats: tuple[int, int, int]):
    hp_player, atk_player, def_player = stats
    
    player_dict['hp'] = hp_player
    player_dict['hp_original'] = hp_player
    player_dict['attack'] = atk_player
    player_dict['defense'] = def_player