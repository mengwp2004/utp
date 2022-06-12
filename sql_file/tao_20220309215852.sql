-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tao
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_record`
--

DROP TABLE IF EXISTS `app_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_record` (
  `id` int NOT NULL,
  `userid` int NOT NULL,
  `count` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_record`
--

LOCK TABLES `app_record` WRITE;
/*!40000 ALTER TABLE `app_record` DISABLE KEYS */;
INSERT INTO `app_record` VALUES (1,1,1),(2,2,2);
/*!40000 ALTER TABLE `app_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_student`
--

DROP TABLE IF EXISTS `app_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `age` int NOT NULL,
  `addr` varchar(30) NOT NULL,
  `grade` varchar(30) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `gold` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10024 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_student`
--

LOCK TABLES `app_student` WRITE;
/*!40000 ALTER TABLE `app_student` DISABLE KEYS */;
INSERT INTO `app_student` VALUES (10019,'mengliping','女',20,'山西','3','15822216429',200),(10020,'刘涛','男',18,'天津','三年级','13764172557',500),(10021,'刘涛','男',90,'天津','三年级','13764172559',500),(10022,'刘涛','男',90,'天津','三年级','13764172059',200),(10023,'hah','女',18,'北京','五年级','13803443959',300);
/*!40000 ALTER TABLE `app_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user`
--

DROP TABLE IF EXISTS `app_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user` (
  `id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `passwd` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user`
--

LOCK TABLES `app_user` WRITE;
/*!40000 ALTER TABLE `app_user` DISABLE KEYS */;
INSERT INTO `app_user` VALUES (1,'mengliping','123456');
/*!40000 ALTER TABLE `app_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meng`
--

DROP TABLE IF EXISTS `meng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meng` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` char(20) NOT NULL DEFAULT '',
  `gender` char(1) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meng`
--

LOCK TABLES `meng` WRITE;
/*!40000 ALTER TABLE `meng` DISABLE KEYS */;
INSERT INTO `meng` VALUES (1,'liutao','F'),(2,'甜甜','F'),(3,'mengliping','M');
/*!40000 ALTER TABLE `meng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usering`
--

DROP TABLE IF EXISTS `usering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usering` (
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `failcount` int DEFAULT '0',
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usering`
--

LOCK TABLES `usering` WRITE;
/*!40000 ALTER TABLE `usering` DISABLE KEYS */;
INSERT INTO `usering` VALUES ('liutao','a21655e7ace9bbc670f290c1dc9bbe28',1,'正常'),('geda','d490ecb776cedf701241ef8046634c59',2,'正常'),('haha','5182c8982fed8b28e5a6692e9e6d4a51',0,'正常'),('baba','de574b34e1f5951744d9b172bb2fd3fb',0,'正常'),('疙瘩','d490ecb776cedf701241ef8046634c59',3,'锁定'),('nnnnn','3b1ed1e168f2f0a48b5316e1e813f984',NULL,NULL),('uuu','16d4ec536bcdd91fdb71643ae2440673',0,'正常'),('pppp','55bca73be9bf67952257630507ee1c94',0,'正常'),('zzz','c62f73b7c65525e558334e52a8243ca2',3,'锁定'),('xxx','c62f73b7c65525e558334e52a8243ca2',3,'锁定'),('aaa','c62f73b7c65525e558334e52a8243ca2',1,'正常');
/*!40000 ALTER TABLE `usering` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-09 21:58:52
