import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgres://aohwcepllagdbo:0e92b0ac95c35b58facbd6bd7ff5d7b4f76584a7de6a73ddcddc0f0a6f846ad9@ec2-54-247-188-107.eu-west-1.compute.amazonaws.com:5432/dfn59a7e5u2a21')
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = os.environ \
                   .get('SECRET_KEY',
                        'Z\xf0\xfb\xf0r\x8c\r\xa4\xc6Qf\xc2\x15\xcb\x12')
