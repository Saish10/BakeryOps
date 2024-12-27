"""
User utils
"""
import logging
from .models import UserAccount
from base.models import Country, State
logger = logging.getLogger(__name__)

class UserManager:
    """
    User manager
    """
    def __init__(self, request):
        self.request = request

    def get_all_users(self):
        """
        Get all users
        """
        try:
            users = UserAccount.objects.all().order_by("-created_at")
            return users
        except Exception as e:
            logger.error("Error getting users: %s", e, exc_info=True)
            return []

    def get_user(self, internal_id):
        """
        Get user
        """
        try:
            user = UserAccount.objects.get(internal_id=internal_id)
            return user
        except Exception as e:
            logger.error("Error getting user: %s", e, exc_info=True)
            return None

    def update_user(self, internal_id, **kwargs):
        """
        Update user
        """
        try:
            user = self.get_user(internal_id)
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save()
            return user
        except Exception as e:
            logger.error("Error updating user: %s", e, exc_info=True)
            return None

    def delete_user(self, internal_id):
        """
        Delete user
        """
        try:
            user = self.get_user(internal_id)
            user.delete()
            return True
        except Exception as e:
            logger.error("Error deleting user: %s", e, exc_info=True)
            return False

    def signup(self, **data):
        """
        Create user
        """
        try:
            if data.get('country'):
                country = data.get('country')
                data['country'] = Country.objects.get(id=country)
            if data.get('state'):
                state = data.get('state')
                data['state'] = State.objects.get(id=state)
            user = UserAccount.objects.create_user(**data)
            return user
        except Exception as e:
            logger.error("Error creating user: %s", e, exc_info=True)
            return None