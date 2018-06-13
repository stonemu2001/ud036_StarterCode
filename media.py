# Video class
class Video:
    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline


# Movie class inherits Video class, which intinialize
# the Video instance and assign the moveie trailer and
# image url
class Movie(Video):
    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, storyline)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
