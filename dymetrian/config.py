import os
class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))                   #applicatioon directory
    DEBUG = True                                                                    #the debug is set to true
    SECRET_KEY = '&\xfb?\xfbL\xd7\xc0z\x19ewF\xdd\xe6\xce(M\xbc\x15,'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/dymetrian.db' %APPLICATION_DIR          #setting the location to save our database
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')                            #identifying the location of our static file
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')                                 #setting the location to save our image files