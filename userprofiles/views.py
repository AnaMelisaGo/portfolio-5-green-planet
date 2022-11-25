from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm, UserForm
from checkout.models import Transaction


@login_required
def user_profile(request):
    """
    Function to show the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'account': 'active',
    }
    return render(request, template, context)


@login_required
@transaction.atomic
def edit_profile(request):
    """
    Function to edit the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and userprofile_form.is_valid():
            user_form.save()
            userprofile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(instance=profile)
        messages.warning(request, f'Updating profile...')
    template = 'profiles/edit_profile.html'
    context = {
        'account': 'active',
        'profile': profile,
        'user_form': user_form,
        'userprofile_form': userprofile_form,
        'on_profile_page': True,
    }
    return render(request, template, context)


@login_required
def view_history(request):
    """
    Function to view user's transactions history
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    transactions = profile.account.all()
    template = 'profiles/view_history.html'
    context = {
        'account': 'active',
        'profile': profile,
        'transactions': transactions,
    }
    return render(request, template, context)


@login_required
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
        'account': 'active',
        'from_profile': True,
        'transaction': transaction,
    }
    return render(request, template, context)
