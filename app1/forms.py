from django import forms
from .models import *
from .models import noninventory

class ImageForm(forms.ModelForm):
    class Meta:
        model = service
        fields = ['img', 'name', 'sku', 'sac', 'unit','categ','descr','check1','saleprice','income','check2','tax','abatement','sertype']


class ImageForm2(forms.ModelForm):
    class Meta:
        model=noninventory
        fields=("image","name","sku","hsn","unit","category","initialqty","date","stockalrt","invacnt","description","salesprice","incomeacnt","tax","purchaseinfo","cost","expacnt","purtax","revcharge","presupplier",)


class ImageForm3(forms.ModelForm):
    class Meta:
        model = bundle
        fields = ['image', 'name', 'sku', 'description']

class ImageForm4(forms.ModelForm):
    class Meta:
        model=inventory
        fields=("image","name","sku","hsn","unit","category","initialqty","date","stockalrt","invacnt","description","salesprice","incomeacnt","tax","purchaseinfo","cost","expacnt","purtax","revcharge","presupplier")


#----------sumayya------------------------------------------------------------------------------------------------------------
class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    #attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea )
    
    #----------Rijin-----------------------------------------------------
# forms.py
from django import forms

from .models import BankAccountHolder, BankAccount, BankConfiguration, MailingAddress, BankingDetails, OpeningBalance

class BankAccountHolderForm(forms.ModelForm):
    class Meta:
        model = BankAccountHolder
        fields = ['name', 'alias', 'account_type']
        widgets = {
            'account_type': forms.Select(attrs={'class': 'black-select'})
        }


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['holder_name', 'account_number', 'ifsc_code', 'swift_code', 'bank_name', 'branch_name']


class MailingAddressForm(forms.ModelForm):
    class Meta:
        model = MailingAddress
        fields = ['name', 'address', 'country', 'state', 'pin']


class OpeningBalanceForm(forms.ModelForm):
    class Meta:
        model = OpeningBalance
        fields = ['date', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'})
        }
class BankingDetailsForm(forms.ModelForm):
    set_alter_gst_details = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect)

    class Meta:
        model = BankingDetails
        fields = ['pan_it_number', 'registration_details', 'gstin_un', 'set_alter_gst_details']

class BankConfigurationForm(forms.ModelForm):
    set_cheque_book_range = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect)
    enable_cheque_printing = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect)
    set_cheque_printing_configuration = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect)

    class Meta:
        model = BankConfiguration
        fields = ['set_cheque_book_range', 'enable_cheque_printing', 'set_cheque_printing_configuration']


   