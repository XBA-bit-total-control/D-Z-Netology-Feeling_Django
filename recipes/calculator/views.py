from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'soup': {
        'вода': 2,
        'морковь': 1,
        'лук': 0.5,
        'мясо': 1.25,
        'картофан': 4,
        'масло': 0.15
    },
    'pilaf': {
        'ykropka': 1,
        'cat buns': 1,
        'potato': 25,
        'mandArinas': 17,
        'bucket of water': 1,
        'horseradish to taste': 1
    },
}


def cook(request):
    return HttpResponse("Укажи в адресной строке название рецепта")


def show_recipe_omlet(request):
    quantity = int(request.GET.get('servings', 1))

    context = DATA.get('omlet', "Что вы хотите приготовить?")

    if isinstance(context, dict):
        сomposition = {name: round(num * quantity, 3) for name, num in context.items()}
        context = {'recipe': сomposition}

        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse(context)


def show_recipe_pasta(request):
    quantity = int(request.GET.get('servings', 1))

    context = DATA.get('pasta', "Что вы хотите приготовить?")

    if isinstance(context, dict):
        сomposition = {name: round(num * quantity, 3) for name, num in context.items()}
        context = {'recipe': сomposition}

        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse(context)


def show_recipe_buter(request):
    quantity = int(request.GET.get('servings', 1))

    context = DATA.get('buter', "Что вы хотите приготовить?")

    if isinstance(context, dict):
        сomposition = {name: round(num * quantity, 3) for name, num in context.items()}
        context = {'recipe': сomposition}

        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse(context)


def show_recipe_soup(request):
    quantity = int(request.GET.get('servings', 1))

    context = DATA.get('soup', "Что вы хотите приготовить?")

    if isinstance(context, dict):
        сomposition = {name: round(num * quantity, 3) for name, num in context.items()}
        context = {'recipe': сomposition}

        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse(context)


def show_recipe_pilaf(request):
    quantity = int(request.GET.get('servings', 1))

    context = DATA.get('pilaf', "Что вы хотите приготовить?")

    if isinstance(context, dict):
        сomposition = {name: round(num * quantity, 3) for name, num in context.items()}
        context = {'recipe': сomposition}

        return render(request, 'calculator/index.html', context)
    else:
        return HttpResponse(context)