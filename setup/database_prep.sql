/*
 Assumes you are logged in as root in your local mysql instance.
 Run this before you run the microservice.
 */

CREATE USER 'UniPal'@'localhost' IDENTIFIED BY 'Listing';
CREATE DATABASE UniPal_Listing;
GRANT ALL PRIVILEGES ON UniPal_Listing.* TO 'UniPal'@'localhost';
FLUSH PRIVILEGES;