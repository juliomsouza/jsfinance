-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: FINANCAS
-- ------------------------------------------------------
-- Server version	5.7.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CATEGORIAS`
--

DROP TABLE IF EXISTS `CATEGORIAS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CATEGORIAS` (
  `ID_CAT` int(11) NOT NULL AUTO_INCREMENT,
  `DESC_CAT` varchar(100) DEFAULT NULL,
  `OBS_CAT` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`ID_CAT`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CONTAS_PAGAR`
--

DROP TABLE IF EXISTS `CONTAS_PAGAR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CONTAS_PAGAR` (
  `IDCONTA` int(11) NOT NULL AUTO_INCREMENT,
  `ID_CAT` int(11) DEFAULT NULL,
  `VALOR` double(10,2) DEFAULT NULL,
  `DATA_COMPRA` date DEFAULT NULL,
  `DATA_VENCIMENTO` date DEFAULT NULL,
  `PAGO` enum('SIM','NAO') DEFAULT NULL,
  `DATA_PGTO` date DEFAULT NULL,
  `TIPO_PGTO` varchar(40) DEFAULT NULL,
  `OBS` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`IDCONTA`)
) ENGINE=InnoDB AUTO_INCREMENT=259 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ENTRADAS`
--

DROP TABLE IF EXISTS `ENTRADAS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ENTRADAS` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FONTE_PGTO` varchar(100) DEFAULT NULL,
  `VALOR` decimal(10,2) DEFAULT NULL,
  `DATA_PGTO` date DEFAULT NULL,
  `OBSERVACOES` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `FATURAS`
--

DROP TABLE IF EXISTS `FATURAS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FATURAS` (
  `IDFATURA` int(11) NOT NULL AUTO_INCREMENT,
  `DESC_CARTAO` varchar(50) NOT NULL,
  `VALOR_CARTAO` decimal(10,2) DEFAULT NULL,
  `DATA_VENCIMENTO` date DEFAULT NULL,
  `PAGO` varchar(3) DEFAULT NULL,
  `DATA_PAGAMENTO` date DEFAULT NULL,
  `VALOR_PAGAMENTO` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`IDFATURA`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `TIPO_PAGTO`
--

DROP TABLE IF EXISTS `TIPO_PAGTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_PAGTO` (
  `IDPGTO` int(11) NOT NULL AUTO_INCREMENT,
  `DESC_PGTO` varchar(50) NOT NULL,
  `OBS` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`IDPGTO`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-03 21:27:18
