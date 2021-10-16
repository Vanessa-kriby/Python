from django.urls import path
from app6.dateview.addInventorys import *
from app6.dateview.showInventorys import *
from app6.dateview.updateInventory import *
from app6.dateview.delInventory import *

urlpatterns =[
    path("addInventorys",addInventorys,name="addInventorys"),
    path("showInventorys",showInventorys,name="showInventorys"),
    path("updateInventory",updateInventory,name="updateInventory"),
    path("delInventory",delInventory,name="delInventory"),
]