from django.db import models


class RelationshipManager(models.Manager):
    def import_model(self):
        from apps.friends.models import Relationship
        return Relationship
    
    
    def invatation_received(self, receiver):
        """
        Args:
            receiver : invitation reçu
        Returns:
            cette méthode renvoie tout les profiles dans lequel tu as reçu une invitation
        """
        
        qs = self.import_model().objects.filter(receiver=receiver, status='send')
        return qs


    def invatation_sended(self, sender):
        """
        Args:
            receiver : invitation reçu
        Returns:
            cette méthode renvoie tout les profiles dans lequel tu as envoyer une invitation
        """
        
        qs = self.import_model().objects.filter(sender=sender, status='send')
        return qs