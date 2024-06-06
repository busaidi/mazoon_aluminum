from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Category, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


def post_list(request):
    posts = Post.objects.all()
    latest_posts = Post.objects.order_by('-created_at')[:5]
    latest_comments = Comment.objects.order_by('-created_at')[:5]
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'latest_posts': latest_posts,
        'latest_comments': latest_comments,
    })


def post_detail(request, category_slug, slug):
    category = get_object_or_404(Category, slug=category_slug)
    post = get_object_or_404(Post, category=category, slug=slug)
    comments = post.comments.filter(parent__isnull=True)
    latest_posts = Post.objects.order_by('-created_at')[:5]
    latest_comments = Comment.objects.order_by('-created_at')[:5]
    comment_form = CommentForm(initial={'post_id': post.id})
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'latest_posts': latest_posts,
        'latest_comments': latest_comments,
    })


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = get_object_or_404(Comment, id=parent_id)
                comment.parent = parent_comment
            comment.save()
            messages.success(request, _('Your comment has been added successfully.'))
        else:
            messages.error(request, _('There was an error adding your comment. Please try again.'))
    return redirect('post_detail', category_slug=post.category.slug, slug=post.slug)


@login_required
def post_create(request):
    latest_posts = Post.objects.order_by('-created_at')[:5]
    latest_comments = Comment.objects.order_by('-created_at')[:5]
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, _('Your post has been created successfully.'))
            return redirect('post_detail', category_slug=post.category.slug, slug=post.slug)
        else:
            messages.error(request, _('There was an error creating your post. Please try again.'))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
