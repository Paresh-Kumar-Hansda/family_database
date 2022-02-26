from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Parent(models.Model):
        name=models.CharField(max_length=200, null=True ,blank=True)
        def __str__(self):
                return self.name



class Person(models.Model):
        VAC=[
             ('covidshield', (
            ('CS1st', 'CS1st'),
            ('CS2nd', 'CS2nd'),("CS3rd","CS3rd"),
            )
          ),
           ('cowaxin', (
            ('CW1st', 'CW1st'),
            ('CW2nd', 'CW2nd'),("CW3rd","CW3rd"),
          )
          ),
           ('unknown', 'Unknown'),
           ]
        name = models.CharField(max_length=200, null=True)
        django_username = models.OneToOneField(User,on_delete= models.SET_NULL,max_length=200,blank=True,  null=True)
        image= models.ImageField(blank=False, upload_to='profile_images',null=False,default='default.jpg')
        father = models.ForeignKey(Parent,on_delete= models.SET_NULL,related_name="beta",max_length=200,blank=True, null=True)
        mother=models.ForeignKey(Parent,on_delete= models.SET_NULL,related_name="child",max_length=200,blank=True, null=True)
        phone = models.CharField(max_length=200, null=True ,blank=True)
        #uida = models.CharField(max_length=200, null=True)
        #pan_no=models.CharField(max_length=200, null=True)
        dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
        #cast = models.CharField(max_length=200, null=True)
        #resident = models.CharField(max_length=200, null=True)
        #voter_id = models.CharField(max_length=200, null=True)
        vaccine=models.CharField(max_length=200,blank=True, null=True, choices=VAC)
        def __str__(self):
                return str(self.django_username)



class Jharsewa(models.Model):
        JHAR=(
                ("resident","resident"),
                ("cast","cast"),
              )
        person = models.ForeignKey(Person, on_delete= models.SET_NULL, null=True)
        #product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
        date_of_issue = models.DateField(auto_now=False, auto_now_add=False, null=True)
        type = models.CharField(max_length=200, null=True, choices=JHAR)
        #cert_type=models.CharField(max_length=200, null=True,choices=JHAR)
        cert_no = models.CharField(max_length=200, null=True)
        token_no=models.CharField(max_length=200, null=True)
        document = models.FileField(upload_to='jhar/',null=True,blank=True)
        def __str__(self):
                return "%s %s" % (self.date_of_issue, self.cert_no)


class Identy(models.Model):
        ID=(("uida","uida"),("pan","pan"),("voter_id","voter_id"),("covid","covid"),)
        person = models.OneToOneField(Person, on_delete= models.SET_NULL, null=True)
        #product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
        #date_of_issue = models.DateField(auto_now=False, auto_now_add=False, null=T>
        id_type = models.CharField(max_length=200, null=True, choices=ID)
        #cert_type=models.CharField(max_length=200, null=True,choices=JHAR)
        cert_no = models.CharField(max_length=200, null=True)
        remark=models.CharField(max_length=200, null=True)
        idcard = models.FileField(upload_to='id/',null=False,blank=False,default='default.jpg')
        def __str__(self):
                return "%s %s" % (self.id_type, self.cert_no)



class Education(models.Model):
        CGPA_PERC=(
                     ("CGPA","CGPA"),
                     ("percentage","percentage"),
                         )
        EXAM=(
                       ("ITI","ITI"),
                       ("10","10"),
                       ("12","12"),
                       ("diploma","diploma"),
                       ("Graduation","Graduation")


                                 )
        BOARD = (
                        ("cbse","cbse"),
                        ("JAC","JAC"),
                        ("skmu","skmu"),
                        ("bbkmu","bbkmu"),
                        ("sbtej","SBTE,Jharkhand"),
                        )

        person = models.ForeignKey(Person, on_delete= models.SET_NULL, null=True)
        #product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
        year_of_pass = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
        board = models.CharField(max_length=200, null=True, choices=BOARD)
        exam_passed = models.CharField(max_length=200, null=True, choices=EXAM)
        admit = models.FileField(upload_to='admit/',null=True,blank=True)
        marksheet = models.FileField(upload_to='marksheet/',null=True,blank=True)
        passing = models.FileField(upload_to='pass/',null=True,blank=True)
        roll_no = models.CharField(max_length=200, null=True)
        cgpa_perc = models.CharField(max_length=200, null=True, choices=CGPA_PERC)
        scored=models.CharField(max_length=200, null=True)
        def __str__(self):
                return "%s %s %s" % (self.year_of_pass, self.scored, self.exam_passed)
