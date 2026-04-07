from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, Avg
from reviews.forms import ReviewForm
from reviews.models import Review
from .models import Gun, Category
from .forms import GunForm, CategoryForm
import math
from users.mixins import ModeratorRequiredMixin


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class GunListView(ListView):
    model = Gun
    template_name = 'guns/gun_list.html'
    context_object_name = 'guns'

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort', 'name')
        order = self.request.GET.get('order', 'asc')


        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(game__icontains=query)
            )


        if sort_by in ['name', 'game']:
            if order == 'desc':
                sort_by = f'-{sort_by}'
            qs = qs.order_by(sort_by)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['sort_by'] = self.request.GET.get('sort', 'name')
        context['order'] = self.request.GET.get('order', 'asc')
        return context

class GunDetailView(DetailView):
    model = Gun
    template_name = 'guns/gun_detail.html'
    context_object_name = 'gun'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gun = self.object
        reviews = gun.reviews.all().order_by('-created_at')
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        average_rating_int = math.floor(average_rating)


        if self.request.method == 'POST':
            form = ReviewForm(self.request.POST)
            if form.is_valid() and self.request.user.is_authenticated:
                review = form.save(commit=False)
                review.gun = gun
                review.save()
                return redirect('gun_detail', slug=gun.slug)
        else:
            form = ReviewForm()

        context.update({
            'reviews': reviews,
            'form': form,
            'average_rating': average_rating,
            'average_rating_int': average_rating_int,
        })
        return context

class GunCreateView(LoginRequiredMixin, CreateView):
    model = Gun
    form_class = GunForm
    template_name = 'guns/gun_form.html'
    success_url = reverse_lazy('gun_list')
    login_url = 'login'

class GunUpdateView(LoginRequiredMixin, UpdateView):
    model = Gun
    form_class = GunForm
    template_name = 'guns/gun_form.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('gun_detail', kwargs={'slug': self.object.slug})

class GunDeleteView(LoginRequiredMixin, DeleteView):
    model = Gun
    template_name = 'guns/gun_confirm_delete.html'
    success_url = reverse_lazy('gun_list')
    login_url = 'login'


class CategoryListView(ListView):
    model = Category
    template_name = 'guns/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'guns/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guns'] = self.object.guns.all()
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'guns/category_form.html'
    success_url = reverse_lazy('category_list')
    login_url = 'login'

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'guns/category_form.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('category_list')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'guns/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
    login_url = 'login'