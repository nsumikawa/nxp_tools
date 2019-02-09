
import logging

if __name__ == "__main__":

    from common.utils.operating_system.logger import initialize_logging
    initialize_logging( path='', level=logging.DEBUG )

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'main.settings')

    import django
    django.setup()

    from training.models import Document
    print Document.objects.filter(description__icontains='merge')
