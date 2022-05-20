import requests


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

resp = 1
while resp != 3 :
	print('Что вы хотите сделать?', '1.Создать заметку', '2.Вывести список заметок','3.Выйти', sep='\n')
	resp = int(input())
	if resp == 1:
		print('Введите имя заметки:')
		name = input()
		print('Введите текст заметки:')
		data = input()
		create_note(name, data)
		print_note(name)
	if resp == 2:
		resp1 = 1
		while resp1 != -1:
			print('Введите номер заметки, что перейти к ней или -1, чтобы выйти')
			notes_list = get_list()
			notes_list.pop(-1)
			i = 0
			for note in notes_list:
				i += 1
				print(i, '. ', note, sep='')
			resp1 = int(input())
			if resp1 != -1:
				print()
				print_note(notes_list[resp1 - 1])
				print()
				print('1.Редактировать заметку', '2.Удалить заметку', '3.Вернуться', sep='\n')
				resp2 = int(input())
				if resp2 == 1:
					edit_note(notes_list[resp1 - 1])
				if resp2 == 2:
					delete_note(notes_list[resp1 - 1])
				if resp2 == 3:
					pass
	if resp == 3:
		pass
