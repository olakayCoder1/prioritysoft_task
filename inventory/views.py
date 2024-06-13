from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, filters
from inventory.pagination import StandardResultsSetPagination
from .models import Item, Supplier
from .serializers import ItemSerializer, SupplierSerializer



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'date_added']

    @method_decorator(cache_page(30*1)) 
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)




class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'contact_info']
    ordering_fields = ['name']

    @method_decorator(cache_page(30*1))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
