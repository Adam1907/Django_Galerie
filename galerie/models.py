from django.db import models
from django.urls import reverse


def attachment_path(instance, filename):
    return "picture/" + str(instance.painting.id) + "/attachments/" +filename

def picture_path(instance, filename):
    return "painting/" + str(instance.id)+filename

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Jmeno autora",
help_text='Zadejte jmeno autora:')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Painting(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    year = models.IntegerField(blank=True, null=True, help_text="Zadejte rok vzniku:",verbose_name="Year")
    price = models.IntegerField(blank=True, null=True, verbose_name="Price")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to=picture_path, blank=True, null=True, verbose_name="Picture")


    class Meta:
        ordering = ["-year","name"]

    def __str__(self):
        return f"{self.name} ({self.year})"

    def get_absolute_url(self):
        return reverse("painting-detail", args=[str(self.id)])


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")

    last_update = models.DateTimeField(auto_now=True)

    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )

    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True,
            default='image', help_text='Select allowed attachment type',
            verbose_name="Attachment type")

    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)

    class Meta:
        ordering = ["type", "-last_update"]


    def __str__(self):
        return f"{self.title}, ({self.type})"

