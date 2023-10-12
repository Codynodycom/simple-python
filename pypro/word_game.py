import turtle
import random

w = turtle.Turtle()
w.speed(10000000)
# ,'колонка','коньки','лошадь'
words = ['микрофон','диск', 'коньки', 'мяч']
w.hideturtle()
secret_word = random.choice(words)
word_list = [let for let in secret_word]

a = 0
w.penup()
w.goto(-240,100)
w.write("Слово:", font=('Arial',20,'normal'))
w.goto(-240,80)
w.pendown()
dlina_bykv= len(secret_word.strip())

def draw_square():
	for u in range(4):
		w.forward(50)
		w.right(90)

for j in range(len(secret_word)):
	draw_square()
	for i in range(1):
		w.penup()
		w.forward(55)
		w.pendown()

# если длина слова < 8, то добавляем пробелы
while len(secret_word) < 8:
	secret_word = secret_word + ' '

max_i = len(secret_word)
e = True
# print('загадано:', secret_word, len(secret_word))
while e:
	ww = input('введи букву: ')
	if ww == secret_word[0] and word_list[0] != '#':
		w.penup()
		w.goto(-225,50)
		w.pendown()
		w.write(secret_word[0], font=('Arial',20,'normal'))
		a += 1
		word_list[0] = '#'
	
	elif ww == secret_word[1] and  word_list[1] != '#':
		w.penup()
		w.goto(-170,50)
		w.pendown()
		w.write(secret_word[1], font=('Arial',20,'normal'))
		a += 1
		word_list[1] = '#'

	elif ww == secret_word[2] and  word_list[2] != '#':
		w.penup()
		w.goto(-110,50)
		w.pendown()
		w.write(secret_word[2], font=('Arial',20,'normal'))
		a += 1
		word_list[2] = '#'

	elif ww == secret_word[3] and  word_list[3] != '#':
		w.penup()
		w.goto(-50,50)
		w.pendown()
		w.write(secret_word[3], font=('Arial',20,'normal'))
		a += 1
		word_list[3] = '#'
	elif ww == secret_word[4] and  word_list[4] != '#':
		w.penup()
		w.goto(0,50)
		w.pendown()
		w.write(secret_word[4], font=('Arial',20,'normal'))
		a += 1
		word_list[4] = '#'
	elif ww == secret_word[5] and  word_list[5] != '#':
		w.penup()
		w.goto(50,50)
		w.pendown()
		w.write(secret_word[5], font=('Arial',20,'normal'))
		a += 1
		word_list[5] = '#'
	elif ww == secret_word[6] and  word_list[6] != '#':
		w.penup()
		w.goto(100,50)
		w.pendown()
		w.write(secret_word[6], font=('Arial',20,'normal'))
		a += 1
		word_list[6] = '#'
	elif ww == secret_word[7] and  word_list[7] != '#':
		w.penup()
		w.goto(170,50)
		w.pendown()
		w.write(secret_word[7], font=('Arial',20,'normal'))
		a += 1
		word_list[7] = '#'
	
	if dlina_bykv == a:
		print('Все буквы есть! Вы выиграли!')
		e = False


# word = 'asd    '
# print(len(word.strip()))
