from django.forms import ModelForm, Textarea
from .models import Document, Directory, FAQ

# class DocumentForm(ModelForm):
#     class Meta:
#         model = Document
#         fields = ['name', 'directory', 'description', 'pptx_href', 'video_href']
#         widgets = {
#             'description': Textarea(attrs={'cols': 40, 'rows': 15}),
#             }
#
#     def save( self ) :
#         """ saves the model to the database """
#         from datetime import datetime
#
#         obj_list = Document.objects.filter( name=self.cleaned_data['name'] )
#
#         if len( obj_list ) == 0 :
#             obj = Document(
#                         date = datetime.now(),
#                         name = self.cleaned_data['name'],
#                         directory = self.cleaned_data['directory'],
#                         description = self.cleaned_data['description'],
#                         pptx_href = self.cleaned_data['pptx_href'],
#                         video_href = self.cleaned_data['video_href'],
#
#             )
#             obj.save()
#
#         else :
#             obj = obj_list[0]
#             obj.directory = self.cleaned_data['directory']
#             obj.description = self.cleaned_data['description']
#             obj.pptx_href = self.cleaned_data['pptx_href']
#             obj.video_href = self.cleaned_data['video_href']
#             obj.save()
#
#
# class FAQForm(ModelForm):
#     class Meta:
#         model = FAQ
#         fields = ['directory', 'question', 'answer', 'pptx_href', 'video_href', 'img_href']
#         widgets = {
#             'answer': Textarea(attrs={'cols': 40, 'rows': 15}),
#             }
#
#     def save( self ) :
#         """ saves the model to the database """
#         from datetime import datetime
#
#         obj_list = FAQ.objects.filter( question=self.cleaned_data['question'] )
#
#         if len( obj_list ) == 0 :
#             obj = FAQ(
#                         date = datetime.now(),
#                         directory = self.cleaned_data['directory'],
#                         question = self.cleaned_data['question'],
#                         answer = self.cleaned_data['answer'],
#                         pptx_href = self.cleaned_data['pptx_href'],
#                         video_href = self.cleaned_data['video_href'],
#                         img_href = self.cleaned_data['img_href'],
#
#             )
#             obj.save()
#
#         else :
#             obj = obj_list[0]
#             obj.directory = self.cleaned_data['directory']
#             obj.answer = self.cleaned_data['answer']
#             obj.pptx_href = self.cleaned_data['pptx_href']
#             obj.video_href = self.cleaned_data['video_href']
#             obj.img_href = self.cleaned_data['img_href']
#             obj.save()
