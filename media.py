import webbrowser

class Movie():
    """ uses the init and the show_traler fucnctions to create instances of movies that will display on webpage with title, storyline, poster art, and a viewable trailer"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

