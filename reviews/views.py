from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from guns.models import Gun
from .models import Review
from .forms import ReviewForm



class ReviewOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        review = self.get_object()
        return review.user == self.request.user



class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        self.gun = get_object_or_404(Gun, slug=self.kwargs['gun_slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.gun = self.gun
        review.user = self.request.user  # 🔥 important for ownership
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('gun_detail', kwargs={'slug': self.gun.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gun'] = self.gun
        context['title'] = f'Add Review for {self.gun.name}'
        return context


class ReviewUpdateView(LoginRequiredMixin, ReviewOwnerMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('gun_detail', kwargs={'slug': self.object.gun.slug})


class ReviewDeleteView(LoginRequiredMixin, ReviewOwnerMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('gun_detail', kwargs={'slug': self.object.gun.slug})