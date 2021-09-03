from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Invoice, InvoiceLine
from .serializer import InvoiceSerializer, InvoiceLineSerializer
from app.accounts.models import Customer


# class CreateOrder(APIView):
#     # def get_queryset(self,request,  *args, **kwargs):
#     #     client = get_object_or_404(Customer, user__email=request.data.user)
#     #     queryset = Invoice.objects.get_or_create(
#     #         customer=client,
#     #         status='O'
#     #     )
#     #     return queryset
#     def get(self, request):
#         client = get_object_or_404(Customer, user__email=request.user)
#         queryset = Invoice.objects.get_or_create(
#             customer=client,
#             status='O'
#         )
#         data = InvoiceSerializer(queryset).data
#         return Response(data)
#     serializer_class = InvoiceSerializer
# class CreateOrder(generics.ListCreateAPIView):
#     serializer_class = InvoiceSerializer
#     #
#     # def get_queryset(self, request):
#     #     queryset = Invoice.objects.all()
#     #     print(request)
#     #     return queryset
#     def get_queryset(self):
#         # qs = super(CreateOrder, self).get_queryset(self,request, *args, **kwargs)
#         qs = Invoice.objects.filter(customer__user__email=self.request.user)
#         return qs
class CreateOrder(APIView):
    serializer_class = InvoiceLineSerializer

    def post(self, request, pk, choice_pk):
        # voted_by = request.data.get("voted_by")
        # data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        data = {'choice': choice_pk}
        serializer = InvoiceLineSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddOrder(generics.CreateAPIView):
    serializer_class = InvoiceLineSerializer
    queryset = InvoiceLine.objects.all()
    #
    # def get_queryset(self, request):
    #     queryset = Invoice.objects.all()
    #     print(request)
    #     return queryset
    # def get_queryset(self):
    #     # qs = super(CreateOrder, self).get_queryset(self,request, *args, **kwargs)
    #     qs = Invoice.objects.filter(customer__user__email=self.request.user)
    #     return qs


class InvoiceApiView(GenericViewSet):
    serializer_class = InvoiceSerializer

    @action(methods=['GET'], detail=True, url_name='invoice', url_path='invoice_show')
    def invoice_show(self, request, *args, **kwargs):
        qs = Invoice.objects.all()
        qs_ser = InvoiceSerializer(qs, many=True)
        return Response(data={'result': qs_ser.data}, status=200)

    # @action(methods=['GET'], detail=False, url_name='invoice_item', url_path='invoice_item')
    # def invoice_show(self, request, *args, **kwargs):
    #     qs = InvoiceLine.objects.all()
    #     qs_ser = InvoiceLineSerializer(qs, many=True)
    #     return Response(data={'result': qs_ser.data}, status=200)


class InvoiceLineApiView(GenericViewSet):
    serializer_class = InvoiceLineSerializer

    @action(methods=['POST'], detail=False, url_name='invoice_cal', url_path='invoice_cal')
    def invoice_cal(self, request, *args, **kwargs):
        # qs = Invoice.get_object()
        qs_ser = InvoiceLineSerializer(data=request.data)
        if qs_ser.is_valid():
            # qs.set_password(qs_ser.validated_data['password'])
            qs_ser.save()
            return Response({'status': 'COMPLETED'})
        else:
            return Response(qs_ser.errors, status=status.HTTP_400_BAD_REQUEST)
