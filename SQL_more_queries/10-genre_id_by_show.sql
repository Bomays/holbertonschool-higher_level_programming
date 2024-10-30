#!/bin/bash
-- 10-genre_id_by_show.sql
-- Script that list all shows contained in the database hbtn_0d_tvshows

USE `hbtn_0d_tvshows`
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id
