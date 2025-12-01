from django.http import JsonResponse

def DashboardStatsView(request):
    return JsonResponse({"status": "OK", "message": "Dashboard stats working"})
