# імпортуємо модуль pygame
import pygame
# імпортуємо модуль os 
import os

from image import Image
#Налаштували pygame для роботи із системою 
pygame.init()

list_map = [
    '1000000000000000000001',
    '1000000000000000000001',
    '1111000000000001000010',
    '0000001001111100111000',
    '0000111110100000000100',
    '0001000001000000000001',
    '0100000000111110001111',
    '0010000001000000010000',
    '0000000000000000010000',
    '0000000000000000000000',
    '0000000000000000000000',
]
x = 0
y = 0
for row in list_map:
    for cell in row:
        if cell == '1':
            self.image_blocks.image_path = 'images/blocks/1.png'



# створюємо клас для зображень
class Image:
    def __init__(self, image_path, width, height, x, y):
        #створюєио змінну image_path, яка відповідає за відносний шлях до картинки у папці проекту
        self.image_path = image_path
        #створюємо змінні ширина і висота
        self.width = width
        self.height = height
        #створюємо змінні координат
        self.x = x
        self.y = y
        #викликаємо метод load_image, який відповідає за завантаження зображення
        self.load_image()
        
    # створюємо функцію для показу зображеннь
    def show_image(self, window):
        # показати картинку
        window.blit(self.scaled_image, (self.x, self.y))
    #створ. функцію для завантаження зображення
    def load_image(self, direction = False):
        # знайти шлях до папку проекту
        self.project_folder_path = os.path.abspath(__file__ + '/..')
        # знайти абсолютний шлях до зображення
        self.absolute_image_path = os.path.join(self.project_folder_path, self.image_path)
        # загрузити картинку за шляхом
        self.loaded_image = pygame.image.load(self.absolute_image_path)
        # 
        self.flipped_image = pygame.transform.flip(self.loaded_image, direction, False)
        # задаємо розміри зображенню
        self.scaled_image = pygame.transform.scale(self.flipped_image, (self.width, self.height))


#створ. клас, щоб працювати із спрайтом гравця 
class Player:
    #конструктор класу, куди передаємо необхідні аргументи
    def __init__(self, image_path, width, heigth, x, y, speed, speed_gravitation):
        #створ. об'єкт картинки гравця
        self.image_player = Image(image_path, width, heigth, x, y)
        #швидкість руху
        self.speed = speed
        #змінна, в якій зберіг. індекс кожного спрайта(в даній ситуац. присвоюємо змінній індекс першого спрайта)
        self.number_of_costume = 1
        #лічильник для контролю швидкості спрайта; задаємо лічильнику початкове значення 
        self.count_animation = 1
        # Відзеркалення зображення вимкнуто
        self.flip_direction = False
        # Швидкість гравітація
        self.speed_gravitation = speed_gravitation

        self.is_jump = False
        self.speed_jump = 10
        self.count_jump = 0

    #метод(функція) для руху спрайта 
    def sprite_move(self):
                      
        #можливість працювати із кнопками на клавіатурі
        keys = pygame.key.get_pressed()
        #якщо натиснута клавіша вправо
        if keys[pygame.K_RIGHT]:
            #задаємо швидкість координаті х в додатньому напрямку (тобто змушуємо спрайт рухатись вправо)
            self.image_player.x += self.speed
            # Відзеркалення зображення вимкнуто
            self.flip_direction = False
            #викликаємо метод animation
            self.animation()
        #якщо натиснута клавіша вліво
        elif keys[pygame.K_LEFT]:
            #задаємо швидкість координаті х у від'ємному напрямку (тобто змушуємо спрайт рухатись вліво)
            self.image_player.x -= self.speed
            # Відзеркалення зображення увімкнене
            self.flip_direction = True
            # Анімація
            self.animation()
        # Інакше
        else:
            # Шлях до зображення
            self.image_player.image_path = 'images/player/stay.png'
            # Завантажуємо зображення
            self.image_player.load_image(direction=self.flip_direction)
    #функція(метод) для анімації спрайта
    def animation(self):
        #об'єднуємо шлях до кожного спрайта із його індексом(створ. повний шлях до кожного спрайта)
        self.image_player.image_path = f'images/player/{self.number_of_costume}.png'
        #викликаємо функцію load_image відносно спрайта
        self.image_player.load_image(direction=self.flip_direction)
        #збільшуємо значення лічильника на одиницю
        self.count_animation += 1
        #якщо знач. лічильника дорів. 5 
        if self.count_animation == 5:
            #змінюємо індекс спрайта на наступний 
            self.number_of_costume += 1
            #якщо індекс спрайта більше або дорів. 7 
            if self.number_of_costume >= 7:
                #задаємо індекс першого спрайта
                self.number_of_costume = 1
            #задаємо початкове значення лічильника 
            self.count_animation = 1
    # Функція гравітація
    def gravitation(self):
        # Якщо ігрик зображення гравця + висота зображення гравця меньше висоти вікна то
        if self.image_player.y + self.image_player.height <= window_settings['height']:
            self.image_player.image_path = 'images/player/down.png'
            self.image_player.load_image(direction=self.flip_direction)
            # ігрик зображення гравця + Швидкість гравітація
            self.image_player.y += self.speed_gravitation
        else:
            self.is_jump = False
            self.count_jump = 25
    
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.is_jump = True

        if self.is_jump:
            if self.count_jump > 0:
                self.image_player.y -= self.speed_jump
                self.count_jump -= 1
                self.image_player.image_path = 'images/player/up.png'
                self.image_player.load_image(direction=self.flip_direction)
class Blocks:
    def __init__(self, image_path, width, heigth, x, y):
        self.image_blocks = Image(image_path, width, heigth, x, y)
        self.flip_direction = False





        

# Віконі налаштування
window_settings = {
    'width': 1320,#Ширина
    'height': 720,#Висота
    'caption':'Платформер'#Газва вікна
}
#створ. об'єкт для можливості відслідковувати час, працювати із ним
clock = pygame.time.Clock()
#створ. об'єкт спрайта(гравця), вказуємо його розміри, координати, швидкість, швидкість, з якою гравець буде падати 
object_player = Player('images/player/stay.png', 90, 105, 500, 0, 5,5)
# створюємо задній фон
background = Image('images/bg.png',1200, 780, 0, 00)
#створ. об'єкт спрайта(монети), вказуємо його розміри та коодинати
money = Image('images/coin.png', 60, 60, 1140, 0)
# вказуємо розміри екрану
window = pygame.display.set_mode((window_settings['width'], window_settings['height']))
#створюємо заголовок 
pygame.display.set_caption(window_settings['caption'])
# Змінна, що відповідає за роботу гри
game = True
# поки гра запущена
while game == True:
    # заливка вікна 
    # window.fill((0, 233, 255))
    #відображаємо задній фон та монету
    background.show_image(window)
    money.show_image(window)
    #через змінну об'єкта спрайта звертаємося до самої картинки спрайта і відображаємо її
    object_player.image_player.show_image(window)
    #викликаємо функцію sprite_move, щоб спрайт міг рухатись
    object_player.sprite_move()
    object_player.gravitation()
    object_player.jump()
    # перебираємо події
    for event in pygame.event.get():
        # якщо подія це вийти з гри то
        if event.type == pygame.QUIT:
            # вимнкути гру
            game = False
    # постійне оновлення екрану
    pygame.display.flip()
    #задаємо кількість кадрів за 1 секунду 
    clock.tick(60)
    
