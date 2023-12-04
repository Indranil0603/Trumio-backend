from mongoengine import *

class CoursesUdemy(Document):
    meta = {'collection': 'CoursesUdemy'}
    course_id = StringField( )
    url = StringField()
    title = StringField()
    is_paid = BooleanField()
    instructors = StringField()
    image_480x270 = StringField()
    published_title  = StringField()
    headline = StringField()
    num_subscribers = LongField()
    avg_rating = FloatField()
    avg_rating_recent = FloatField()    
    rating = FloatField()
    num_reviews = LongField()
    num_published_lectures = IntField()
    num_published_practice_tests = IntField()
    has_closed_caption = BooleanField()
    created_at = StringField()
    # "2015-10-30T15:09:33Z"
    instructional_level = StringField()
    published_at = StringField()
    # "2015-11-10T22:18:22Z"
    objectives_summary = StringField()
    is_recently_published = BooleanField()
    last_update_date = StringField()
    # "2017-06-14"
    content_info = StringField()
    category = StringField()

