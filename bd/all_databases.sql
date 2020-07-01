-- MySQL dump 10.14  Distrib 5.5.64-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: 
-- ------------------------------------------------------
-- Server version	5.5.64-MariaDB

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
-- Current Database: `h9d1v8`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `h9d1v8` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `h9d1v8`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add Арома',1,'add_aroma'),(2,'Can change Арома',1,'change_aroma'),(3,'Can delete Арома',1,'delete_aroma'),(4,'Can view Арома',1,'view_aroma'),(5,'Can add Карта дна',2,'add_bottom_map'),(6,'Can change Карта дна',2,'change_bottom_map'),(7,'Can delete Карта дна',2,'delete_bottom_map'),(8,'Can view Карта дна',2,'view_bottom_map'),(9,'Can add Крючок',3,'add_crochet'),(10,'Can change Крючок',3,'change_crochet'),(11,'Can delete Крючок',3,'delete_crochet'),(12,'Can view Крючок',3,'view_crochet'),(13,'Can add Район',4,'add_district'),(14,'Can change Район',4,'change_district'),(15,'Can delete Район',4,'delete_district'),(16,'Can view Район',4,'view_district'),(17,'Can add Кормоёмкость кормушки',5,'add_feed_capacity'),(18,'Can change Кормоёмкость кормушки',5,'change_feed_capacity'),(19,'Can delete Кормоёмкость кормушки',5,'delete_feed_capacity'),(20,'Can view Кормоёмкость кормушки',5,'view_feed_capacity'),(21,'Can add Рыба',6,'add_fish'),(22,'Can change Рыба',6,'change_fish'),(23,'Can delete Рыба',6,'delete_fish'),(24,'Can view Рыба',6,'view_fish'),(25,'Can add Рыбалка',7,'add_fishing'),(26,'Can change Рыбалка',7,'change_fishing'),(27,'Can delete Рыбалка',7,'delete_fishing'),(28,'Can view Рыбалка',7,'view_fishing'),(29,'Can add Поводок',8,'add_fishing_leash'),(30,'Can change Поводок',8,'change_fishing_leash'),(31,'Can delete Поводок',8,'delete_fishing_leash'),(32,'Can view Поводок',8,'view_fishing_leash'),(33,'Can add Прикормочная смесь',9,'add_fishing_lure'),(34,'Can change Прикормочная смесь',9,'change_fishing_lure'),(35,'Can delete Прикормочная смесь',9,'delete_fishing_lure'),(36,'Can view Прикормочная смесь',9,'view_fishing_lure'),(37,'Can add Монтаж',10,'add_fishing_montage'),(38,'Can change Монтаж',10,'change_fishing_montage'),(39,'Can delete Монтаж',10,'delete_fishing_montage'),(40,'Can view Монтаж',10,'view_fishing_montage'),(41,'Can add Точка ловли',11,'add_fishing_point'),(42,'Can change Точка ловли',11,'change_fishing_point'),(43,'Can delete Точка ловли',11,'delete_fishing_point'),(44,'Can view Точка ловли',11,'view_fishing_point'),(45,'Can add Рыболовная снасть',12,'add_fishing_tackle'),(46,'Can change Рыболовная снасть',12,'change_fishing_tackle'),(47,'Can delete Рыболовная снасть',12,'delete_fishing_tackle'),(48,'Can view Рыболовная снасть',12,'view_fishing_tackle'),(49,'Can add Название модели кормушки',13,'add_model_trough_name'),(50,'Can change Название модели кормушки',13,'change_model_trough_name'),(51,'Can delete Название модели кормушки',13,'delete_model_trough_name'),(52,'Can view Название модели кормушки',13,'view_model_trough_name'),(53,'Can add Наживка/насадка',14,'add_nozzle'),(54,'Can change Наживка/насадка',14,'change_nozzle'),(55,'Can delete Наживка/насадка',14,'delete_nozzle'),(56,'Can view Наживка/насадка',14,'view_nozzle'),(57,'Can add Состояние насадки',15,'add_nozzle_state'),(58,'Can change Состояние насадки',15,'change_nozzle_state'),(59,'Can delete Состояние насадки',15,'delete_nozzle_state'),(60,'Can view Состояние насадки',15,'view_nozzle_state'),(61,'Can add Облачность',16,'add_overcast'),(62,'Can change Облачность',16,'change_overcast'),(63,'Can delete Облачность',16,'delete_overcast'),(64,'Can view Облачность',16,'view_overcast'),(65,'Can add Темп',17,'add_pace'),(66,'Can change Темп',17,'change_pace'),(67,'Can delete Темп',17,'delete_pace'),(68,'Can view Темп',17,'view_pace'),(69,'Can add Покрытие дна',18,'add_priming'),(70,'Can change Покрытие дна',18,'change_priming'),(71,'Can delete Покрытие дна',18,'delete_priming'),(72,'Can view Покрытие дна',18,'view_priming'),(73,'Can add Погодное явление',19,'add_weather_phenomena'),(74,'Can change Погодное явление',19,'change_weather_phenomena'),(75,'Can delete Погодное явление',19,'delete_weather_phenomena'),(76,'Can view Погодное явление',19,'view_weather_phenomena'),(77,'Can add Погода',20,'add_weather'),(78,'Can change Погода',20,'change_weather'),(79,'Can delete Погода',20,'delete_weather'),(80,'Can view Погода',20,'view_weather'),(81,'Can add Водоем',21,'add_water'),(82,'Can change Водоем',21,'change_water'),(83,'Can delete Водоем',21,'delete_water'),(84,'Can view Водоем',21,'view_water'),(85,'Can add Точка карты дна',22,'add_point'),(86,'Can change Точка карты дна',22,'change_point'),(87,'Can delete Точка карты дна',22,'delete_point'),(88,'Can view Точка карты дна',22,'view_point'),(89,'Can add Место рыбалки',23,'add_place'),(90,'Can change Место рыбалки',23,'change_place'),(91,'Can delete Место рыбалки',23,'delete_place'),(92,'Can view Место рыбалки',23,'view_place'),(93,'Can add Модель кормушки',24,'add_model_trough'),(94,'Can change Модель кормушки',24,'change_model_trough'),(95,'Can delete Модель кормушки',24,'delete_model_trough'),(96,'Can view Модель кормушки',24,'view_model_trough'),(97,'Can add Прикорм',25,'add_lure'),(98,'Can change Прикорм',25,'change_lure'),(99,'Can delete Прикорм',25,'delete_lure'),(100,'Can view Прикорм',25,'view_lure'),(101,'Can add Рыболовная кормушка',26,'add_fishing_trough'),(102,'Can change Рыболовная кормушка',26,'change_fishing_trough'),(103,'Can delete Рыболовная кормушка',26,'delete_fishing_trough'),(104,'Can view Рыболовная кормушка',26,'view_fishing_trough'),(105,'Can add Результат рыбалки',27,'add_fishing_result'),(106,'Can change Результат рыбалки',27,'change_fishing_result'),(107,'Can delete Результат рыбалки',27,'delete_fishing_result'),(108,'Can view Результат рыбалки',27,'view_fishing_result'),(109,'Can add Трофейный улов',28,'add_fish_trophy'),(110,'Can change Трофейный улов',28,'change_fish_trophy'),(111,'Can delete Трофейный улов',28,'delete_fish_trophy'),(112,'Can view Трофейный улов',28,'view_fish_trophy'),(113,'Can add log entry',29,'add_logentry'),(114,'Can change log entry',29,'change_logentry'),(115,'Can delete log entry',29,'delete_logentry'),(116,'Can view log entry',29,'view_logentry'),(117,'Can add permission',30,'add_permission'),(118,'Can change permission',30,'change_permission'),(119,'Can delete permission',30,'delete_permission'),(120,'Can view permission',30,'view_permission'),(121,'Can add group',31,'add_group'),(122,'Can change group',31,'change_group'),(123,'Can delete group',31,'delete_group'),(124,'Can view group',31,'view_group'),(125,'Can add user',32,'add_user'),(126,'Can change user',32,'change_user'),(127,'Can delete user',32,'delete_user'),(128,'Can view user',32,'view_user'),(129,'Can add content type',33,'add_contenttype'),(130,'Can change content type',33,'change_contenttype'),(131,'Can delete content type',33,'delete_contenttype'),(132,'Can view content type',33,'view_contenttype'),(133,'Can add session',34,'add_session'),(134,'Can change session',34,'change_session'),(135,'Can delete session',34,'delete_session'),(136,'Can view session',34,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8_bin NOT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$sOaat5fROzPF$eCK1xUHwGRSnEtx3LdmZg1h4OGVPS7VOzCwweg1fFi0=','2020-04-14 17:20:24.269497',1,'admin','','','',1,1,'2020-04-14 17:20:02.764508');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-14 17:20:35.088308','1','Dunaev Scopex',1,'[{\"added\": {}}]',1,1),(2,'2020-04-14 17:20:57.210122','1','Сальский район',1,'[{\"added\": {}}]',4,1),(3,'2020-04-14 17:21:01.859675','1','Сальский район - река Маныч',1,'[{\"added\": {}}]',21,1),(4,'2020-04-14 17:21:38.450190','1','Сальский район - река Маныч',1,'[{\"added\": {}}]',2,1),(5,'2020-04-14 17:21:51.493537','1','Малая',1,'[{\"added\": {}}]',5,1),(6,'2020-04-14 17:21:57.289598','2','Средняя',1,'[{\"added\": {}}]',5,1),(7,'2020-04-14 17:22:02.087494','3','Большая',1,'[{\"added\": {}}]',5,1),(8,'2020-04-14 17:22:17.392649','1','Gamakatsu LS-2283B 12',1,'[{\"added\": {}}]',3,1),(9,'2020-04-14 17:22:55.465404','1','Ил',1,'[{\"added\": {}}]',18,1),(10,'2020-04-14 17:22:58.494620','1','Ил',1,'[{\"added\": {}}]',11,1),(11,'2020-04-14 17:23:00.970108','1','Сальский район - река Маныч: Манычстрой',1,'[{\"added\": {}}]',23,1),(12,'2020-04-14 17:23:17.654599','1','Пуля',1,'[{\"added\": {}}]',13,1),(13,'2020-04-14 17:23:21.001851','1','Пуля пластик',1,'[{\"added\": {}}]',24,1),(14,'2020-04-14 17:23:34.197492','1','Гарднер ',1,'[{\"added\": {}}]',10,1),(15,'2020-04-14 17:23:48.086647','1','Опарыш',1,'[{\"added\": {}}]',14,1),(16,'2020-04-14 17:25:15.599280','1','Переменная облачность',1,'[{\"added\": {}}]',16,1),(17,'2020-04-14 17:25:34.402818','1','леска 0.14 25 см.',1,'[{\"added\": {}}]',8,1),(18,'2020-04-14 17:25:54.734765','1','без явлений',1,'[{\"added\": {}}]',19,1),(19,'2020-04-14 17:26:09.001272','1','Weather object (1)',1,'[{\"added\": {}}]',20,1),(20,'2020-04-14 17:26:55.908070','1','Резанная',1,'[{\"added\": {}}]',15,1),(21,'2020-04-14 17:26:57.563877','1','Fishing_Lure object (1)',1,'[{\"added\": {}}]',9,1),(22,'2020-04-14 17:27:19.554116','1','Lure object (1)',1,'[{\"added\": {}}]',25,1),(23,'2020-04-14 17:29:38.313561','1','Flagman Legend 3.6 100',1,'[{\"added\": {}}]',12,1),(24,'2020-04-14 17:29:56.821650','1','Дядя Вася: Малая Пуля пластик 70гр.',1,'[{\"added\": {}}]',26,1),(25,'2020-04-14 17:30:18.459141','1','Быстрый (до 2 минут)',1,'[{\"added\": {}}]',17,1),(26,'2020-04-14 17:30:21.366440','1','2020-04-14 20:30:21.364459',1,'[{\"added\": {}}]',7,1),(27,'2020-04-14 17:32:12.940401','1','Лещ',1,'[{\"added\": {}}]',6,1),(28,'2020-04-14 17:33:48.930102','1','Лещ: 2шт. 1.2кг.',1,'[{\"added\": {}}]',27,1),(29,'2020-04-14 17:34:28.400097','1','Fish_Trophy object (1)',1,'[{\"added\": {}}]',28,1),(30,'2020-04-14 19:34:11.125674','1','2020-04-14 20:30:21',2,'[]',7,1),(31,'2020-04-14 19:34:41.986930','2','2020-04-01 22:34:18',1,'[{\"added\": {}}]',7,1),(32,'2020-04-16 16:35:20.265556','2','Ясно',1,'[{\"added\": {}}]',16,1),(33,'2020-04-16 16:35:36.955574','3','Малооблачно',1,'[{\"added\": {}}]',16,1),(34,'2020-04-16 18:34:57.691344','2','Трофей: Лещ 1.5кг.',1,'[{\"added\": {}}]',28,1),(35,'2020-04-16 18:35:51.424435','2','Трофей: Лещ 1.5кг.',2,'[{\"changed\": {\"fields\": [\"\\u0412\\u0435\\u0441 \\u0442\\u0440\\u043e\\u0444\\u0435\\u044f\"]}}]',28,1),(36,'2020-04-16 18:39:51.464733','2','Fishing_Lure object (2)',1,'[{\"added\": {}}]',9,1),(37,'2020-04-17 09:20:39.904085','4','Лещ: 2шт. 2кг.',1,'[{\"added\": {}}]',27,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (29,'admin','logentry'),(31,'auth','group'),(30,'auth','permission'),(32,'auth','user'),(33,'contenttypes','contenttype'),(1,'fishing','aroma'),(2,'fishing','bottom_map'),(3,'fishing','crochet'),(4,'fishing','district'),(5,'fishing','feed_capacity'),(6,'fishing','fish'),(28,'fishing','fish_trophy'),(7,'fishing','fishing'),(8,'fishing','fishing_leash'),(9,'fishing','fishing_lure'),(10,'fishing','fishing_montage'),(11,'fishing','fishing_point'),(27,'fishing','fishing_result'),(12,'fishing','fishing_tackle'),(26,'fishing','fishing_trough'),(25,'fishing','lure'),(24,'fishing','model_trough'),(13,'fishing','model_trough_name'),(14,'fishing','nozzle'),(15,'fishing','nozzle_state'),(16,'fishing','overcast'),(17,'fishing','pace'),(23,'fishing','place'),(22,'fishing','point'),(18,'fishing','priming'),(21,'fishing','water'),(20,'fishing','weather'),(19,'fishing','weather_phenomena'),(34,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-14 17:19:38.215545'),(2,'auth','0001_initial','2020-04-14 17:19:38.535963'),(3,'admin','0001_initial','2020-04-14 17:19:39.833614'),(4,'admin','0002_logentry_remove_auto_add','2020-04-14 17:19:40.194280'),(5,'admin','0003_logentry_add_action_flag_choices','2020-04-14 17:19:40.236668'),(6,'contenttypes','0002_remove_content_type_name','2020-04-14 17:19:40.456002'),(7,'auth','0002_alter_permission_name_max_length','2020-04-14 17:19:40.559478'),(8,'auth','0003_alter_user_email_max_length','2020-04-14 17:19:40.676590'),(9,'auth','0004_alter_user_username_opts','2020-04-14 17:19:40.699817'),(10,'auth','0005_alter_user_last_login_null','2020-04-14 17:19:40.819013'),(11,'auth','0006_require_contenttypes_0002','2020-04-14 17:19:40.830800'),(12,'auth','0007_alter_validators_add_error_messages','2020-04-14 17:19:40.869019'),(13,'auth','0008_alter_user_username_max_length','2020-04-14 17:19:41.017500'),(14,'auth','0009_alter_user_last_name_max_length','2020-04-14 17:19:41.127146'),(15,'auth','0010_alter_group_name_max_length','2020-04-14 17:19:41.230239'),(16,'auth','0011_update_proxy_permissions','2020-04-14 17:19:41.268731'),(17,'fishing','0001_initial','2020-04-14 17:19:44.618105'),(18,'sessions','0001_initial','2020-04-14 17:19:46.303000'),(19,'fishing','0002_auto_20200414_2024','2020-04-14 17:24:54.431178'),(20,'fishing','0003_auto_20200414_2036','2020-04-14 17:36:47.930184'),(21,'fishing','0004_auto_20200416_2126','2020-04-16 18:26:52.235608'),(22,'fishing','0005_auto_20200416_2135','2020-04-16 18:35:42.590365');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gto1rlukfo0rlrpvw6qh04p2awoerhdu','MGE5ZTBhMmViMWIwNDFlZmJhY2YxMTNjZjEyODJhMTBjM2MwZDhmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNDQxYTg1MzU2ODViNGQ1ZDMyZTA3YjI4MzE5YWE4YzUwMTJhYzc5In0=','2020-04-28 17:20:24.290798');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_aroma`
--

DROP TABLE IF EXISTS `fishing_aroma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_aroma` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aroma_manufacturer` varchar(100) COLLATE utf8_bin NOT NULL,
  `aroma_name` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_aroma`
--

LOCK TABLES `fishing_aroma` WRITE;
/*!40000 ALTER TABLE `fishing_aroma` DISABLE KEYS */;
INSERT INTO `fishing_aroma` VALUES (1,'Dunaev','Scopex');
/*!40000 ALTER TABLE `fishing_aroma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_bottom_map`
--

DROP TABLE IF EXISTS `fishing_bottom_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_bottom_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bottom_map_northern_degree` int(11) NOT NULL,
  `bottom_map_northern_minute` int(11) NOT NULL,
  `bottom_map_northern_second` decimal(5,3) NOT NULL,
  `bottom_map_easter_degree` int(11) NOT NULL,
  `bottom_map_easter_minute` int(11) NOT NULL,
  `bottom_map_easter_second` decimal(5,3) NOT NULL,
  `water_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `water_id` (`water_id`),
  CONSTRAINT `fishing_bottom_map_water_id_4dbcd335_fk_fishing_water_id` FOREIGN KEY (`water_id`) REFERENCES `fishing_water` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_bottom_map`
--

LOCK TABLES `fishing_bottom_map` WRITE;
/*!40000 ALTER TABLE `fishing_bottom_map` DISABLE KEYS */;
INSERT INTO `fishing_bottom_map` VALUES (1,46,38,19.000,41,38,11.000,1);
/*!40000 ALTER TABLE `fishing_bottom_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_crochet`
--

DROP TABLE IF EXISTS `fishing_crochet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_crochet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `crochet_manufacturer` varchar(20) COLLATE utf8_bin NOT NULL,
  `crochet_model` varchar(20) COLLATE utf8_bin NOT NULL,
  `crochet_size` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_crochet`
--

LOCK TABLES `fishing_crochet` WRITE;
/*!40000 ALTER TABLE `fishing_crochet` DISABLE KEYS */;
INSERT INTO `fishing_crochet` VALUES (1,'Gamakatsu','LS-2283B',12);
/*!40000 ALTER TABLE `fishing_crochet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_district`
--

DROP TABLE IF EXISTS `fishing_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_district` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `district_name` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_district`
--

LOCK TABLES `fishing_district` WRITE;
/*!40000 ALTER TABLE `fishing_district` DISABLE KEYS */;
INSERT INTO `fishing_district` VALUES (1,'Сальский район');
/*!40000 ALTER TABLE `fishing_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_feed_capacity`
--

DROP TABLE IF EXISTS `fishing_feed_capacity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_feed_capacity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feed_capacity_name` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_feed_capacity`
--

LOCK TABLES `fishing_feed_capacity` WRITE;
/*!40000 ALTER TABLE `fishing_feed_capacity` DISABLE KEYS */;
INSERT INTO `fishing_feed_capacity` VALUES (1,'Малая'),(2,'Средняя'),(3,'Большая');
/*!40000 ALTER TABLE `fishing_feed_capacity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fish`
--

DROP TABLE IF EXISTS `fishing_fish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fish` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_of_fish` varchar(20) COLLATE utf8_bin NOT NULL,
  `fish_description` longtext COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fish`
--

LOCK TABLES `fishing_fish` WRITE;
/*!40000 ALTER TABLE `fishing_fish` DISABLE KEYS */;
INSERT INTO `fishing_fish` VALUES (1,'Лещ','Лещ (молодые особи – подлещики) – рыба семейства карповых, единственный представитель рода лещи. Широко распространен в бассейнах Черного, Азовского, Каспийского, Балтийского и Северного морей. Акклиматизирован в бассейнах некоторых сибирских рек, также встречается в Аральском море.\r\nКарп имеет значительную промысловую ценность и пользуется большой популярностью среди рыболовов-любителей. Ежегодно во всем мире вылавливается более 60 тысяч тонн рыбы этого вида. В море промышленный вылов ведется ставными сетями и ставными неводами, а в реках и озерах для лова лещей используются вентери и неводы.\r\nПо своим вкусовым качествам лещ превосходит большинство других видов речных рыб. В продажу лещ поступает в свежем, мороженом, копченом, вяленом и консервированном виде.\r\n\r\nВнешний вид\r\nЛещ имеет высокое, сплюснутое с боков тело с небольшой головой. Средняя длина составляет около 30-50 сантиметров при массе до 5-6 килограммов, изредка встречаются особи длиной 50-80 сантиметров и весом более 6 килограммов. Окраска леща разнится в зависимости от возраста. Молодые рыбы имеют серебристый окрас, тогда как у взрослых лещей бока золотисто-коричневые, спина серая, а брюхо желтоватое.\r\n\r\nОбраз жизни\r\nЛещ обитает в прудах, озерах, реках и водохранилищах, предпочитая глубокие места с водной растительностью. Держится лещ, как правило, небольшими группами, однако в крупных водоемах и на сильных течениях может собираться в довольно большие стаи. Питается рыба улитками, ракушками, трубочниками и личинками комара, а также растительностью. Для зимовки лещи выбирают глубокие места.\r\n\r\nНерест\r\nПоловой зрелости лещ достигает на третьем-четвертом году жизни в южных регионах и в четыре-пять лет на севере. В зависимости от климатических условий нерест начинается в апреле или в первых числах мая при температуре воды 12-14 градусов. Для икрометания рыба выбирает травянистые отмели.\r\nПлодовитость самок существенно варьируется в соответствии с размерами их тела и может составлять от 92 до 338 тысяч икринок. Личинки из икры выходят через 4-6 суток после икрометания.\r\nРастет лещ медленно, достигая на втором году жизни веса лишь 20-30 граммов. Массу в полкилограмма рыба набирает только в 5-7 лет, при этом максимальная зарегистрированная продолжительность жизни леща составляет 23 года.');
/*!40000 ALTER TABLE `fishing_fish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fish_trophy`
--

DROP TABLE IF EXISTS `fishing_fish_trophy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fish_trophy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fish_trophy_weight` decimal(4,1) NOT NULL,
  `fish_id` int(11) NOT NULL,
  `fishing_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fish_trophy_fish_id_818ecdf2_fk_fishing_fish_id` (`fish_id`),
  KEY `fishing_fish_trophy_fishing_id_d9397629_fk_fishing_fishing_id` (`fishing_id`),
  CONSTRAINT `fishing_fish_trophy_fishing_id_d9397629_fk_fishing_fishing_id` FOREIGN KEY (`fishing_id`) REFERENCES `fishing_fishing` (`id`),
  CONSTRAINT `fishing_fish_trophy_fish_id_818ecdf2_fk_fishing_fish_id` FOREIGN KEY (`fish_id`) REFERENCES `fishing_fish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fish_trophy`
--

LOCK TABLES `fishing_fish_trophy` WRITE;
/*!40000 ALTER TABLE `fishing_fish_trophy` DISABLE KEYS */;
INSERT INTO `fishing_fish_trophy` VALUES (1,1.0,1,1),(2,1.5,1,1);
/*!40000 ALTER TABLE `fishing_fish_trophy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing`
--

DROP TABLE IF EXISTS `fishing_fishing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `aroma_id` int(11) NOT NULL,
  `crochet_id` int(11) NOT NULL,
  `fishing_leash_id` int(11) NOT NULL,
  `fishing_lure_id` int(11) NOT NULL,
  `fishing_montage_id` int(11) NOT NULL,
  `fishing_tackle_id` int(11) NOT NULL,
  `fishing_trough_id` int(11) NOT NULL,
  `nozzle_id` int(11) NOT NULL,
  `pace_id` int(11) NOT NULL,
  `place_id` int(11) NOT NULL,
  `weather_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishing_fishing_leash_id_5f14ca44_fk_fishing_f` (`fishing_leash_id`),
  KEY `fishing_fishing_fishing_lure_id_be36c2ad_fk_fishing_f` (`fishing_lure_id`),
  KEY `fishing_fishing_fishing_montage_id_f4c13924_fk_fishing_f` (`fishing_montage_id`),
  KEY `fishing_fishing_fishing_tackle_id_34854d74_fk_fishing_f` (`fishing_tackle_id`),
  KEY `fishing_fishing_fishing_trough_id_6f0f1cd5_fk_fishing_f` (`fishing_trough_id`),
  KEY `fishing_fishing_nozzle_id_f0856399_fk_fishing_nozzle_id` (`nozzle_id`),
  KEY `fishing_fishing_pace_id_d3d20faa_fk_fishing_pace_id` (`pace_id`),
  KEY `fishing_fishing_place_id_c3a97595_fk_fishing_place_id` (`place_id`),
  KEY `fishing_fishing_weather_id_ac377240_fk_fishing_weather_id` (`weather_id`),
  KEY `fishing_fishing_aroma_id_eb3cee94_fk_fishing_aroma_id` (`aroma_id`),
  KEY `fishing_fishing_crochet_id_477862af_fk_fishing_crochet_id` (`crochet_id`),
  CONSTRAINT `fishing_fishing_aroma_id_eb3cee94_fk_fishing_aroma_id` FOREIGN KEY (`aroma_id`) REFERENCES `fishing_aroma` (`id`),
  CONSTRAINT `fishing_fishing_crochet_id_477862af_fk_fishing_crochet_id` FOREIGN KEY (`crochet_id`) REFERENCES `fishing_crochet` (`id`),
  CONSTRAINT `fishing_fishing_fishing_leash_id_5f14ca44_fk_fishing_f` FOREIGN KEY (`fishing_leash_id`) REFERENCES `fishing_fishing_leash` (`id`),
  CONSTRAINT `fishing_fishing_fishing_lure_id_be36c2ad_fk_fishing_f` FOREIGN KEY (`fishing_lure_id`) REFERENCES `fishing_fishing_lure` (`id`),
  CONSTRAINT `fishing_fishing_fishing_montage_id_f4c13924_fk_fishing_f` FOREIGN KEY (`fishing_montage_id`) REFERENCES `fishing_fishing_montage` (`id`),
  CONSTRAINT `fishing_fishing_fishing_tackle_id_34854d74_fk_fishing_f` FOREIGN KEY (`fishing_tackle_id`) REFERENCES `fishing_fishing_tackle` (`id`),
  CONSTRAINT `fishing_fishing_fishing_trough_id_6f0f1cd5_fk_fishing_f` FOREIGN KEY (`fishing_trough_id`) REFERENCES `fishing_fishing_trough` (`id`),
  CONSTRAINT `fishing_fishing_nozzle_id_f0856399_fk_fishing_nozzle_id` FOREIGN KEY (`nozzle_id`) REFERENCES `fishing_nozzle` (`id`),
  CONSTRAINT `fishing_fishing_pace_id_d3d20faa_fk_fishing_pace_id` FOREIGN KEY (`pace_id`) REFERENCES `fishing_pace` (`id`),
  CONSTRAINT `fishing_fishing_place_id_c3a97595_fk_fishing_place_id` FOREIGN KEY (`place_id`) REFERENCES `fishing_place` (`id`),
  CONSTRAINT `fishing_fishing_weather_id_ac377240_fk_fishing_weather_id` FOREIGN KEY (`weather_id`) REFERENCES `fishing_weather` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing`
--

LOCK TABLES `fishing_fishing` WRITE;
/*!40000 ALTER TABLE `fishing_fishing` DISABLE KEYS */;
INSERT INTO `fishing_fishing` VALUES (1,'2020-04-14','20:30:21.000000',1,1,1,1,1,1,1,1,1,1,1),(2,'2020-04-01','22:34:18.000000',1,1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `fishing_fishing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing_leash`
--

DROP TABLE IF EXISTS `fishing_fishing_leash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing_leash` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_leash_material` varchar(20) COLLATE utf8_bin NOT NULL,
  `fishing_leash_diameter` decimal(4,2) NOT NULL,
  `fishing_leash_length` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing_leash`
--

LOCK TABLES `fishing_fishing_leash` WRITE;
/*!40000 ALTER TABLE `fishing_fishing_leash` DISABLE KEYS */;
INSERT INTO `fishing_fishing_leash` VALUES (1,'леска',0.14,25);
/*!40000 ALTER TABLE `fishing_fishing_leash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing_lure`
--

DROP TABLE IF EXISTS `fishing_fishing_lure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing_lure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nozzle_id` int(11) NOT NULL,
  `nozzle_state_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishing_lure_nozzle_id_c551727c_fk_fishing_nozzle_id` (`nozzle_id`),
  KEY `fishing_fishing_lure_nozzle_state_id_55389326_fk_fishing_n` (`nozzle_state_id`),
  CONSTRAINT `fishing_fishing_lure_nozzle_id_c551727c_fk_fishing_nozzle_id` FOREIGN KEY (`nozzle_id`) REFERENCES `fishing_nozzle` (`id`),
  CONSTRAINT `fishing_fishing_lure_nozzle_state_id_55389326_fk_fishing_n` FOREIGN KEY (`nozzle_state_id`) REFERENCES `fishing_nozzle_state` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing_lure`
--

LOCK TABLES `fishing_fishing_lure` WRITE;
/*!40000 ALTER TABLE `fishing_fishing_lure` DISABLE KEYS */;
INSERT INTO `fishing_fishing_lure` VALUES (1,1,1),(2,1,1);
/*!40000 ALTER TABLE `fishing_fishing_lure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing_montage`
--

DROP TABLE IF EXISTS `fishing_fishing_montage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing_montage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_montage_name` varchar(15) COLLATE utf8_bin NOT NULL,
  `fishing_montage_sliding` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing_montage`
--

LOCK TABLES `fishing_fishing_montage` WRITE;
/*!40000 ALTER TABLE `fishing_fishing_montage` DISABLE KEYS */;
INSERT INTO `fishing_fishing_montage` VALUES (1,'Гарднер',0);
/*!40000 ALTER TABLE `fishing_fishing_montage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing_point`
--

DROP TABLE IF EXISTS `fishing_fishing_point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing_point` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_point_azimuth` int(10) unsigned NOT NULL,
  `fishing_point_distance` int(10) unsigned NOT NULL,
  `fishing_poiny_depth` decimal(4,2) NOT NULL,
  `priming_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishing_point_priming_id_799cbbb7_fk_fishing_priming_id` (`priming_id`),
  CONSTRAINT `fishing_fishing_point_priming_id_799cbbb7_fk_fishing_priming_id` FOREIGN KEY (`priming_id`) REFERENCES `fishing_priming` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing_point`
--

LOCK TABLES `fishing_fishing_point` WRITE;
/*!40000 ALTER TABLE `fishing_fishing_point` DISABLE KEYS */;
INSERT INTO `fishing_fishing_point` VALUES (1,100,42,2.50,1);
/*!40000 ALTER TABLE `fishing_fishing_point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing_result`
--

DROP TABLE IF EXISTS `fishing_fishing_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number_of_fish` int(10) unsigned NOT NULL,
  `fish_weight` decimal(6,1) NOT NULL,
  `fish_id` int(11) NOT NULL,
  `fishing_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishing_result_fish_id_60fb081d_fk_fishing_fish_id` (`fish_id`),
  KEY `fishing_fishing_result_fishing_id_6f62e9b8_fk_fishing_fishing_id` (`fishing_id`),
  CONSTRAINT `fishing_fishing_result_fishing_id_6f62e9b8_fk_fishing_fishing_id` FOREIGN KEY (`fishing_id`) REFERENCES `fishing_fishing` (`id`),
  CONSTRAINT `fishing_fishing_result_fish_id_60fb081d_fk_fishing_fish_id` FOREIGN KEY (`fish_id`) REFERENCES `fishing_fish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing_result`
--

LOCK TABLES `fishing_fishing_result` WRITE;
/*!40000 ALTER TABLE `fishing_fishing_result` DISABLE KEYS */;
INSERT INTO `fishing_fishing_result` VALUES (1,2,1.0,1,1),(4,2,2.0,1,1);
/*!40000 ALTER TABLE `fishing_fishing_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing_tackle`
--

DROP TABLE IF EXISTS `fishing_fishing_tackle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing_tackle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_tackle_manufacturer` varchar(20) COLLATE utf8_bin NOT NULL,
  `fishing_tackle_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `fishing_tackle_length` decimal(3,1) NOT NULL,
  `fishing_tackle_casting_weight` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing_tackle`
--

LOCK TABLES `fishing_fishing_tackle` WRITE;
/*!40000 ALTER TABLE `fishing_fishing_tackle` DISABLE KEYS */;
INSERT INTO `fishing_fishing_tackle` VALUES (1,'Flagman','Legend',3.6,100);
/*!40000 ALTER TABLE `fishing_fishing_tackle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishing_trough`
--

DROP TABLE IF EXISTS `fishing_fishing_trough`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishing_trough` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_trough_manufacturer` varchar(50) COLLATE utf8_bin NOT NULL,
  `fishing_trough_weight` int(10) unsigned NOT NULL,
  `feed_capacity_id` int(11) NOT NULL,
  `model_trough_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishing_trou_feed_capacity_id_00040da5_fk_fishing_f` (`feed_capacity_id`),
  KEY `fishing_fishing_trou_model_trough_id_f9ef39f3_fk_fishing_m` (`model_trough_id`),
  CONSTRAINT `fishing_fishing_trou_feed_capacity_id_00040da5_fk_fishing_f` FOREIGN KEY (`feed_capacity_id`) REFERENCES `fishing_feed_capacity` (`id`),
  CONSTRAINT `fishing_fishing_trou_model_trough_id_f9ef39f3_fk_fishing_m` FOREIGN KEY (`model_trough_id`) REFERENCES `fishing_model_trough` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing_trough`
--

LOCK TABLES `fishing_fishing_trough` WRITE;
/*!40000 ALTER TABLE `fishing_fishing_trough` DISABLE KEYS */;
INSERT INTO `fishing_fishing_trough` VALUES (1,'Дядя Вася',70,1,1);
/*!40000 ALTER TABLE `fishing_fishing_trough` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_lure`
--

DROP TABLE IF EXISTS `fishing_lure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_lure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lure_manufacturer` varchar(100) COLLATE utf8_bin NOT NULL,
  `lure_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `fishing_lure_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_lure_fishing_lure_id_1ef0c75a_fk_fishing_fishing_lure_id` (`fishing_lure_id`),
  CONSTRAINT `fishing_lure_fishing_lure_id_1ef0c75a_fk_fishing_fishing_lure_id` FOREIGN KEY (`fishing_lure_id`) REFERENCES `fishing_fishing_lure` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_lure`
--

LOCK TABLES `fishing_lure` WRITE;
/*!40000 ALTER TABLE `fishing_lure` DISABLE KEYS */;
INSERT INTO `fishing_lure` VALUES (1,'Dunaev Fadeev','Carp classic',1);
/*!40000 ALTER TABLE `fishing_lure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_model_trough`
--

DROP TABLE IF EXISTS `fishing_model_trough`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_model_trough` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model_trough_plastic` tinyint(1) NOT NULL,
  `model_trough_lugs` tinyint(1) NOT NULL,
  `model_trough_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_model_trough_model_trough_name_id_7dea6b76_fk_fishing_m` (`model_trough_name_id`),
  CONSTRAINT `fishing_model_trough_model_trough_name_id_7dea6b76_fk_fishing_m` FOREIGN KEY (`model_trough_name_id`) REFERENCES `fishing_model_trough_name` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_model_trough`
--

LOCK TABLES `fishing_model_trough` WRITE;
/*!40000 ALTER TABLE `fishing_model_trough` DISABLE KEYS */;
INSERT INTO `fishing_model_trough` VALUES (1,1,0,1);
/*!40000 ALTER TABLE `fishing_model_trough` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_model_trough_name`
--

DROP TABLE IF EXISTS `fishing_model_trough_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_model_trough_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model_trough_name` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_model_trough_name`
--

LOCK TABLES `fishing_model_trough_name` WRITE;
/*!40000 ALTER TABLE `fishing_model_trough_name` DISABLE KEYS */;
INSERT INTO `fishing_model_trough_name` VALUES (1,'Пуля');
/*!40000 ALTER TABLE `fishing_model_trough_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_nozzle`
--

DROP TABLE IF EXISTS `fishing_nozzle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_nozzle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bait` tinyint(1) NOT NULL,
  `nozzle_manufacturer` varchar(100) COLLATE utf8_bin NOT NULL,
  `nozzle_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `nozzel_diameter` int(10) unsigned NOT NULL,
  `nozzel_type` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_nozzle`
--

LOCK TABLES `fishing_nozzle` WRITE;
/*!40000 ALTER TABLE `fishing_nozzle` DISABLE KEYS */;
INSERT INTO `fishing_nozzle` VALUES (1,1,'','Опарыш',0,'');
/*!40000 ALTER TABLE `fishing_nozzle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_nozzle_state`
--

DROP TABLE IF EXISTS `fishing_nozzle_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_nozzle_state` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_nozzle_state`
--

LOCK TABLES `fishing_nozzle_state` WRITE;
/*!40000 ALTER TABLE `fishing_nozzle_state` DISABLE KEYS */;
INSERT INTO `fishing_nozzle_state` VALUES (1,'Резанная');
/*!40000 ALTER TABLE `fishing_nozzle_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_overcast`
--

DROP TABLE IF EXISTS `fishing_overcast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_overcast` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `overcast_name` varchar(30) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_overcast`
--

LOCK TABLES `fishing_overcast` WRITE;
/*!40000 ALTER TABLE `fishing_overcast` DISABLE KEYS */;
INSERT INTO `fishing_overcast` VALUES (1,'Переменная облачность'),(2,'Ясно'),(3,'Малооблачно');
/*!40000 ALTER TABLE `fishing_overcast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_pace`
--

DROP TABLE IF EXISTS `fishing_pace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_pace` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pace_interval` varchar(30) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_pace`
--

LOCK TABLES `fishing_pace` WRITE;
/*!40000 ALTER TABLE `fishing_pace` DISABLE KEYS */;
INSERT INTO `fishing_pace` VALUES (1,'Быстрый (до 2 минут)');
/*!40000 ALTER TABLE `fishing_pace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_place`
--

DROP TABLE IF EXISTS `fishing_place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_place` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `place_locality` varchar(50) COLLATE utf8_bin NOT NULL,
  `place_northern_degree` int(11) NOT NULL,
  `place_northern_minute` int(11) NOT NULL,
  `place_northern_second` decimal(5,3) NOT NULL,
  `place_easter_degree` int(11) NOT NULL,
  `place_easter_minute` int(11) NOT NULL,
  `place_easter_second` decimal(5,3) NOT NULL,
  `fishing_point_id` int(11) NOT NULL,
  `water_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_place_fishing_point_id_3c5e85f0_fk_fishing_f` (`fishing_point_id`),
  KEY `fishing_place_water_id_2025e2bf_fk_fishing_water_id` (`water_id`),
  CONSTRAINT `fishing_place_fishing_point_id_3c5e85f0_fk_fishing_f` FOREIGN KEY (`fishing_point_id`) REFERENCES `fishing_fishing_point` (`id`),
  CONSTRAINT `fishing_place_water_id_2025e2bf_fk_fishing_water_id` FOREIGN KEY (`water_id`) REFERENCES `fishing_water` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_place`
--

LOCK TABLES `fishing_place` WRITE;
/*!40000 ALTER TABLE `fishing_place` DISABLE KEYS */;
INSERT INTO `fishing_place` VALUES (1,'Манычстрой',46,38,19.000,41,38,11.000,1,1);
/*!40000 ALTER TABLE `fishing_place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_point`
--

DROP TABLE IF EXISTS `fishing_point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_point` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `point_azimuth` int(10) unsigned NOT NULL,
  `point_distance` int(10) unsigned NOT NULL,
  `point_depth` decimal(4,2) NOT NULL,
  `bottom_map_id` int(11) NOT NULL,
  `priming_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bottom_map_id` (`bottom_map_id`),
  KEY `fishing_point_priming_id_e1e3f9c7_fk_fishing_priming_id` (`priming_id`),
  CONSTRAINT `fishing_point_bottom_map_id_e46da29a_fk_fishing_bottom_map_id` FOREIGN KEY (`bottom_map_id`) REFERENCES `fishing_bottom_map` (`id`),
  CONSTRAINT `fishing_point_priming_id_e1e3f9c7_fk_fishing_priming_id` FOREIGN KEY (`priming_id`) REFERENCES `fishing_priming` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_point`
--

LOCK TABLES `fishing_point` WRITE;
/*!40000 ALTER TABLE `fishing_point` DISABLE KEYS */;
/*!40000 ALTER TABLE `fishing_point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_priming`
--

DROP TABLE IF EXISTS `fishing_priming`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_priming` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `priming_name` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_priming`
--

LOCK TABLES `fishing_priming` WRITE;
/*!40000 ALTER TABLE `fishing_priming` DISABLE KEYS */;
INSERT INTO `fishing_priming` VALUES (1,'Ил');
/*!40000 ALTER TABLE `fishing_priming` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_water`
--

DROP TABLE IF EXISTS `fishing_water`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_water` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `water_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `district_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_water_district_id_5782a3e7_fk_fishing_district_id` (`district_id`),
  CONSTRAINT `fishing_water_district_id_5782a3e7_fk_fishing_district_id` FOREIGN KEY (`district_id`) REFERENCES `fishing_district` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_water`
--

LOCK TABLES `fishing_water` WRITE;
/*!40000 ALTER TABLE `fishing_water` DISABLE KEYS */;
INSERT INTO `fishing_water` VALUES (1,'река Маныч',1);
/*!40000 ALTER TABLE `fishing_water` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_weather`
--

DROP TABLE IF EXISTS `fishing_weather`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_weather` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weather_temperature` decimal(4,1) NOT NULL,
  `pressure` int(10) unsigned NOT NULL,
  `direction_wind` varchar(30) COLLATE utf8_bin NOT NULL,
  `wind_speed` decimal(4,1) NOT NULL,
  `lunar_day` int(10) unsigned NOT NULL,
  `overcast_id` int(11) NOT NULL,
  `weather_phenomena_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_weather_overcast_id_a5af9a29_fk_fishing_overcast_id` (`overcast_id`),
  KEY `fishing_weather_weather_phenomena_id_13eb48c6_fk_fishing_w` (`weather_phenomena_id`),
  CONSTRAINT `fishing_weather_overcast_id_a5af9a29_fk_fishing_overcast_id` FOREIGN KEY (`overcast_id`) REFERENCES `fishing_overcast` (`id`),
  CONSTRAINT `fishing_weather_weather_phenomena_id_13eb48c6_fk_fishing_w` FOREIGN KEY (`weather_phenomena_id`) REFERENCES `fishing_weather_phenomena` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_weather`
--

LOCK TABLES `fishing_weather` WRITE;
/*!40000 ALTER TABLE `fishing_weather` DISABLE KEYS */;
INSERT INTO `fishing_weather` VALUES (1,19.0,760,'СВ',5.0,0,1,1);
/*!40000 ALTER TABLE `fishing_weather` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_weather_phenomena`
--

DROP TABLE IF EXISTS `fishing_weather_phenomena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_weather_phenomena` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weather_phenomena_name` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_weather_phenomena`
--

LOCK TABLES `fishing_weather_phenomena` WRITE;
/*!40000 ALTER TABLE `fishing_weather_phenomena` DISABLE KEYS */;
INSERT INTO `fishing_weather_phenomena` VALUES (1,'без явлений');
/*!40000 ALTER TABLE `fishing_weather_phenomena` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-17 12:26:17
