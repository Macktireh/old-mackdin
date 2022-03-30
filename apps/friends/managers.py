from django.db import models


class RelationshipManager(models.Manager):
    def invatation_received(self, receiver):
        """
        Args:
            receiver : invitation reçu
        Returns:
            cette méthode renvoie tout les profiles dans lequel tu as reçu une invitation
        """
        from apps.friends.models import Relationship
        
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs