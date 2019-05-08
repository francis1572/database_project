from django.db import models

import uuid  # Required for unique book instances


# Create your models here.
class FoodType(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    typeName = models.CharField(
        max_length=200,
        help_text="Enter a food type name:"
        )
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.typeName

class Food(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    foodName = models.CharField(
        max_length=200,
        help_text="Enter a food name:"
        )
    price = models.IntegerField(
        help_text="Enter a food price:"
        )
    typeID = models.ForeignKey('FoodType', on_delete = models.CASCADE, null=True)
    featID = models.ForeignKey('FoodFeature', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.foodName

#===============================================================================================

from django.contrib.auth.models import User  # Required to assign User as a borrower
class Order(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    orderID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this order.")
    foodID = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    orderDate = models.DateTimeField(null=True, blank=True, auto_now = True)

    ###樓上那個auto_now是我另外加的，可能會有bug。
    
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return '{0} ({1})'.format(self.orderID, self.foodID.foodName)

        ###這也是我自己打出來的


class Evaluation(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    evalID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this evaluation.")
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    foodID = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    #grade = models.IntegerField(help_text="Enter a food price:")



    r1 = '1'
    r2 = '2'
    r3 = '3'
    r4 = '4'
    r5 = '5'
    RANK_CHOICES = (
        (r1, '1 star(the worst)'),
        (r2, '2 stars'),
        (r3, '3 stars'),
        (r4, '4 stars'),
        (r5, '5 stars(the best)'),
    )
    grade = models.CharField(
        max_length=1,
        choices=RANK_CHOICES,
        default=r3,
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.grade)

class FoodMaterial (models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    matName = models.CharField(
        max_length=200,
        help_text="Enter a food material name:"
        )
    matFrom = models.CharField(
        max_length=200,
        help_text="Enter a food material source:"
        )
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.matName


class make (models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    foodID = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    matID = models.ForeignKey('FoodMaterial', on_delete=models.SET_NULL, null=True)
    WayToCook = models.CharField(
        max_length=200,
        help_text="Enter how a food was cooked:"
        )
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.WayToCook

class FoodFeature (models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    FoodFeat = models.CharField(
        max_length=200,
        help_text="Enter a food feature name:"
        )
    #foodID = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.FoodFeat









