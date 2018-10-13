import requests
from django.http import HttpResponse
from django.shortcuts import render

nav = [
    {
        'title': 'About',
        'path': '/about',
    },
    {
        'title': 'Blog',
        'path': '/blog',
    },
    {
        'title': 'Projects',
        'path': '/projects',
    },
    {
        'title': 'My GitHub Repos',
        'path': '/github',
    },
]


def index(request):
    context = {
        'page_title': 'Home',
        'nav': nav,
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'page_title': 'About',
        'nav': nav,
    }
    return render(request, 'about.html', context)


def blog(request):
    context = {
        'page_title': 'Blog',
        'nav': nav,
    }
    return render(request, 'blog.html', context)


def projects(request):
    context = {
        'page_title': 'Projects',
        'nav': nav,
    }
    return render(request, 'projects.html', context)


def github_api(request):
    '''Get my github repos'''
    response = requests.get('https://api.github.com/users/manananggal/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
        'page_title': 'My GitHub Repos',
        'nav': nav,
    }
    return render(request, 'github.html', context)
