#!/bin/bash
-- 4-first_table.sql
-- Script that creates a table called first_table in the current database of MySQL server.

CREATE TABLE IF NOT EXISTS `first_table` (`id` INT PRIMARY KEY NOT NULL, `name` VARCHAR(256) NOT NULL)
