CREATE TABLE weather (
    id INT NOT NULL AUTO_INCREMENT,
    highest_temperature TINYINT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    wind_speed TINYINT NOT NULL,
    rainfall TINYINT NOT NULL,
    humidity TINYINT NOT NULL,
    PRIMARY KEY(id)
) CHARSET=utf8;

CREATE TABLE heat_level (
    id INT NOT NULL AUTO_INCREMENT,
    temperature_range VARCHAR(20) NOT NULL,
    highest_temperature TINYINT NOT NULL,
    PRIMARY KEY(id)
) CHARSET=utf8;

CREATE TABLE clothes (
    id INT NOT NULL AUTO_INCREMENT,
    clothes_name VARCHAR(20) NOT NULL,
    heat_level_id INT NOT NULL,
    FOREIGN KEY (heat_level_id) REFERENCES heat_level(id),
    PRIMARY KEY(id)
) CHARSET=utf8;
