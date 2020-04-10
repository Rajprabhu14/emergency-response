from django.apps import AppConfig


class VolunteerConfig(AppConfig):
    name = 'volunteer'

    def read(self):
        import volunteer.signals # NOQA
