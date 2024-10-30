#!/bin/bash
-- 8-cities_of_california_subquery.sql
-- Script that list all cities of California that can be found in database hbtn_0d_usa

USE `hbtn_0d_usa`
SELECT `id`, `name` FROM `cities`
WHERE `cities`.`state_id` = (SELECT `id` FROM `states` WHERE `name` = "California") 
ORDER BY `cities`.`id` ASC;
