#!/bin/bash
-- 3-force_name.sql
-- Script that creates the table force_name on MySQL server

CREATE TABLE IF NOT EXISTS `force_name` (`id` INT, `name` VARCHAR (256) NOT NULL)
