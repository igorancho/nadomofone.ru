# coding=utf-8
from annoying.decorators import ajax_request
from core.models import User

__author__ = 'alexy'


@ajax_request
def moderator_remove(request):
    if request.method == 'GET':
        if request.GET.get('item_id'):
            user = User.objects.get(id=int(request.GET.get('item_id')))
            user.delete()
            return {
                'success': int(request.GET.get('item_id'))
            }
        else:
            return {
                'error': True
            }
    else:
        return {
            'error': True
        }
