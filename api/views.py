from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import MyUuid
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from django.core.paginator import Paginator


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def aut_test(request):
    
    try:
        # create a new uuid
        generated_id = get_random_string(length=32)
        MyUuid.objects.create(uuid=generated_id)

        uuid_list = []
        # create pagination of data at 10 limit per page
        myuuid = MyUuid.objects.all().order_by('id').reverse()
        limit = request.GET.get('limit', 10)
        page_num = request.GET.get('page', 1)
        myuuid = Paginator(myuuid, limit)
        pages = myuuid .num_pages
        myuuid = myuuid.page(page_num)
        myuuid = myuuid.object_list
        total_uuid = 0

        for uid in myuuid:
            total_uuid += 1
            uuid_list.append({
                str(uid.created): uid.uuid,
            })
        


        data ={
            'uuid': uuid_list,
            'pages': pages,
            'total_uuid': total_uuid,
        }
        return Response({'status': HTTP_200_OK, 'message': 'okay', 'data': data}, status=HTTP_200_OK)
    except Exception as error:
        # print(error)
        return Response({'error': 'An Error Occured', 'message': error}, status=HTTP_500_INTERNAL_SERVER_ERROR)