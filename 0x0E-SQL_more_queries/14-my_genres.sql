-- script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter.

SELECT g.name FROM tv_genres g
JOIN tv_show_genres t ON g.id = t.genre_id
JOIN tv_shows s ON s.id = t.show_id
WHERE s.title = "Dexter"
ORDER BY g.name;
