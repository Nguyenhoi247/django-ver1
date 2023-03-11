from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm, CommentForm
from django.http import JsonResponse



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        avatar = request.FILES.get('avatar')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Tên người dùng đã tồn tại'})
        user = User.objects.create_user(username=username, email=email, password=password)

        if avatar:
            user.profile.avatar = avatar
            user.profile.save()

        return redirect('login')
    return render(request, 'register.html', {'succeed': 'đăng kí thành công'})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'thông tin không hợp lệ'})
    return render(request, 'login.html')


@login_required
def home(request):
    logged_in_users = User.objects.filter(is_active=True)
    posts = Post.objects.all()

    # handle comment form submission for home page
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        post_form = PostForm(request.POST,  request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('home')
        elif post_form.is_valid():
            # image = post_form.cleaned_data['image']
            post = post_form.save(commit=False)
            post.authorr = request.user
            post.save()
            return redirect('home')
    else:
        comment_form = CommentForm()
        post_form = PostForm()

    # build comments for each post
    comments = {}
    for post in posts:
        comment_list = post.comments.all()
        comment_form = CommentForm(initial={'post': post})
        comments[post.id] = {
            'comment_list': comment_list,
            'form': comment_form,
        }

    context = {
        'logged_in_users': logged_in_users,
        'posts': posts,
        'comment_form': comment_form,
        'post_form': post_form,
        'comments': comments,
        # 'image':image
    }

    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def post(request, pk=None):
    post = None
    if pk:
        post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        if pk:
            form = CommentForm(request.POST, author=request.user, post=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
        else:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')
    comments = {}
    if post:
        comments[post.id] = {
            'comment_list': post.comments.all(),
            'form': CommentForm(author=request.user, post=post),
        }
    context = {
        'logged_in_users': User.objects.filter(is_active=True),
        'posts': Post.objects.all() if not post else [post],
        'comment_form': form,
        'comments': comments,
    }
    template_name = 'create_post.html' if not pk else 'home.html'
    return render(request, template_name, context)

# tạo nút like
def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)

    # Kiểm tra xem người dùng đã thích bài đăng hay chưa
    liked_posts = request.session.get('liked_posts', [])
    if post_id in liked_posts:
        # Nếu bài đăng đã được thích, bỏ thích và giảm likes
        post.likes -= 1
        liked_posts.remove(post_id)
    else:
        # Nếu bài đăng chưa được thích, thích và tăng likes
        post.likes += 1
        liked_posts.append(post_id)

    # Lưu trạng thái đã thích vào session
    request.session['liked_posts'] = liked_posts

    # Lưu trạng thái của bài đăng
    post.save()

    return JsonResponse({'likes': post.likes})


# def my_view(request):
#     img_list = [    'img/meo.jpg',    'img/img-p1.jpg',    'img/img-p2.jpg',]

    
#     # Lấy một đường dẫn ảnh ngẫu nhiên từ danh sách img_list
#     img_path = random.choice(img_list)

#     # Các dòng code khác của view ở đây
#     context = {'logged_in_users': request.user, 'img_path': img_path}
#     return render(request, 'home.html', context)



# def my_view(request):
#     # Tạo ảnh ngẫu nhiên với kích thước 200x200 pixels và màu sắc ngẫu nhiên
#     img = Image.new('RGB', (200, 200), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     response = HttpResponse(content_type="image/png")
#     # Lưu ảnh vào response
#     img.save(response, "PNG")
#     return response

# def error_404(request, exception):
#    context = {}
#    return render(request,'home.html', context)

# def error_500(request):
#    context = {}
#    return render(request,'home.html', context)

# def upload_avatar(request):
#     if request.method == 'POST':
#         avatar_file = request.FILES.get('avatar')
#         # do something with the file, like save it
#         return render(request, 'home.html')
#     return render(request, 'register.html')