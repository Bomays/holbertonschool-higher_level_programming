#!/bin/bash
-- 0-privileges.sql
-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the sever in localhost

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
