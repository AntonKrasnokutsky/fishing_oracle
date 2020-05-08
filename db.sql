-- MySQL dump 10.14  Distrib 5.5.65-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: h9d1v8
-- ------------------------------------------------------
-- Server version	5.5.65-MariaDB

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
INSERT INTO `auth_permission` VALUES (1,'Can add Арома',1,'add_aroma'),(2,'Can change Арома',1,'change_aroma'),(3,'Can delete Арома',1,'delete_aroma'),(4,'Can view Арома',1,'view_aroma'),(5,'Can add Карта дна',2,'add_bottommap'),(6,'Can change Карта дна',2,'change_bottommap'),(7,'Can delete Карта дна',2,'delete_bottommap'),(8,'Can view Карта дна',2,'view_bottommap'),(9,'Can add Крючок',3,'add_crochet'),(10,'Can change Крючок',3,'change_crochet'),(11,'Can delete Крючок',3,'delete_crochet'),(12,'Can view Крючок',3,'view_crochet'),(13,'Can add Район',4,'add_district'),(14,'Can change Район',4,'change_district'),(15,'Can delete Район',4,'delete_district'),(16,'Can view Район',4,'view_district'),(17,'Can add Кормоёмкость кормушки',5,'add_feedcapacity'),(18,'Can change Кормоёмкость кормушки',5,'change_feedcapacity'),(19,'Can delete Кормоёмкость кормушки',5,'delete_feedcapacity'),(20,'Can view Кормоёмкость кормушки',5,'view_feedcapacity'),(21,'Can add Рыба',6,'add_fish'),(22,'Can change Рыба',6,'change_fish'),(23,'Can delete Рыба',6,'delete_fish'),(24,'Can view Рыба',6,'view_fish'),(25,'Can add Рыбалка',7,'add_fishing'),(26,'Can change Рыбалка',7,'change_fishing'),(27,'Can delete Рыбалка',7,'delete_fishing'),(28,'Can view Рыбалка',7,'view_fishing'),(29,'Can add Прикормочная смесь',8,'add_fishinglure'),(30,'Can change Прикормочная смесь',8,'change_fishinglure'),(31,'Can delete Прикормочная смесь',8,'delete_fishinglure'),(32,'Can view Прикормочная смесь',8,'view_fishinglure'),(33,'Can add Облачность',9,'add_overcast'),(34,'Can change Облачность',9,'change_overcast'),(35,'Can delete Облачность',9,'delete_overcast'),(36,'Can view Облачность',9,'view_overcast'),(37,'Can add Темп',10,'add_pace'),(38,'Can change Темп',10,'change_pace'),(39,'Can delete Темп',10,'delete_pace'),(40,'Can view Темп',10,'view_pace'),(41,'Can add Покрытие дна',11,'add_priming'),(42,'Can change Покрытие дна',11,'change_priming'),(43,'Can delete Покрытие дна',11,'delete_priming'),(44,'Can view Покрытие дна',11,'view_priming'),(45,'Can add Погодное явление',12,'add_weatherphenomena'),(46,'Can change Погодное явление',12,'change_weatherphenomena'),(47,'Can delete Погодное явление',12,'delete_weatherphenomena'),(48,'Can view Погодное явление',12,'view_weatherphenomena'),(49,'Can add Погода',13,'add_weather'),(50,'Can change Погода',13,'change_weather'),(51,'Can delete Погода',13,'delete_weather'),(52,'Can view Погода',13,'view_weather'),(53,'Can add Водоем',14,'add_water'),(54,'Can change Водоем',14,'change_water'),(55,'Can delete Водоем',14,'delete_water'),(56,'Can view Водоем',14,'view_water'),(57,'Can add Точка карты дна',15,'add_point'),(58,'Can change Точка карты дна',15,'change_point'),(59,'Can delete Точка карты дна',15,'delete_point'),(60,'Can view Точка карты дна',15,'view_point'),(61,'Can add Место рыбалки',16,'add_place'),(62,'Can change Место рыбалки',16,'change_place'),(63,'Can delete Место рыбалки',16,'delete_place'),(64,'Can view Место рыбалки',16,'view_place'),(65,'Can add Состояние насадки',17,'add_nozzlestate'),(66,'Can change Состояние насадки',17,'change_nozzlestate'),(67,'Can delete Состояние насадки',17,'delete_nozzlestate'),(68,'Can view Состояние насадки',17,'view_nozzlestate'),(69,'Can add Наживка/насадка',18,'add_nozzle'),(70,'Can change Наживка/насадка',18,'change_nozzle'),(71,'Can delete Наживка/насадка',18,'delete_nozzle'),(72,'Can view Наживка/насадка',18,'view_nozzle'),(73,'Can add Название модели кормушки',19,'add_modeltroughname'),(74,'Can change Название модели кормушки',19,'change_modeltroughname'),(75,'Can delete Название модели кормушки',19,'delete_modeltroughname'),(76,'Can view Название модели кормушки',19,'view_modeltroughname'),(77,'Can add Модель кормушки',20,'add_modeltrough'),(78,'Can change Модель кормушки',20,'change_modeltrough'),(79,'Can delete Модель кормушки',20,'delete_modeltrough'),(80,'Can view Модель кормушки',20,'view_modeltrough'),(81,'Can add Прикорм',21,'add_lure'),(82,'Can change Прикорм',21,'change_lure'),(83,'Can delete Прикорм',21,'delete_lure'),(84,'Can view Прикорм',21,'view_lure'),(85,'Can add Трофейный улов',22,'add_fishtrophy'),(86,'Can change Трофейный улов',22,'change_fishtrophy'),(87,'Can delete Трофейный улов',22,'delete_fishtrophy'),(88,'Can view Трофейный улов',22,'view_fishtrophy'),(89,'Can add Рыболовная кормушка',23,'add_fishingtrough'),(90,'Can change Рыболовная кормушка',23,'change_fishingtrough'),(91,'Can delete Рыболовная кормушка',23,'delete_fishingtrough'),(92,'Can view Рыболовная кормушка',23,'view_fishingtrough'),(93,'Can add Рыболовная снасть',24,'add_fishingtackle'),(94,'Can change Рыболовная снасть',24,'change_fishingtackle'),(95,'Can delete Рыболовная снасть',24,'delete_fishingtackle'),(96,'Can view Рыболовная снасть',24,'view_fishingtackle'),(97,'Can add Результат рыбалки',25,'add_fishingresult'),(98,'Can change Результат рыбалки',25,'change_fishingresult'),(99,'Can delete Результат рыбалки',25,'delete_fishingresult'),(100,'Can view Результат рыбалки',25,'view_fishingresult'),(101,'Can add Точка ловли',26,'add_fishingpoint'),(102,'Can change Точка ловли',26,'change_fishingpoint'),(103,'Can delete Точка ловли',26,'delete_fishingpoint'),(104,'Can view Точка ловли',26,'view_fishingpoint'),(105,'Can add Монтаж',27,'add_fishingmontage'),(106,'Can change Монтаж',27,'change_fishingmontage'),(107,'Can delete Монтаж',27,'delete_fishingmontage'),(108,'Can view Монтаж',27,'view_fishingmontage'),(109,'Can add Поводок',28,'add_fishingleash'),(110,'Can change Поводок',28,'change_fishingleash'),(111,'Can delete Поводок',28,'delete_fishingleash'),(112,'Can view Поводок',28,'view_fishingleash'),(113,'Can add Пользователь',29,'add_customuser'),(114,'Can change Пользователь',29,'change_customuser'),(115,'Can delete Пользователь',29,'delete_customuser'),(116,'Can view Пользователь',29,'view_customuser'),(117,'Can add log entry',30,'add_logentry'),(118,'Can change log entry',30,'change_logentry'),(119,'Can delete log entry',30,'delete_logentry'),(120,'Can view log entry',30,'view_logentry'),(121,'Can add permission',31,'add_permission'),(122,'Can change permission',31,'change_permission'),(123,'Can delete permission',31,'delete_permission'),(124,'Can view permission',31,'view_permission'),(125,'Can add group',32,'add_group'),(126,'Can change group',32,'change_group'),(127,'Can delete group',32,'delete_group'),(128,'Can view group',32,'view_group'),(129,'Can add content type',33,'add_contenttype'),(130,'Can change content type',33,'change_contenttype'),(131,'Can delete content type',33,'delete_contenttype'),(132,'Can view content type',33,'view_contenttype'),(133,'Can add session',34,'add_session'),(134,'Can change session',34,'change_session'),(135,'Can delete session',34,'delete_session'),(136,'Can view session',34,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
INSERT INTO `django_content_type` VALUES (30,'admin','logentry'),(32,'auth','group'),(31,'auth','permission'),(33,'contenttypes','contenttype'),(1,'fishing','aroma'),(2,'fishing','bottommap'),(3,'fishing','crochet'),(4,'fishing','district'),(5,'fishing','feedcapacity'),(6,'fishing','fish'),(7,'fishing','fishing'),(28,'fishing','fishingleash'),(8,'fishing','fishinglure'),(27,'fishing','fishingmontage'),(26,'fishing','fishingpoint'),(25,'fishing','fishingresult'),(24,'fishing','fishingtackle'),(23,'fishing','fishingtrough'),(22,'fishing','fishtrophy'),(21,'fishing','lure'),(20,'fishing','modeltrough'),(19,'fishing','modeltroughname'),(18,'fishing','nozzle'),(17,'fishing','nozzlestate'),(9,'fishing','overcast'),(10,'fishing','pace'),(16,'fishing','place'),(15,'fishing','point'),(11,'fishing','priming'),(14,'fishing','water'),(13,'fishing','weather'),(12,'fishing','weatherphenomena'),(34,'sessions','session'),(29,'users','customuser');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-05-08 08:02:44.007689'),(2,'contenttypes','0002_remove_content_type_name','2020-05-08 08:02:44.055271'),(3,'auth','0001_initial','2020-05-08 08:02:44.107573'),(4,'auth','0002_alter_permission_name_max_length','2020-05-08 08:02:44.198460'),(5,'auth','0003_alter_user_email_max_length','2020-05-08 08:02:44.204581'),(6,'auth','0004_alter_user_username_opts','2020-05-08 08:02:44.214608'),(7,'auth','0005_alter_user_last_login_null','2020-05-08 08:02:44.221340'),(8,'auth','0006_require_contenttypes_0002','2020-05-08 08:02:44.224196'),(9,'auth','0007_alter_validators_add_error_messages','2020-05-08 08:02:44.230434'),(10,'auth','0008_alter_user_username_max_length','2020-05-08 08:02:44.237679'),(11,'auth','0009_alter_user_last_name_max_length','2020-05-08 08:02:44.257197'),(12,'auth','0010_alter_group_name_max_length','2020-05-08 08:02:44.281521'),(13,'auth','0011_update_proxy_permissions','2020-05-08 08:02:44.289623'),(14,'users','0001_initial','2020-05-08 08:02:44.324230'),(15,'admin','0001_initial','2020-05-08 08:02:44.512807'),(16,'admin','0002_logentry_remove_auto_add','2020-05-08 08:02:44.581531'),(17,'admin','0003_logentry_add_action_flag_choices','2020-05-08 08:02:44.593308'),(18,'fishing','0001_initial','2020-05-08 08:02:45.944678'),(19,'sessions','0001_initial','2020-05-08 08:02:46.784253');
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
INSERT INTO `django_session` VALUES ('65zsxf5nb20g4bzd2r5vhils9bcc7a5v','ZDE4NmM0NmE4YzY4MTFiOGVhMTQ0Mzg5MWJlMjNjZTBiMjRhMTVmNDp7Im51bV92aXNpdHMiOjUsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MzdjYmI4M2FhYWU5MDYwYWRiNDlmY2IwYzk4OTc3Y2NiNzdiMWRlIn0=','2020-05-22 11:45:01.358335');
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_aroma_owner_id_f3531fb9_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_aroma_owner_id_f3531fb9_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_aroma`
--

LOCK TABLES `fishing_aroma` WRITE;
/*!40000 ALTER TABLE `fishing_aroma` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  `water_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `water_id` (`water_id`),
  KEY `fishing_bottommap_owner_id_f3e016df_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_bottommap_owner_id_f3e016df_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_bottommap_water_id_29312b8f_fk_fishing_water_id` FOREIGN KEY (`water_id`) REFERENCES `fishing_water` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_bottommap`
--

LOCK TABLES `fishing_bottommap` WRITE;
/*!40000 ALTER TABLE `fishing_bottommap` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_crochet_owner_id_c6a2c6aa_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_crochet_owner_id_c6a2c6aa_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_crochet`
--

LOCK TABLES `fishing_crochet` WRITE;
/*!40000 ALTER TABLE `fishing_crochet` DISABLE KEYS */;
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
  UNIQUE KEY `district_name` (`district_name`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_district`
--

LOCK TABLES `fishing_district` WRITE;
/*!40000 ALTER TABLE `fishing_district` DISABLE KEYS */;
INSERT INTO `fishing_district` VALUES (44,'Азов город'),(1,'Азовский район'),(2,'Аксайский район'),(3,'Багаевский район'),(45,'Батайск город'),(4,'Белокалитвинский район'),(5,'Боковский район'),(6,'Верхнедонской район'),(7,'Веселовский район'),(46,'Волгодонск город'),(8,'Волгодонской район'),(47,'Гуково город'),(48,'Донецк город'),(9,'Дубовский район'),(10,'Егорлыкский район'),(11,'Заветинский район'),(49,'Зверево город'),(12,'Зерноградский район'),(13,'Зимовниковский район'),(14,'Кагальницкий район'),(50,'Каменск-Шахтинский город'),(15,'Каменский район'),(16,'Кашарский район'),(17,'Константиновский район'),(18,'Красносулинский район'),(19,'Куйбышевский район'),(20,'Мартыновский район'),(21,'Матвеево-Курганский район'),(22,'Миллеровский район'),(23,'Милютинский район'),(24,'Морозовский район'),(25,'Мясниковский район'),(26,'Неклиновский район'),(51,'Новочеркасск город'),(52,'Новошахтинск город'),(27,'Обливский район'),(28,'Октябрьский район'),(29,'Орловский район'),(30,'Песчанокопский район'),(31,'Пролетарский район'),(32,'Ремонтненский район'),(33,'Родионово-Несветайский район'),(53,'Ростов-на-Дону город'),(34,'Сальский район'),(35,'Семикаракорский район'),(36,'Советский район'),(54,'Таганрог город'),(37,'Тарасовский район'),(38,'Тацинский район'),(39,'Усть-Донецкий район'),(40,'Целинский район'),(41,'Цимлянский район'),(42,'Чертковский район'),(55,'Шахты город'),(43,'Шолоховский район');
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
INSERT INTO `fishing_feedcapacity` VALUES (1,'Груз'),(2,'Малая'),(3,'Средняя'),(4,'Большая');
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
  UNIQUE KEY `name_of_fish` (`name_of_fish`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fish`
--

LOCK TABLES `fishing_fish` WRITE;
/*!40000 ALTER TABLE `fishing_fish` DISABLE KEYS */;
INSERT INTO `fishing_fish` VALUES (1,'Лещ','Лещ');
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
  `owner_id` int(11) NOT NULL,
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
  KEY `fishing_fishing_owner_id_1317e47e_fk_users_customuser_id` (`owner_id`),
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
  CONSTRAINT `fishing_fishing_owner_id_1317e47e_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_fishing_pace_id_d3d20faa_fk_fishing_pace_id` FOREIGN KEY (`pace_id`) REFERENCES `fishing_pace` (`id`),
  CONSTRAINT `fishing_fishing_place_id_c3a97595_fk_fishing_place_id` FOREIGN KEY (`place_id`) REFERENCES `fishing_place` (`id`),
  CONSTRAINT `fishing_fishing_weather_id_ac377240_fk_fishing_weather_id` FOREIGN KEY (`weather_id`) REFERENCES `fishing_weather` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishing`
--

LOCK TABLES `fishing_fishing` WRITE;
/*!40000 ALTER TABLE `fishing_fishing` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingleash_owner_id_b6fbe80d_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_fishingleash_owner_id_b6fbe80d_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingleash`
--

LOCK TABLES `fishing_fishingleash` WRITE;
/*!40000 ALTER TABLE `fishing_fishingleash` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishinglure_nozzle_id_a1d45da5_fk_fishing_nozzle_id` (`nozzle_id`),
  KEY `fishing_fishinglure_nozzle_state_id_92e99ef8_fk_fishing_n` (`nozzle_state_id`),
  KEY `fishing_fishinglure_owner_id_318c5212_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_fishinglure_owner_id_318c5212_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_fishinglure_nozzle_id_a1d45da5_fk_fishing_nozzle_id` FOREIGN KEY (`nozzle_id`) REFERENCES `fishing_nozzle` (`id`),
  CONSTRAINT `fishing_fishinglure_nozzle_state_id_92e99ef8_fk_fishing_n` FOREIGN KEY (`nozzle_state_id`) REFERENCES `fishing_nozzlestate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishinglure`
--

LOCK TABLES `fishing_fishinglure` WRITE;
/*!40000 ALTER TABLE `fishing_fishinglure` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingmontage_owner_id_7d3a4c48_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_fishingmontage_owner_id_7d3a4c48_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingmontage`
--

LOCK TABLES `fishing_fishingmontage` WRITE;
/*!40000 ALTER TABLE `fishing_fishingmontage` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  `place_id` int(11) NOT NULL,
  `priming_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `place_id` (`place_id`),
  KEY `fishing_fishingpoint_owner_id_2fa2dbb9_fk_users_customuser_id` (`owner_id`),
  KEY `fishing_fishingpoint_priming_id_1f8fcb90_fk_fishing_priming_id` (`priming_id`),
  CONSTRAINT `fishing_fishingpoint_priming_id_1f8fcb90_fk_fishing_priming_id` FOREIGN KEY (`priming_id`) REFERENCES `fishing_priming` (`id`),
  CONSTRAINT `fishing_fishingpoint_owner_id_2fa2dbb9_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_fishingpoint_place_id_3112c6f3_fk_fishing_place_id` FOREIGN KEY (`place_id`) REFERENCES `fishing_place` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingpoint`
--

LOCK TABLES `fishing_fishingpoint` WRITE;
/*!40000 ALTER TABLE `fishing_fishingpoint` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingresult_fish_id_d834a94c_fk_fishing_fish_id` (`fish_id`),
  KEY `fishing_fishingresult_fishing_id_743b8270_fk_fishing_fishing_id` (`fishing_id`),
  KEY `fishing_fishingresult_owner_id_4f2c7857_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_fishingresult_owner_id_4f2c7857_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_fishingresult_fishing_id_743b8270_fk_fishing_fishing_id` FOREIGN KEY (`fishing_id`) REFERENCES `fishing_fishing` (`id`),
  CONSTRAINT `fishing_fishingresult_fish_id_d834a94c_fk_fishing_fish_id` FOREIGN KEY (`fish_id`) REFERENCES `fishing_fish` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingresult`
--

LOCK TABLES `fishing_fishingresult` WRITE;
/*!40000 ALTER TABLE `fishing_fishingresult` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingtackle_owner_id_01c573a0_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_fishingtackle_owner_id_01c573a0_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingtackle`
--

LOCK TABLES `fishing_fishingtackle` WRITE;
/*!40000 ALTER TABLE `fishing_fishingtackle` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishingtroug_feed_capacity_id_a0fd9b68_fk_fishing_f` (`feed_capacity_id`),
  KEY `fishing_fishingtroug_model_trough_id_4c9f1d85_fk_fishing_m` (`model_trough_id`),
  KEY `fishing_fishingtrough_owner_id_9993dd36_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_fishingtrough_owner_id_9993dd36_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_fishingtroug_feed_capacity_id_a0fd9b68_fk_fishing_f` FOREIGN KEY (`feed_capacity_id`) REFERENCES `fishing_feedcapacity` (`id`),
  CONSTRAINT `fishing_fishingtroug_model_trough_id_4c9f1d85_fk_fishing_m` FOREIGN KEY (`model_trough_id`) REFERENCES `fishing_modeltrough` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishingtrough`
--

LOCK TABLES `fishing_fishingtrough` WRITE;
/*!40000 ALTER TABLE `fishing_fishingtrough` DISABLE KEYS */;
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
  `fish_trophy_weight` decimal(4,2) NOT NULL,
  `fish_id` int(11) NOT NULL,
  `fishing_id` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_fishtrophy_fish_id_294a821b_fk_fishing_fish_id` (`fish_id`),
  KEY `fishing_fishtrophy_fishing_id_64a6283c_fk_fishing_fishing_id` (`fishing_id`),
  KEY `fishing_fishtrophy_owner_id_f136ab9c_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_fishtrophy_owner_id_f136ab9c_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_fishtrophy_fishing_id_64a6283c_fk_fishing_fishing_id` FOREIGN KEY (`fishing_id`) REFERENCES `fishing_fishing` (`id`),
  CONSTRAINT `fishing_fishtrophy_fish_id_294a821b_fk_fishing_fish_id` FOREIGN KEY (`fish_id`) REFERENCES `fishing_fish` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_fishtrophy`
--

LOCK TABLES `fishing_fishtrophy` WRITE;
/*!40000 ALTER TABLE `fishing_fishtrophy` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_lure_fishing_lure_id_1ef0c75a_fk_fishing_fishinglure_id` (`fishing_lure_id`),
  KEY `fishing_lure_owner_id_599493ae_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_lure_owner_id_599493ae_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_lure_fishing_lure_id_1ef0c75a_fk_fishing_fishinglure_id` FOREIGN KEY (`fishing_lure_id`) REFERENCES `fishing_fishinglure` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_lure`
--

LOCK TABLES `fishing_lure` WRITE;
/*!40000 ALTER TABLE `fishing_lure` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_modeltrough_model_trough_name_id_6d4b38f6_fk_fishing_m` (`model_trough_name_id`),
  KEY `fishing_modeltrough_owner_id_bd79360b_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_modeltrough_owner_id_bd79360b_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `fishing_modeltrough_model_trough_name_id_6d4b38f6_fk_fishing_m` FOREIGN KEY (`model_trough_name_id`) REFERENCES `fishing_modeltroughname` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_modeltrough`
--

LOCK TABLES `fishing_modeltrough` WRITE;
/*!40000 ALTER TABLE `fishing_modeltrough` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `model_trough_name` (`model_trough_name`),
  KEY `fishing_modeltroughname_owner_id_5d0786a0_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_modeltroughname_owner_id_5d0786a0_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_modeltroughname`
--

LOCK TABLES `fishing_modeltroughname` WRITE;
/*!40000 ALTER TABLE `fishing_modeltroughname` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_nozzle_owner_id_4ff3df64_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_nozzle_owner_id_4ff3df64_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_nozzle`
--

LOCK TABLES `fishing_nozzle` WRITE;
/*!40000 ALTER TABLE `fishing_nozzle` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `state` (`state`),
  KEY `fishing_nozzlestate_owner_id_4d9694f5_fk_users_customuser_id` (`owner_id`),
  CONSTRAINT `fishing_nozzlestate_owner_id_4d9694f5_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_nozzlestate`
--

LOCK TABLES `fishing_nozzlestate` WRITE;
/*!40000 ALTER TABLE `fishing_nozzlestate` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_overcast`
--

LOCK TABLES `fishing_overcast` WRITE;
/*!40000 ALTER TABLE `fishing_overcast` DISABLE KEYS */;
INSERT INTO `fishing_overcast` VALUES (1,'Ясно'),(2,'Небольшая облачность'),(3,'Малооблачно'),(4,'Облачно с прояснениями'),(5,'Значительная облачность');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_pace`
--

LOCK TABLES `fishing_pace` WRITE;
/*!40000 ALTER TABLE `fishing_pace` DISABLE KEYS */;
INSERT INTO `fishing_pace` VALUES (1,'Быстрый (до 2 минут)'),(2,'Средний (от 2 до 5 минут)'),(3,'Медленный (более 5 минут)');
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
  `owner_id` int(11) NOT NULL,
  `water_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fishing_place_owner_id_db22b896_fk_users_customuser_id` (`owner_id`),
  KEY `fishing_place_water_id_2025e2bf_fk_fishing_water_id` (`water_id`),
  CONSTRAINT `fishing_place_water_id_2025e2bf_fk_fishing_water_id` FOREIGN KEY (`water_id`) REFERENCES `fishing_water` (`id`),
  CONSTRAINT `fishing_place_owner_id_db22b896_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_place`
--

LOCK TABLES `fishing_place` WRITE;
/*!40000 ALTER TABLE `fishing_place` DISABLE KEYS */;
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
  `owner_id` int(11) NOT NULL,
  `priming_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bottom_map_id` (`bottom_map_id`),
  KEY `fishing_point_owner_id_b9cf7b1b_fk_users_customuser_id` (`owner_id`),
  KEY `fishing_point_priming_id_e1e3f9c7_fk_fishing_priming_id` (`priming_id`),
  CONSTRAINT `fishing_point_priming_id_e1e3f9c7_fk_fishing_priming_id` FOREIGN KEY (`priming_id`) REFERENCES `fishing_priming` (`id`),
  CONSTRAINT `fishing_point_bottom_map_id_e46da29a_fk_fishing_bottommap_id` FOREIGN KEY (`bottom_map_id`) REFERENCES `fishing_bottommap` (`id`),
  CONSTRAINT `fishing_point_owner_id_b9cf7b1b_fk_users_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `users_customuser` (`id`)
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_priming`
--

LOCK TABLES `fishing_priming` WRITE;
/*!40000 ALTER TABLE `fishing_priming` DISABLE KEYS */;
INSERT INTO `fishing_priming` VALUES (1,'Ил'),(2,'Песок'),(3,'Глина'),(4,'Ракушка'),(5,'Камень'),(6,'Трава'),(7,'Камень');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_weather`
--

LOCK TABLES `fishing_weather` WRITE;
/*!40000 ALTER TABLE `fishing_weather` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fishing_weatherphenomena`
--

LOCK TABLES `fishing_weatherphenomena` WRITE;
/*!40000 ALTER TABLE `fishing_weatherphenomena` DISABLE KEYS */;
INSERT INTO `fishing_weatherphenomena` VALUES (1,'Гроза'),(2,'Бриз'),(3,'Смерч'),(4,'Обледенение'),(5,'Метель'),(6,'Туман'),(7,'Мгла'),(8,'Дым'),(9,'Зарница');
/*!40000 ALTER TABLE `fishing_weatherphenomena` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser`
--

DROP TABLE IF EXISTS `users_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_customuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser`
--

LOCK TABLES `users_customuser` WRITE;
/*!40000 ALTER TABLE `users_customuser` DISABLE KEYS */;
INSERT INTO `users_customuser` VALUES (1,'pbkdf2_sha256$180000$rihBnHOI52rN$kN032aKfBrcCihxewIa7NdY7R1hwOzLN+PdTBnXkwLQ=','2020-05-08 08:03:31.978975',1,'admin@admin.ru',1,1,'2020-05-08 08:03:06.697949');
/*!40000 ALTER TABLE `users_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_groups`
--

DROP TABLE IF EXISTS `users_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_customuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_groups`
--

LOCK TABLES `users_customuser_groups` WRITE;
/*!40000 ALTER TABLE `users_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_user_permissions`
--

DROP TABLE IF EXISTS `users_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_customuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_user_permissions`
--

LOCK TABLES `users_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-08 15:08:49
