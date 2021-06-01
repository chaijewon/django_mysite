from django.db import models

# Create your models here.
# 책정보
class Book(models.Model):
    title=models.CharField(max_length=500)
    '''
       VARCHAR2 (VARCHAR) , CLOB(longtext)
       CharField(max_length=10)                   TextField()
    '''
    authors=models.ManyToManyField('Author')
    '''
       N:1 => 저자한명 = 책은 여러개 연결 
    '''
    publisher=models.ForeignKey('Publisher',on_delete=models.CASCADE)
    '''
       Publisher => 특정 출판사를 삭제 => 자동으로 Book도 삭제
    '''
    publication_date=models.DateField()
    '''
       publication_date DATE
       DateField , DateTimeField():댓글,공지
    '''
    def __str__(self):
        return self.title
# 저자정보
class Author(models.Model):
    name=models.CharField(max_length=34)
    salutation=models.CharField(max_length=500)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=100)
    website=models.URLField()
    def __str__(self):
        return self.name
