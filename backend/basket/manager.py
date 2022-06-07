from django.db.models import Manager


class BasketActivesManager(Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(complete=False)
