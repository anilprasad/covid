import itertools

from django.utils.text import slugify
from django.contrib.gis.db import models


class SlugableModel(models.Model):
    class Meta:
        abstract = True

    def generate_slug(self):
        if hasattr(self, 'slug') and hasattr(self, 'name'):
            max_length = self.__class__._meta.get_field('slug').max_length
            self.slug = orig = slugify(self.name)[:max_length]

            for x in itertools.count(1):
                if not self.__class__.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                    break

                # Truncate the original slug dynamically. Minus 1 for the hyphen.
                self.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

    def save(self, *args, **kwargs):
        # if self._state.adding:
        self.generate_slug()

        super(SlugableModel, self).save(*args, **kwargs)
