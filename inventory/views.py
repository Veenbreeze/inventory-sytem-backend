from django.http import JsonResponse

def DashboardStatsView(request):
    return JsonResponse({"status": "OK", "message": "Dashboard stats working"})
    return JsonResponse({"status": "OK", "message": "Dashboard stats working"})
        return JsonResponse({"detail": "Google OAuth is not yet implemented."}, status=501)     