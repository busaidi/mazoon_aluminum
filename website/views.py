from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import ContactForm
from django.utils.translation import get_language


def home(request):
    context = {'redirect_to': request.path}
    features = [
        {
            'icon': 'fas fa-temperature-low',
            'title': _('Thermal Efficiency'),
            'description': _(
                'Our windows and doors help insulate outside heat from your home. Your home stays warm in cold times '
                'and cool in hot times. This means less use of heaters or air conditioners, saving you money.'),
        },
        {
            'icon': 'fas fa-volume-mute',
            'title': _('Sound Barrier'),
            'description': _(
                'Tired of street noise and outside sounds in general? Our products isolate most unwanted sounds. '
                'Enjoy the peace inside, even if there is noise outside.'),
        },
        {
            'icon': 'fas fa-cloud-rain',
            'title': _('Rain Guard'),
            'description': _(
                'Don\'t worry about rainwater getting inside. Our windows and doors have special seals to keep the '
                'rain outside.'),
        },
        {
            'icon': 'fas fa-tools',
            'title': _('Low Maintenance'),
            'description': _('Cleaning is easy. A little wipe-down is all you need to make them look new again.'),
        },
        {
            'icon': 'fas fa-leaf',
            'title': _('Eco Choice'),
            'description': _(
                'Aluminum is special because it can be recycled many times, saving lots of energy. When we recycle '
                'it, we create less waste, and the recycled aluminum is just as good as new.'),
        },
        {
            'icon': 'fas fa-shield-alt',
            'title': _('Built Strong'),
            'description': _(
                'Aluminum is easy to form and strong, so it can withstand sun, wind and rain for many years.'),
        },
        {
            'icon': 'fas fa-ruler-combined',
            'title': _('Design Flexibility'),
            'description': _('Want different designs? We have many designs to suit the look of your home.'),
        },
        {
            'icon': 'fas fa-wrench',
            'title': _('Easy Install'),
            'description': _(
                'Light yet strong, our windows and doors are easy to manufacture, install and are long-lasting.'),
        },
    ]
    context['features'] = features
    return render(request, 'website/home.html', context)


def about(request):
    context = {'redirect_to': request.path}
    return render(request, 'website/about.html', context)


def mazoon45(request):
    context = {'redirect_to': request.path}
    return render(request, 'website/products/mazoon45.html', context)


def mazoon_lab_view(request):
    context = {'redirect_to': request.path}
    return render(request, 'website/mazoon_lab.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your message has been sent successfully!'))
            return redirect('contact')
        else:
            messages.error(request, _('There was an error with your submission.'))
    else:
        form = ContactForm()

    context = {'form': form, 'redirect_to': request.path}
    return render(request, 'website/contact.html', context)
