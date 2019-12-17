from django.db import models
from datetime import date, datetime

def is_available(field):
    return False if ((field is None) or field == "") else True

# Create your models here.
class Audiobook(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150, blank=True)
    narrator = models.CharField(max_length=150, blank=True)
    release_date = models.DateField(verbose_name='date of release', blank=True, null=True)

    def __str__(self):
        audiobook_str = f"{self.title}"
        audiobook_str += f" by {self.author}" if is_available(self.author) else ""
        audiobook_str += f" narrated by {self.narrator}" if is_available(self.narrator) else ""
        audiobook_str += f" release date {self.format_date()}" if is_available(self.release_date) else ""
        return audiobook_str

    def format_date(self):
        return date.strftime(self.release_date, "%b %d, %Y")


class Review(models.Model):
    RATING_OPTIONS = [(1, '1 star'), (2, '2 stars'),
                      (3, '3 stars'), (4, '4 stars'),
                      (5, '5 stars'), (0, 'undecided')]
    rating = models.IntegerField(choices=RATING_OPTIONS, blank=True, default=0)
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    audiobook = models.ForeignKey(to=Audiobook, on_delete=models.CASCADE, null=True)

    def __str__(self):
        review_str = f"rating: {self.get_rating_display()}"
        review_str += f" comment: {self.comment}" if is_available(self.comment) else ""
        review_str += f" added {self.format_timestamp()}"
        return review_str

    def format_timestamp(self):
        return datetime.strftime(self.timestamp, "%d-%m-%Y %H:%M:%S")
