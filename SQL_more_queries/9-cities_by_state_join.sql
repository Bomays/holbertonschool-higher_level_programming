#!/bin/bash
-- 9-cities_by_state_join.sql
-- Script that list all cities contained in the database hbtn_0d_usa

SELECT cities.id,
cities.name AS name,
states.name AS name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
