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

class BankConfigurationForm(forms.ModelForm):
    set_cheque_book_range = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)
    enable_cheque_printing = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)
    set_cheque_printing_configuration = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)

    class Meta:
        model = BankConfiguration
        fields = ['set_cheque_book_range', 'enable_cheque_printing', 'set_cheque_printing_configuration']

class MailingAddressForm(forms.ModelForm):
    class Meta:
        model = MailingAddress
        fields = ['name', 'address', 'country', 'state', 'pin']

class BankingDetailsForm(forms.ModelForm):
    set_alter_gst_details = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)

    class Meta:
        model = BankingDetails
        fields = ['pan_it_number', 'registration_details', 'gstin_un', 'set_alter_gst_details']

class OpeningBalanceForm(forms.ModelForm):
    class Meta:
        model = OpeningBalance
        fields = ['date', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


    def save(self):
        # Get the cleaned data from the form
        cleaned_data = self.cleaned_data

        # Create a new BankAccountHolder object
        bank_account_holder = BankAccountHolder(
            name=cleaned_data['name'],
            alias=cleaned_data['alias'],
            account_type=cleaned_data['account_type']
        )
        bank_account_holder.save()

        # Create a new BankAccount object
        bank_account = BankAccount(
            holder_name=cleaned_data['holder_name'],
            account_number=cleaned_data['account_number'],
            ifsc_code=cleaned_data['ifsc_code'],
            swift_code=cleaned_data['swift_code'],
            bank_name=cleaned_data['bank_name'],
            branch_name=cleaned_data['branch_name']
        )
        bank_account.save()

        # Create a new BankConfiguration object
        bank_configuration = BankConfiguration(
            set_cheque_book_range=(cleaned_data['set_cheque_book_range'] == 'yes'),
            enable_cheque_printing=(cleaned_data['enable_cheque_printing'] == 'yes'),
            set_cheque_printing_configuration=(cleaned_data['set_cheque_printing_configuration'] == 'yes')
        )
        bank_configuration.save()

        # Create a new MailingAddress object
        mailing_address = MailingAddress(
            name=cleaned_data['name'],
            address=cleaned_data['address'],
            country=cleaned_data['country'],
            state=cleaned_data['state'],
            pin=cleaned_data['pin']
        )
        mailing_address.save()

        # Create a new BankingDetails object
        banking_details = BankingDetails(
            pan_it_number=cleaned_data['pan_it_number'],
            registration_details=cleaned_data['registration_details'],
            gstin_un=cleaned_data['gstin_un'],
            set_alter_gst_details=(cleaned_data['set_alter_gst_details'] == 'yes')
        )
        banking_details.save()

        # Create a new OpeningBalance object
        opening_balance = OpeningBalance(
            date=cleaned_data['date'],
            amount=cleaned_data['amount']
        )
        opening_balance.save()