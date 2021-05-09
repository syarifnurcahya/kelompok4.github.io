-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               10.5.9-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for qc
CREATE DATABASE IF NOT EXISTS `qc` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `qc`;

-- Dumping structure for table qc.delivery_product
CREATE TABLE IF NOT EXISTS `delivery_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table qc.delivery_product: ~4 rows (approximately)
DELETE FROM `delivery_product`;
/*!40000 ALTER TABLE `delivery_product` DISABLE KEYS */;
INSERT INTO `delivery_product` (`id`, `name`, `date`) VALUES
	(1, 'Mobil', 'Rp. 6.000.000'),
	(2, 'Sepeda', 'Rp. 1.000.000'),
	(3, 'Bajaj', 'Rp. 4.000.000'),
	(4, 'Motor', 'Rp. 2.000.000');
/*!40000 ALTER TABLE `delivery_product` ENABLE KEYS */;

-- Dumping structure for table qc.sparepart
CREATE TABLE IF NOT EXISTS `sparepart` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_part` varchar(50) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT current_timestamp(),
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=latin1;

-- Dumping data for table qc.sparepart: ~9 rows (approximately)
DELETE FROM `sparepart`;
/*!40000 ALTER TABLE `sparepart` DISABLE KEYS */;
INSERT INTO `sparepart` (`Id`, `nama_part`, `timestamp`, `status`) VALUES
	(1, 'Sepeda', '2021-05-07 14:57:23', 'Good'),
	(2, 'Bajai', '2021-05-07 14:57:33', 'Good'),
	(3, 'Bajai', '2021-05-07 14:57:43', 'Good'),
	(4, 'Mobil', '2021-05-07 14:57:53', 'Good'),
	(5, 'Bajai', '2021-05-07 14:58:14', 'Good'),
	(6, 'Sepeda', '2021-05-07 14:58:15', 'Not Good'),
	(7, 'Mobil', '2021-05-07 14:58:16', 'Not Good'),
	(8, 'Mobil', '2021-05-07 14:58:17', 'Not Good'),
	(9, 'Mobil', '2021-05-07 14:58:18', 'Good');
/*!40000 ALTER TABLE `sparepart` ENABLE KEYS */;

-- Dumping structure for table qc.user_managemen
CREATE TABLE IF NOT EXISTS `user_managemen` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `Column 5` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;

-- Dumping data for table qc.user_managemen: ~5 rows (approximately)
DELETE FROM `user_managemen`;
/*!40000 ALTER TABLE `user_managemen` DISABLE KEYS */;
INSERT INTO `user_managemen` (`id`, `name`, `email`, `password`, `Column 5`) VALUES
	(1, 'Admin', 'kelompok4@arm2', '$2b$12$9PVAqFfDN7O7R5W9sO9L/.eIZhG4oJ2etVMpTPEIaDkIQ3GPT9NoO', NULL),
	(2, 'Admin', 'kelompok4@arm2adm', '$2b$12$suX0CV6udGq82QdiGCujn.1EGIVFjpcZt919/crZVm8IuHk./lUnu', NULL),
	(40, 'SYARIF MUHAMMAD NUR CAHYA', 'syarifnurcahya@gmail.com', '$2b$12$mT6vuoBdv3EDACFlWr9ZW.MTCx4OZGV7.kF7ylUY8mkQKymx6iQhK', NULL),
	(41, 'SYARIF MUHAMMAD NUR CAHYA', 'syarifnurcahya@gmail.com', '$2b$12$cNv3UeDesvIlmM1ySRr40uW0iC4t4Lf1wM/wD7CbTIMT5kvV774DK', NULL),
	(42, 'SYARIF MUHAMMAD NUR CAHYA', 'syarifnurcahya@gmail.com', '$2b$12$92qVWkONMFMegRHlbLapV.kVl5RrGnx8AWDrEEHVmWXwGTfl/zE4u', NULL);
/*!40000 ALTER TABLE `user_managemen` ENABLE KEYS */;

-- Dumping structure for table qc.validasi_product
CREATE TABLE IF NOT EXISTS `validasi_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `date` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `status` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Dumping data for table qc.validasi_product: ~4 rows (approximately)
DELETE FROM `validasi_product`;
/*!40000 ALTER TABLE `validasi_product` DISABLE KEYS */;
INSERT INTO `validasi_product` (`id`, `name`, `date`, `status`) VALUES
	(1, 'Mobil', '4 Mei 2021', '-'),
	(2, 'Sepeda', '1 mei 2020', '-'),
	(3, 'Bajaj', '2 mei 2021', '-'),
	(4, 'Motor', '10 Mei 2021', '-');
/*!40000 ALTER TABLE `validasi_product` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
