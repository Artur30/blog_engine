from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={
            self.model.__name__.lower(): obj
        })


class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})
    
    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            new_obj = form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': form})


class ObjectListMixin:
    model = None
    template = None

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, context={
            self.model.__name__.lower() + 's': obj
        })


class ObjectUpdateMixin:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form(instance=obj)
        context = {
            'form': form,
            self.model.__name__.lower(): obj
        }
        return render(request, self.template, context=context)
    
    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form(request.POST, instance=obj)
        context = {
            'form': form,
            self.model.__name__.lower(): obj
        }

        if form.is_valid():
            update_obj = form.save()
            return redirect(update_obj)
        return render(request, self.template, context=context)


class ObjectDeleteMixin:
    model = None
    redirect_url = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={
            self.model.__name__.lower(): obj
        })

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(self.redirect_url)



