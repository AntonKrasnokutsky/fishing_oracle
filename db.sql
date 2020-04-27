-- MySQL dump 10.14  Distrib 5.5.64-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: h9d1v8
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'fishermen');
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
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
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
INSERT INTO `auth_permission` VALUES (1,'Can add Арома',1,'add_aroma'),(2,'Can change Арома',1,'change_aroma'),(3,'Can delete Арома',1,'delete_aroma'),(4,'Can view Арома',1,'view_aroma'),(5,'Can add Карта дна',2,'add_bottommap'),(6,'Can change Карта дна',2,'change_bottommap'),(7,'Can delete Карта дна',2,'delete_bottommap'),(8,'Can view Карта дна',2,'view_bottommap'),(9,'Can add Крючок',3,'add_crochet'),(10,'Can change Крючок',3,'change_crochet'),(11,'Can delete Крючок',3,'delete_crochet'),(12,'Can view Крючок',3,'view_crochet'),(13,'Can add Район',4,'add_district'),(14,'Can change Район',4,'change_district'),(15,'Can delete Район',4,'delete_district'),(16,'Can view Район',4,'view_district'),(17,'Can add Кормоёмкость кормушки',5,'add_feedcapacity'),(18,'Can change Кормоёмкость кормушки',5,'change_feedcapacity'),(19,'Can delete Кормоёмкость кормушки',5,'delete_feedcapacity'),(20,'Can view Кормоёмкость кормушки',5,'view_feedcapacity'),(21,'Can add Рыба',6,'add_fish'),(22,'Can change Рыба',6,'change_fish'),(23,'Can delete Рыба',6,'delete_fish'),(24,'Can view Рыба',6,'view_fish'),(25,'Can add Рыбалка',7,'add_fishing'),(26,'Can change Рыбалка',7,'change_fishing'),(27,'Can delete Рыбалка',7,'delete_fishing'),(28,'Can view Рыбалка',7,'view_fishing'),(29,'Can add Поводок',8,'add_fishingleash'),(30,'Can change Поводок',8,'change_fishingleash'),(31,'Can delete Поводок',8,'delete_fishingleash'),(32,'Can view Поводок',8,'view_fishingleash'),(33,'Can add Прикормочная смесь',9,'add_fishinglure'),(34,'Can change Прикормочная смесь',9,'change_fishinglure'),(35,'Can delete Прикормочная смесь',9,'delete_fishinglure'),(36,'Can view Прикормочная смесь',9,'view_fishinglure'),(37,'Can add Монтаж',10,'add_fishingmontage'),(38,'Can change Монтаж',10,'change_fishingmontage'),(39,'Can delete Монтаж',10,'delete_fishingmontage'),(40,'Can view Монтаж',10,'view_fishingmontage'),(41,'Can add Точка ловли',11,'add_fishingpoint'),(42,'Can change Точка ловли',11,'change_fishingpoint'),(43,'Can delete Точка ловли',11,'delete_fishingpoint'),(44,'Can view Точка ловли',11,'view_fishingpoint'),(45,'Can add Рыболовная снасть',12,'add_fishingtackle'),(46,'Can change Рыболовная снасть',12,'change_fishingtackle'),(47,'Can delete Рыболовная снасть',12,'delete_fishingtackle'),(48,'Can view Рыболовная снасть',12,'view_fishingtackle'),(49,'Can add Название модели кормушки',13,'add_modeltroughname'),(50,'Can change Название модели кормушки',13,'change_modeltroughname'),(51,'Can delete Название модели кормушки',13,'delete_modeltroughname'),(52,'Can view Название модели кормушки',13,'view_modeltroughname'),(53,'Can add Наживка/насадка',14,'add_nozzle'),(54,'Can change Наживка/насадка',14,'change_nozzle'),(55,'Can delete Наживка/насадка',14,'delete_nozzle'),(56,'Can view Наживка/насадка',14,'view_nozzle'),(57,'Can add Состояние насадки',15,'add_nozzlestate'),(58,'Can change Состояние насадки',15,'change_nozzlestate'),(59,'Can delete Состояние насадки',15,'delete_nozzlestate'),(60,'Can view Состояние насадки',15,'view_nozzlestate'),(61,'Can add Облачность',16,'add_overcast'),(62,'Can change Облачность',16,'change_overcast'),(63,'Can delete Облачность',16,'delete_overcast'),(64,'Can view Облачность',16,'view_overcast'),(65,'Can add Темп',17,'add_pace'),(66,'Can change Темп',17,'change_pace'),(67,'Can delete Темп',17,'delete_pace'),(68,'Can view Темп',17,'view_pace'),(69,'Can add Покрытие дна',18,'add_priming'),(70,'Can change Покрытие дна',18,'change_priming'),(71,'Can delete Покрытие дна',18,'delete_priming'),(72,'Can view Покрытие дна',18,'view_priming'),(73,'Can add Погодное явление',19,'add_weatherphenomena'),(74,'Can change Погодное явление',19,'change_weatherphenomena'),(75,'Can delete Погодное явление',19,'delete_weatherphenomena'),(76,'Can view Погодное явление',19,'view_weatherphenomena'),(77,'Can add Погода',20,'add_weather'),(78,'Can change Погода',20,'change_weather'),(79,'Can delete Погода',20,'delete_weather'),(80,'Can view Погода',20,'view_weather'),(81,'Can add Водоем',21,'add_water'),(82,'Can change Водоем',21,'change_water'),(83,'Can delete Водоем',21,'delete_water'),(84,'Can view Водоем',21,'view_water'),(85,'Can add Точка карты дна',22,'add_point'),(86,'Can change Точка карты дна',22,'change_point'),(87,'Can delete Точка карты дна',22,'delete_point'),(88,'Can view Точка карты дна',22,'view_point'),(89,'Can add Место рыбалки',23,'add_place'),(90,'Can change Место рыбалки',23,'change_place'),(91,'Can delete Место рыбалки',23,'delete_place'),(92,'Can view Место рыбалки',23,'view_place'),(93,'Can add Модель кормушки',24,'add_modeltrough'),(94,'Can change Модель кормушки',24,'change_modeltrough'),(95,'Can delete Модель кормушки',24,'delete_modeltrough'),(96,'Can view Модель кормушки',24,'view_modeltrough'),(97,'Can add Прикорм',25,'add_lure'),(98,'Can change Прикорм',25,'change_lure'),(99,'Can delete Прикорм',25,'delete_lure'),(100,'Can view Прикорм',25,'view_lure'),(101,'Can add Трофейный улов',26,'add_fishtrophy'),(102,'Can change Трофейный улов',26,'change_fishtrophy'),(103,'Can delete Трофейный улов',26,'delete_fishtrophy'),(104,'Can view Трофейный улов',26,'view_fishtrophy'),(105,'Can add Рыболовная кормушка',27,'add_fishingtrough'),(106,'Can change Рыболовная кормушка',27,'change_fishingtrough'),(107,'Can delete Рыболовная кормушка',27,'delete_fishingtrough'),(108,'Can view Рыболовная кормушка',27,'view_fishingtrough'),(109,'Can add Результат рыбалки',28,'add_fishingresult'),(110,'Can change Результат рыбалки',28,'change_fishingresult'),(111,'Can delete Результат рыбалки',28,'delete_fishingresult'),(112,'Can view Результат рыбалки',28,'view_fishingresult'),(113,'Can add log entry',29,'add_logentry'),(114,'Can change log entry',29,'change_logentry'),(115,'Can delete log entry',29,'delete_logentry'),(116,'Can view log entry',29,'view_logentry'),(117,'Can add permission',30,'add_permission'),(118,'Can change permission',30,'change_permission'),(119,'Can delete permission',30,'delete_permission'),(120,'Can view permission',30,'view_permission'),(121,'Can add group',31,'add_group'),(122,'Can change group',31,'change_group'),(123,'Can delete group',31,'delete_group'),(124,'Can view group',31,'view_group'),(125,'Can add user',32,'add_user'),(126,'Can change user',32,'change_user'),(127,'Can delete user',32,'delete_user'),(128,'Can view user',32,'view_user'),(129,'Can add content type',33,'add_contenttype'),(130,'Can change content type',33,'change_contenttype'),(131,'Can delete content type',33,'delete_contenttype'),(132,'Can view content type',33,'view_contenttype'),(133,'Can add session',34,'add_session'),(134,'Can change session',34,'change_session'),(135,'Can delete session',34,'delete_session'),(136,'Can view session',34,'view_session');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$tQiSK6qe5nHM$cRjpF9Ap/TYyeRMTJqsx38ufl/wRDeNWnDe483sQceY=','2020-04-19 06:16:21.892476',1,'admin','','','',1,1,'2020-04-19 06:15:58.064444'),(2,'pbkdf2_sha256$180000$lD84hCH75fxA$2uasYQdAc9msKR0zgBCkmpiMFYbRCl6dF9EIDg6vVTI=',NULL,0,'user','','','',0,1,'2020-04-26 18:48:07.000000');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1);
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
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-19 06:16:50.941144','1','Dunaev Scopex',1,'[{\"added\": {}}]',1,1),(2,'2020-04-19 06:17:00.318969','1','Сальский район',1,'[{\"added\": {}}]',4,1),(3,'2020-04-19 06:17:02.608126','1','река Маныч',1,'[{\"added\": {}}]',21,1),(4,'2020-04-19 06:17:17.169144','1','река Маныч',1,'[{\"added\": {}}]',2,1),(5,'2020-04-19 06:17:25.138195','1','Большая',1,'[{\"added\": {}}]',5,1),(6,'2020-04-19 06:17:31.433849','2','Малая',1,'[{\"added\": {}}]',5,1),(7,'2020-04-19 06:17:34.241914','3','Средняя',1,'[{\"added\": {}}]',5,1),(8,'2020-04-19 06:17:41.150779','4','груз',1,'[{\"added\": {}}]',5,1),(9,'2020-04-19 06:17:55.954427','1','Gamakatsu LS-2283B 14',1,'[{\"added\": {}}]',3,1),(10,'2020-04-19 06:18:20.804187','1','Ил',1,'[{\"added\": {}}]',18,1),(11,'2020-04-19 06:18:22.928760','1','Ил',1,'[{\"added\": {}}]',11,1),(12,'2020-04-19 06:18:24.110211','1','река Маныч: Манычстрой',1,'[{\"added\": {}}]',23,1),(13,'2020-04-19 06:18:37.082929','1','Аллигатор',1,'[{\"added\": {}}]',13,1),(14,'2020-04-19 06:18:39.679321','1','Аллигатор металл с грунтозацепами',1,'[{\"added\": {}}]',24,1),(15,'2020-04-19 06:18:49.058807','1','Гарднер ',1,'[{\"added\": {}}]',10,1),(16,'2020-04-19 06:18:58.128299','1','Опарыш',1,'[{\"added\": {}}]',14,1),(17,'2020-04-19 06:19:14.223733','1','Ясно',1,'[{\"added\": {}}]',16,1),(18,'2020-04-19 06:19:26.155094','1','леска 0.08 25 см.',1,'[{\"added\": {}}]',8,1),(19,'2020-04-19 06:19:35.996791','1','без явлений',1,'[{\"added\": {}}]',19,1),(20,'2020-04-19 06:19:44.983856','1','Weather object (1)',1,'[{\"added\": {}}]',20,1),(21,'2020-04-19 06:20:15.319961','1','Топленый',1,'[{\"added\": {}}]',15,1),(22,'2020-04-19 06:20:17.017372','1','FishingLure object (1)',1,'[{\"added\": {}}]',9,1),(23,'2020-04-19 06:20:21.053875','1','Dunaev Fadeev Carp classic',1,'[{\"added\": {}}]',25,1),(24,'2020-04-19 09:36:52.484422','1','Flagman Legend 3.6 100',1,'[{\"added\": {}}]',12,1),(25,'2020-04-19 09:37:07.638692','1','Дядя Вася: Большая Аллигатор металл с грунтозацепами 100гр.',1,'[{\"added\": {}}]',27,1),(26,'2020-04-19 09:37:20.588624','1','Быстрый (до 2 минут)',1,'[{\"added\": {}}]',17,1),(27,'2020-04-19 09:37:22.245604','1','2020-04-19 12:36:40',1,'[{\"added\": {}}]',7,1),(28,'2020-04-19 09:37:40.952242','1','Лещ',1,'[{\"added\": {}}]',6,1),(29,'2020-04-19 09:37:46.100148','1','Лещ: 3шт. 3кг.',1,'[{\"added\": {}}]',28,1),(30,'2020-04-19 09:38:07.762942','1','река Маныч: 100 50',1,'[{\"added\": {}}]',22,1),(31,'2020-04-19 09:38:26.720202','1','Трофей: Лещ 2кг.',1,'[{\"added\": {}}]',26,1),(32,'2020-04-26 18:47:01.026057','1','fishermen',1,'[{\"added\": {}}]',31,1),(33,'2020-04-26 18:48:07.528657','2','user',1,'[{\"added\": {}}]',32,1),(34,'2020-04-26 18:49:14.703888','2','user',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',32,1);
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
INSERT INTO `django_content_type` VALUES (29,'admin','logentry'),(31,'auth','group'),(30,'auth','permission'),(32,'auth','user'),(33,'contenttypes','contenttype'),(1,'fishing','aroma'),(2,'fishing','bottommap'),(3,'fishing','crochet'),(4,'fishing','district'),(5,'fishing','feedcapacity'),(6,'fishing','fish'),(7,'fishing','fishing'),(8,'fishing','fishingleash'),(9,'fishing','fishinglure'),(10,'fishing','fishingmontage'),(11,'fishing','fishingpoint'),(28,'fishing','fishingresult'),(12,'fishing','fishingtackle'),(27,'fishing','fishingtrough'),(26,'fishing','fishtrophy'),(25,'fishing','lure'),(24,'fishing','modeltrough'),(13,'fishing','modeltroughname'),(14,'fishing','nozzle'),(15,'fishing','nozzlestate'),(16,'fishing','overcast'),(17,'fishing','pace'),(23,'fishing','place'),(22,'fishing','point'),(18,'fishing','priming'),(21,'fishing','water'),(20,'fishing','weather'),(19,'fishing','weatherphenomena'),(34,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-19 06:15:34.433335'),(2,'auth','0001_initial','2020-04-19 06:15:34.782660'),(3,'admin','0001_initial','2020-04-19 06:15:35.892173'),(4,'admin','0002_logentry_remove_auto_add','2020-04-19 06:15:36.084473'),(5,'admin','0003_logentry_add_action_flag_choices','2020-04-19 06:15:36.149273'),(6,'contenttypes','0002_remove_content_type_name','2020-04-19 06:15:36.629321'),(7,'auth','0002_alter_permission_name_max_length','2020-04-19 06:15:36.728214'),(8,'auth','0003_alter_user_email_max_length','2020-04-19 06:15:36.882816'),(9,'auth','0004_alter_user_username_opts','2020-04-19 06:15:36.908973'),(10,'auth','0005_alter_user_last_login_null','2020-04-19 06:15:37.081012'),(11,'auth','0006_require_contenttypes_0002','2020-04-19 06:15:37.091622'),(12,'auth','0007_alter_validators_add_error_messages','2020-04-19 06:15:37.136328'),(13,'auth','0008_alter_user_username_max_length','2020-04-19 06:15:37.281662'),(14,'auth','0009_alter_user_last_name_max_length','2020-04-19 06:15:37.410504'),(15,'auth','0010_alter_group_name_max_length','2020-04-19 06:15:37.520686'),(16,'auth','0011_update_proxy_permissions','2020-04-19 06:15:37.556768'),(17,'fishing','0001_initial','2020-04-19 06:15:40.872700'),(18,'sessions','0001_initial','2020-04-19 06:15:42.476718'),(19,'fishing','0002_auto_20200419_1555','2020-04-19 12:55:31.058473'),(20,'fishing','0003_auto_20200419_1559','2020-04-19 12:59:54.871736');
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
INSERT INTO `django_session` VALUES ('wgxq9835il8lox1yr8vsxi1nh1bzzf83','YmNiOGNiNjgyYTU2MWM2OTY5OWJhMTkwNzg0ZWQ2YjllNzBhMTJjNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyNmEzYzJlNzNmNGFkMzgxOGVkMjY4N2IyNzg0MTM5YzVkZmI2M2U3IiwibnVtX3Zpc2l0cyI6MTh9','2020-05-10 18:34:41.056671');
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
-- Table structure for table `fishing_bottommap`
--

DROP TABLE IF EXISTS `fishing_bottommap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_bottommap` (
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
  CONSTRAINT `fishing_bottommap_water_id_29312b8f_fk_fishing_water_id` FOREIGN KEY (`water_id`) REFERENCES `fishing_water` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_bottommap`
--

LOCK TABLES `fishing_bottommap` WRITE;
/*!40000 ALTER TABLE `fishing_bottommap` DISABLE KEYS */;
INSERT INTO `fishing_bottommap` VALUES (1,46,38,11.000,41,38,19.000,1);
/*!40000 ALTER TABLE `fishing_bottommap` ENABLE KEYS */;
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
INSERT INTO `fishing_crochet` VALUES (1,'Gamakatsu','LS-2283B',14);
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `fishing_district_district_name_7ad9aa15_uniq` (`district_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_district`
--

LOCK TABLES `fishing_district` WRITE;
/*!40000 ALTER TABLE `fishing_district` DISABLE KEYS */;
INSERT INTO `fishing_district` VALUES (3,'Пролетарский район'),(1,'Сальский район');
/*!40000 ALTER TABLE `fishing_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_feedcapacity`
--

DROP TABLE IF EXISTS `fishing_feedcapacity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_feedcapacity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feed_capacity_name` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_feedcapacity`
--

LOCK TABLES `fishing_feedcapacity` WRITE;
/*!40000 ALTER TABLE `fishing_feedcapacity` DISABLE KEYS */;
INSERT INTO `fishing_feedcapacity` VALUES (1,'Большая'),(2,'Малая'),(3,'Средняя'),(4,'груз');
/*!40000 ALTER TABLE `fishing_feedcapacity` ENABLE KEYS */;
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `fishing_fish_name_of_fish_5dc979e1_uniq` (`name_of_fish`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fish`
--

LOCK TABLES `fishing_fish` WRITE;
/*!40000 ALTER TABLE `fishing_fish` DISABLE KEYS */;
INSERT INTO `fishing_fish` VALUES (1,'Лещ','лещ');
/*!40000 ALTER TABLE `fishing_fish` ENABLE KEYS */;
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
  CONSTRAINT `fishing_fishing_crochet_id_477862af_fk_fishing_crochet_id` FOREIGN KEY (`crochet_id`) REFERENCES `fishing_crochet` (`id`),
  CONSTRAINT `fishing_fishing_aroma_id_eb3cee94_fk_fishing_aroma_id` FOREIGN KEY (`aroma_id`) REFERENCES `fishing_aroma` (`id`),
  CONSTRAINT `fishing_fishing_fishing_leash_id_5f14ca44_fk_fishing_f` FOREIGN KEY (`fishing_leash_id`) REFERENCES `fishing_fishingleash` (`id`),
  CONSTRAINT `fishing_fishing_fishing_lure_id_be36c2ad_fk_fishing_f` FOREIGN KEY (`fishing_lure_id`) REFERENCES `fishing_fishinglure` (`id`),
  CONSTRAINT `fishing_fishing_fishing_montage_id_f4c13924_fk_fishing_f` FOREIGN KEY (`fishing_montage_id`) REFERENCES `fishing_fishingmontage` (`id`),
  CONSTRAINT `fishing_fishing_fishing_tackle_id_34854d74_fk_fishing_f` FOREIGN KEY (`fishing_tackle_id`) REFERENCES `fishing_fishingtackle` (`id`),
  CONSTRAINT `fishing_fishing_fishing_trough_id_6f0f1cd5_fk_fishing_f` FOREIGN KEY (`fishing_trough_id`) REFERENCES `fishing_fishingtrough` (`id`),
  CONSTRAINT `fishing_fishing_nozzle_id_f0856399_fk_fishing_nozzle_id` FOREIGN KEY (`nozzle_id`) REFERENCES `fishing_nozzle` (`id`),
  CONSTRAINT `fishing_fishing_pace_id_d3d20faa_fk_fishing_pace_id` FOREIGN KEY (`pace_id`) REFERENCES `fishing_pace` (`id`),
  CONSTRAINT `fishing_fishing_place_id_c3a97595_fk_fishing_place_id` FOREIGN KEY (`place_id`) REFERENCES `fishing_place` (`id`),
  CONSTRAINT `fishing_fishing_weather_id_ac377240_fk_fishing_weather_id` FOREIGN KEY (`weather_id`) REFERENCES `fishing_weather` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing`
--

LOCK TABLES `fishing_fishing` WRITE;
/*!40000 ALTER TABLE `fishing_fishing` DISABLE KEYS */;
INSERT INTO `fishing_fishing` VALUES (1,'2020-04-19','12:36:40.000000',1,1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `fishing_fishing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishingleash`
--

DROP TABLE IF EXISTS `fishing_fishingleash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishingleash` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_leash_material` varchar(20) COLLATE utf8_bin NOT NULL,
  `fishing_leash_diameter` decimal(4,2) NOT NULL,
  `fishing_leash_length` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingleash`
--

LOCK TABLES `fishing_fishingleash` WRITE;
/*!40000 ALTER TABLE `fishing_fishingleash` DISABLE KEYS */;
INSERT INTO `fishing_fishingleash` VALUES (1,'леска',0.08,25);
/*!40000 ALTER TABLE `fishing_fishingleash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishinglure`
--

DROP TABLE IF EXISTS `fishing_fishinglure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishinglure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nozzle_id` int(11) NOT NULL,
  `nozzle_state_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishinglure_nozzle_id_a1d45da5_fk_fishing_nozzle_id` (`nozzle_id`),
  KEY `fishing_fishinglure_nozzle_state_id_92e99ef8_fk_fishing_n` (`nozzle_state_id`),
  CONSTRAINT `fishing_fishinglure_nozzle_state_id_92e99ef8_fk_fishing_n` FOREIGN KEY (`nozzle_state_id`) REFERENCES `fishing_nozzlestate` (`id`),
  CONSTRAINT `fishing_fishinglure_nozzle_id_a1d45da5_fk_fishing_nozzle_id` FOREIGN KEY (`nozzle_id`) REFERENCES `fishing_nozzle` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishinglure`
--

LOCK TABLES `fishing_fishinglure` WRITE;
/*!40000 ALTER TABLE `fishing_fishinglure` DISABLE KEYS */;
INSERT INTO `fishing_fishinglure` VALUES (1,1,1);
/*!40000 ALTER TABLE `fishing_fishinglure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishingmontage`
--

DROP TABLE IF EXISTS `fishing_fishingmontage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishingmontage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_montage_name` varchar(15) COLLATE utf8_bin NOT NULL,
  `fishing_montage_sliding` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingmontage`
--

LOCK TABLES `fishing_fishingmontage` WRITE;
/*!40000 ALTER TABLE `fishing_fishingmontage` DISABLE KEYS */;
INSERT INTO `fishing_fishingmontage` VALUES (1,'Гарднер',0);
/*!40000 ALTER TABLE `fishing_fishingmontage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishingpoint`
--

DROP TABLE IF EXISTS `fishing_fishingpoint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishingpoint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_point_azimuth` int(10) unsigned NOT NULL,
  `fishing_point_distance` int(10) unsigned NOT NULL,
  `fishing_poiny_depth` decimal(4,2) NOT NULL,
  `priming_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingpoint_priming_id_1f8fcb90_fk_fishing_priming_id` (`priming_id`),
  CONSTRAINT `fishing_fishingpoint_priming_id_1f8fcb90_fk_fishing_priming_id` FOREIGN KEY (`priming_id`) REFERENCES `fishing_priming` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingpoint`
--

LOCK TABLES `fishing_fishingpoint` WRITE;
/*!40000 ALTER TABLE `fishing_fishingpoint` DISABLE KEYS */;
INSERT INTO `fishing_fishingpoint` VALUES (1,100,42,2.50,1);
/*!40000 ALTER TABLE `fishing_fishingpoint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishingresult`
--

DROP TABLE IF EXISTS `fishing_fishingresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishingresult` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number_of_fish` int(10) unsigned NOT NULL,
  `fish_weight` decimal(6,1) NOT NULL,
  `fish_id` int(11) NOT NULL,
  `fishing_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingresult_fish_id_d834a94c_fk_fishing_fish_id` (`fish_id`),
  KEY `fishing_fishingresult_fishing_id_743b8270_fk_fishing_fishing_id` (`fishing_id`),
  CONSTRAINT `fishing_fishingresult_fishing_id_743b8270_fk_fishing_fishing_id` FOREIGN KEY (`fishing_id`) REFERENCES `fishing_fishing` (`id`),
  CONSTRAINT `fishing_fishingresult_fish_id_d834a94c_fk_fishing_fish_id` FOREIGN KEY (`fish_id`) REFERENCES `fishing_fish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingresult`
--

LOCK TABLES `fishing_fishingresult` WRITE;
/*!40000 ALTER TABLE `fishing_fishingresult` DISABLE KEYS */;
INSERT INTO `fishing_fishingresult` VALUES (1,3,3.0,1,1);
/*!40000 ALTER TABLE `fishing_fishingresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishingtackle`
--

DROP TABLE IF EXISTS `fishing_fishingtackle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishingtackle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_tackle_manufacturer` varchar(20) COLLATE utf8_bin NOT NULL,
  `fishing_tackle_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `fishing_tackle_length` decimal(3,1) NOT NULL,
  `fishing_tackle_casting_weight` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingtackle`
--

LOCK TABLES `fishing_fishingtackle` WRITE;
/*!40000 ALTER TABLE `fishing_fishingtackle` DISABLE KEYS */;
INSERT INTO `fishing_fishingtackle` VALUES (1,'Flagman','Legend',3.6,100);
/*!40000 ALTER TABLE `fishing_fishingtackle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishingtrough`
--

DROP TABLE IF EXISTS `fishing_fishingtrough`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishingtrough` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fishing_trough_manufacturer` varchar(50) COLLATE utf8_bin NOT NULL,
  `fishing_trough_weight` int(10) unsigned NOT NULL,
  `feed_capacity_id` int(11) NOT NULL,
  `model_trough_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingtroug_feed_capacity_id_a0fd9b68_fk_fishing_f` (`feed_capacity_id`),
  KEY `fishing_fishingtroug_model_trough_id_4c9f1d85_fk_fishing_m` (`model_trough_id`),
  CONSTRAINT `fishing_fishingtroug_model_trough_id_4c9f1d85_fk_fishing_m` FOREIGN KEY (`model_trough_id`) REFERENCES `fishing_modeltrough` (`id`),
  CONSTRAINT `fishing_fishingtroug_feed_capacity_id_a0fd9b68_fk_fishing_f` FOREIGN KEY (`feed_capacity_id`) REFERENCES `fishing_feedcapacity` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingtrough`
--

LOCK TABLES `fishing_fishingtrough` WRITE;
/*!40000 ALTER TABLE `fishing_fishingtrough` DISABLE KEYS */;
INSERT INTO `fishing_fishingtrough` VALUES (1,'Дядя Вася',100,1,1);
/*!40000 ALTER TABLE `fishing_fishingtrough` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_fishtrophy`
--

DROP TABLE IF EXISTS `fishing_fishtrophy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_fishtrophy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fish_trophy_weight` decimal(4,1) NOT NULL,
  `fish_id` int(11) NOT NULL,
  `fishing_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishtrophy_fish_id_294a821b_fk_fishing_fish_id` (`fish_id`),
  KEY `fishing_fishtrophy_fishing_id_64a6283c_fk_fishing_fishing_id` (`fishing_id`),
  CONSTRAINT `fishing_fishtrophy_fishing_id_64a6283c_fk_fishing_fishing_id` FOREIGN KEY (`fishing_id`) REFERENCES `fishing_fishing` (`id`),
  CONSTRAINT `fishing_fishtrophy_fish_id_294a821b_fk_fishing_fish_id` FOREIGN KEY (`fish_id`) REFERENCES `fishing_fish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishtrophy`
--

LOCK TABLES `fishing_fishtrophy` WRITE;
/*!40000 ALTER TABLE `fishing_fishtrophy` DISABLE KEYS */;
INSERT INTO `fishing_fishtrophy` VALUES (1,2.0,1,1);
/*!40000 ALTER TABLE `fishing_fishtrophy` ENABLE KEYS */;
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
  KEY `fishing_lure_fishing_lure_id_1ef0c75a_fk_fishing_fishinglure_id` (`fishing_lure_id`),
  CONSTRAINT `fishing_lure_fishing_lure_id_1ef0c75a_fk_fishing_fishinglure_id` FOREIGN KEY (`fishing_lure_id`) REFERENCES `fishing_fishinglure` (`id`)
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
-- Table structure for table `fishing_modeltrough`
--

DROP TABLE IF EXISTS `fishing_modeltrough`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_modeltrough` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model_trough_plastic` tinyint(1) NOT NULL,
  `model_trough_lugs` tinyint(1) NOT NULL,
  `model_trough_name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_modeltrough_model_trough_name_id_6d4b38f6_fk_fishing_m` (`model_trough_name_id`),
  CONSTRAINT `fishing_modeltrough_model_trough_name_id_6d4b38f6_fk_fishing_m` FOREIGN KEY (`model_trough_name_id`) REFERENCES `fishing_modeltroughname` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_modeltrough`
--

LOCK TABLES `fishing_modeltrough` WRITE;
/*!40000 ALTER TABLE `fishing_modeltrough` DISABLE KEYS */;
INSERT INTO `fishing_modeltrough` VALUES (1,0,1,1);
/*!40000 ALTER TABLE `fishing_modeltrough` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_modeltroughname`
--

DROP TABLE IF EXISTS `fishing_modeltroughname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_modeltroughname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model_trough_name` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fishing_modeltroughname_model_trough_name_2405a6a2_uniq` (`model_trough_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_modeltroughname`
--

LOCK TABLES `fishing_modeltroughname` WRITE;
/*!40000 ALTER TABLE `fishing_modeltroughname` DISABLE KEYS */;
INSERT INTO `fishing_modeltroughname` VALUES (1,'Аллигатор');
/*!40000 ALTER TABLE `fishing_modeltroughname` ENABLE KEYS */;
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
-- Table structure for table `fishing_nozzlestate`
--

DROP TABLE IF EXISTS `fishing_nozzlestate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_nozzlestate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fishing_nozzlestate_state_d4215635_uniq` (`state`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_nozzlestate`
--

LOCK TABLES `fishing_nozzlestate` WRITE;
/*!40000 ALTER TABLE `fishing_nozzlestate` DISABLE KEYS */;
INSERT INTO `fishing_nozzlestate` VALUES (1,'Топленый');
/*!40000 ALTER TABLE `fishing_nozzlestate` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_overcast`
--

LOCK TABLES `fishing_overcast` WRITE;
/*!40000 ALTER TABLE `fishing_overcast` DISABLE KEYS */;
INSERT INTO `fishing_overcast` VALUES (1,'Ясно');
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
  CONSTRAINT `fishing_place_water_id_2025e2bf_fk_fishing_water_id` FOREIGN KEY (`water_id`) REFERENCES `fishing_water` (`id`),
  CONSTRAINT `fishing_place_fishing_point_id_3c5e85f0_fk_fishing_f` FOREIGN KEY (`fishing_point_id`) REFERENCES `fishing_fishingpoint` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_place`
--

LOCK TABLES `fishing_place` WRITE;
/*!40000 ALTER TABLE `fishing_place` DISABLE KEYS */;
INSERT INTO `fishing_place` VALUES (1,'Манычстрой',46,38,11.000,41,38,19.000,1,1);
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
  CONSTRAINT `fishing_point_priming_id_e1e3f9c7_fk_fishing_priming_id` FOREIGN KEY (`priming_id`) REFERENCES `fishing_priming` (`id`),
  CONSTRAINT `fishing_point_bottom_map_id_e46da29a_fk_fishing_bottommap_id` FOREIGN KEY (`bottom_map_id`) REFERENCES `fishing_bottommap` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_point`
--

LOCK TABLES `fishing_point` WRITE;
/*!40000 ALTER TABLE `fishing_point` DISABLE KEYS */;
INSERT INTO `fishing_point` VALUES (1,100,50,2.00,1,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_priming`
--

LOCK TABLES `fishing_priming` WRITE;
/*!40000 ALTER TABLE `fishing_priming` DISABLE KEYS */;
INSERT INTO `fishing_priming` VALUES (1,'Ил'),(3,'Песок');
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
  CONSTRAINT `fishing_weather_weather_phenomena_id_13eb48c6_fk_fishing_w` FOREIGN KEY (`weather_phenomena_id`) REFERENCES `fishing_weatherphenomena` (`id`),
  CONSTRAINT `fishing_weather_overcast_id_a5af9a29_fk_fishing_overcast_id` FOREIGN KEY (`overcast_id`) REFERENCES `fishing_overcast` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_weather`
--

LOCK TABLES `fishing_weather` WRITE;
/*!40000 ALTER TABLE `fishing_weather` DISABLE KEYS */;
INSERT INTO `fishing_weather` VALUES (1,19.0,760,'СВ',2.5,0,1,1);
/*!40000 ALTER TABLE `fishing_weather` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fishing_weatherphenomena`
--

DROP TABLE IF EXISTS `fishing_weatherphenomena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fishing_weatherphenomena` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weather_phenomena_name` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_weatherphenomena`
--

LOCK TABLES `fishing_weatherphenomena` WRITE;
/*!40000 ALTER TABLE `fishing_weatherphenomena` DISABLE KEYS */;
INSERT INTO `fishing_weatherphenomena` VALUES (1,'без явлений');
/*!40000 ALTER TABLE `fishing_weatherphenomena` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-27 19:37:35
