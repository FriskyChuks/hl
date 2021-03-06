from django.db import models

from accounts.models import User

COUNTRY = (
        ('nigeria', 'Nigeria'),
    )


STATE = (
            ('lagos', 'Lagos'),
            ('nasarawa', 'Nasarawa'),
            ('abia', 'Abia'),
            ('adamawa', 'Adamawa'),
            ('anambra', 'Anambra'),
            ('akwa-ibom', 'Akwa-Ibom'),
            ('delta', 'Delta'),
            ('edo', 'Edo'),
            ('enugu', 'Enugu'),
            ('jigawa', 'Jigawa'),
            ('ondo', 'Ondo'),
            ('imo', 'Imo'),
            ('bauchi', 'Bauchi'),
            ('plateau', 'Plateau'),
            ('ogun', 'Ogun'),
            ('kaduna', 'Kaduna'),
            ('katsina', 'Katsina'),
            ('sokoto', 'Sokoto'),
            ('osun', 'Osun'),
            ('benue', 'Benue'),
            ('kogi', 'Kogi'),
            ('fct(Abuja)', 'FCT(Abuja)'),
            ('ebonyi', 'Ebonyi'),
            ('cross-rivers', 'Cross-Rivers'),
        )

RELATIONSHIP = (
        ('spouse', 'Spouse'),
        ('brother', 'Brother'),
        ('sister', 'Sister'),
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('cousin', 'Cousin'),
        ('nephew', 'Nephew'),
        ('niece', 'Niece'),
        ('uncle', 'Uncle'),
        ('aunt', 'Aunt'),
        ('neighbour', 'Neighbour'),
        ('son', 'Son'),
        ('daughter', 'Daughter'),
        ('son', 'Son'),
    )

MARITAL_STATUS = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
    )

ACCOUNT_TYPE = (
    ('1', 'Current'),
    ('2', 'Savings'),
)


class CarOwnerDriverRegister(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # image           = models.ImageField(default='car.png', blank=True)
    date_of_birth   = models.DateField()
    marital_status  = models.CharField(max_length=10, choices=MARITAL_STATUS)
    nationality     = models.CharField(max_length=20, choices=COUNTRY, default="Nigeria")
    state_of_origin = models.CharField(max_length=15, choices=STATE)
    lga_of_origin   = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=100)
    state_of_residence = models.CharField(max_length=50, choices=STATE, default='fct(Abuja)')
    lga_of_residence = models.CharField(max_length=50)
    address_of_residence = models.CharField(max_length=100)
    next_of_kin     = models.CharField(max_length=100)
    next_of_kin_relationship  = models.CharField(max_length=50, choices=RELATIONSHIP)
    phone           = models.PositiveIntegerField()
    address         = models.CharField(max_length=150)
    date_created    = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated         = models.DateTimeField(auto_now_add=False, auto_now=True)
    active          = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} || {self.user.phone1}"


class BankAccountInformation(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    account_name	= models.CharField(max_length=100)
    account_type	= models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    bank_name		= models.CharField(max_length=50)
    account_number	= models.CharField(max_length=10)
    date_created    = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.account_name} || {self.account_number}|| {self.bank_name}"


class DriverRequest(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    valid_licence	= models.BooleanField(default=False)
    licence_issue_date = models.DateField()
    licence_exp_date = models.DateField()
    licence_no      = models.CharField(max_length=20)
    comments		= models.TextField(max_length=500)
    status 			= models.CharField(max_length=9, default='pending')
    date_created	= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated			= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        if self.valid_licence:
            return f"{self.user.first_name} {self.user.last_name} || Has a valid Licence"
        else:
            return f"{self.user.first_name} {self.user.last_name} || Does not have a valid Licence"


class SitBackAndEarn(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    car_make	    = models.CharField(max_length=100)
    model           = models.CharField(max_length=100)
    car_year        = models.CharField(max_length=4)
    image           = models.ImageField(null=True, blank=True, upload_to="car_owner/cars/")
    particulars		= models.ImageField(null=True, blank=True, upload_to="car_owner/particulars/")
    valid_id 		= models.ImageField(null=True, blank=True, upload_to="car_owner/id_cards/")
    status 			= models.CharField(max_length=9, default='pending')
    date_created	= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated			= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.car_make} {self.model} {self.car_year}"
