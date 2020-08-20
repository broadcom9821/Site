from django.shortcuts import render
from django.views.generic import ListView, DetailView
from PenpineappleapplePen.models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "app/index.html"
    paginate_by = 3


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = "app/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

def EGE_I_GIA(request):
    return render(request, 'app/Education/EGE_I_GIA.html')


def Mattex_obesp(request):
    return render(request, 'app/Education/Mattex_obesp.html')


def Obr_model(request):
    return render(request, 'app/Education/Obr_model.html')


def Obr_stand(request):
    return render(request, 'app/Education/Obr_stand.html')


def Dop_obraz(request):
    return render(request, 'app/Education/Dop_obraz.html')


def about(request):
    return render(request, 'app/About/about.html')


def contact(request):
    return render(request, 'app/About/contact.html')


def Gallery(request):
    return render(request, 'app/About/Gallery.html')


def History(request):
    return render(request, 'app/About/History.html')


def SMI(request):
    return render(request, 'app/About/SMI.html')


def Team(request):
    return render(request, 'app/About/Team.html')


def fullwidth(request):
    return render(request, 'app/full-width.html')


def sidebar(request):
    return render(request, 'app/sidebar.html')


def faq(request):
    return render(request, 'app/Admission/faq.html')


def error(request):
    return render(request, 'app/404.html')


def services(request):
    return render(request, 'app/services.html')


def About_adm(request):
    return render(request, 'app/Admission/About_adm.html')


def Recomendation_adm(request):
    return render(request, 'app/Admission/Recomendation_adm.html')


def Results_adm(request):
    return render(request, 'app/Admission/Results_adm.html')


def Stipendia_adm(request):
    return render(request, 'app/Admission/Stipendia_adm.html')
