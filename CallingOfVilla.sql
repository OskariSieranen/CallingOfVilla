CREATE TABLE Location
(
  Location_id VARCHAR(10) NOT NULL,
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
  Location VARCHAR(10),
  Available BOOLEAN,
  Takeable BOOLEAN,
  Death BOOLEAN,
  Music VARCHAR(40),
  Location_id VARCHAR(10),
  PRIMARY KEY (Object_id),
  FOREIGN KEY (Location_id) REFERENCES Location(Location_id)
);
-- Vaihdettiin passagelocation id 1 ja 2  -> StartLocation, Destination
CREATE TABLE Passage
(
  Direction VARCHAR(10),
  Locknote VARCHAR(40),
  Locked BOOLEAN,
  Death BOOLEAN,
  Music VARCHAR(40),
  StartLocation VARCHAR(10) NOT NULL,
  Destination VARCHAR(10) NOT NULL,
  PRIMARY KEY (StartLocation, Destination),
  FOREIGN KEY (StartLocation) REFERENCES Location(Location_id),
  FOREIGN KEY (Destination) REFERENCES Location(Location_id)
);

