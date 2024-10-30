#!/bin/bash
-- 8-cities_of_california_subquery.sql
-- Script that list all cities of California that can be found in database hbtn_0d_usa

USE `hbtn_0d_usa`
SELECT `cities.id`, `cities.name` FROM `cities`, `states`
WHERE `cities.state_id`= states.id AND `states.name` = "California" ORDER BY `cities.id` ASC;
