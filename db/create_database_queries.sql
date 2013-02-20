CREATE DATABASE stocrates COLLATE=utf8_general_ci;

USE stocrates;

CREATE TABLE analyst (
	id BIGINT(20) AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50) NULL, 
	last_name VARCHAR(50) NULL,
	description VARCHAR(255) NULL,
	firm VARCHAR(100) NULL,
	revenue_under_mgmt DECIMAL(20,5) NULL,
	confidence_factor DECIMAL(20,5) NOT NULL DEFAULT 0,
	insert_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE forecast (
	id BIGINT(20) AUTO_INCREMENT PRIMARY KEY,
	analyst_id BIGINT(20) NULL,
	source VARCHAR(100) NULL,
	stock_symbol VARCHAR(10) NOT NULL,
	price_at_forecast DECIMAL(20,5) NOT NULL,
	date_of_forecast DATETIME NOT NULL,
	forecasted_price DECIMAL(20,5) NOT NULL,
	forecasted_date DATETIME NOT NULL,
	is_forecast_calculated INT(1) NOT NULL,
	insert_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	CONSTRAINT fk_analyst FOREIGN KEY fk_analyst (analyst_id) REFERENCES stocrates.analyst (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
	INDEX i_stock_symbol (stock_symbol ASC)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE forecast_result (
	id BIGINT(20) AUTO_INCREMENT PRIMARY KEY,
	forecast_id BIGINT(20) NULL,
	INDEX (forecast_id ASC),
	actual_price DECIMAL(20,5) NOT NULL,
	score DECIMAL(20,5) NOT NULL,
	insert_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	CONSTRAINT fk_forecast FOREIGN KEY fk_forecast (forecast_id) REFERENCES stocrates.forecast (id) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX i_score (score ASC)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

--Show the table structure
SHOW TABLE STATUS LIKE 'table_name'\G;

--Show the table column structure
DESCRIBE table_name;