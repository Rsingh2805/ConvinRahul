import datetime, threading, time, hashlib
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import DataModel
from ConvinRahul.settings import LOGGING_FILE

BLOCK_SIZE = 65536


def long_func(instance):
    time.sleep(20)
    file_hash = hashlib.sha256()
    fb = instance.file.read(BLOCK_SIZE)
    while len(fb) > 0:  # While there is still data being read from the file
        file_hash.update(fb)  # Update the hash
        fb = instance.file.read(BLOCK_SIZE)  # Read the next block from the file
    result = file_hash.hexdigest()
    instance.encrypted = result
    instance.save()
    print(result)


@receiver(post_save, sender=DataModel)
def updated_created(sender, instance, **kwargs):
    if instance.tracker.previous('file') is None:
        f = open(LOGGING_FILE, 'a')
        f.write(str(datetime.datetime.now()) + ": DataModel for ID " + str(instance.pk) + " created" + "\n")
        f.close()
        x = threading.Thread(target=long_func, args=(instance,), daemon=True)
        x.start()
    elif instance.tracker.has_changed('file'):
        f = open(LOGGING_FILE, 'a')
        f.write(str(datetime.datetime.now()) + ": File field for ID " + str(instance.pk) + " changed from " +
                instance.tracker.previous('file').name + " to " + instance.file.name + "\n")
        f.close()
        x = threading.Thread(target=long_func, args=(instance, ), daemon=True)
        x.start()
    elif instance.tracker.has_changed('encrypted'):
        f = open(LOGGING_FILE, 'a')
        f.write(str(datetime.datetime.now()) + ": Encrypted field for ID " + str(instance.pk) + " changed from " +
                instance.tracker.previous('encrypted') + " to " + instance.encrypted + "\n")
        f.close()


