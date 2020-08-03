from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import UserMoves, Contact

from django.contrib import messages


# Create your views here.
def home_view(request, *args, **kwargs):
    #prints current user login cool!
    print(request.user)
    
    return render(request, 'index.html'   ,{}) #pass data

def about_view(request, *args,**kwargs):

    return render(request, 'about.html', {})


def contact_view(request, *args,**kwargs):
    return render(request, 'contact.html', {})

def puzzle_view(request, *args,**kwargs):
    return render(request, 'puzzle.html', {})

def puzzledoris_view(request, *args,**kwargs):
    return render(request, 'puzzledoris.html', {})

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
from random import randint
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def contact_index(request):
    	
	if request.method == 'POST':
		if request.user.is_authenticated:
		
			print(request.body)
			name = request.POST.get('name')
			email = request.POST.get('email')
			message = request.POST.get('message')

			messages.success(request, f'Thank you for getting in touch, we\'ll get back you shortly')
			

			c = Contact(name=name, email=email, message=message,user=request.user)
			c.save()


			print(name, email, message)
		else:
			print(request.body)
			name = request.POST.get('name')
			email = request.POST.get('email')
			message = request.POST.get('message')

			messages.success(request, f'Thank you for getting in touch, we\'ll get back you shortly')


			c = Contact(name=name, email=email,message=message)
			c.save()


			print(name, email, message)
    			
    			


	return render(request, 'index.html'   ,{}) #pass data


xpos = -1
ypos = -1

saved_moves = {}

def score(b,comp,p,turn): #checks if a player has won or not
	flag = 0
	for i in range(3):
		count = 0
		for j in range(3):
			if(b[i][j] == turn):
				count = count+1
		if(count == 3):
			flag = 1

	for i in range(3):
		count = 0
		for j in range(3):
			if(b[j][i] == turn):
				count = count+1
		if(count == 3):
			flag = 1

	if(b[0][0] == turn and b[1][1] == turn and b[2][2] == turn):
		flag = 1
	if(b[0][2] == turn and b[1][1] == turn and b[2][0] == turn):
		flag = 1
	if(flag == 1):
		if(turn == comp):
			return 10
		else:
			return -10
	return 0
def checkdraw(b): #checks for draw
	for i in range(3):
		for j in range(3):
			if(b[i][j] == 0):
				return 0
	return 1

def tictac(b,comp,p,turn,g): #min-max algorithm for tic-tac toe
	curr = comp
	global xpos
	global ypos
	mx = -1000
	mn = 1000
	if(turn == comp):
		curr = p
	check = score(b,comp,p,curr)
	if(check == 10):
		return 10 - g
	elif(check == -10):
		return -10 + g
	elif(checkdraw(b)):
		return 0

	if(turn == comp):
		for i in range(3):
			for j in range(3):
				if(b[i][j] == 0):
					b[i][j] = comp
					x = tictac(b,comp,p,p,g+1)
					#print x
					if(x > mx):
						mx = x
						if(g == 0):
							xpos = i
							ypos = j
							#print g,xpos,ypos
					b[i][j] = 0
		return mx
	elif(turn == p):
		for i in range(3):
			for j in range(3):
				if(b[i][j] == 0):
					b[i][j] = p
					y = tictac(b,comp,p,comp,g+1)
					if(y < mn):
						mn = y
						if(g == 0):
							xpos = i
							ypos = j
					b[i][j] = 0
		
		return mn
@csrf_exempt
def index(request): #when the user submits his choice

	data = {}

	with open('test.json') as f:
		data = json.load(f)

		

		# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
		# print(data)

	size = len(data.get('moves'))
	print(size)

	# x  = data.get('moves')[size]
	# print(x)

	if request.method == 'POST':
			



		

		board = request.POST.getlist('board[]')

		

		
		a = [[0 for x in range(3)] for x in range(3)]
	
		for i in range(3):
			for j in range(3):
				a[i][j] = int(board[3*i+j])
		# print(a)

		print(data.get('moves')[size-1])
		# if(data.get('moves')[size-1]['127.0.0.1:8000'][1]=='{'):
			
		# 	print('hello')
		# else:
		# 	print('hhhhh')
		# 	print(data.get('moves')[size-1]['127.0.0.1:8000'])
		# 	print(type(a))
		# 	print(type(x))
			
		
			


		s = score(a,1,2,2)
		x = request.get_host()
		

		moves = {x:str(a)}



      
		write_json(data)  


		if(s == -10):
	



			return JsonResponse({'val':0,'res':1,'winner':'player'})
		elif(checkdraw(a) == 1):

		    			

			return JsonResponse({'val':0,'res':1,'winner':'draw'})

		tictac(a,1,2,1,0)
		a[xpos][ypos] = 1
		s = score(a,1,2,1)
		if(s == 10):
				
		
		
			return JsonResponse({'val':xpos*3+ypos,'res':1,'winner':'comp'})
			
		elif(checkdraw(a) == 1):
		
		
			return JsonResponse({'val':xpos*3+ypos,'res':1,'winner':'draw'})


		return JsonResponse({'val':xpos*3+ypos,'res':0,'winner':'none'})
	else:
		return JsonResponse({'val':"error"})

@csrf_exempt
def tictactoe_view(request): #displaying the home page
	context = {}
	return render(request,"tictactoe.html",context)



		

# function to add to JSON 
def write_json(data, filename='test.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
@csrf_exempt     
def store_game(request):
    	
	x = request.POST.get('last_move')
	y = request.POST.get('go')
	# print(x)
	# print(y)	

	# print(request.POST.getlist('board[]'))
    	
	if request.user.is_authenticated:
    		

		with open('test.json') as json_file: 
			data = json.load(json_file) 

			temp = data['moves'] 

	
    		
		board = request.POST.getlist('board[]')

		user =  str(request.user.id)

		temp.append(board) 
	
		write_json(data) 	
		

		data = {1:board}
		

		data = json.dumps(data)


		m = UserMoves(moves=data,last_move=x,user=request.user)
		m.save()

		return JsonResponse({'status':'200'})
	return JsonResponse({'status':'403'})

@csrf_exempt     

def load_game(request):
    
	if request.user.is_authenticated:
    		
		data = dict()
		print('hello00000000')

		
		y = UserMoves.objects.filter(user=request.user)
		z = y.last()
	
		data = z.moves
		last_move = z.last_move

		# print(last_move)


    
		data = res = json.loads(data) 

		

		# print(data)



	return JsonResponse(data)



