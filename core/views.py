from django.shortcuts import render, redirect
from datetime import datetime
import random


def index(request):
    if request.method == 'POST':
        participants_count = int(request.POST.get('participants_count', 3))
        participants = []

        for i in range(participants_count):
            participant = {
                'name': request.POST.get(f'name_{i}', f'Участник {i + 1}'),
                'start': request.POST.get(f'start_{i}', ''),
                'transport': request.POST.get(f'transport_{i}', 'метро'),
            }
            participants.append(participant)

        request.session['participants'] = participants
        return redirect('calculate')

    return render(request, 'core/index.html')


def calculate(request):
    participants = request.session.get('participants', [])

    if not participants:
        return redirect('index')

    meeting_places = [
        {'name': 'ТРЦ "Европейский"', 'address': 'пл. Киевского Вокзала, 2',
         'description': 'Крупный ТЦ, удобная парковка, метро "Киевская"', 'rating': 4.8},
        {'name': 'Кафе "Уют"', 'address': 'ул. Тверская, 15',
         'description': 'Уютное кафе, метро "Тверская"', 'rating': 4.6},
        {'name': 'Парк "Зарядье"', 'address': 'ул. Варварка, 6',
         'description': 'Красивый парк', 'rating': 4.9},
        {'name': 'Антикафе "Время"', 'address': 'ул. Арбат, 20',
         'description': 'Для дружеских встреч', 'rating': 4.7},
    ]

    routes = []
    for p in participants:
        travel_time = random.randint(15, 50)
        routes.append({
            'name': p['name'],
            'start': p['start'],
            'transport': p['transport'],
            'time': travel_time,
            'distance': random.randint(3, 20),
        })

    best_places = random.sample(meeting_places, min(3, len(meeting_places)))
    for place in best_places:
        place['avg_time'] = sum(r['time'] for r in routes) // len(routes)

    context = {
        'best_place': best_places[0] if best_places else None,
        'all_places': best_places,
        'routes': routes,
        'calculated_at': datetime.now().strftime('%d.%m.%Y %H:%M'),
    }

    return render(request, 'core/result.html', context)