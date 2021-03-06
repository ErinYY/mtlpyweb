from datetime import datetime

from django.contrib.syndication.views import Feed

from mtlpy.blog.models import Post


class BlogEntriesFeed(Feed):
    title = "Montréal-Python"
    link = "/feed/"
    description = "News from the Montréal-Python community"

    def items(self):
        return Post.published_objects.order_by('-publish')[:5]

    def item_pubdate(self, item):
        return datetime.combine(item.publish, datetime.min.time())

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html_content()

    # item_link is only needed if NewsItem has no get_absolute_url
    # method.
    def item_link(self, item):
        return item.get_absolute_url()
