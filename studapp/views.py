from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from studapp.models import StudentDb
from studapp.serializers import RegistrationSerializer,StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.
class RegistrationView(APIView):
    def get(self,request):

        users = User.objects.all()
        serializer_intsnace = RegistrationSerializer(users,many=True)
        return Response(data=serializer_intsnace.data)
    
    def post(self,request):
        serializer_instance = RegistrationSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message":"Registration successfull..."})
        return Response({"error":serializer_instance.errors})


class StudentCreateListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        student = StudentDb.objects.all()
        serializer_instance = StudentSerializer(student,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):

        serializer_instance = StudentSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=
                            {
                                "Message":"Student added successfully....",
                                "Student Details": serializer_instance.data
                            })
        return Response(serializer_instance.errors)

class StudentRetrieveUpdateDeleteView(APIView):

        permission_classes = [permissions.IsAuthenticated]
        
        def get(self,request,st_id):

            student = get_object_or_404(StudentDb,id=st_id)
            serializer_instance = StudentSerializer(student)
            return Response(data=serializer_instance.data)

        def put(self,request,st_id):

            student = get_object_or_404(StudentDb,id=st_id)
            serializer_instance = StudentSerializer(data=request.data,instance = student)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response({
                    "Message":"Student details updated successfully...",
                    "Updated Details of student" : serializer_instance.data
                })
            return Response({"errors":serializer_instance.errors})

        def delete(self,request,st_id):

            student = get_object_or_404(StudentDb,id=st_id)
            student.delete()
            return Response({"Message":"Student deleted successfully..."})

class LogOutView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):

        token = request.user.auth_token
        token.delete()
        return Response({"Message":"Logout Successfull...."})


