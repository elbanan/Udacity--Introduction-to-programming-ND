# import media from python library
import media

# import fresh_tomatoes form our current directory
import fresh_tomatoes




music_lyrics = media.Movie("Music & Lyrics",
                            95, "Romance", "PG-13", 2007,
                            "A washed up singer is given a couple days to compose a chart-topping hit for an aspiring teen sensation." + \
                            " Though he's never written a decent lyric in his life, he sparks with an offbeat younger woman with a flair for words.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d3/Music_and_lyrics.jpg",
                            "https://www.youtube.com/watch?v=4C6sSZlVKZE")



first_50 = media.Movie("50 First Dates",
                            99, "Romance", "PG-13", 2004,
                            "Henry Roth is a man afraid of commitment up until he meets the beautiful Lucy." + \
                            "They hit it off and Henry think he's finally found the girl of his dreams, until he discovers she has short-term memory loss and forgets him the very next day.",
                            "https://upload.wikimedia.org/wikipedia/en/9/9d/50FirstDates.jpg",
                            "https://www.youtube.com/watch?v=BCGziZVA7sA")


avatar = media.Movie("Avatar",
                            162, "Action", "PG-13", 2009,
                            "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                            "https://www.youtube.com/watch?v=5PSNL1qE6VY")




argo = media.Movie("Argo",
                            120, "Drama", "R", 2012,
                            "Acting under the cover of a Hollywood producer scouting a location for a science fiction film, " + \
                            "a CIA agent launches a dangerous operation to rescue six Americans in Tehran during the U.S. hostage crisis in Iran in 1980.",
                            "https://upload.wikimedia.org/wikipedia/en/e/e1/Argo2012Poster.jpg",
                            "https://www.youtube.com/watch?v=w918Eh3fij0")




eat_pray = media.Movie("Eat, Pray, Love",
                            133, "Drama", "PG-13", 2010,
                            "A married woman realizes how unhappy her marriage really is, and that her life needs to go in a different direction." +\
                            " After a painful divorce, she takes off on a round-the-world journey to 'find herself'.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7e/Eat_pray_love_ver2.jpg",
                            "https://www.youtube.com/watch?v=mjay5vgIwt4")


martian = media.Movie("The Martian",
                            144, "Sci-Fi", "PG-13", 2015,
                            "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew." +\
                            " But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive.",
                            "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                            "https://www.youtube.com/watch?v=ej3ioOneTy8")


blind_side = media.Movie("The Blind Side",
                            129, "Drama", "PG-13", 2009,
                            "The story of Michael Oher, a homeless and traumatized boy who became an All American football player " +\
                            "and first round NFL draft pick with the help of a caring woman and her family.",
                            "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
                            "https://www.youtube.com/watch?v=gvqj_Tk_kuM")



# this list defines a list of the movie titles that will be displayed in our webpage.
movies = [music_lyrics, first_50, avatar, argo, eat_pray, martian, blind_side]

# here we recall the function open_movies_page from fresh_tomatoes to view a list of the movies defined in list "movies" above as a wabpage.
fresh_tomatoes.open_movies_page(movies)
