import media
import fresh_tomatoes
#toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

#avatar = media.Movie("Avatar", "A marine on an alien planet", "Avatar Poster Link","https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print (avatar.storyline)
#avatar.show_trailer()

shogun_assassin = media.Movie("Shogun Assassin", "A Samurai Warrior and his son flee the Emperor's assassination attempts", "https://img.discogs.com/itzaax05G4EOmQQ3vAlM4b0-Zlw=/fit-in/590x587/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-2226989-1270991277.jpeg.jpg", "https://www.youtube.com/watch?v=bFOjbAQmIjY") 
#shogun_assassin.show_trailer()
#print (shogun_assassin.storyline)

tombstone = media.Movie("Tombstone", "A sheriff and his brothers try to clean up a town", "http://img.moviepostershop.com/tombstone-movie-poster-1993-1010259614.jpg", "https://www.youtube.com/watch?v=0JjRoh13vzY")

blade = media.Movie("Blade", "A half-man half-vampire called a 'daywalker' tries to avenge his mother's death", "http://www.impawards.com/2004/posters/blade_trinity.jpg", "https://www.youtube.com/watch?v=kaU2A7KyOu4")

the_long_kiss_goodnight = media.Movie("The Long Kiss Goodnight", "A story of ex spie who slowly finds out her past", "https://fanart.tv/fanart/movies/11412/movieposter/the-long-kiss-goodnight-555657e210f18.jpg", "https://www.youtube.com/watch?v=nm2QHKByRQQ")

a_knights_tale = media.Movie("A Knight's Tale", "Story of a commoner who pretends to be of royal blood so he can enter jousts", "https://s-media-cache-ak0.pinimg.com/originals/33/08/34/33083498b1b305db6e818d31dfa9fa41.jpg", "https://www.youtube.com/watch?v=zH6U5y086hw")

bladerunner = media.Movie("Bladerunner", "A futeristic story of androids who go renegade when they have reached the end of their existence", "http://www.impawards.com/1982/posters/blade_runner_xlg.jpg", "https://www.youtube.com/watch?v=hiH4hxhKBmY")

movies = [shogun_assassin, tombstone, blade, the_long_kiss_goodnight, a_knights_tale, bladerunner]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.__name__)
#print (media.Movie.__module__)
