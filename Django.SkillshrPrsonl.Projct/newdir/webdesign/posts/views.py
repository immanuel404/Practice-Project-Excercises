from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def post_list_view(request):
	queryset = Post.objects.all()
	random = Post.objects.all().order_by("?")
	context = { 'object_list': queryset, 'random_list': random, }
	return render(request, "posts/list.html", context)

def post_detail_view(request, id=None):
	obj = get_object_or_404(Post, id=id)
	context = { 'object': obj }
	return render(request, "posts/detail.html", context)

def post_search_view(request):
	print(request.GET)
	request_params = request.GET
	query = request_params.get("q")
	queryset = Post.objects.none()
	if query:
		queryset = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
	context = {'object_list': queryset}
	return render(request, "posts/detail.html", context)
