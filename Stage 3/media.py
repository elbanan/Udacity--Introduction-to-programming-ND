#import webbrowser from python Library
import webbrowser

class Movie ():
    """
        This class defines the different functions that will be used for each movie
    """


    #This function determines different varibles for each movie item. Each fo these attributes will be an attribute of Movie class itself.
    def __init__(self, video_title, video_duration, movie_genre, movie_rating, movie_year, movie_storyline, movie_image, movie_trailer):
        self.title = video_title
        self.duration = video_duration
        self.genre = movie_genre
        self.rating = movie_rating
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer

    #This function displays the youtube trailer link specified by user in entertainment_center.py into the browser
    def show_movie(self):
        webbrowser.open(self.trailer_youtube_url)
