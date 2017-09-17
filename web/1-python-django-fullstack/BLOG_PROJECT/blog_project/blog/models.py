from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    """Model definition for Post."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """String representation of Post."""
        return self.title

    def __unicode__(self):
        """Unicode representation of Post."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Post."""
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def publish(self):
        """Set a Post publish date."""
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        """Approve Comments."""
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    """Model definition for Comment."""

    post = models.ForeignKey("blog.Post", related_name="comments")
    author = models.CharField(max_length=128)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """String representation of Comment."""
        return self.text

    def __unicode__(self):
        """Unicode representation of Comment."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Comments."""
        return reverse('blog:post_list')

    def approve(self):
        """Approves a Comment."""
        self.approved_comment = True
        self.save()
