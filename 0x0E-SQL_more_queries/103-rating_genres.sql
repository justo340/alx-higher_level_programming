-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genre.name - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command


SELECT tv_genre.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genre
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
