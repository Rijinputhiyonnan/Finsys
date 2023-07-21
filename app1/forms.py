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

class BankAccountHolderForm(forms.Form):
    # BankAccountHolder fields
    name = forms.CharField(max_length=100)
    alias = forms.CharField(max_length=100)
    ACCOUNT_TYPE_CHOICES = [
        ('CC', 'Credit Card'),
        ('BA', 'Bank Account'),
    ]
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES)

    # BankAccount fields
    holder_name = forms.CharField(max_length=100)
    account_number = forms.CharField(max_length=20)
    ifsc_code = forms.CharField(max_length=11)
    swift_code = forms.CharField(max_length=11)
    BANK_NAME_CHOICES = [
        ('SBI', 'State Bank of India'),
        ('BOB', 'Bank of Baroda'),
        ('BOI', 'Bank of India'),
        ('BOM', 'Bank of Maharashtra'),
        ('CAN', 'Canara Bank'),
        ('CBI', 'Central Bank of India'),
        ('IND', 'Indian Bank'),
        ('IOB', 'Indian Overseas Bank'),
        ('PSB', 'Punjab & Sind Bank'),
        ('PNB', 'Punjab National Bank'),
        ('UCO', 'UCO Bank'),
        ('UBI', 'Union Bank of India'),
        ('AXIS', 'Axis Bank Ltd.'),
        ('BANDHAN', 'Bandhan Bank Ltd.'),
        ('CSB', 'CSB Bank Limited'),
        ('CUB', 'City Union Bank Ltd.'),
        ('DCB', 'DCB Bank Ltd.'),
        ('DHANLAXMI', 'Dhanlaxmi Bank Ltd.'),
        ('FEDERAL', 'Federal Bank Ltd.'),
        ('HDFC', 'HDFC Bank Ltd.'),
        ('ICICI', 'ICICI Bank Ltd.'),
        # add more banks here
    ]
    bank_name = forms.ChoiceField(choices=BANK_NAME_CHOICES)
    branch_name = forms.CharField(max_length=100)

    # BankConfiguration fields
    set_cheque_book_range = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, required=False)
    enable_cheque_printing = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, required=False)
    set_cheque_printing_configuration = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, required=False)

    # MailingAddress fields
    name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    country = CountryField().formfield()
    STATE_CHOICES = [
          ('AN', 'Andaman and Nicobar Islands'),
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CH', 'Chhattisgarh'),
    ('DL', 'National Capital Territory of Delhi'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu and Kashmir'),
    ('LA', 'Ladakh'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OR', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TG', 'Telangana'),
    ('TR', 'Tripura'),
    ('UT', 'Uttarakhand'),
    ('UP', 'Uttar Pradesh'),
    ('WB', 'West Bengal')
    ]
    state = forms.ChoiceField(choices=STATE_CHOICES)
    pin = forms.CharField(max_length=6)

    # BankingDetails fields
    pan_it_number = forms.CharField(max_length=10)
    registration_details = forms.CharField(widget=forms.Textarea)
    gstin_un = forms.CharField(max_length=15)
    set_alter_gst_details = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, required=False)

    # OpeningBalance fields
    date = forms.DateField(input_formats=['%d %m %Y'])
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    
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