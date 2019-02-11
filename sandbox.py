
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

    models.DocumentType.objects.get_or_create( name='Powerpoint')
    models.DocumentType.objects.get_or_create( name='Video')
    models.DocumentType.objects.get_or_create( name='PDF')
