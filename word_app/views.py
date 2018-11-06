from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from word_app.data import *
import word_app.game as game
from .models import WordGame
import datetime

# Create your views here.

draw = None
word= None
word_score= None
max_word= None
max_word_score= None
max_word_value= None
game_score= None


def gameView(request):
	return render(request, 'game.html')

def play(request):	
	global draw
	draw = game.draw_letters()	
	return render(request, 'play.html', { 'letters': draw, 'word': word, 'word_score': word_score, 'max_word': max_word, 'max_word_score': max_word_score, 'game_score': game_score})	

def calculate(request):
	#get the word from the form input	
	global word
	global word_score
	global max_word
	global max_word_score
	global max_word_value
	global game_score
	word = request.POST['inword']	
	word_score = game.calc_word_value(word)

	possible_words = game.get_possible_dict_words(draw)

	max_word = game.max_word_value(possible_words)
	max_word_score = game.calc_word_value(max_word)
	print('Optimal word possible: {} (value: {})'.format(
                 max_word, max_word_score))

	game_score = word_score / max_word_score * 100
	print('You scored: {:.1f}'.format(game_score))

	#store records to db
	now = datetime.datetime.now()
	datval = str("{}-{}-{} {}:{}:{} {}".format(now.year, now.month, now.day, now.hour, now.minute, now.second, now.strftime("%A")))
	new_score = WordGame(word=word, score=game_score, dateval=datval)
	new_score.save()

	return HttpResponseRedirect("/play/")

def topscores(request):
	all_scores = WordGame.objects.all()
	return render(request, "allscores.html", {'all_scores': all_scores})

# class GameView(View):
# 	def __init__(self, request):
# 		self.draw_letters = None
# 		self.word = None
# 		self.word_score = None
# 		self.possible_words = None
# 		self.max_word = None
# 		self.max_word_score = None
# 		self.game_score = None
	
# 	def game(self, request):
# 		return render(request, 'game.html')

# 	def play(self, request):
# 		self.draw_letters = game.draw_letters()
# 		return render(request, 'play.html', { 'letters': draw_letters, 'word':word, 'word_score': word_score, 'max_word': max_word, 'max_word_score': max_word_score, 'game_score': game_score})

# 	def calculate(self, request):
# 		#get the word from the form input
# 		self.word = request.POST['word']	
# 		self.word_score = calc_word_value(word)

# 		self.possible_words = get_possible_dict_words(draw)

# 		self.max_word = max_word_value(possible_words)
# 		self.max_word_score = calc_word_value(max_word)
# 	#             print('Optimal word possible: {} (value: {})'.format(
# 	#                 max_word, max_word_score))

# 		self.game_score = word_score / max_word_score * 100
# 	#             print('You scored: {:.1f}'.format(game_score))
# 		return HttpResponseRedirect("/play/")
