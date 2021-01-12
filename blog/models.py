from django.db import models
import readtime 
# Create your models here.
class BlogPost(models.Model):
    blog_categories = (
        ('Sport', 'Sport'),
        ('Politics', 'Politics'),
        ('Business', 'Business'),
        ('Health', 'Health'),
        ('Design', 'Design'),
        ('Tech', 'Tech'),
        ('Movies', 'Movies'),
    )
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=True)
    categorie = models.CharField(max_length=30,choices=blog_categories,default='O')
    image = models.CharField(max_length=2040,default='Helloworld.com')
    slug = models.CharField(max_length=240, null=True, blank=False)
    body = models.TextField()
    body_preview = models.TextField(null=False,blank=False,default=" Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure alias, corporis, quod odio repellendus voluptatum aspernatur voluptatem neque consequuntur perspiciatis natus quam id nostrum repellat molestiae itaque exercitationem sunt a. Commodi labore repudiandae debitis et incidunt itaque a dolorum corporis nobis in, non beatae laudantium, magnam, ipsum rem obcaecati fugiat.")
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    published = models.BooleanField(default=True)

    def get_readtime(self):
      result = readtime.of_text(self.body)
      return result.text 

    def __str__(self):
      return self.title
