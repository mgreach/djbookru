from django.conf import settings


POSTS_ON_PAGE = getattr(settings, 'FORUM_POSTS_ON_PAGE', 100)
