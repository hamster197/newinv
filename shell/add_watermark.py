from crm.models import flat_obj_gal

for pict in flat_obj_gal.objects.all():
    pict.save_water()