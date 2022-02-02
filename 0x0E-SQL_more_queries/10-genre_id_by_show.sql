-- lists all shows contained in the database hbtn_0d_tvshows.
-- lists all rows of a database that have one column in common.
SELECT tv_shows.title, tv-show_genres.genre_id FROM tv-shows INNER JOIN tv_show_genres ON tv-shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
