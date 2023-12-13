# artical link : https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets

from django import forms


# for showing todays date
import datetime
# for date
from django.forms.widgets import NumberInput
class ExampleForm(forms.Form):
    #for one line input
    name = forms.CharField(initial='Swapno')

    #for multiple line of input
    comment = forms.CharField(widget=forms.Textarea)

    #to decrise the height of our text area we can decrise rows from 10 to 1
    comment_sm = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    #for email address
    email = forms.EmailField(label='Please Enter Your Email ')

    # boolean field takes t/f as inptu
    aggree = forms.BooleanField()

    #for birthday
    
    # birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    #input date and initiall it show todays
    day = forms.DateField(initial= datetime.date.today)

    #create pre-built choice fields so the user does not have to enter any information and only selects from the predefined choices.  
    FAVORITE_COLORS = [
        ('blue','BLUE'),
        ('red','RED'),
        ('black','BLACK'),
    ]
    favourit_color = forms.ChoiceField(choices=FAVORITE_COLORS)

    favourit_color_radio = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS)

    # for multichoice field
    favourit_multiple_color = forms.MultipleChoiceField(choices=FAVORITE_COLORS)

    # multichoice field with checkbox
    favourit_multiple_checkbox_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS)


    # allow for multiple-choice selection, use ModelMultipleChoiceField. If you wish to change the drop-down menu to checkboxes, add the widget CheckboxSelectMultiple. 
    

from django import forms
from .models import MyModel

# Create your forms here.

# class ExampleForm(forms.Form):
#     model_choices = forms.ModelMultipleChoiceField(
#         widget = forms.CheckboxSelectMultiple,
#         queryset = MyModel.objects.all(),
#         initial = 0
#         )
