from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from studapp.models import StudentDb

class RegistrationSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id','username','email','password','date_joined']
        read_only_fields = ['id','date_joined']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)

class StudentSerializer(ModelSerializer):

    class Meta:
        model = StudentDb
        fields = '__all__'

    
