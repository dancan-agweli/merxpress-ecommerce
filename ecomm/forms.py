from django import forms
from ecomm.models import SignUp
from django.contrib.auth.forms import AuthenticationForm
from .models import Order, OrderItem, Cancellation, Return, Refund

class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields='__all__'
    
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        phone=cleaned_data.get('phone')
        if phone and len(str(phone))!= 10:
            self.add_error('phone',"Mobile number should be exactly 10 digits")

        return cleaned_data
    
class LoginForm(AuthenticationForm):
    email=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter email id'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))

#orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'status']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']

class CancellationForm(forms.ModelForm):
    class Meta:
        model = Cancellation
        fields = ['order', 'reason']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['order', 'reason']

class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['order', 'amount']