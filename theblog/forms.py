from django import forms
from .models import Post,  Category, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'' ,'id':'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Dynamically fetch categories
        choice_list = [(c.name, c.name) for c in Category.objects.all()]
        self.fields['category'].widget = forms.Select(
            choices=choice_list,
            attrs={'class': 'form-control'}
        )   

class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag','body','snippet','header_image')

    widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'title_tag': forms.TextInput(attrs={'class':'form-control'}),
      'category': forms.Select(attrs={'class':'form-control'}),
      'body': forms.Textarea(attrs={'class':'form-control'}),
      'snippet': forms.Textarea(attrs={'class':'form-control'}),

    }   

class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ('name', 'body')  

      widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'body': forms.Textarea(attrs={'class':'form-control'}),
      

    }   

