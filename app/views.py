from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home(request, username):
    name = ""
    image = ""
    try:
        html = requests.get(f"https://github.com/{username}").text
        soup = BeautifulSoup(html, 'lxml')
        name = " ".join(soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden').text.split())
        image = soup.find("div", "position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0").a['href']
        return render(request, "find.html", context={"name": name, "image":image})
    except:
        return render(request, "404.html", context={"username": username})
    
def index(request):
    if request.method == "GET":
        try:
            searchinput = request.GET['user']
            return redirect(f"/{searchinput}")
        except MultiValueDictKeyError:
            return render(request, "index.html")

        
    