"""
Many-to-many relationships between the same two tables

In this example, a ``Person`` can have many friends, who are also ``Person``
objects. Friendship is a symmetrical relationship - if I am your friend, you
are my friend. Here, ``friends`` is an example of a symmetrical
``ManyToManyField``.

A ``Person`` can also have many idols - but while I may idolize you, you may
not think the same of me. Here, ``idols`` is an example of a non-symmetrical
``ManyToManyField``. Only recursive ``ManyToManyField`` fields may be
non-symmetrical, and they are symmetrical by default.

This test validates that the many-to-many table is created using a mangled name
if there is a name clash, and tests that symmetry is preserved where
appropriate.
"""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django_postgres_extensions.models.fields.related import ArrayManyToManyField


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=20)
    friends = ArrayManyToManyField('self')
    idols = ArrayManyToManyField('self', symmetrical=False, related_name='stalkers')

    def __str__(self):
        return self.name
