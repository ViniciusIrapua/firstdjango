CREATE TABLE news (
    nw_id INT PRIMARY KEY AUTO_INCREMENT,
    nw_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nw_author VARCHAR(127),
    nw_title VARCHAR(127),
    nw_resume VARCHAR(255),
    nw_complete TEXT,
    nw_views INT,
    nw_status ENUM('on', 'off') DEFAULT 'on'
);

CREATE TABLE contact (
    ct_id INT PRIMARY KEY AUTO_INCREMENT,
    ct_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ct_name VARCHAR(127) NOT NULL,
    ct_email VARCHAR(127) NOT NULL,
    ct_subject VARCHAR(127) NOT NULL,
    ct_message TEXT NOT NULL,
    ct_status ENUM('received', 'readed', 'responded', 'deleted') DEFAULT 'received'
);