from django import forms
from .models import Mine


class MineForm(forms.ModelForm):
    class Meta:
        model = Mine
        fields = ('name',
                  'stone_type',
                  'discovery_license_number',
                  'operating_license_number',
                  'minimum_operating_tonnage',
                  'government_law',
                  'issue_date',
                  'province',
                  'city',
                  'village',
                  'description',
                  )

        labels = {
            'name': "نام",
            'stone_type': "نوع سنگ",
            'discovery_license_number': "شماره مجوز کشف",
            'operating_license_number': "شماره پروانه بهره برداری",
            'minimum_operating_tonnage': "حداقل تناژ بهره برداری",
            'government_law': "حقوق دولتی (تومان/تن)",
            'issue_date': "تاریخ صدور",
            'province': "استان",
            'city': "شهرستان",
            'village': "روستا",
            'description': "توضیحات",
        }
