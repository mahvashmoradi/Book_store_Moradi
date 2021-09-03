from django import forms


class BookForm(forms.Form):
    """
    فرم ایجاد یا ویرایش کتاب
    """
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': "name"}))
    author = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "author"}))
    price = forms.IntegerField()
    categories = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "author"}))
    # categories = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    inventory = forms.IntegerField()
    image = forms.ImageField(required=False)
    # description = forms.CharField(max_length=250, widget=forms.Textarea, )