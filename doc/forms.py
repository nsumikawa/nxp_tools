from django.forms import ModelForm, Textarea
import models as models

class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ['tool', 'type', 'name', 'description']
        widgets = {
            'description': Textarea(attrs={ 'cols': 40, 'rows': 15,
                                            'placeholder':'Enter Description : '}),
            }

    def save( self, idx ) :
        """ saves the model to the database """
        from datetime import datetime

        if idx != 'None' :
            obj = models.Category.objects.get( id = idx )
            obj.tool = self.cleaned_data['tool']
            obj.type = self.cleaned_data['type']
            obj.name = self.cleaned_data['name']

        else :
            obj = models.Category.objects.get_or_create(tool = self.cleaned_data['tool'],
                                                        type = self.cleaned_data['type'],
                                                        name = self.cleaned_data['name'] )[0]

        obj.description = self.cleaned_data['description']
        obj.save()

        return obj


class ElementForm(ModelForm):
    class Meta:
        model = models.Element
        fields = ['category', 'name', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 15}),
            }

    def save( self, idx ) :
        """ saves the model to the database """

        if idx != 'None' :
            obj = models.Element.objects.get( id = idx )
            obj.category = self.cleaned_data['category']
            obj.name = self.cleaned_data['name']

        else :
            obj = models.Element.objects.get_or_create( category = self.cleaned_data['category'],
                                                        name = self.cleaned_data['name'] )[0]

        obj.description = self.cleaned_data['description']
        obj.save()

        return obj


class DocumentForm(ModelForm):
    class Meta:
        model = models.Document
        fields = ['element', 'type', 'link']
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 15}),
            }

    def save( self, request, idx ) :
        """ saves the model to the database """

        if idx != 'None' :
            obj = models.Document.objects.get( id = idx )
            obj.element = self.cleaned_data['element']
            obj.type = self.cleaned_data['type']

        else :
            obj = models.Document.objects.get_or_create(element = self.cleaned_data['element'],
                                                        type = self.cleaned_data['type'],
                                                        author = request.user )[0]

        obj.link = self.cleaned_data['link']
        obj.save()

        return obj

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
