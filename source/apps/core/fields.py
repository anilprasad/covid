import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

from django import forms
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import ValidationError
from django.contrib.gis.geos import Point
from django.contrib.postgres.fields import ArrayField


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django 1.9's postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)

    def to_python(self, value):
        res = super().to_python(value)
        if isinstance(res, list):
            value = [self.base_field.to_python(val) for val in res]
        return value


class ImageField(models.ImageField):

    def save_form_data(self, instance, data):
        if data is not None:
            file = getattr(instance, self.attname)
            if file != data:
                file.delete(save=False)
        super(ImageField, self).save_form_data(instance, data)


class PointField(forms.Field):
    def clean(self, value):
        if not isinstance(value, (Point, )):
            if value is None:
                value = Point(x=-0.693400, y=52.302898)
            else:
                data = [x.strip() for x in value.split(',')]
                value = Point(x=float(data[1]), y=float(data[0]))
        return value


class PhoneFiled(forms.Field):
    def validate(self, value):
        try:
            phonenumbers.parse(value)
        except NumberParseException:
            raise ValidationError(_("Invalid phone number. Please use international format. e.g: +44 1234 567 890"))
        return value
