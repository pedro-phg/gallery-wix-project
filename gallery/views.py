from django.shortcuts import render, redirect
from .services.RestAPIService import RestAPIService
from .forms import PictureForm

def gallery(request):

    wixConnection = RestAPIService('https://interantar.com')

    picturesInformation = wixConnection.get('/_functions/gallery')


    return render(request, 'pages/gallery.html', context = {
        'pictures': picturesInformation.json()
    })




def postPicture(request):

    wixConnection = RestAPIService('https://interantar.com')

    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            wixConnection.post(endpoint='/_functions/gallery', data=data)
            print("Successfully Submitted Form!")
    else:
        form = PictureForm()
    
    return render(request, 'pages/form.html', {'form': form})



