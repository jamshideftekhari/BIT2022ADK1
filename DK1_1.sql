-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Dk1_2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Dk1_2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Dk1_2` DEFAULT CHARACTER SET utf8 ;
USE `Dk1_2` ;

-- -----------------------------------------------------
-- Table `Dk1_2`.`Chips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dk1_2`.`Chips` (
  `ChipsId` INT NOT NULL AUTO_INCREMENT,
  `Type` VARCHAR(45) NOT NULL,
  `vendor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ChipsId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dk1_2`.`person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dk1_2`.`person` (
  `PersonId` INT NOT NULL,
  `Fname` VARCHAR(45) NOT NULL,
  `LName` VARCHAR(45) NOT NULL,
  `Age` INT NOT NULL,
  `Chips_ChipsId` INT NOT NULL,
  PRIMARY KEY (`PersonId`),
  INDEX `fk_person_Chips_idx` (`Chips_ChipsId` ASC) VISIBLE,
  CONSTRAINT `fk_person_Chips`
    FOREIGN KEY (`Chips_ChipsId`)
    REFERENCES `Dk1_2`.`Chips` (`ChipsId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
