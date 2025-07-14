import os
import json
import pygame as pg
import random as rd
import modules.variables as var

def show_text(surface: pg.Surface, texto: str, pos: tuple, font, color = pg.Color('black')) -> None:
    words = []

    for word in texto.splitlines():
        words.append(word.split(' '))

    space = font.size(' ')[0]
    ancho_max, alto_max = surface.get_size()
    x, y = pos

    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            ancho_palabara, alto_palabra = word_surface.get_size()

            if x + ancho_palabara >= ancho_max:
                x = pos[0]
                y += alto_palabra
            surface.blit(word_surface, (x, y))
            x += ancho_palabara + space
        x = pos[0]
        y += alto_palabra

def create_cuadro(dimensiones: tuple, coordenadas: tuple, color: tuple) -> dict:
    cuadro = {}
    
    cuadro['superficie'] = pg.Surface(dimensiones)
    cuadro['rectangulo'] = cuadro.get('superficie').get_rect()
    cuadro['rectangulo'].topleft = coordenadas
    cuadro['superficie'].fill(pg.Color(color))

    return cuadro

def resize_image_card(path: str, porcentage: int) -> pg.Surface:
    img_raw = pg.image.load(path)
    height = int(img_raw.get_height() * float(porcentage / 2)) # Para que no quede desproporcionada, asumiendo un ratio 2:1
    width = int(img_raw.get_width() * float(porcentage))

    return pg.transform.scale(img_raw, (height, width))

def map_ranking_values(matrix: list[list], index: int, cb) -> None:
    for row in range(len(matrix)):
        value = matrix[row][1]
        matrix[row][index] = cb(value)

def load_ranking() -> list:
    ranking = []

    with open(var.RANKING_PATH, 'r', encoding='utf-8') as file:
        lines = file.read()

        for line in lines.split('\n'):
            if line:
                ranking.append(line.split(','))

    map_ranking_values(ranking, 1, lambda value: int(value) if value.isdigit() else value )
    ranking.sort(key=lambda row: row[1], reverse=True)

    return ranking

def save_ranking(player_dict: dict):
    with open(var.RANKING_PATH, 'a', encoding='utf-8') as file:
        data = f'{player_dict.get("name")},{player_dict.get("score")}\n'
        file.write(data)
        print('Ranking updated successfully')

def load_configs(path = var.CONFIG_JSON_PATH) -> dict:
    configs = {}

    with open(path, 'r', encoding='utf-8') as file:
        configs = json.load(file)

    return configs


def save_configs(key: str, value: str, path = var.CONFIG_JSON_PATH) -> dict:
    with open(path, 'r+', encoding='utf-8') as file:
        configs = json.load(file)
        file.seek(0)
        
        configs[key] = value

        json.dump(configs, file, indent=2)
        file.truncate()

        file.close()
    
    
def generate_db(root_path_cards: str) -> dict:
    cards_dict = {
        "cards": {}
    }
    
    for root, dir, files in os.walk(root_path_cards, topdown=True):
        reverse_path = ""
        deck_cards = []
        if os.name in ['nt', 'dos']:
            deck_name = root.split('\\')[-1]
        else:
            deck_name = root.split('/')[-1]
        
        for file in files:
            path_card = os.path.join(root, file)

            if 'reverse' in path_card:
                reverse_path = path_card
            else:
                file = file.replace('\\', '/')
                filename = file.split('.')[-2]
                card_data = filename.split("_")

                card = {
                    'id': f'{deck_name}-{filename}',
                    "hp": card_data[2],
                    "attack": card_data[4],
                    "defense": card_data[6],
                    "bonus": card_data[7],
                    'path_imagen_frente': path_card,
                }

                if card_data[2]:
                    card["hp"] = card_data[2]

                deck_cards.append(card)

        for index_card in range(len(deck_cards)):
            deck_cards[index_card]['path_imagen_reverso'] = reverse_path

        cards_dict['cards'][deck_name] = deck_cards

    return cards_dict