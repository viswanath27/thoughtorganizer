from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView





def home(request):
	return render(request,'dailyactivities/home.html')

#def journey(request):
#	return render(request,'dailyactivities/journey.html')

#def notes(request):
#	return render(request,'dailyactivities/notes.html')

#def requirementunderstanding(request):
#	return render(request,'dailyactivities/requirementunderstanding.html')

#def interviewquestions(request):
#	return render(request,'dailyactivities/interviewquestions.html')	
class dailyevents(LoginRequiredMixin, UserPassesTestMixin,ListView):
	model = Post
	template_name = 'dailyactivities/dailyevents.html'
	#model = Post
	success_url = 'dailyactivities/dailyevents'
	#context_object_name = 'post'
	def test_func(self):
		#post = self.get_object()
		#if self.request.user == post.author:
		#	return True
		return True 
	def get_queryset(self):
		return True
		#user = get_object_or_404(User,username=self.kwargs.get('username'))
		#return Post.objects.filter(author=user).order_by('-date_posted')

class journey(LoginRequiredMixin, UserPassesTestMixin,ListView):
	model = Post
	template_name = 'dailyactivities/journey.html'
	#model = Post
	success_url = 'dailyactivities/journey'
	#context_object_name = 'post'
	def test_func(self):
		#post = self.get_object()
		#if self.request.user == post.author:
		#	return True
		return True 
	def get_queryset(self):
		return True
		#user = get_object_or_404(User,username=self.kwargs.get('username'))
		#return Post.objects.filter(author=user).order_by('-date_posted')


class notes(LoginRequiredMixin, UserPassesTestMixin,ListView):
	model = Post
	template_name = 'dailyactivities/notes.html'
	#model = Post
	success_url = 'dailyactivities/notes'
	#context_object_name = 'post'
	def test_func(self):
		#post = self.get_object()
		#if self.request.user == post.author:
		#	return True
		return True 
	def get_queryset(self):
		return True
		#user = get_object_or_404(User,username=self.kwargs.get('username'))
		#return Post.objects.filter(author=user).order_by('-date_posted')



class interviewquestions(LoginRequiredMixin, UserPassesTestMixin,ListView):
	model = Post
	template_name = 'dailyactivities/interviewquestions.html'
	#model = Post
	success_url = 'dailyactivities/interviewquestions'
	#context_object_name = 'post'
	def test_func(self):
		#post = self.get_object()
		#if self.request.user == post.author:
		#	return True
		return True 
	def get_queryset(self):
		return True
		#user = get_object_or_404(User,username=self.kwargs.get('username'))
		#return Post.objects.filter(author=user).order_by('-date_posted')


class requirementunderstanding(LoginRequiredMixin, UserPassesTestMixin,ListView):
	model = Post
	template_name = 'dailyactivities/requirementunderstanding.html'
	#model = Post
	success_url = 'dailyactivities/requirementunderstanding'
	#context_object_name = 'post'
	def test_func(self):
		#post = self.get_object()
		#if self.request.user == post.author:
		#	return True
		return True 
	def get_queryset(self):
		return True
		#user = get_object_or_404(User,username=self.kwargs.get('username'))
		#return Post.objects.filter(author=user).order_by('-date_posted')

class fitness(LoginRequiredMixin, UserPassesTestMixin,ListView):
	model = Post
	template_name = 'dailyactivities/fitness.html'
	#model = Post
	success_url = 'dailyactivities/fitness'
	#context_object_name = 'post'
	def test_func(self):
		#post = self.get_object()
		#if self.request.user == post.author:
		#	return True
		return True 
	def get_queryset(self):
		return True
		#user = get_object_or_404(User,username=self.kwargs.get('username'))
		#return Post.objects.filter(author=user).order_by('-date_posted')



#def thoughts(request):
#	context = {
#	'posts': Post.objects.all()
#	}
#	return render(request,'dailyactivities/thoughts.html',context)	


class PostListView(LoginRequiredMixin,ListView):
	model = Post
	template_name = 'dailyactivities/thoughts.html' #<app>/<model>_<view_type>.html
	context_object_name = 'posts'
	ordering=['-date_posted']
	paginate_by = 5

class UserPostListView(LoginRequiredMixin,ListView):
	model = Post
	template_name = 'dailyactivities/user_thoughts.html' #<app>/<model>_<view_type>.html
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post
	
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/dailyactivities/thoughts'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#def fitness(request):
#	return render(request,'dailyactivities/fitness.html')	

#def dailyevents(request):
#	return render(request,'dailyactivities/dailyevents.html')					
# Create your views here.
