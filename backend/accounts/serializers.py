from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password], 
        help_text="Your password can’t be too similar to your other personal information, must contain at least 8 characters and can’t be entirely numeric."
        )
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name','last_name','email')
        # extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')

        # Verifiy if username or email allready exists
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "You can't use this username."})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "You can't use this e-mail."})

        return attrs