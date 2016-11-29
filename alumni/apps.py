from django.apps import AppConfig


class AlumniConfig(AppConfig):
    name = 'alumni'


    def ready(self):
        import alumni.signals
