from django.shortcuts import render
from django.views import View
from patients.models import Patient
from .models import Site_admin
from django.core.paginator import Paginator
from math import ceil
# Create your views here.

def Home_admin_view(request):

	return render(request, 'site_admins/home_base_view.html', {})

def admin_patient_view(request):
    patients = Site_admin.objects.all()
    return render(request, "site_admins/admin_patient_view.html", {'patients': patients})

def search_results(request):
    #Lay yeu cau query tu request
    # query = request.GET.get('q')
    #Thuc hiện query
    results = Site_admin.objects.all()
    #Paginator: phân trang trong django
    #result là cái cần phân, 2: mỗi trang 2 phần tử
    amount_per_page = 2
    paginator = Paginator(results, amount_per_page)
    #Lấy số trang để hiển thị các result thuộc trang đó, mặc định là 1
    #page lấy từ url được push lên trong <form>
    page = request.GET.get('page', 1)
    try:
        page_results = paginator.page(page)
    except PageNotAnInteger:
        # Nếu page không phải là một số nguyên, trả về trang đầu tiên
        page_results = paginator.page(1)
    except EmptyPage:
        # Nếu page vượt quá số lượng trang có sẵn, trả về trang cuối cùng
        page_results = paginator.page(paginator.num_pages)
    total_result_page = ceil((results.count())/amount_per_page)
    context = {
        'query_results': paginator,
        'page_results': page_results,
        'result_counter': results.count(),
        'total_page': total_result_page,
        'page_range': paginator.page_range,
    }
    return render(request, 'site_admins/admin_patient_view.html', context)