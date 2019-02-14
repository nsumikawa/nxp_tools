from django.forms import ModelForm, Textarea
import models as models
#
# class CategoryForm(ModelForm):
#     class Meta:
#         model = models.Category
#         fields = ['tool', 'type', 'name', 'description']
#         widgets = {
#             'description': Textarea(attrs={ 'cols': 40, 'rows': 15,
#                                             'placeholder':'Enter Description : '}),
#             }
#
#     def save( self, idx ) :
#         """ saves the model to the database """
#         from datetime import datetime
#
#         if idx != 'None' :
#             obj = models.Category.objects.get( id = idx )
#             obj.tool = self.cleaned_data['tool']
#             obj.type = self.cleaned_data['type']
#             obj.name = self.cleaned_data['name']
#
#         else :
#             obj = models.Category.objects.get_or_create(tool = self.cleaned_data['tool'],
#                                                         type = self.cleaned_data['type'],
#                                                         name = self.cleaned_data['name'] )[0]
#
#         obj.description = self.cleaned_data['description']
#         obj.save()
#
#         return obj
