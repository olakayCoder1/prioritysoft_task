from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
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
    

    @action(detail=True, methods=['get'])
    def suppliers(self, request, pk=None):
        item = self.get_object()
        suppliers = item.suppliers.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)




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
    

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        supplier = self.get_object()
        items = supplier.items.all()  # Assuming 'items' is a related_name in your Supplier model
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
