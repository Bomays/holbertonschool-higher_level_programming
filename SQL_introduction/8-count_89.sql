#!/bin/bash
-- 8-count_89.sql
-- Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in MySQL server.

SELECT COUNT(*) FROM `first_table` WHERE `id` = 89;
