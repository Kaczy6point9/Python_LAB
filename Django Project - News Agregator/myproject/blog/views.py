from django.shortcuts import render

from .models import Post
# Create your views here.
def post_list_view(request):
	context = {
		'object_list': Post.objects.filter(public=True).order_by("-date_publish")
	}

	return render(request, 'blog/post_list.html', context)

def post_detail_view(request, post_id):
	context = { 'object': Post.objects.get(id=post_id)}
	return render(request, 'blog/post_detail.html', context)


def posts_in_category(request, category_name):
	context = { 'object_list': Post.objects.filter(category__name=category_name) }
	return render(request, 'blog/post_list.html', context)
