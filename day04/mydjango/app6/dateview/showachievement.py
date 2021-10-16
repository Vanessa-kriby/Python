from app1.models import *
from app1.util.utils import *

def showAchievements(request):
    '''
        http://127.0.0.1:8000/showAchievements
    '''
    result=Achievement.objects.values("score","gain_date","student_id","course_id")
    return showJsonresult(result)