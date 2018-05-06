DROP TABLE IF EXISTS Passage;
DROP TABLE IF EXISTS Object;
DROP TABLE IF EXISTS Location;

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
INSERT INTO Location VALUES ('PLAYER', 'I have ', '', '');
-- First floor
INSERT INTO Location VALUES ('MAINHALL', ' main hall', 'There are large statue of a man with face hidden by moss. There are also two sets of stairs going to the second floor, the rightmost ones being broken', '');
INSERT INTO Location VALUES ('LIBRARY', ' library', 'There are broken book pieces scattered around room, but some random bits and pieces can still be read from some volumes', '');
INSERT INTO Location VALUES ('TROPHYROOM', ' trophy room', 'There are all kinds of stuffes animals their eyes seem to always one around', '');
INSERT INTO Location VALUES ('DININGHALL', ' dining hall', 'There are large wooden dining table, still set from the last time it was used', '');
INSERT INTO Location VALUES ('KITCHEN', ' kitchen', 'The kitchen looks clean, it was clear that the workers were very organized', '');
INSERT INTO Location VALUES ('SECRETROOM', ' hidden servant*s room', 'There is a large closet with some equipment and table with a deck of cards laying about it. Perhaps the servants of the house used to have their brakes here.', '');

-- Second floor
INSERT INTO Location VALUES ('HALLWAY', ' hallway', 'The hallway is best lit so far, featuring large window owerlooking the decrepit garden', '');
INSERT INTO Location VALUES ('QUESTBEDROOM', ' quest bedroom', 'The guest bedroom is the direct opposite of the master bedroom, having half of the ceiling collapsed on the room, making it unusable for anything', '');
INSERT INTO Location VALUES ('MASTERBEDROOM', ' master bedroom', 'The master bedroom has inexplicably survived, looking how one would expect the house’s lord’s bedroom to look', '');
INSERT INTO Location VALUES ('STUDY', ' study', '', '');
INSERT INTO Location VALUES ('CHILDRENSROOM', ' children*s room', 'The children’s room is at start almost as horrid as the guest bedroom', '');
INSERT INTO Location VALUES ('MIDDLEROOM', ' middle room', 'There are fully broken stairs down', '');
INSERT INTO Location VALUES ('WALKWAYBATH', ' walkway to the bathroom', 'From the window you see the dead garden', '');
INSERT INTO Location VALUES ('BATHROOM', ' bathroom', 'The bathroom has seen better days, looking generally very sticky', '');
INSERT INTO Location VALUES ('NOFLOORROOM1', ' room with minimal amount of floor at the door', '', '');
INSERT INTO Location VALUES ('NOFLOORROOM2', ' room with minimal amount of floor at the door', '', '');
INSERT INTO Location VALUES ('DEATHROOM', 'I DIED', '', '');

-- Attic
INSERT INTO Location VALUES ('ATTIC', ' attic', 'Everything in the attic is covered in dust. In the middle of the room, there is a switch. Illuminating the room is a big round window overlooking the entrance to the house', '');

-- Garden
INSERT INTO Location VALUES ('GARDENENTRANCE', ' garden entrance', 'The garden is in full bloom and looks well kept', '');
INSERT INTO Location VALUES ('GARDENPROPER', ' garden proper', 'It''s dark and moist', '');
INSERT INTO Location VALUES ('TOOLSHED', ' tool shed', 'The shed is small and full of spiders', '');
INSERT INTO Location VALUES ('FOUNTAIN', 'I am near fountain', 'There is giant fountain in front of you', '');

-- Cellar
INSERT INTO Location VALUES ('RIDDLEROOM', ' room full of puzzles', 'wordplay', '');
INSERT INTO Location VALUES ('WELL', ' well', 'There looks to be some light at the bottom of well', '');
INSERT INTO Location VALUES ('THEEND', 'I am in a nice opening of forest', 'I see behind me hidden entrance to the psychiatric hospital and in front of you big forest', '');
INSERT INTO Location VALUES ('EXIT', '', '', '');

-- PASSAGE
-- First floor
INSERT INTO Passage VALUES ('w', '', '', FALSE, FALSE, '', 'MAINHALL', 'LIBRARY');
INSERT INTO Passage VALUES ('e', '', '', FALSE, FALSE, '', 'LIBRARY', 'MAINHALL');
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'LIBRARY', 'TROPHYROOM');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'TROPHYROOM', 'LIBRARY');
INSERT INTO Passage VALUES ('e', '', '', FALSE, FALSE, '', 'MAINHALL', 'DININGHALL');
INSERT INTO Passage VALUES ('w', '', '', FALSE, FALSE, '', 'DININGHALL', 'MAINHALL');
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'DININGHALL', 'KITCHEN');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'KITCHEN', 'DININGHALL');
INSERT INTO Passage VALUES ('w', '', '', FALSE, FALSE, '', 'KITCHEN', 'SECRETROOM');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'SECRETROOM', 'KITCHEN');

INSERT INTO Passage VALUES ('u', 'I can''t go up to the second floor', '', TRUE, FALSE, '', 'MAINHALL', 'MIDDLEROOM');
INSERT INTO Passage VALUES ('d', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'MAINHALL');
INSERT INTO Passage VALUES ('ne', 'I can''t go up to the second floor', '', TRUE, FALSE, '', 'MAINHALL', 'MIDDLEROOM');
INSERT INTO Passage VALUES ('sw', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'MAINHALL');

-- Second floor
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'WALKWAYBATH');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'WALKWAYBATH', 'MIDDLEROOM');
INSERT INTO Passage VALUES ('w', '', '', FALSE, FALSE, '', 'WALKWAYBATH', 'BATHROOM');
INSERT INTO Passage VALUES ('e', '', '', FALSE, FALSE, '', 'BATHROOM', 'WALKWAYBATH');
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'BATHROOM', 'NOFLOORROOM');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'NOFLOORROOM1', 'BATHROOM');
-- death if not go back same way
INSERT INTO Passage VALUES ('n', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM1', 'DEATHROOM');
INSERT INTO Passage VALUES ('e', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM1', 'DEATHROOM');
INSERT INTO Passage VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM1', 'DEATHROOM');

INSERT INTO Passage VALUES ('nw', '', '', FALSE, FALSE, '', 'MAINHALL', 'NOFLOORROOM2');
INSERT INTO Passage VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM2', 'MAINHALL');
INSERT INTO Passage VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM2', 'MAINHALL');
INSERT INTO Passage VALUES ('w', '', 'I died by falling to the first floor', FALSE, TRUE, '', 'NOFLOORROOM2', 'MAINHALL');

INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'MIDDLEROOM', 'HALLWAY');
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'HALLWAY', 'MIDDLEROOM');
INSERT INTO Passage VALUES ('sw', '', '', FALSE, FALSE, '', 'HALLWAY', 'MASTERBEDROOM');
INSERT INTO Passage VALUES ('ne', '', '', FALSE, FALSE, '', 'MASTERBEDROOM', 'HALLWAY');
INSERT INTO Passage VALUES ('nw', '', '', FALSE, FALSE, '', 'HALLWAY', 'QUESTBEDROOM');
INSERT INTO Passage VALUES ('se', '', '', FALSE, FALSE, '', 'QUESTBEDROOM', 'HALLWAY');
INSERT INTO Passage VALUES ('se', '', '', FALSE, FALSE, '', 'HALLWAY', 'CHILDRENSROOM');
INSERT INTO Passage VALUES ('nw', '', '', FALSE, FALSE, '', 'CHILDRENSROOM', 'HALLWAY');
INSERT INTO Passage VALUES ('ne', '', '', FALSE, FALSE, '', 'HALLWAY', 'STUDY');
INSERT INTO Passage VALUES ('sw', '', '', FALSE, FALSE, '', 'STUDY', 'HALLWAY');

-- Attic
INSERT INTO Passage VALUES ('s', 'Attic is locked', '', TRUE, FALSE, '', 'HALLWAY', 'ATTIC');
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'ATTIC', 'HALLWAY');

-- Garden
INSERT INTO Passage VALUES ('n', '', 'A statue fell on you', FALSE, TRUE, '', 'MAINHALL', 'GARDENENTRANCE');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'GARDENENTRANCE', 'MAINHALL');
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'GARDENENTRANCE', 'GARDENPROPER');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'GARDENPROPER', 'GARDENENTRANCE');
INSERT INTO Passage VALUES ('n', '', '', FALSE, FALSE, '', 'GARDENPROPER', 'FOUNTAIN');
INSERT INTO Passage VALUES ('s', '', '', FALSE, FALSE, '', 'FOUNTAIN', 'GARDENPROPER');
INSERT INTO Passage VALUES ('e', '', '', FALSE, FALSE, '', 'GARDENPROPER', 'TOOLSHED');
INSERT INTO Passage VALUES ('w', '', '', FALSE, FALSE, '', 'TOOLSHED', 'GARDENPROPER');

-- Cellar
INSERT INTO Passage VALUES ('w', 'The door is locked', '', TRUE, FALSE, '', 'TROPHYROOM', 'RIDDLEROOM');
INSERT INTO Passage VALUES ('e', '', '', FALSE, FALSE, '', 'RIDDLEROOM', 'TROPHYROOM');

INSERT INTO Passage VALUES ('e', 'The door is locked', '', TRUE, FALSE, '', 'RIDDLEROOM', 'WELL');
INSERT INTO Passage VALUES ('w', '', '', FALSE, FALSE, '', 'WELL', 'RIDDLEROOM');

INSERT INTO Passage VALUES ('e', 'I can''t go', '', TRUE, FALSE, '', 'WELL', 'THEEND');


-- OBJECT
-- All objects
INSERT INTO Object VALUES ('LADDER', 'Old ladder', 'ladder', 'Old used wooden ladder', 'SECRETROOM', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('STUDYKEY', 'Key to the study', 'key', 'Beatifully engraved iron key', 'DININGHALL', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('MANIFEST', 'Worn manifest', 'manifest', '', 'STUDY', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('BIOGRAPHY', '', 'biography', '', 'LIBRARY', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('ATTICKEY', 'Key to the attic', 'key', 'Old sturdy iron key', 'LIBRARY', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('LAMP', 'Rusty oil lamp', 'lamp', 'Rusty oil lamp with small amount of oil inside', 'CHILDRENSROOM', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('CLOTHES', 'Old clothes to wear', 'clothes', 'Old and darkish worn out clothes', 'CHILDRENSROOM', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('GLIMMER', 'Key to the cellar', 'glimmer', 'Glimmering and rusty iron key', 'FOUNTAIN', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('BUCKET', 'Wooden bucket with some rope attached to it', 'bucket', '', 'TOOLSHED', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('ROPE', 'Old rope', 'rope', '', 'TOOLSHED', '', FALSE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('PHONE', 'Old an reliable NOKIA 3310', 'phone', 'NOKIA 3310. Possible to use as a weapon and call after 1 year without charging. Better than a brick', 'WELL', '', FALSE, TRUE, FALSE,'');
INSERT INTO Object VALUES ('FLASHLIGHT', 'Convoy S2+ LED Flashlight ', 'flashlight', '', 'PLAYER', '', TRUE, TRUE, FALSE, '');
INSERT INTO Object VALUES ('FOOD', '', 'food', 'A traditional braised beef stew with thick, rich gravy. It looks so fresh..', 'KITCHEN', '', TRUE, FALSE, TRUE, '');
INSERT INTO Object VALUES ('NEWSPAPER', '', 'newspaper', 'May 19th, 1874. A small child was the only one who survived a terrible fire in Lottersbyck Mansion. The child is badly traumatized..', 'STUDY', '', TRUE, FALSE, TRUE, '');
INSERT INTO Object VALUES ('PILLOW', 'A Soft white pillow', 'pillow', '', 'MASTERBEDROOM', '', TRUE, FALSE, TRUE, '');
INSERT INTO Object VALUES ('CAMERA', 'A small camera, much like my own', 'camera', '', 'WELL', '', FALSE, FALSE, FALSE, '');
