import requests
import sys
import pygame


adress = 'http://127.0.0.1:5000/'


def create_note(name, data):
	r = requests.post(adress + '/create_note'+'?'+'name='+name+'&'+'text='+data)

def print_note(name):
	r = requests.get(adress + '/' + name+'/get')
	print(r.text.split(5 * '<///>')[0], r.text.split(5 * '<///>')[1], sep='\n')
	
def get_list():
	r = requests.get(adress + '/get_list')
	return r.text.split('<///>')

def edit_note(name):
	print('Введите новое имя заметки:')
	new_name = input()
	print('Введите новый текст заметки:')
	new_text = input()
	r = requests.post(adress+'/edit_note/'+name+'?'+'new_name='+new_name+'&'+'new_text='+new_text)

def delete_note(name):
	r = requests.post(adress+'/edit_note/'+name+'?'+'deleted=yes')

# Инициализация pygame
pygame.init()
# Размер окна
screen = pygame.display.set_mode((1280, 720))
# Заголовок окна
pygame.display.set_caption('Blue Circle')

while True:
    # Задаем цвет фона
    screen.fill((255, 255, 224))
    pygame.draw.circle(screen, (50, 50, 200), (150, 150), 75)
    # Обновляем экран
    pygame.display.flip()
    pygame.font.init()
    font = pygame.font.SysFont(name='font', size=20)
    surf = font.render(text='Click on the circle', antialias=True, color=(0, 0, 0))
    screen.blit(surf, (70, 260))
    pygame.display.flip()	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

