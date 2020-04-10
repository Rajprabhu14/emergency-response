from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(regex='(?:(?:\+|0{0,2})91(\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$',
                                       message='Phone Number not in indian standard format',
                                       code='invalid_phone_number'
                                       )  # NOQA
password_validator = RegexValidator(regex='(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.{8,16})',
                                   message='Password Must contain atleast 1 lowecase, 1 uppercase, 1 numeric & contains any of !@#$%^&* with length of 8 to 16',
                                   code='invalid_password') # NOQA
