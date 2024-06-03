from PIL import Image

NEW_SIZE = (720, 720)

ENEMY_1_1 = "material/Icons/enemy/enemy_type1/enemy-type1-frame1.png" 
ENEMY_1_2 = "material/Icons/enemy/enemy_type1/enemy-type1-frame2.png"

ENEMY_2_1 = "material/Icons/enemy/enemy_type2/enemy-type2-frame1.png"
ENEMY_2_2 = "material/Icons/enemy/enemy_type2/enemy-type2-frame2.png"

ENEMY_3_1 = "material/Icons/enemy/enemy_type3/enemy-type3-frame1.png"
ENEMY_3_2 = "material/Icons/enemy/enemy_type3/enemy-type3-frame2.png"

MYSTERY = "material/Icons/enemy/mystery/mystery-frame1.png"

BLOW_EFFECT = "material/Icons/enemy/enemy-blow-effect.png"

MYSTERY_BLOW_EFFECT = "material/Icons/enemy/mystery/mystery-blow-effect.png"

def resize(file_path: str, new_size: tuple, new_name: str) -> None:
    
    image = Image.open(file_path)

    image = image.resize(new_size)

    image.save(new_name)

LIST = [ENEMY_1_1, ENEMY_1_2, ENEMY_2_1, ENEMY_2_2, ENEMY_3_1, ENEMY_3_2, MYSTERY, BLOW_EFFECT, MYSTERY_BLOW_EFFECT]

for index, path in enumerate(LIST, 1):
    resize(path, NEW_SIZE, "temp/temp"+ str(index) + ".png")



