import pygame, random
import os.path

FPS = 15
TILE_SIZE = 40
tile_w = tile_h = 40

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Meny:
    def __init__(self):
        running = True
        clock = pygame.time.Clock()
        image = pygame.image.load("data/sprites/fon_meny.jpg")
        screen.blit(image, (35, 0))
        image = pygame.image.load("data/sprites/character_v.png")
        screen.blit(image, (350, 470))
        f1 = pygame.font.Font(None, 70)
        hp_bur = f1.render("Нажмите пробел", 1, (0, 0, 0))
        screen.blit(hp_bur, (600, 670))
        file_path = "data/saves/user.txt"
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if os.path.exists(file_path):
                            running = False
                        else:
                            with open("data/saves/user.txt", "w") as f:
                                f.write("1" + '\n')
                                f.write("1" + '\n')
                                f.write("map0" + '\n')
                                f.write("None" + '\n')
                                f.write("None" + '\n')
                            running = False
            pygame.display.flip()
            clock.tick(FPS)


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.x, self.y = pos_x, pos_y
        self.image = pygame.image.load("data/sprites/wall.jpg")
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))
        self.rect = self.image.get_rect().move(pos_x * tile_w + 5, pos_y * tile_h + 5)


class Map_editor:
    def __init__(self, map_name, free_tile, finish_tile):
        self.map = []
        with open("data/maps/" + map_name) as map_file:
            for line in map_file:
                self.map.append(list(map(int, line.split())))
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tile
        self.finish_tile = finish_tile

    def render(self, screen):
        image = pygame.image.load("data/sprites/fon.jpg")
        screen.blit(image, (1000, 20))
        image = pygame.image.load("data/sprites/char_inventory.png")
        screen.blit(image, (1000, 20))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1040, 180))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1390, 180))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1215, 40))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1215, 370))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1215, 150))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1000, 550))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1070, 550))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1140, 550))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1210, 550))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1280, 550))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1350, 550))
        image = pygame.image.load("data/sprites/pole_inventori.png")
        screen.blit(image, (1420, 550))
        image = pygame.image.load("data/sprites/heart.png")
        screen.blit(image, (1000, 650))
        image = pygame.image.load("data/sprites/armor.png")
        screen.blit(image, (1250, 630))
        image = pygame.image.load("data/sprites/damage.png")
        screen.blit(image, (1250, 700))
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 1:
                    Tile(y, x)
                elif self.map[y][x] == 3:
                    image = pygame.image.load("data/sprites/item.png")
                    screen.blit(image, (y * self.tile_size + 5, x * self.tile_size + 5))
                elif self.map[y][x] == 4:
                    image = pygame.image.load("data/sprites/door.png")
                    screen.blit(image, (y * self.tile_size + 5, x * self.tile_size + 5))
                elif self.map[y][x] == 5:
                    image = pygame.image.load("data/sprites/door.png")
                    screen.blit(image, (y * self.tile_size + 5, x * self.tile_size + 5))
                elif self.map[y][x] == 6:
                    image = pygame.image.load("data/sprites/door.png")
                    screen.blit(image, (y * self.tile_size + 5, x * self.tile_size + 5))
                elif self.map[y][x] == 7:
                    image = pygame.image.load("data/sprites/door.png")
                    screen.blit(image, (y * self.tile_size + 5, x * self.tile_size + 5))
                elif self.map[y][x] == 8:
                    image = pygame.image.load("data/sprites/demon.png")
                    screen.blit(image, (y * self.tile_size + 5, x * self.tile_size + 5))

    def is_free(self, pos_x, pos_y):
        if int(self.map[pos_x][pos_y]) == 3:
            return 3

        return int(self.map[pos_x][pos_y]) in self.free_tiles

    def nexy_map(self, map_name):
        self.map = []
        with open("data/maps/" + map_name) as map_file:
            for line in map_file:
                self.map.append(list(map(int, line.split())))


class Character(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.invtntory = []
        self.eqwipment = []
        with open("data/saves/user.txt", "r") as f:
            if list(f)[3].rstrip('\n') != 'None':
                f.seek(0)
                for i in range(len(list(f)[3].rstrip('\n').split())):
                    f.seek(0)
                    self.invtntory.append(ITEMS_SWOP_OUT[list(f)[3].rstrip('\n').split()[i]])
        with open("data/saves/user.txt", "r") as f:
            if list(f)[4].rstrip('\n') != 'None':
                f.seek(0)
                for i in range(len(list(f)[4].rstrip('\n').split())):
                    f.seek(0)
                    self.eqwipment.append(ITEMS_SWOP_OUT[list(f)[4].rstrip('\n').split()[i]])
        self.head = True
        self.bady = True
        self.legs = True
        self.left_hand = True
        self.right_hand = True
        self.armor = 20
        self.hp = 100
        self.damage = 15
        self.x, self.y = pos_x, pos_y
        self.image = pygame.image.load("data/sprites/character.png")
        self.rect = self.image.get_rect().move(pos_x * tile_w + 5, pos_y * tile_h + 5)

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        self.hp = 100
        self.armor = 20
        self.damage = 15
        for i in range(len(self.eqwipment)):
            self.hp += self.eqwipment[i].get_state()[1]
            self.damage += self.eqwipment[i].get_state()[2]
            self.armor += self.eqwipment[i].get_state()[3]
            if self.eqwipment[i].get_state()[0] == "head":
                screen.blit(self.eqwipment[i].image, (1220, 40))
            if self.eqwipment[i].get_state()[0] == "bady":
                screen.blit(self.eqwipment[i].image, (1220, 147))
            if self.eqwipment[i].get_state()[0] == "legs":
                screen.blit(self.eqwipment[i].image, (1220, 367))
            if self.eqwipment[i].get_state()[0] == "right_hand":
                screen.blit(self.eqwipment[i].image, (1045, 180))
            if self.eqwipment[i].get_state()[0] == "left_hand":
                screen.blit(self.eqwipment[i].image, (1398, 180))
        for i in range(len(self.invtntory)):
            screen.blit(self.invtntory[i].image, (1000 + (70 * i), 550))
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))
        f1 = pygame.font.Font(None, 70)
        hp_bur = f1.render(str(self.hp), 1, (0, 0, 0))
        screen.blit(hp_bur, (1100, 670))
        damage_bur = f1.render(str(self.damage), 1, (0, 0, 0))
        screen.blit(damage_bur, (1330, 700))
        armor_bur = f1.render(str(self.armor), 1, (0, 0, 0))
        screen.blit(armor_bur, (1330, 635))

    def add_item(self, item):
        if len(self.invtntory) <= 7:
            self.invtntory.append(item)

    def eqwip_item(self, item):
        if item.get_state()[0] == "head":
            if self.head:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.head = False
        if item.get_state()[0] == "bady":
            if self.bady:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.bady = False
        if item.get_state()[0] == "legs":
            if self.legs:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.legs = False
        if item.get_state()[0] == "right_hand":
            if self.right_hand:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.right_hand = False

        if item.get_state()[0] == "left_hand":
            if self.left_hand:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.left_hand = False

    def remove_item(self, item):
        del self.eqwipment[item]

    def aneqwip_item(self, item):
        if item.get_state()[0] == "head":
            if self.head:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.head = False
        if item.get_state()[0] == "bady":
            if self.bady:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.bady = False
        if item.get_state()[0] == "legs":
            if self.legs:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.legs = False
        if item.get_state()[0] == "right_hand":
            if self.right_hand:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.right_hand = False

        if item.get_state()[0] == "left_hand":
            if self.left_hand:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.left_hand = False


width, height = 600, 600


class Game:
    def __init__(self, mapp, character):
        self.mapp = mapp
        self.character = character

    def rendr(self):
        self.mapp.render(screen)
        self.character.render(screen)
        with open("data/saves/user.txt", "r") as f:
            old_data = f.read()
            self.new_data = old_data

    def update_character(self):
        next_x, next_y = self.character.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            next_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            next_x += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            next_y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            next_y += 1
        if self.mapp.is_free(next_x, next_y):
            self.character.set_position((next_x, next_y))
        if self.mapp.is_free(next_x, next_y) == 3:
            self.mapp.map[next_x][next_y] = '0'
            self.character.set_position((next_x, next_y))
            x = random.randrange(1, 101)
            if x <= 50:
                item = random.choice(ITEMS)
                del ITEMS[ITEMS.index(item)]
                charik.add_item(item)
                item.render(screen)
            else:
                batl = Battle(charik, random.choice(MOBSS))
                batl.render(screen)
        if self.mapp.map[next_x][next_y] == 4:
            charik.set_position((1, 1))
            with open("data/saves/user.txt", "r") as f:
                old_data = f.read()

            self.new_data = old_data.replace(old_data.split("\n")[2], "map1")
            with open("data/saves/user.txt", "w") as f:
                f.write(self.new_data)
            mapor.nexy_map("map1")

        if self.mapp.map[next_x][next_y] == 5:
            charik.set_position((1, 1))
            with open("data/saves/user.txt", "r") as f:
                old_data = f.read()

            self.new_data = old_data.replace(old_data.split("\n")[2], "map2")
            with open("data/saves/user.txt", "w") as f:
                f.write(self.new_data)
            mapor.nexy_map("map2")
        if self.mapp.map[next_x][next_y] == 6:
            charik.set_position((1, 1))
            with open("data/saves/user.txt", "r") as f:
                old_data = f.read()

            self.new_data = old_data.replace(old_data.split("\n")[2], "map3")
            with open("data/saves/user.txt", "w") as f:
                f.write(self.new_data)
            mapor.nexy_map("map3")
        if self.mapp.map[next_x][next_y] == 7:
            running = True
            clock = pygame.time.Clock()
            image = pygame.image.load("data/sprites/fon_meny.jpg")
            screen.blit(image, (35, 0))
            image = pygame.image.load("data/sprites/character_v.png")
            screen.blit(image, (350, 470))
            f1 = pygame.font.Font(None, 70)
            hp_bur = f1.render("Вы выбролись из подземелия,", 1, (0, 0, 0))
            screen.blit(hp_bur, (600, 670))
            f1 = pygame.font.Font(None, 70)
            hp_bur = f1.render("по крайней мере вы так думаете....", 1, (0, 0, 0))
            screen.blit(hp_bur, (600, 740))
            file_path = "data/saves/user.txt"
            pygame.display.flip()
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            with open("data/saves/user.txt", "w") as f:
                                f.write("1" + '\n')
                                f.write("1" + '\n')
                                f.write("map0" + '\n')
                                f.write("None" + '\n')
                                f.write("None" + '\n')
                                running = False
            pygame.quit()
        if self.mapp.map[next_x][next_y] == 8:
            bos = Battle(charik, demon)
            self.mapp.map[next_x][next_y] = '0'
            bos.render(screen)


class Item:
    def __init__(self, pos, hp, damage, armore, image, name, text, images_v):
        self.image = pygame.image.load(image)
        self.image_v = pygame.image.load(images_v)
        self.name = name
        self.text = text
        self.pos = pos
        self.hp = hp
        self.damage = damage
        self.armore = armore

    def get_state(self):
        return [self.pos, self.hp, self.damage, self.armore]

    def render(self, screen):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
            screen.fill((0, 0, 0))
            screen.blit(self.image_v, (620, 50))
            f1 = pygame.font.Font(None, 70)
            name = f1.render(str(self.name), 1, (255, 255, 255))
            screen.blit(name, (630, 320))
            f1 = pygame.font.Font(None, 35)
            text = f1.render(str(self.text), 1, (255, 255, 255))
            screen.blit(text, (550, 550))
            image = pygame.image.load("data/sprites/heart.png")
            screen.blit(image, (420, 430))
            image = pygame.image.load("data/sprites/armor.png")
            screen.blit(image, (670, 430))
            image = pygame.image.load("data/sprites/damage.png")
            screen.blit(image, (920, 430))
            f1 = pygame.font.Font(None, 45)
            hp_bur = f1.render(str(self.hp), 1, (255, 255, 255))
            screen.blit(hp_bur, (570, 450))
            armor_bur = f1.render(str(self.armore), 1, (255, 255, 255))
            screen.blit(armor_bur, (790, 450))
            damage_bur = f1.render(str(self.damage), 1, (255, 255, 255))
            screen.blit(damage_bur, (1020, 450))
            pygame.display.flip()
            clock.tick(FPS)


class Mobs:
    def __init__(self, hp, damage, armore, image, name):
        self.image = pygame.image.load(image)
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armore = armore

    def get_state(self):
        return [self.hp, self.damage, self.armore]


class Battle:
    def __init__(self, carik, mob):
        self.carik = carik
        self.mob = mob

    def render(self, screen):
        running = True
        moves = 1
        screen.fill((0, 0, 0))
        while running:
            screen.blit(pygame.image.load("data/sprites/character_v.png"), (70, 30))
            screen.blit(self.mob.image, (1000, 30))
            image = pygame.image.load("data/sprites/heart.png")
            screen.blit(image, (120, 430))
            image = pygame.image.load("data/sprites/armor.png")
            screen.blit(image, (120, 530))
            image = pygame.image.load("data/sprites/damage.png")
            screen.blit(image, (120, 630))
            image = pygame.image.load("data/sprites/heart.png")
            screen.blit(image, (1120, 430))
            image = pygame.image.load("data/sprites/armor.png")
            screen.blit(image, (1120, 530))
            image = pygame.image.load("data/sprites/damage.png")
            screen.blit(image, (1120, 630))
            f1 = pygame.font.Font(None, 45)
            hp_bur = f1.render(str(charik.hp), 1, (255, 255, 255))
            screen.blit(hp_bur, (220, 450))
            armor_bur = f1.render(str(charik.armor), 1, (255, 255, 255))
            screen.blit(armor_bur, (220, 550))
            damage_bur = f1.render(str(charik.damage), 1, (255, 255, 255))
            screen.blit(damage_bur, (220, 650))
            hp_bur1 = f1.render(str(self.mob.hp), 1, (255, 255, 255))
            screen.blit(hp_bur1, (920, 450))
            armor_bur1 = f1.render(str(self.mob.armore), 1, (255, 255, 255))
            screen.blit(armor_bur1, (920, 550))
            damage_bur1 = f1.render(str(self.mob.damage), 1, (255, 255, 255))
            screen.blit(damage_bur1, (920, 650))
            for event in pygame.event.get():
                if self.carik.hp <= 0:
                    while running:
                        image = pygame.image.load("data/sprites/died.jpg")
                        screen.blit(image, (45, 0))
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    running = False
                        pygame.display.flip()
                    with open("data/saves/user.txt", "w") as f:
                        f.write("1" + '\n')
                        f.write("1" + '\n')
                        f.write("map0" + '\n')
                        f.write("None" + '\n')
                        f.write("None" + '\n')
                    pygame.quit()
                if self.mob.hp <= 0:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if moves == 1:
                            screen.fill((0, 0, 0))
                            self.mob.hp -= round(self.carik.damage - ((self.carik.damage / 1000) * self.mob.armore))
                            f1 = pygame.font.Font(None, 45)
                            news = f1.render("Вы наносите " + str(self.mob.name) + ' ' + str(
                                round(self.carik.damage - ((self.carik.damage / 1000) * self.mob.armore))), 1,
                                             (255, 255, 255))
                            screen.blit(news, (300, 300))
                            moves = 2
                        else:
                            screen.fill((0, 0, 0))
                            self.carik.hp -= round(self.mob.damage - ((self.mob.damage / 1000) * self.carik.armor))
                            f1 = pygame.font.Font(None, 45)
                            news = f1.render(str(self.mob.name) + ' ' + 'наносит вам ' + str(
                                round(self.mob.damage - ((self.mob.damage / 1000) * self.carik.armor))), 1,
                                             (255, 255, 255))
                            screen.blit(news, (300, 300))
                            moves = 1
            pygame.display.flip()
            clock.tick(FPS)


sword = Item("right_hand", 0, 30, 0, "data/sprites/sword.png", "Меч", '"ИЗВИНИСЬ ПЕРЕД РЫЦЫРЕМ!"',
             "data/sprites/sword_v.png")
shield = Item("left_hand", 0, 10, 20, "data/sprites/shield.png", "Щит", '"Оуууу шит!"', "data/sprites/shield_v.png")
foil_hat = Item("head", 00, 0, 20, "data/sprites/foil_hat.png", "Шапочка из фольги", '"100% защита от инопланетян"',
                "data/sprites/foil_hat_v.png")
bulletproof_diaper = Item("legs", 10, 0, 40, "data/sprites/bulletproof_diaper.png", "Пуленепробиваемый подгузник",
                          '"гарантия безопасности"', "data/sprites/bulletproof_diaper_v.png")
electric_broom = Item("right_hand", 0, 50, 0, "data/sprites/electric_broom.png", "Электро-веник",
                      '"Говорят им пользовался сам Зевс"', "data/sprites/electric_broom_v.png")
chain_mail = Item("bady", 20, 0, 50, "data/sprites/chain_mail.png", "Кольчуга",
                  '"да, это кольчуга, а не кусок битых пикселей"', "data/sprites/chain_mail_v.png")
festive_cap = Item("head", 25, 0, 5, "data/sprites/festive_cap.png", "Празднечный колпак", '"С праздником!"',
                   "data/sprites/festive_cap_v.png")
klacic_fingershooter = Item("left_hand", 0, 45, 0, "data/sprites/klacic_fingershooter.png", "Класический пальцестрел",
                            '"Пау, Пау!"', "data/sprites/klacic_fingershooter_v.png")
t_shirt_guchi = Item("bady", 5, 0, 5, "data/sprites/T-shirt_guchi.png", "Майка Гучи",
                     '"какая то бедность дотронулась до меня"', "data/sprites/T-shirt_guchi_v.png")
rkn = Item("head", 0, 0, 0, "data/sprites/rkn.png", "РКН",
           '"Запрещаю вам использовать голову"', "data/sprites/rkn_v.png")
cup = Item("right_hand", 0, 99, 0, "data/sprites/cup.png", "Пласмасовый стаканчик",
           '"Смертоносное оружие"', "data/sprites/cup_v.png")
banana = Item("left_hand", 0, 100, 0, "data/sprites/banana.png", "Идеальный бананс",
              '"Эталон гармонии"', "data/sprites/banana_v.png")
thorn_crown = Item("head", -10, 00, 70, "data/sprites/thorn_crown.png", "Терновая корона",
                   '"И хочеться и колиться"', "data/sprites/thorn_crown_v.png")
gold = Item("bady", 10, 00, 150, "data/sprites/gold.png", "20ти килограмовый крест",
            '"Из чистого золота!"', "data/sprites/gold_v.png")
an_cenon = Item("right_hand", 0, 250, 0, "data/sprites/an_cenon.png", "АНИГИЛЯТОРНАЯ ПУШКАА",
            '"Я шипну тебе на ушко.."', "data/sprites/an_cenon_v.png")

ITEMS = [sword, shield, foil_hat, bulletproof_diaper, electric_broom, chain_mail, festive_cap, klacic_fingershooter,
         t_shirt_guchi, rkn, cup, banana, thorn_crown, gold, an_cenon]
ITEMS_SWOP_TO = {sword: "sword", shield: "shield", foil_hat: "foil_hat", bulletproof_diaper: "bulletproof_diaper",
                 electric_broom: "electric_broom", chain_mail: "chain_mail", festive_cap: "festive_cap",
                 klacic_fingershooter: "klacic_fingershooter", t_shirt_guchi: "t_shirt_guchi", rkn: "rkn", cup: "cup",
                 banana: "banana", thorn_crown: "thorn_crown", gold: "gold", an_cenon: "an_cenon"}
ITEMS_SWOP_OUT = {"sword": sword, "shield": shield, "foil_hat": foil_hat, "bulletproof_diaper": bulletproof_diaper,
                  "electric_broom": electric_broom, "chain_mail": chain_mail, "festive_cap": festive_cap,
                  "klacic_fingershooter": klacic_fingershooter, "t_shirt_guchi": t_shirt_guchi, "rkn": rkn, "cup": cup,
                  "banana": banana, "thorn_crown": thorn_crown, "gold": gold, "an_cenon": an_cenon}
bear = Mobs(200, 40, 10, "data/sprites/bear.png", "Медведь")
demon = Mobs(666, 66, 6, "data/sprites/demon_v.png", "Чорт")
goblin = Mobs(50, 20, 5, "data/sprites/goblin.png", "Гоблин")
turt = Mobs(70, 25, 100, "data/sprites/turt.png", "Черепаха")
bug = Mobs(77, 77, 77, "data/sprites/bug.png", "Баг")
MOBSS = [bear, goblin, turt, bug]

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = (1500, 800)
    screen = pygame.display.set_mode(size)
    m = Meny()
    with open("data/saves/user.txt", "r", encoding="UTF-8") as f:
        x = int(list(f)[0].rstrip("\n"))
    with open("data/saves/user.txt", "r", encoding="UTF-8") as f:
        y = int(list(f)[1].rstrip("\n"))
        charik = Character(x, y)
    with open("data/saves/user.txt", "r", encoding="UTF-8") as f:
        mapor = Map_editor(list(f)[2].rstrip("\n"), [0, 3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8])
    game = Game(mapor, charik)
    image = pygame.image.load("data/sprites/item.png")
    screen.blit(image, (80, 80))

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("data/saves/user.txt", "r+") as f:
                    f.write(str(charik.get_position()[0]) + '\n')
                    f.write(str(charik.get_position()[1]) + '\n')
                    f.write(game.new_data.split()[2].rstrip('\n') + '\n')
                    if charik.invtntory:
                        for i in range(len(charik.invtntory)):
                            if i == len(charik.invtntory) - 1:
                                f.write(ITEMS_SWOP_TO[charik.invtntory[i]] + '\n')
                            else:
                                f.write(ITEMS_SWOP_TO[charik.invtntory[i]] + ' ')
                    else:
                        f.write("None" + '\n')
                    if charik.eqwipment:
                        for i in range(len(charik.eqwipment)):
                            if i == len(charik.eqwipment) - 1:
                                f.write(ITEMS_SWOP_TO[charik.eqwipment[i]] + '\n')
                            else:
                                f.write(ITEMS_SWOP_TO[charik.eqwipment[i]] + ' ')
                    else:
                        f.write("None" + '\n')
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if len(charik.invtntory) >= 1:
                        charik.eqwip_item(charik.invtntory[0])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    if len(charik.invtntory) >= 2:
                        charik.eqwip_item(charik.invtntory[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    if len(charik.invtntory) >= 3:
                        charik.eqwip_item(charik.invtntory[2])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    if len(charik.invtntory) >= 4:
                        charik.eqwip_item(charik.invtntory[3])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:
                    if len(charik.invtntory) >= 5:
                        charik.eqwip_item(charik.invtntory[4])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_6:
                    if len(charik.invtntory) >= 6:
                        charik.eqwip_item(charik.invtntory[5])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_7:
                    if len(charik.invtntory) >= 7:
                        charik.eqwip_item(charik.invtntory[6])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    if not charik.head:
                        for i in range(len(charik.eqwipment)):
                            if charik.eqwipment[i].pos == "head":
                                charik.remove_item(i)
                                charik.head = True
                                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if not charik.right_hand:
                        for i in range(len(charik.eqwipment)):
                            if charik.eqwipment[i].pos == "right_hand":
                                charik.remove_item(i)
                                charik.right_hand = True
                                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    if not charik.left_hand:
                        for i in range(len(charik.eqwipment)):
                            if charik.eqwipment[i].pos == "left_hand":
                                charik.remove_item(i)
                                charik.left_hand = True
                                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    if not charik.legs:
                        for i in range(len(charik.eqwipment)):
                            if charik.eqwipment[i].pos == "legs":
                                charik.remove_item(i)
                                charik.legs = True
                                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if not charik.bady:
                        for i in range(len(charik.eqwipment)):
                            if charik.eqwipment[i].pos == "bady":
                                charik.remove_item(i)
                                charik.bady = True
                                break

        game.update_character()
        screen.fill((0, 0, 0))
        game.rendr()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
