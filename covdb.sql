DROP TABLE IF EXISTS PASSAGE;
DROP TABLE IF EXISTS OBJECT;
DROP TABLE IF EXISTS LOCATION;

CREATE TABLE Location
(
  Location_id VARCHAR(15) NOT NULL,
  Description VARCHAR(120),
  Details VARCHAR(1000),
  Music VARCHAR(40),
  PRIMARY KEY (Location_id)
);

CREATE TABLE Object
(
  Object_id VARCHAR(10) NOT NULL,
  Description VARCHAR(40),
  Refname VARCHAR(40),
  Details VARCHAR(1000),
  Location VARCHAR(15),
  Deathnote VARCHAR(100),
  Available BOOLEAN,
  Takeable BOOLEAN,
  Death BOOLEAN,
  Music VARCHAR(40),
  PRIMARY KEY (Object_id),
  FOREIGN KEY (Location) REFERENCES Location(Location_id)
);
-- Vaihdettiin passagelocation id 1 ja 2  -> StartLocation, Destination
CREATE TABLE Passage
(
  Direction VARCHAR(10),
  Locknote VARCHAR(40),
  Deathnote VARCHAR(100),
  Locked BOOLEAN,
  Death BOOLEAN,
  Music VARCHAR(40),
  StartLocation VARCHAR(15) NOT NULL,
  Destination VARCHAR(15) NOT NULL,
  PRIMARY KEY (StartLocation, Destination),
  FOREIGN KEY (StartLocation) REFERENCES Location(Location_id),
  FOREIGN KEY (Destination) REFERENCES Location(Location_id)
);


-- LOCATION
INSERT INTO LOCATION VALUES ('PLAYER', 'I have ', '', '');
-- First floor
INSERT INTO LOCATION VALUES ('MAINHALL', 'I am in the main hall', 'There are large statue of a man with face hidden by moss. There are also two sets of stairs going to the second floor, the rightmost ones being broken', '');
INSERT INTO LOCATION VALUES ('LIBRARY', 'I am in the library', 'There are broken book pieces scattered around room, but some random bits and pieces can still be read from some volumes', '');
INSERT INTO LOCATION VALUES ('TROPHYROOM', 'I am in the trophy room', 'There are all kinds of stuffes animals their eyes seem to always one around', '');
INSERT INTO LOCATION VALUES ('DININGHALL', 'I am in the dining hall', 'There are large wooden dining table, still set from the last time it was used', '');
INSERT INTO LOCATION VALUES ('KITCHEN', 'I am in the kitchen', 'The kitchen looks clean, it was clear that the workers were very organized', '');
INSERT INTO LOCATION VALUES ('SECRETROOM', 'I am in the hidden servant*s room', 'There is a large closet with some equipment and table with a deck of cards laying about it. Perhaps the servants of the house used to have their brakes here.', '');

-- Second floor
INSERT INTO LOCATION VALUES ('HALLWAY', 'I am in the hallway', 'The hallway is best lit so far, featuring large window owerlooking the decrepit garden', '');
INSERT INTO LOCATION VALUES ('QUESTBEDROOM', 'I am in the quest bedroom', 'The guest bedroom is the direct opposite of the master bedroom, having half of the ceiling collapsed on the room, making it unusable for anything', '');
INSERT INTO LOCATION VALUES ('MASTERBEDROOM', 'I am in the master bedroom', 'The master bedroom has inexplicably survived, looking how one would expect the house’s lord’s bedroom to look', '');
INSERT INTO LOCATION VALUES ('STUDY', 'I am in the study', '', '');
INSERT INTO LOCATION VALUES ('CHILDRENSROOM', 'I am in the children*s room', 'The children’s room is at start almost as horrid as the guest bedroom', '');
INSERT INTO LOCATION VALUES ('MIDDLEROOM', 'I am in the middle room', 'There are fully broken stairs down', '');
INSERT INTO LOCATION VALUES ('WALKWAYBATH', 'I am in the walkway to the bathroom', 'From the window you see the dead garden', '');
INSERT INTO LOCATION VALUES ('BATHROOM', 'I am in the bathroom', 'The bathroom has seen better days, looking generally very sticky', '');
INSERT INTO LOCATION VALUES ('NOFLOORROOM1', 'I am in the room with minimal amount of floor at the door', '', '');
INSERT INTO LOCATION VALUES ('NOFLOORROOM2', 'I am in the room with minimal amount of floor at the door', '', '');
INSERT INTO LOCATION VALUES ('DEATHROOM', 'I DIED', '', '');

-- Attic
INSERT INTO LOCATION VALUES ('ATTIC', 'I am in the attic', 'Everything in the attic is covered in dust. In the middle of the room, there is a switch. Illuminating the room is a big round window overlooking the entrance to the house', '');

-- Garden
INSERT INTO LOCATION VALUES ('GARDENENTRANCE', 'I am in the garden entrance', 'The garden is in full bloom and looks well kept', '');
INSERT INTO LOCATION VALUES ('GARDENPROPER', 'I am in the garden proper', 'It''s dark and moist', '');
INSERT INTO LOCATION VALUES ('TOOLSHED', 'I am in the tool shed', 'The shed is small and full of spiders', '');
INSERT INTO LOCATION VALUES ('FOUNTAIN', 'I am near fountain', 'There is giant fountain in front of you', '');

-- Cellar
INSERT INTO LOCATION VALUES ('RIDDLEROOM', 'I am in the room full of puzzles', 'wordplay', '');
INSERT INTO LOCATION VALUES ('WELL', 'I am in the well', 'There looks to be some light at the bottom of well', '');
INSERT INTO LOCATION VALUES ('THEEND', 'I am in a nice opening of forest', 'I see behind me hidden entrance to the psychiatric hospital and in front of you big forest', '');
INSERT INTO LOCATION VALUES ('EXIT', '', '', '');

-- PASSAGE
-- First floor
INSERT INTO PASSAGE VALUES ('w', '', '', FALSE, FALSE, '', 'MAINHALL', 'LIBRARY');
INSERT INTO PASSAGE VALUES ('e', '', '', FALSE, FALSE, '', 'LIBRARY', 'MAINHALL');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'LIBRARY', 'TROPHYROOM');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'TROPHYROOM', 'LIBRARY');
INSERT INTO PASSAGE VALUES ('e', '', '', FALSE, FALSE, '', 'MAINHALL', 'DININGHALL');
INSERT INTO PASSAGE VALUES ('w', '', '', FALSE, FALSE, '', 'DININGHALL', 'MAINHALL');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'DININGHALL', 'KITCHEN');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'KITCHEN', 'DININGHALL');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'KITCHEN', 'SECRETROOM');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'SECRETROOM', 'KITCHEN');

INSERT INTO PASSAGE VALUES ('u', 'I can''t go up to the second floor', '', TRUE, FALSE, '', 'MAINHALL', 'MIDDLEROOM');
INSERT INTO PASSAGE VALUES ('d', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'MAINHALL');
INSERT INTO PASSAGE VALUES ('ne', 'I can''t go up to the second floor', '', TRUE, FALSE, '', 'MAINHALL', 'MIDDLEROOM');
INSERT INTO PASSAGE VALUES ('sw', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'MAINHALL');

-- Second floor
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'WALKWAYBATH');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'WALKWAYBATH', 'MIDDLEROOM');
INSERT INTO PASSAGE VALUES ('w', '', '', FALSE, FALSE, '', 'WALKWAYBATH', 'BATHROOM');
INSERT INTO PASSAGE VALUES ('e', '', '', FALSE, FALSE, '', 'BATHROOM', 'WALKWAYBATH');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'BATHROOM', 'NOFLOORROOM');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'NOFLOORROOM1', 'BATHROOM');
-- death if not go back same way
INSERT INTO PASSAGE VALUES ('n', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM1', 'DEATHROOM');
INSERT INTO PASSAGE VALUES ('e', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM1', 'DEATHROOM');
INSERT INTO PASSAGE VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM1', 'DEATHROOM');

INSERT INTO PASSAGE VALUES ('nw', '', '', FALSE, FALSE, '', 'MAINHALL', 'NOFLOORROOM2');
INSERT INTO PASSAGE VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM2', 'MAINHALL');
INSERT INTO PASSAGE VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM2', 'MAINHALL');
INSERT INTO PASSAGE VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM2', 'MAINHALL');

INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'HALLWAY');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'HALLWAY', 'MIDDLEROOM');
INSERT INTO PASSAGE VALUES ('sw', '', '', FALSE, FALSE, '', 'HALLWAY', 'MASTERBEDROOM');
INSERT INTO PASSAGE VALUES ('ne', '', '', FALSE, FALSE, '', 'MASTERBEDROOM', 'HALLWAY');
INSERT INTO PASSAGE VALUES ('nw', '', '', FALSE, FALSE, '', 'HALLWAY', 'QUESTBEDROOM');
INSERT INTO PASSAGE VALUES ('se', '', '', FALSE, FALSE, '', 'QUESTBEDROOM', 'HALLWAY');
INSERT INTO PASSAGE VALUES ('se', '', '', FALSE, FALSE, '', 'HALLWAY', 'CHILDRENSROOM');
INSERT INTO PASSAGE VALUES ('nw', '', '', FALSE, FALSE, '', 'CHILDRENSROOM', 'HALLWAY');
INSERT INTO PASSAGE VALUES ('ne', '', '', FALSE, FALSE, '', 'HALLWAY', 'STUDY');
INSERT INTO PASSAGE VALUES ('sw', '', '', FALSE, FALSE, '', 'STUDY', 'HALLWAY');

-- Attic
INSERT INTO PASSAGE VALUES ('s', 'Attic is locked', '', TRUE, FALSE, '', 'HALLWAY', 'ATTIC');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'ATTIC', 'HALLWAY');

-- Garden
INSERT INTO PASSAGE VALUES ('n', '', 'You died because of statue fell on you', FALSE, TRUE, '', 'MAINHALL', 'GARDENENTRANCE');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'GARDENENTRANCE', 'MAINHALL');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'GARDENENTRANCE', 'GARDENPROPER');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'GARDENPROPER', 'GARDENENTRANCE');
INSERT INTO PASSAGE VALUES ('n', '', '', FALSE, FALSE, '', 'GARDENPROPER', 'FOUNTAIN');
INSERT INTO PASSAGE VALUES ('s', '', '', FALSE, FALSE, '', 'FOUNTAIN', 'GARDENPROPER');
INSERT INTO PASSAGE VALUES ('e', '', '', FALSE, FALSE, '', 'GARDENPROPER', 'TOOLSHED');
INSERT INTO PASSAGE VALUES ('w', '', '', FALSE, FALSE, '', 'TOOLSHED', 'GARDENPROPER');

-- Cellar
INSERT INTO PASSAGE VALUES ('w', 'The door is locked', '', TRUE, FALSE, '', 'TROPHYROOM', 'RIDDLEROOM');
INSERT INTO PASSAGE VALUES ('e', '', '', FALSE, FALSE, '', 'RIDDLEROOM', 'TROPHYROOM');

INSERT INTO PASSAGE VALUES ('e', 'The door is locked', '', TRUE, FALSE, '', 'RIDDLEROOM', 'WELL');
INSERT INTO PASSAGE VALUES ('w', '', '', FALSE, FALSE, '', 'WELL', 'RIDDLEROOM');

INSERT INTO PASSAGE VALUES ('e', 'I can''t go', '', TRUE, FALSE, '', 'WELL', 'THEEND');


-- OBJECT
-- All objects
INSERT INTO PASSAGE VALUES ('LADDER', 'Old ladder', 'ladder', 'Old used wooden ladder', 'SECRETROOM', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('STUDYKEY', 'Key to the study', 'key', 'Beatifully engraved iron key', 'DININGHALL', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('MANIFEST', 'Worn manifest', 'manifest', '', 'STUDY', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('BIOGRAPHY', '', 'biography', '', 'LIBRARY', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('ATTICKEY', 'Key to the attic', 'key', 'Old sturdy iron key', 'LIBRARY', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('LAMP', 'Rusty oil lamp', 'lamp', 'Rusty oil lamp with small amount of oil inside', 'CHILDRENSROOM', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('CLOTHES', 'Old clothes to wear', 'clothes', 'Old and darkish worn out clothes', 'CHILDRENSROOM', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('GLIMMER', 'Key to the cellar', 'glimmer', 'Glimmering and rusty iron key', 'FOUNTAIN', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('BUCKET', 'Wooden bucket', 'bucket', '', 'TOOLSHED', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('ROPE', 'W', 'rope', '', 'TOOLSHED', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('PHONE', 'Old an reliable NOKIA 3310', 'phone', 'NOKIA 3310. Possible to use as a weapon and call after 1 year without charging. Better than a brick', 'WELL', FALSE, TRUE, FALSE, '');
INSERT INTO PASSAGE VALUES ('FLASHLIGHT', '', 'flashlight', '', 'PLAYER', TRUE, TRUE, FALSE, '');

