from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    SlugRelatedField,
    ValidationError,
)
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=('user', 'following')
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise ValidationError('Ошибка! Нельзя подписаться на самого себя')
        return value


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
