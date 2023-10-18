from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        help_text="Your password can’t be too similar to your other personal information, must contain at least 8 characters and can’t be entirely numeric.",
    )
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")

        # Verify if username or email already exists
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": "You can't use this username."}
            )

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "You can't use this e-mail."})

        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
