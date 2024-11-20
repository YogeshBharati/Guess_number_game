from django.shortcuts import render, redirect
from random import randint

def home(request):
    # Initialize the game
    if 'number_to_guess' not in request.session:
        request.session['number_to_guess'] = randint(1, 100)
        request.session['attempts'] = 0

    message = ''
    if request.method == 'POST':
        try:
            user_guess = int(request.POST.get('guess'))
            request.session['attempts'] += 1

            if user_guess < request.session['number_to_guess']:
                message = "Too low! Try again."
            elif user_guess > request.session['number_to_guess']:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You guessed the number in {request.session['attempts']} attempts."
                # Reset the game
                del request.session['number_to_guess']
                del request.session['attempts']
        except ValueError:
            message = "Please enter a valid number."

    return render(request, 'game/home.html', {'message': message})
