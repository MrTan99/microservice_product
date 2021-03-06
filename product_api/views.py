from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

from product_api.models import Product

from rest_framework import generics

from django.conf import settings

import requests


class ProductAccessView(APIView):
	authentication_classes = []
	permission_classes = []
	parser_classes = (JSONParser,)
	
	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404
	
	#get all products
	def get(self, request, format=None):
		try:
			products = Product.objects.all().order_by('-id')
			serializer = ProductSerializer(products, many=True)
			return Response(serializer.data)
		except:
			return Response(status.HTTP_404_NOT_FOUND)
	
	
	#create product
	def post(self, request, format=None):
		try:
			if not checkauth(request):
				return Response(status.HTTP_403_FORBIDDEN)
			serializer = ProductSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(status.HTTP_204_NO_CONTENT)
		except:
			return Response(status.HTTP_403_FORBIDDEN)
	
	#update dan delete product
	def put(self, request, pk, format=None):
		if not checkauth(request):
			print("1")
			return Response(status.HTTP_403_FORBIDDEN)
		product = Product.objects.get(pk=pk)
		serializer = ProductSerializer(product, data=request.data)
		if serializer.is_valid():
			print("2")
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def checkauth(request):
    try:
        auth_header_value = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header_value:
            req = requests.get(settings.SERVICE_API + "/authentication/auth/", timeout=10, headers={"Authorization":auth_header_value})
            if not req.status_code == 200:
                return 0
            return 1
        return 0
    except:
        return 0


class ProductAccessView1(APIView):
	authentication_classes = []
	permission_classes = []
	parser_classes = (JSONParser,)

	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404

	#search products
	def get(self, request, pk, format=None):
		try:
			products = Product.objects.all().filter(name__icontains=pk)
			serializer = ProductSerializer(products, many=True)
			return Response(serializer.data)
		except:
			return Response(status.HTTP_404_NOT_FOUND)

class ProductAccessView2(APIView):
	authentication_classes = []
	permission_classes = []
	parser_classes = (JSONParser,)

	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404

	#get detail products
	def get(self, request, pk, format=None):
		try:
			product = Product.objects.get(id=pk)
			serializer = ProductSerializer(product, many=False)
			return Response(serializer.data)
		except:
			return Response(status.HTTP_404_NOT_FOUND)



# @api_view(['GET'])
# def productList(request):
# 	products = Product.objects.all().order_by('-id')
# 	serializer = ProductSerializer(products, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def searchProduct(request, pk):
# 	products = Product.objects.all().filter(name__contains=pk)
# 	serializer = ProductSerializer(products, many=True)
# 	return Response(serializer.data)


# @api_view(['GET'])
# def productDetail(request, pk):
# 	products = Product.objects.get(id=pk)
# 	serializer = ProductSerializer(products, many=False)
# 	return Response(serializer.data)

# @api_view(['POST'])
# def productCreate(request):
# 	print(request.data["product_picture"])


# 	serializer = ProductSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

# @api_view(['PATCH'])
# def productUpdate(request, pk):
# 	product = Product.objects.get(id=pk)
# 	serializer = ProductSerializer(instance=product, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

# @api_view(['PATCH'])
# def productDelete(request, pk):
# 	product = Product.objects.get(id=pk)
# 	serializer = ProductSerializer(instance=product, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response('Item succsesfully delete!')


