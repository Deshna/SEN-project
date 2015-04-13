from django import forms
from models import Images

class UploadImageForm(forms.ModelForm):
	class Meta:
		model = Images
		exclude = ["product"]
		