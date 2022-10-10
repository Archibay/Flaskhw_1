CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT UNIQUE NOT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  track_length INTEGER NOT NULL
);

INSERT INTO tracks (id, title, artist, genre, track_length)
VALUES
  ('1', 'Sweet Emotion', 'Aerosmith', 'Rock', '240'),
  ('2', 'Kashmir', 'Led Zeppelin', 'Rock', '480'),
  ('3', 'Gimme Shelter', 'The Rolling Stones', 'Rock', '259'),
  ('4', 'Back in Black', 'AC/DC', 'Rock', '248'),
  ('5', "Ain't No Half Steppin", 'Big Daddy Kane', 'Rap', '311'),
  ('6', 'Stan', 'Eminem', 'Rap', '485'),
  ('7', 'I Used to Love H.E.R.', 'Common Sense', 'Rock', '480'),
  ('8', 'Unholy', 'Sam Smith & Kim Petras', 'Pop', '257'),
  ('9', "I Ain't Worried", 'OneRepublic', 'Pop', '140'),
  ('10', "Thriller", 'Michael Jackson', 'Pop', '257');
