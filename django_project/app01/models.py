from django.db import models


# Create your models here.

class User_info(models.Model):
    # 数据库中存1，0
    sex_chiose = ((1, '男'), (0, '女'))
    user_id = models.AutoField(primary_key=True)
    user_account = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_sex = models.CharField(max_length=2, choices=sex_chiose, default=1)
    user_birthday = models.DateField(null=True)
    user_money = models.IntegerField(default=1000)

    def __str__(self):
        return self.user_name


class Lucky_award(models.Model):
    award_id = models.AutoField(primary_key=True)
    award_name = models.CharField(max_length=20)
    award_rate = models.FloatField(default=0.01)

    def __str__(self):
        return self.award_name


class User_stores(models.Model):
    stores_id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey("User_info", on_delete=models.CASCADE, null=True)
    store_name = models.ForeignKey("Lucky_award", on_delete=models.CASCADE, null=True)
    store_num = models.IntegerField(default=0)

    def __str__(self):
        return self.store_id


class Danmu(models.Model):
    danmu_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User_info", on_delete=models.CASCADE, null=True)
    danmu_name = models.CharField(max_length=255)
    danmu_time = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.danmu_id)
