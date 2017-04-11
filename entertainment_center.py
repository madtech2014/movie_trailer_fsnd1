import media
import fresh_tomatoes

# create Movie class instances by compiling a list of favorite movies
# (title, storyline, link to poster art & link to trailer)

shogun_assassin = media.Movie(
     "Shogun Assassin", "A Samurai Warrior and his son flee the Emperor's\
     assassination attempts",
     "http://images.moviepostershop.com/\
     shogun-assassin-movie-poster-1980-1010466606.jpg",
     "https://www.youtube.com/watch?v=bFOjbAQmIjY")

tombstone = media.Movie(
    "Tombstone", "A sheriff and his brothers try to clean up a town",
    "http://img.moviepostershop.com/\
    tombstone-movie-poster-1993-1010259614.jpg",
    "https://www.youtube.com/watch?v=IPS7xnVh4qk")

blade = media.Movie(
    "Blade", "A half-man half-vampire called a 'daywalker' tries\
    to avenge his mother's death",
    "http://www.impawards.com/2004/posters/blade_trinity.jpg",
    "https://www.youtube.com/watch?v=kaU2A7KyOu4")

the_long_kiss_goodnight = media.Movie(
    "The Long Kiss Goodnight", "A story of ex spie who slowly finds\
    out her past",
    "http://images.moviepostershop.com/\
    the-long-kiss-goodnight-movie-poster-1996-1020190502.jpg",
    "https://www.youtube.com/watch?v=nm2QHKByRQQ")

a_knights_tale = media.Movie(
    "A Knight's Tale", "Story of a commoner who pretends to be\
    of royal blood so he can enter jousts",
    "http://image.tmdb.org/t/p/original/lZlIstMpCxBoMrcPKV4cMX6Nix3.jpg",
    "https://www.youtube.com/watch?v=zH6U5y086hw")

bladerunner = media.Movie(
    "Bladerunner", "A futeristic story of androids who go renegade when\
    they have reached the end of their existence",
    "http://www.impawards.com/1982/posters/blade_runner_xlg.jpg",
    "https://www.youtube.com/watch?v=hiH4hxhKBmY")

# call Movie __init__  & open_movie functions

movies = [shogun_assassin, tombstone, blade, the_long_kiss_goodnight,
          a_knights_tale, bladerunner]
fresh_tomatoes.open_movies_page(movies)


