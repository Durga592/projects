from django import forms

from django.forms import ModelForm

from ice.models import Document, Order

from django.forms.widgets import DateInput


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class OrderForm(forms.ModelForm):
	class Meta:
		model 	=	Order
		fields 	=	'__all__'
		#widget 	=	{"date":DateInput}
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for field, field_inst in self.fields.items():
			field_inst.widget.attrs.update({"class":"form-control"})