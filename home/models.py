# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Users(models.Model):

    #__Users_FIELDS__
    user_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Dealer(models.Model):

    #__Dealer_FIELDS__
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Dealer_FIELDS__END

    class Meta:
        verbose_name        = _("Dealer")
        verbose_name_plural = _("Dealer")


class Productgroup(models.Model):

    #__Productgroup_FIELDS__
    productgroupname = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Productgroup_FIELDS__END

    class Meta:
        verbose_name        = _("Productgroup")
        verbose_name_plural = _("Productgroup")


class Product(models.Model):

    #__Product_FIELDS__
    productname = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    productgroup = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Inventory(models.Model):

    #__Inventory_FIELDS__
    quantity = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    totalprice = models.CharField(max_length=255, null=True, blank=True)

    #__Inventory_FIELDS__END

    class Meta:
        verbose_name        = _("Inventory")
        verbose_name_plural = _("Inventory")


class Reservation(models.Model):

    #__Reservation_FIELDS__
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    is_asked = models.BooleanField()
    is_sended = models.BooleanField()
    is_confirmed = models.BooleanField()
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Reservation_FIELDS__END

    class Meta:
        verbose_name        = _("Reservation")
        verbose_name_plural = _("Reservation")


class Configurationoptions(models.Model):

    #__Configurationoptions_FIELDS__
    paragraph = models.CharField(max_length=255, null=True, blank=True)
    itemcode = models.CharField(max_length=255, null=True, blank=True)
    itemdescription = models.TextField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    #__Configurationoptions_FIELDS__END

    class Meta:
        verbose_name        = _("Configurationoptions")
        verbose_name_plural = _("Configurationoptions")



#__MODELS__END
