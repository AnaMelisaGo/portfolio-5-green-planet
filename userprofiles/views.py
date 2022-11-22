from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Transaction


def user_profile(request):
    """
    Function to show the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


def edit_profile(request):
    """
    Function to edit the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    template = 'profiles/edit_profile.html'
    context = {
        'profile': profile,
        'form': form,
        'on_profile_page': True,
    }
    return render(request, template, context)


def view_history(request):
    """
    Function to view user's transactions history
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    transactions = profile.account.all()
    template = 'profiles/view_history.html'
    context = {
        'profile': profile,
        'transactions': transactions,
    }
    return render(request, template, context)


def transaction_history(request, transaction_number):
    """
    Function to view user's transactions history
    """
    transaction = get_object_or_404(
        Transaction, transaction_number=transaction_number
    )
    messages.info(request, (
        f'Past transaction for the transaction number {transaction_number}.'
        ' An email was already sent during purchase.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'from_profile': True,
        'transaction': transaction,
    }
    return render(request, template, context)
