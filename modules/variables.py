import pygame as pg

GAME_FPS = 60

GAME_TITLE = 'Dragon Ball Game - Bruno Lippi'
GAME_ICON_PATH = './assets/img/icons/1_star.png'
game_icon = pg.image.load(GAME_ICON_PATH)
GAME_DIMENSIONS = (1280, 720)

FONT_ALAGARD = './assets/fonts/alagard.ttf'

COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_ROJO = (255, 0, 0)
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)

# ------ Menu ------
MENU_MUSIC_PATH = './assets/audio/music/form_main_menu.ogg' 
MENU_BG_PATH = './assets/img/forms/img_1.png'

# ------ Ranking ------
RANKING_MUSIC_PATH = './assets/audio/music/form_ranking.ogg' 
RANKING_BG_PATH = './assets/img/img_20.jpg'
RANKING_PATH = './ranking.csv'

# ------ Game ------
GAME_MUSIC_PATH = './assets/audio/music/battle_music.ogg' 
GAME_BG_PATH = './assets/img/background_cards.png'
GAME_DECKS_PATH = './assets/img/decks'

GAME_TIMER = 60

# ------ Options ------
CONFIG_JSON_PATH = './config.json'
OPTIONS_BG_PATH = './assets/img/forms/img_3.jpg'