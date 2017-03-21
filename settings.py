from django.conf import settings

try:
    GALLERY_LARGE_WIDTH = settings.GALLERY_LARGE_WIDTH
    GALLERY_LARGE_HEIGHT = settings.GALLERY_LARGE_HEIGHT
except AttributeError:
    GALLERY_LARGE_WIDTH = 800
    GALLERY_LARGE_HEIGHT = 600

try:
    GALLERY_IMAGE_WIDTH = settings.GALLERY_IMAGE_WIDTH
    GALLERY_IMAGE_HEIGHT = settings.GALLERY_IMAGE_HEIGHT
except AttributeError:
    GALLERY_IMAGE_WIDTH = 300
    GALLERY_IMAGE_HEIGHT = 225

try:
    GALLERY_THUMBNAIL_WIDTH = settings.GALLERY_THUMBNAIL_WIDTH
    GALLERY_THUMBNAIL_HEIGHT = settings.GALLERY_THUMBNAIL_HEIGHT
except AttributeError:
    GALLERY_THUMBNAIL_WIDTH = 133
    GALLERY_THUMBNAIL_HEIGHT = 100

try:
    GALLERY_PATH = settings.GALLERY_PATH
except AttributeError:
    GALLERY_PATH = 'gallery'

try:
    MEDIA_ROOT = settings.MEDIA_ROOT
except AttributeError:
    MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

try:
    MEDIA_URL = settings.MEDIA_URL
except AttributeError:
    MEDIA_URL = '/media/'
