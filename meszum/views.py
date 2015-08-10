from django.shortcuts import render

def index(request):
#     if request.user.is_superuser == True:
#         association_list = Association.objects.all()
#     else:
#         association_list = Association.objects.filter(users=request.user)
#         
    context_dict = {}
    
    return render(request, 'index.html', context_dict)