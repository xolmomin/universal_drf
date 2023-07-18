# import logging
# from django.utils.deprecation import MiddlewareMixin
# from root import settings
# logger = logging.getLogger("mongolog.request")
#
#
# class RequestMiddleware(MiddlewareMixin):
#
#     def __get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     def process_request(self, request):
#         import pymongo
#
#         myclient = pymongo.MongoClient(settings.MONGODB_URL)
#
#         mydict = {
#             "client_ip": self.__get_client_ip(request),
#             "url": request.build_absolute_uri()
#         }
#
#         myclient.test.mongolog.insert_one(mydict)
