from django.shortcuts import render
from django.views import generic
from game.models import Game_5566


# Create your views here.

def get_5566(request):
    pattern = request.GET.get('pattern')
    if pattern != None and pattern != '':
        game_list = Game_5566.objects.filter(game_title__contains=pattern)
        if game_list.count() != 0:
            return render(request, 'game/game.html', context={"game_list": game_list})
        else:
            not_exist_message = '你查找的不存在'
            return render(request, 'game/game.html', context={'not_exist_message': not_exist_message})
    return render(request, 'game/game.html')
