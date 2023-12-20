from django.shortcuts import render
from pages.models import MainScrollModel, Our_Menus

# Create your views here.
def home_page_view(request):
    scrolls = MainScrollModel.objects.all().order_by('pk')
    menus = Our_Menus.objects.all().order_by('pk')
    context = {
        'scrolls':scrolls,
        'menus':menus
    }
    return render(request, template_name='index.html', context=context)




