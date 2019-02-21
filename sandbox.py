
import logging

if __name__ == "__main__":

    from common.utils.operating_system.logger import initialize_logging
    initialize_logging( path='', level=logging.DEBUG )

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'django_config.settings')

    import django
    django.setup()

    from doc import models
    models.Tool.objects.get_or_create( name='Optimal+')
    models.Tool.objects.get_or_create( name='Exensio Yield')
    models.Tool.objects.get_or_create( name='JMP')
    models.Tool.objects.get_or_create( name='Tableau')

    models.Type.objects.get_or_create( name='Template')
    models.Type.objects.get_or_create( name='Training')

    pptx = models.DocumentType.objects.get_or_create( name='Powerpoint')[0]
    video = models.DocumentType.objects.get_or_create( name='Video')[0]
    models.DocumentType.objects.get_or_create( name='PDF')
    models.DocumentType.objects.get_or_create( name='Link')
    models.DocumentType.objects.get_or_create( name='Template')


    tool = models.Tool.objects.get_or_create( name='Exensio Yield')[0]
    type = models.Type.objects.get_or_create( name='Training')[0]

    from pandas import read_csv
    df1 = read_csv( 'training_document.csv' )
    df2 = read_csv( 'training_directory.csv' ).set_index('id')

    for idx in df2.index :
        val = df2.ix[idx]['name']
        df1['directory_id'] = df1['directory_id'].replace(idx, val)


    df1 = df1.fillna( 'NONE' )
    atts = ['directory_id', 'name','description','pptx_href','video_href']
    for value in df1[atts].values:

        category = models.Category.objects.get_or_create(   tool=tool,
                                                            type=type,
                                                            name=value[0])[0]

        element = models.Element.objects.get_or_create( category=category,
                                                        name=value[1],
                                                        description=value[2])[0]
        if value[3] != 'NONE' :
            models.Document.objects.get_or_create(  element=element,
                                                    name=value[1],
                                                    type = pptx,
                                                    link=value[3])[0]

        if value[4] != 'NONE' :
            models.Document.objects.get_or_create(  element=element,
                                                    name=value[1],
                                                    type = video,
                                                    link=value[4])[0]
