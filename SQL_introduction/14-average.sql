#!/bin/bash
-- 14-average.sql
-- Script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in MySQL

SELECT AVG(score) AS average FROM second_table;
