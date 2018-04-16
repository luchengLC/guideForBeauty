# import copy
# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from django.core import serializers
# import json
#
# # from beauty.models import LcTest, JdHkProductBasemakeup, JdHkProductCologne, JdHkProductParfume, JdHkProductLipstick, \
# #     JdHkProductEye
#
#
#
#
# # 测试
# @require_http_methods(["GET"])
# def show_student(request):
#     response = {}
#     try:
#         stu = LcTest.objects.filter()
#         response['list'] = json.loads(serializers.serialize("json", stu))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 测试                   尽量修改用POST
# @require_http_methods(["GET"])
# def add_student(request):
#     response = {}
#     try:
#         stu = LcTest(sno=request.GET.get('sno'))
#         stu.save()
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # -----------------------------------正式--------------------------------------
#
#
# # 底妆
# @require_http_methods(["GET"])
# def show_baseMakeup(request):
#     response = {}
#     try:
#         baseMakeup = JdHkProductBasemakeup.objects.all()[:50]
#         response['list'] = json.loads(serializers.serialize("json", baseMakeup))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 古龙水
# @require_http_methods(["GET"])
# def show_Cologne(request):
#     response = {}
#     try:
#         cologne = JdHkProductCologne.objects.all()[:50]
#         response['list'] = json.loads(serializers.serialize("json", cologne))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 香精
# @require_http_methods(["GET"])
# def show_parfume(request):
#     response = {}
#     try:
#         parfume = JdHkProductParfume.objects.all()[:50]
#         response['list'] = json.loads(serializers.serialize("json", parfume))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 唇妆
# @require_http_methods(["GET"])
# def show_lipstick(request):
#     response = {}
#     try:
#         lipstick = JdHkProductLipstick.objects.all()[:50]
#         response['list'] = json.loads(serializers.serialize("json", lipstick))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 眼妆
# @require_http_methods(["GET"])
# def show_eye(request):
#     response = {}
#     try:
#         eye = JdHkProductEye.objects.all()[:50]
#         response['list'] = json.loads(serializers.serialize("json", eye))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 请求列表总方法，封装其他的
# @require_http_methods(["GET"])
# def show_list(request):
#     global req
#     req = request
#     cmd = request.GET.get('cmd')
#     print("cmd = ", cmd)
#
#     # 这里偷懒一下，先给个ID来区别，以后换成数字，或者直接在数据库中存一张表，从表中获取对应关系
#     # 以下的顺序是跟前端页面的编码对应的
#     # 这方法 耦合性太高，一定要改！
#     if cmd == '底妆':
#         return show_baseMakeup(req)
#     elif cmd == '古龙水':
#         return show_Cologne(req)
#     elif cmd == '香精':
#         return show_parfume(req)
#     elif cmd == '唇妆':
#         return show_lipstick(req)
#     elif cmd == '眼妆':
#         return show_eye(req)
#
#
# # -----------------------------------搜索--------------------------------------
#
#
# # 查询搜索
# @require_http_methods(["GET"])
# def show_search_list(request):
#     global req
#     req = request
#     cmd = request.GET.get('cmd')
#     print("cmd = ", cmd)
#
#     if cmd == '底妆':
#         return show_search_list_baseMakeup(req)
#     elif cmd == '古龙水':
#         return show_search_list_cologne(req)
#     elif cmd == '香精':
#         return show_search_list_parfume(req)
#     elif cmd == '唇妆':
#         return show_search_list_lipstick(req)
#     elif cmd == '眼妆':
#         return show_search_list_eye(req)
#
#
# # 底妆的查询搜索
# @require_http_methods(["GET"])
# def show_search_list_baseMakeup(request):
#     response = {}
#     try:
#         searchNameMsg = request.GET.get('name')
#         print('step 1')
#         searchList = JdHkProductBasemakeup.objects.filter(name__icontains=searchNameMsg)[:50]
#         response['list'] = json.loads(serializers.serialize("json", searchList))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 古龙水的查询搜索
# @require_http_methods(["GET"])
# def show_search_list_cologne(request):
#     response = {}
#     try:
#         searchNameMsg = request.GET.get('name')
#         print('step 1')
#         searchList = JdHkProductCologne.objects.filter(name__icontains=searchNameMsg)[:50]
#         response['list'] = json.loads(serializers.serialize("json", searchList))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 香精的查询搜索
# @require_http_methods(["GET"])
# def show_search_list_parfume(request):
#     response = {}
#     try:
#         searchNameMsg = request.GET.get('name')
#         print('step 1')
#         searchList = JdHkProductParfume.objects.filter(name__icontains=searchNameMsg)[:50]
#         response['list'] = json.loads(serializers.serialize("json", searchList))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 唇妆的查询搜索
# @require_http_methods(["GET"])
# def show_search_list_lipstick(request):
#     response = {}
#     try:
#         searchNameMsg = request.GET.get('name')
#         print('step 1')
#         searchList = JdHkProductLipstick.objects.filter(name__icontains=searchNameMsg)[:50]
#         response['list'] = json.loads(serializers.serialize("json", searchList))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# # 眼妆的查询搜索
# @require_http_methods(["GET"])
# def show_search_list_eye(request):
#     response = {}
#     try:
#         searchNameMsg = request.GET.get('name')
#         print('step 1')
#         searchList = JdHkProductEye.objects.filter(name__icontains=searchNameMsg)[:50]
#         response['list'] = json.loads(serializers.serialize("json", searchList))
#         response['msg'] = 'success'
#         response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)