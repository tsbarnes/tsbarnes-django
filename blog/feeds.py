from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Article

class BlogFeed(Feed):
  title = "Thea Barnes"
  link = "/blog/"
  description = "The blog of Thea Barnes"

  def items(self):
    return Article.objects.all().order_by("-date")[:5]
		
  def item_title(self, item):
    return item.title
		
  def item_description(self, item):
    return item.short
		
  def item_link(self, item):
    return reverse('blog-detail', kwargs = {'slug': item.slug})