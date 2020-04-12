from django.apps import AppConfig


class VolunteerConfig(AppConfig):
    name = 'volunteer'

    def ready(self):
        import volunteer.signals # NOQA
