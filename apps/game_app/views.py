from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    if 'user' not in request.session:
        return redirect("/")
    return render(request, 'game_app/index.html')
def logout(request):
    request.session.flush()
    return redirect("/")