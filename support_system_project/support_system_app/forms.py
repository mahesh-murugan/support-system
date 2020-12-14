from django import forms


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['email'].widget.attrs['required'] = True
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['autofocus'] = True
        self.fields['password'].widget.attrs['placeholder'] = "Password"
        self.fields['password'].widget.attrs['required'] = True
        self.fields['password'].widget.attrs['class'] = 'form-control'

    email = forms.EmailField(max_length=30, required=True, label="")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=30, required=True, label="")


class CreateTicketForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    departments = (
        ('PWSLab DevOps Support', 'PWSLab DevOps Support'),
        ('iSupport', 'iSupport'))

    priorities = (('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'))

    department = forms.ChoiceField(choices=departments, required=True)
    category = forms.ChoiceField(choices=(('others', 'others'),), required=True)
    subject = forms.CharField(max_length=60, required=True)
    description = forms.CharField(widget=forms.Textarea({"rows": 5, "cols": 20}), required=True)
    priority = forms.ChoiceField(choices=priorities, required=True)
    name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)

