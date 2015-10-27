import fresh_tomatoes

class Movie(object):
  def __init__(self, title, image_url, video_url):
    self.trailer_youtube_url = video_url
    self.title = title
    self.poster_image_url = image_url

movies = [
   Movie(
       title='The Intern',
       video_url='https://www.youtube.com/watch?v=ZU3Xban0Y6A',
       image_url='http://www.impawards.com/2015/posters/intern_xlg.jpg'),
   Movie(
       title='The Martian',
       video_url='https://www.youtube.com/watch?v=ej3ioOneTy8',
       image_url='https://maggielieu.files.wordpress.com/2015/10/maxresdefault.jpg'),
   Movie(
       title='Batman v Superman Dawn of Justice',
       video_url='https://www.youtube.com/watch?v=T89tvJTCohA',
       image_url='http://masterherald.com/wp-content/uploads/2015/06/Batman-v-Superman-Dawn-of-Justice.jpg')
]

fresh_tomatoes.open_movies_page(movies)
