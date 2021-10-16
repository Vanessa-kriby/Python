from django.urls import path
from app6.dateview.addinventory import *
from app6.dateview.showinventory import *
from app6.dateview.delinventory import *
from app6.dateview.updateinventory import *

urlpatterns =[
    path("addInventorys", addInventorys, name="addInventorys"),
    path("showInventorys", showInventorys, name="showInventorys"),
    path("delInventory", delInventory, name="delInventory"),
    path("updateInventory", updateInventory, name="updateInventory"),
]
