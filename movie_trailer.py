import fresh_tomatoes

class Movie(object):
  """Contains basic attributes for a movie trailer."""
  def __init__(self, title, image_url, video_url):
    self.trailer_youtube_url = video_url
    self.title = title
    self.poster_image_url = image_url

# A list of movies to show on the page.
movies = [
   Movie(
       title='The Intern',
       video_url='https://www.youtube.com/watch?v=ZU3Xban0Y6A',
       image_url='http://ia.media-imdb.com/images/M/MV5BMTUyNjE5NjI5OF5BMl5BanBnXkFtZTgwNzYzMzU3NjE@._V1_SX300.jpg'),
   Movie(
       title='The Martian',
       video_url='https://www.youtube.com/watch?v=ej3ioOneTy8',
       image_url='http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SX300.jpg'),
   Movie(
       title='Batman v Superman Dawn of Justice',
       video_url='https://www.youtube.com/watch?v=T89tvJTCohA',
       image_url='http://ia.media-imdb.com/images/M/MV5BMTUyMTIxNzE1M15BMl5BanBnXkFtZTgwOTU0ODQ4MTE@._V1_SX300.jpg')
]

fresh_tomatoes.open_movies_page(movies)
