-- lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT t.title FROM tv_shows t
JOIN tv_show_genres s ON t.id = s.show_id
JOIN tv_genres g ON g.id = s.genre_id
WHERE g.name = "Comedy"
ORDER BY t.title ASC;
