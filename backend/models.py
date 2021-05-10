from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """
    Create and save a SuperUser with the given email and password.
    """

    email = models.EmailField(unique=True)
    password = models.CharField(blank=True, max_length=255)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    teacher_request = models.BooleanField(
        default=False
    )  # When the user applies for a teacher account.
    is_teacher = models.BooleanField(default=False)
    hide_leaderboard = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)  # Bio
    share_code = models.CharField(
        max_length=6, null=True, blank=True
    )  # Number for generating the unique sharable link

    # Permission fields.
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return (
            "TEACHER REQUEST: " if self.teacher_request else ""
        ) + self.email

    def serialize_simple(self):
        return {
            "id": self.id,
            "username": self.username,
            "points": self.points,
            "is_teacher": self.is_teacher,
        }

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "description": self.description,
            "points": self.points,
            "is_teacher": self.is_teacher,
            "hide_leaderboard": self.hide_leaderboard,
            "leaderboard_position": self.ranking()
            if not self.hide_leaderboard
            else None,
        }

    def serialize_leaderboard(self, rank):
        # don't use self.ranking(); rank is calculated more efficiently
        # (using less DB queries) by the leaderboard endpoint.
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "points": self.points,
            "leaderboard_position": rank,
        }

    def ranking(self):
        """
        Given that all users with equal points should be of equal ranking,
        ranking should be calculated by "points class"
        to do this, we use .distinct() to get each unique number of points
        ie, each "points class". then, the ranking of each points class
        can be evaluated by counting the number of classes with more points
        plus 1, so that the top position is "1st" not "0th".
        """
        return (
            User.objects.filter(hide_leaderboard=False, is_staff=False)
            .values("points")
            .distinct()
            .filter(points__gt=self.points)
            .count()
            + 1
        )
