from django.utils.deconstruct import deconstructible
import time
import datetime

@deconstructible
class UploadDirectory(object):

    def __init__(self, name=None):
        #self.root = "communities/"
        self.name = name

    def __call__(self, instance, filename):
        #community = self.get_community(instance)
        date_directories = time.strftime("%Y/%m/%d")
        new_filename = self.get_filename(filename)
        return "/".join([self.name, date_directories, new_filename])

    def get_filename(self, filename):
        slug = filename.split(".")[-1]
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + "." + slug



    # doesnt work because the community is not set on the instance by new creations
    def get_community(self, instance):
        if self.name in ["sermons"]:
            return str(instance.serie.community.id)
        elif self.name in ["creations"]:
            return str(instance.group.community.id)
        elif self.name in ["groups"]:
            return str(instance.community.id)
        elif self.name in ["profiles"]:
            # Warning: if multiple communities - index [0] should be removed
            t = instance.communities.all()
            p = t[0].id
            return str(instance.communities.all().first().id)
        return "failDirectory"
