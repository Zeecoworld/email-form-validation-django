from django.shortcuts import render,redirect
from .utils import validate_custom_email
from django.contrib import messages
from .models import EmailPost
from django.core.exceptions import ValidationError
# Create your views here.


def index(request):
    context = {}
    if request.method == "POST":
        form = request.POST['email_type']
        try:
            validate_custom_email(form)
            form_email = EmailPost.objects.create(email=form)
            form_email_save = form_email.save()
            if form_email_save:
                messages.success(request, 'Email registered successfully!')

        except ValidationError as e:
            context['email_error'] = e.message

        return render(request,"index.html",context)
           
    else:

      return render(request,"index.html")



# if request.method == 'POST':
#         form = EmailEntryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Email registered successfully!')
#             return redirect('email_entry')
#     else:
#         form = EmailEntryForm()
#     return render(request, 'email_entry.html', {'form': form})

# {% if messages %}
#     <ul class="messages">
#         {% for message in messages %}
#         <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
#         {% endfor %}
#     </ul>
#     {% endif %}