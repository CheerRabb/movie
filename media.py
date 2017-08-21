# Mini-Project: Movies Website


class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_release_date, movie_starring,
                 movie_poster, movie_trailer):
        # initialize instance of class Movie
        self.title = movie_title
        self.release_date = movie_release_date
        self.starring = movie_starring
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
