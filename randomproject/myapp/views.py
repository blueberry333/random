from django.shortcuts import render, get_object_or_404, redirect
import random

from .models import Data

# Create your views here.
def name(request):
    return render(request, 'name.html')

def birth(request):
    nickname = Data()
    nickname.name = request.POST['name']
    nickname.save()
    return redirect('birth')

def blood(request, data_id):
    nickname = get_object_or_404(Data, pk=data_id)
    nickname.month = request.POST['month']
    nickname.date = request.POST['date']
    nickname.save()
    return render(request, 'blood.html')

def season(request):
    return render(request, 'season.html')

def color(request):
    return render(request, 'color.html')

def result(request):
    Spring=[flowers, blossoms, shoots]
    Summer=[sea, sunflowers, swim, hot]
    Fall=[Book, maple, maple]
    Winter=[snow, Ulaf, camellia, xmas, snowman, ice]
    
    Jan=[Ganet, Love, Truth, chastity, eternal]
    Feb=[chastity, peace]
    Mar=[Aquamarine, Calm, intelligent, brave, sincere, virtuous]
    Apr=[Diamond, Love, Happiness, Compassion]
    May=[Emerald, Happiness, Luck, Patience, Integrity]
    Jun=[Pearl, Health, Success, Prosperity]
    Jul=[Ruby, Passion, Life]
    Aug=[Peridot, Wisdom, Happiness]
    Sep=[sapphire, benevolence, sincerity, virtue]
    Oct=[Opal, Love, Truth, chastity]
    Nov=[Topaz, Friendship, patience, innocence]
    Dec=[Turqoise, Luck, Success, Prosperity]


    return render(request, 'result.html', {'name':name, 'month':month, 'day':day, 'blood':blood, 'season':season, 'color':color})