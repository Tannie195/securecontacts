
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Message sent successfully!')
            return redirect('contact')
           
        else:
            messages.error(request, '❌ Please fix the errors below.')
      
    else:
        form = ContactForm()
    return render(request, 'contactform/contact.html', {'form': form})

