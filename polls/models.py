import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # was_published_recently의 출력 모양 변경위해 다음의 모델 코드를 추가함
    # 원칙적으로 임의의 메서드에 의한 값을 정렬일 불가능합니다. 대신 다른 값을 기준으로 정렬할 수 있는데 이 기준 항목을 설정하는 항목입니다.
    was_published_recently.admin_order_field = 'pub_date'
    # 값이 불리언 값 형태인지 설정합니다. True로 설정하면 값 대신 아이콘이 나타납니다.
    was_published_recently.boolean = True
    # 항목의 헤더 이름을 설정합니다.
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
