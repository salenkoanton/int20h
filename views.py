from django.http import HttpResponse
import json
import datetime
from card.models import Card, Author, Post


def callback(request):
    print(request.body)
    obj = request.POST.get("object")
    if request.POST.get("type") == 'confirmation':
        return HttpResponse("015e90ff")
    if request.POST.get("type") == 'wall_reply_new':

        author_vk_id = int(obj.get("from_id"))
        author = Author.odjects.get(vk_id=author_vk_id)
        if author is None:
            author = Author.objects.create(vk_id=author_vk_id)
        post_id = int(obj.get("post_id"))
        post = Post.objects.get(vk_id=post_id)
        date_ms = int(obj.get("date"))
        date = datetime.datetime.fromtimestamp(date_ms / 1000.0)
        text = int(obj.get("text"))
        Card.objects.create(author=author, post=post, date=date, type=Card.COMMENT, text=text)
        print("comment")
    if request.POST.get("type") == 'wall_post_new':
        post_id = int(obj.get("post_id"))
        Post.objects.create(vk_id=post_id)
    return HttpResponse("ok")
