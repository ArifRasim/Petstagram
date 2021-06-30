from django import forms

from Petstagram.common.models import Comment


# class CommentForm(forms.Form):
#     comment = forms.CharField(required=True, widget=forms.Textarea(attrs={
#         'class': 'form-control rounded-2'
#     }))
#
#
# class Meta:
#     model = Comment
#     fields = ('comment')

class CommentForm(forms.Form):
    text=forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form-control rounded-2'}
        )
    )
