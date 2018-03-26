from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    tags = models.ManyToManyField('blog.Tag')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class About(models.Model):
    about = models.CharField(max_length=150)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    comment_date = models.DateTimeField()

    def comment(self):
        self.comment_date = timezone.now()
        self.save()

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.name

# class bir nesne tanımladığımızı belirten bir anahtar kelimedir.
# Post modelimizin ismi. Başka bir isim de verebilirdik (yeter ki özel karakterler ve boşluk kullanmayalım). Class isimleri her zaman büyük harf ile başlamalıdır.
# (models.Model) Post'un bir Django Modeli olduğunu belirtir, bu şekilde Django onu veritabanında tutması gerektiğini bilir.
# models.CharField - belirli bir uzunluktaki metinleri tanımlamak için kullanılır.
# models.TextField - bu da uzun metinleri tanımlar. Blog gönderileri için biçilmiş kaftan, değil mi?
# models.DateTimeField - bu da gün ve saati tanımlamada kullanılır.
# models.ForeignKey - başka bir modele referans tanımlar.
# Yöntemler çoğu kez bir şeylere return. __str__ yönteminde bunun bir örneği vardır. Bu durumda __str__()'yi çağırdığımız zaman gönderi başlığı olan bir metin (string) elde ederiz.



