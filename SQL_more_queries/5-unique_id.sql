#!/bin/bash
-- 5-unique_id.sql
-- Script that creates the table unique_id on MySQL server

CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT AUTO_INCREMENT PRIMARY KEY , `name` VARCHAR (256) NOT NULL)
