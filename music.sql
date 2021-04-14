CREATE TABLE artists (
  `fname` VARCHAR(45) NOT NULL,
  `lname` VARCHAR(45) NULL,
  PRIMARY KEY (`fname`));
  
CREATE TABLE albums (
  `album_name` VARCHAR(50) NOT NULL,
  `artist` VARCHAR(45) NULL,
  PRIMARY KEY (`album_name`));
  
  CREATE TABLE songs (
  `album_name` VARCHAR(50) NOT NULL,
  `song_name` VARCHAR(45) NULL,
  `track_number` INT NULL,
  `track_length` INT NULL,
  PRIMARY KEY (`album_name`));
