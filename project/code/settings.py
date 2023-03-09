from mapping import PROJ_DIR
# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

# Weapons
weapon_data ={
    'sword':{'cooldown': 100, 'damage': 15,'graphic':PROJ_DIR+'/graphics/weapons/sword/full.png'},
    'lance':{'cooldown': 400, 'damage': 30,'graphic':PROJ_DIR+'/graphics/weapons/lance/full.png'},
    'axe':{'cooldown': 100, 'damage': 15,'graphic':PROJ_DIR+'/graphics/weapons/axe/full.png'},
    'rapier':{'cooldown': 100, 'damage': 15,'graphic':PROJ_DIR+'/graphics/weapons/rapier/full.png'},
    'sai':{'cooldown': 100, 'damage': 15,'graphic':PROJ_DIR+'/graphics/weapons/sai/full.png'}}