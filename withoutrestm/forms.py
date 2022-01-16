from django import forms

from withoutrestm.models import Employee


class EmployeeForm(forms.ModelForm):
    def clean_country(self):
        input_country = self.cleaned_data['country']
        if input_country == 'Ireland' or input_country == 'United States':
            return input_country
        elif len(input_country) == 0 or input_country is None:
            input_country = 'NULL'
            return input_country
        else:
            raise forms.ValidationError('The country should be either Ireland or United States or leave it optional')

    class Meta:
        model = Employee
        fields = '__all__'
