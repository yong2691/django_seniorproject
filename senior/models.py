from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Qna(TimestampedModel):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=20) #이건 나중에 로그인하면 자동으로 들어갈 수 있도록 한다.
    desc = models.TextField()
    picture = models.ImageField()

    def __str__(self) -> str:
        return self.title

class Review(TimestampedModel):
    qna = models.ForeignKey(Qna, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self) -> str:
        return self.message