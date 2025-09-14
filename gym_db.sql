/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: gym_db
-- ------------------------------------------------------
-- Server version	11.8.3-MariaDB-1+b1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `abonnements_abonnement`
--

DROP TABLE IF EXISTS `abonnements_abonnement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `abonnements_abonnement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  `date_debut` date NOT NULL,
  `date_fin` date NOT NULL,
  `statut` varchar(20) NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `abonnements_abonnement_client_id_1b5af306_fk_users_user_id` (`client_id`),
  CONSTRAINT `abonnements_abonnement_client_id_1b5af306_fk_users_user_id` FOREIGN KEY (`client_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `abonnements_abonnement`
--

LOCK TABLES `abonnements_abonnement` WRITE;
/*!40000 ALTER TABLE `abonnements_abonnement` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `abonnements_abonnement` VALUES
(2,'Annuel Premium','2025-07-09','2026-07-09','ACTIVE','2025-09-07 07:47:44.994014',11),
(3,'Trimestriel','2025-08-08','2025-11-06','ACTIVE','2025-09-07 07:47:45.005088',12),
(4,'Mensuel Standard','2025-07-24','2025-08-23','EXPIRED','2025-09-07 07:47:45.016367',13),
(5,'Hebdomadaire','2025-09-12','2025-09-19','ACTIVE','2025-09-07 07:47:45.027288',14);
/*!40000 ALTER TABLE `abonnements_abonnement` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add Utilisateur',7,'add_user'),
(26,'Can change Utilisateur',7,'change_user'),
(27,'Can delete Utilisateur',7,'delete_user'),
(28,'Can view Utilisateur',7,'view_user'),
(29,'Can add Coach',8,'add_coach'),
(30,'Can change Coach',8,'change_coach'),
(31,'Can delete Coach',8,'delete_coach'),
(32,'Can view Coach',8,'view_coach'),
(33,'Can add Abonnement',9,'add_abonnement'),
(34,'Can change Abonnement',9,'change_abonnement'),
(35,'Can delete Abonnement',9,'delete_abonnement'),
(36,'Can view Abonnement',9,'view_abonnement'),
(37,'Can add Équipement',10,'add_equipement'),
(38,'Can change Équipement',10,'change_equipement'),
(39,'Can delete Équipement',10,'delete_equipement'),
(40,'Can view Équipement',10,'view_equipement'),
(41,'Can add Réservation',11,'add_reservation'),
(42,'Can change Réservation',11,'change_reservation'),
(43,'Can delete Réservation',11,'delete_reservation'),
(44,'Can view Réservation',11,'view_reservation'),
(45,'Can add Progrès',12,'add_progres'),
(46,'Can change Progrès',12,'change_progres'),
(47,'Can delete Progrès',12,'delete_progres'),
(48,'Can view Progrès',12,'view_progres'),
(49,'Can add Session',13,'add_session'),
(50,'Can change Session',13,'change_session'),
(51,'Can delete Session',13,'delete_session'),
(52,'Can view Session',13,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `coachs_coach`
--

DROP TABLE IF EXISTS `coachs_coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `coachs_coach` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `specialite` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coachs_coach`
--

LOCK TABLES `coachs_coach` WRITE;
/*!40000 ALTER TABLE `coachs_coach` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `coachs_coach` VALUES
(9,'Marie Dubois','Cardio et Endurance','marie.dubois@gymms.com','2025-09-07 08:57:15.366832'),
(10,'Pierre Martin','Yoga et Pilates','pierre.martin@gymms.com','2025-09-07 08:57:15.379836'),
(11,'Sophie Laurent','CrossFit et HIIT','sophie.laurent@gymms.com','2025-09-07 08:57:15.412732'),
(12,'Thomas Bernard','Préparation physique','thomas.bernard@gymms.com','2025-09-07 08:57:15.421524');
/*!40000 ALTER TABLE `coachs_coach` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `custom_sessions_session`
--

DROP TABLE IF EXISTS `custom_sessions_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `custom_sessions_session` (
  `id` uuid NOT NULL,
  `session_key` varchar(40) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `session_key` (`session_key`),
  KEY `custom_sessions_session_user_id_c5c8cef4_fk_users_user_id` (`user_id`),
  CONSTRAINT `custom_sessions_session_user_id_c5c8cef4_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_sessions_session`
--

LOCK TABLES `custom_sessions_session` WRITE;
/*!40000 ALTER TABLE `custom_sessions_session` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `custom_sessions_session` VALUES
('8a48a944-0323-4516-b6d4-3737f7160724','b3c789edd4dcebf5965de66d8359feb7d75bb8a5','2025-09-21 09:47:05.941919','2025-09-07 09:47:05.942086',11),
('d38fb556-2799-4ae5-ab3b-5a0c9b7c1637','df83a91fe0ace149ecdd648072b6373703310bab','2025-09-21 09:29:56.479087','2025-09-07 09:29:56.479372',16),
('5fa139ff-015c-4eca-ba48-87e01585b126','10aeb00f645698a5db396eb7ae3a26bc1b659987','2025-09-21 08:50:34.540284','2025-09-07 08:50:34.540514',2),
('bcabb790-d5e3-4e88-99f6-e50f8447505f','0c1030de0ce02c42b9228e9b95ca623afda506bb','2025-09-21 09:48:16.292948','2025-09-07 09:48:16.293224',12),
('5fdfee34-6ac4-4e70-b850-f65ee12f481b','3dbc8949e44793899d95f711fb526e8ac1872ed0','2025-09-21 12:48:21.470642','2025-09-07 12:48:21.471007',1),
('0b48eef3-0b66-4514-aec1-ff0edb2df94a','55e1c556bc2a7e21ff65b80516a7aa16e0df1eed','2025-09-21 10:38:08.702063','2025-09-07 10:38:08.702307',17);
/*!40000 ALTER TABLE `custom_sessions_session` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_content_type` VALUES
(9,'abonnements','abonnement'),
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(8,'coachs','coach'),
(5,'contenttypes','contenttype'),
(13,'custom_sessions','session'),
(10,'equipements','equipement'),
(12,'progres','progres'),
(11,'reservations','reservation'),
(6,'sessions','session'),
(7,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_migrations` VALUES
(1,'users','0001_initial','2025-09-04 17:56:09.181789'),
(2,'abonnements','0001_initial','2025-09-04 17:56:09.746802'),
(3,'coachs','0001_initial','2025-09-04 17:56:10.000676'),
(4,'equipements','0001_initial','2025-09-04 17:56:10.159209'),
(5,'progres','0001_initial','2025-09-04 17:56:11.143312'),
(6,'reservations','0001_initial','2025-09-04 17:56:12.530730'),
(7,'sessions','0001_initial','2025-09-04 17:56:13.173139'),
(8,'users','0002_user_is_active','2025-09-07 06:55:37.764366'),
(9,'users','0003_rename_created_at_user_date_creation_and_more','2025-09-07 08:09:57.597348'),
(10,'abonnements','0002_alter_abonnement_options_and_more','2025-09-07 08:09:58.738639'),
(11,'contenttypes','0001_initial','2025-09-07 08:09:59.326560'),
(12,'auth','0001_initial','2025-09-07 08:10:04.806760'),
(13,'admin','0001_initial','2025-09-07 08:10:06.116590'),
(14,'admin','0002_logentry_remove_auto_add','2025-09-07 08:10:06.152111'),
(15,'admin','0003_logentry_add_action_flag_choices','2025-09-07 08:10:06.177544'),
(16,'contenttypes','0002_remove_content_type_name','2025-09-07 08:10:06.969875'),
(17,'auth','0002_alter_permission_name_max_length','2025-09-07 08:10:07.402681'),
(18,'auth','0003_alter_user_email_max_length','2025-09-07 08:10:07.713167'),
(19,'auth','0004_alter_user_username_opts','2025-09-07 08:10:07.746293'),
(20,'auth','0005_alter_user_last_login_null','2025-09-07 08:10:08.168113'),
(21,'auth','0006_require_contenttypes_0002','2025-09-07 08:10:08.184012'),
(22,'auth','0007_alter_validators_add_error_messages','2025-09-07 08:10:08.203995'),
(23,'auth','0008_alter_user_username_max_length','2025-09-07 08:10:08.534295'),
(24,'auth','0009_alter_user_last_name_max_length','2025-09-07 08:10:08.844674'),
(25,'auth','0010_alter_group_name_max_length','2025-09-07 08:10:09.277447'),
(26,'auth','0011_update_proxy_permissions','2025-09-07 08:10:09.314911'),
(27,'auth','0012_alter_user_first_name_max_length','2025-09-07 08:10:09.721939'),
(28,'coachs','0002_rename_created_at_coach_date_creation_and_more','2025-09-07 08:10:11.609504'),
(29,'equipements','0002_rename_created_at_equipement_date_creation_and_more','2025-09-07 08:10:13.559552'),
(30,'custom_sessions','0001_initial','2025-09-07 08:14:33.121086');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `equipements_equipement`
--

DROP TABLE IF EXISTS `equipements_equipement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipements_equipement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `type` varchar(50) NOT NULL,
  `statut` varchar(20) NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `coach_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `equipements_equipement_coach_id_ac923a70_fk_coachs_coach_id` (`coach_id`),
  CONSTRAINT `equipements_equipement_coach_id_ac923a70_fk_coachs_coach_id` FOREIGN KEY (`coach_id`) REFERENCES `coachs_coach` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipements_equipement`
--

LOCK TABLES `equipements_equipement` WRITE;
/*!40000 ALTER TABLE `equipements_equipement` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `equipements_equipement` VALUES
(1,'Tapis de course','Cardio','DISPONIBLE','2025-09-07 07:38:57.687782',NULL),
(2,'Vélo stationnaire','Cardio','DISPONIBLE','2025-09-07 07:38:57.710644',NULL),
(3,'Rameur Concept2','Cardio','MAINTENANCE','2025-09-07 07:38:57.764352',NULL),
(4,'Banc plat','Poids libres','DISPONIBLE','2025-09-07 07:38:57.789980',NULL),
(5,'Haltères 10kg','Poids libres','DISPONIBLE','2025-09-07 07:38:57.888170',NULL),
(6,'Barre olympique','Poids libres','DISPONIBLE','2025-09-07 07:38:58.022420',NULL),
(7,'Presse à cuisses','Musculation guidée','DISPONIBLE','2025-09-07 07:38:58.109676',NULL),
(8,'Poulie vis-à-vis','Musculation guidée','MAINTENANCE','2025-09-07 07:38:58.160251',NULL),
(9,'Kettlebell 16kg','Accessoires','DISPONIBLE','2025-09-07 07:38:58.402916',NULL),
(10,'Corde à sauter','Accessoires','DISPONIBLE','2025-09-07 07:38:58.725566',NULL);
/*!40000 ALTER TABLE `equipements_equipement` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `progres_progres`
--

DROP TABLE IF EXISTS `progres_progres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `progres_progres` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `notes` longtext NOT NULL,
  `poids` decimal(5,2) DEFAULT NULL,
  `mesures` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`mesures`)),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `coach_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `progres_progres_client_id_e143162d_fk_users_user_id` (`client_id`),
  KEY `progres_progres_coach_id_5bf3a2ec_fk_coachs_coach_id` (`coach_id`),
  CONSTRAINT `progres_progres_client_id_e143162d_fk_users_user_id` FOREIGN KEY (`client_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `progres_progres_coach_id_5bf3a2ec_fk_coachs_coach_id` FOREIGN KEY (`coach_id`) REFERENCES `coachs_coach` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progres_progres`
--

LOCK TABLES `progres_progres` WRITE;
/*!40000 ALTER TABLE `progres_progres` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `progres_progres` VALUES
(8,'2025-09-04','Bien vraiment',72.00,'{\"tour_taille\": 80.0, \"tour_poitrine\": 98.0, \"tour_bras\": 35.0, \"tour_cuisse\": 60.0, \"masse_grasse\": 15.5}','2025-09-07 09:43:27.889525','2025-09-07 10:26:12.259009',12,10);
/*!40000 ALTER TABLE `progres_progres` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `reservations_reservation`
--

DROP TABLE IF EXISTS `reservations_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations_reservation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `heure` time(6) NOT NULL,
  `statut` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `coach_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservations_reservation_coach_id_date_heure_cc411f73_uniq` (`coach_id`,`date`,`heure`),
  KEY `reservations_reservation_client_id_696a60bf_fk_users_user_id` (`client_id`),
  CONSTRAINT `reservations_reservation_client_id_696a60bf_fk_users_user_id` FOREIGN KEY (`client_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `reservations_reservation_coach_id_ff1e3d8e_fk_coachs_coach_id` FOREIGN KEY (`coach_id`) REFERENCES `coachs_coach` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations_reservation`
--

LOCK TABLES `reservations_reservation` WRITE;
/*!40000 ALTER TABLE `reservations_reservation` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `reservations_reservation` VALUES
(1,'2025-09-17','09:00:00.000000','PLANIFIEE','2025-09-07 07:50:14.875474','2025-09-07 09:28:20.425277',12,11),
(2,'2025-09-15','10:30:00.000000','PLANIFIEE','2025-09-07 07:50:14.908371','2025-09-07 09:28:36.085103',13,12),
(5,'2025-08-05','11:00:00.000000','ANNULEE','2025-09-07 07:50:15.291685','2025-09-07 09:27:35.402306',14,9),
(6,'2025-09-19','08:30:00.000000','PLANIFIEE','2025-09-07 07:50:15.333307','2025-09-07 09:28:08.515849',13,10),
(8,'2025-09-09','12:00:00.000000','PLANIFIEE','2025-09-07 09:49:44.432671','2025-09-07 09:49:44.432699',12,9);
/*!40000 ALTER TABLE `reservations_reservation` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `sessions_session`
--

DROP TABLE IF EXISTS `sessions_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `sessions_session` (
  `id` uuid NOT NULL,
  `session_key` varchar(40) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `session_key` (`session_key`),
  KEY `sessions_session_user_id_0337f0ad_fk_users_user_id` (`user_id`),
  CONSTRAINT `sessions_session_user_id_0337f0ad_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions_session`
--

LOCK TABLES `sessions_session` WRITE;
/*!40000 ALTER TABLE `sessions_session` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `sessions_session` VALUES
('720485be-8028-4614-9ca5-a974928a4f00','634c153a1385a84785da004f4ecc46798488f74f','2025-09-21 07:20:09.778035','2025-09-07 07:20:09.778275',2),
('3b2a2978-0c4b-4383-9483-b6c9c70c9abc','e44be743bec633fd257ea36aee6ca1b24346f8eb','2025-09-21 07:06:30.195358','2025-09-07 07:06:30.195678',1);
/*!40000 ALTER TABLE `sessions_session` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `role` varchar(20) NOT NULL,
  `date_creation` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `users_user` VALUES
(1,'Samandari','samandari@gmail.com','pbkdf2_sha256$1000000$ZXYkH0OFX7Bp8aoyONaX9F$+C5UzdQ9/bbnjBbuPhuP3qHEC8CxOh47a0Ml1YKXtbc=','ADMIN','2025-09-05 08:34:03.587057',1,NULL),
(2,'Coach1','coach1@gmail.com','pbkdf2_sha256$1000000$lgQXjeAGvehAnagAO7xX3r$S9CA1ntyV8OTc3OTJxPS7tB/bexJZROex8pS3GXedFU=','COACH','2025-09-07 07:08:27.701380',1,NULL),
(11,'Jean Dupont','jean.dupont@email.com','pbkdf2_sha256$1000000$3ODn9bg3Lx4gpbN796r7x6$MnMGqRoeXU/z1GC5BSW5MXKp8+zD2NNhAW9vDeChP80=','CLIENT','2025-09-07 07:47:40.989317',1,NULL),
(12,'Alice Martin','alice.martin@email.com','pbkdf2_sha256$1000000$3TThhBML3RDndLEWr8YfL7$osX5E3T7FTmnwZ0Z3oHoItFWoTpsVVAPqX0d687GhxA=','CLIENT','2025-09-07 07:47:41.910059',1,NULL),
(13,'Bob Wilson','bob.wilson@email.com','pbkdf2_sha256$1000000$8aAkPFKpOqEuc7CWu2N7QP$YBtVUP2bW3xKC4ntElyvTswYIqsY2EnLH0c42IgeohQ=','CLIENT','2025-09-07 07:47:42.841761',1,NULL),
(14,'Emma Garcia','emma.garcia@email.com','pbkdf2_sha256$1000000$qsxXi0wGB4VAjZM2dYvolR$+/xcsiHGuq2Nyk1DT+4h2F8jD7UYIcIJereuuwESEBU=','CLIENT','2025-09-07 07:47:44.076394',1,NULL),
(16,'Marie Dubois','marie.dubois@gymms.com','pbkdf2_sha256$1000000$u5lt0wSmttJ8jTUJIrQltl$rWkSWIxgJkWgntOBQUPiS/ibVbEW4dx5Co32J4zEDA4=','COACH','2025-09-07 08:57:37.491775',1,NULL),
(17,'Pierre Martin','pierre.martin@gymms.com','pbkdf2_sha256$1000000$Hf4wmfqUdsGd8tPzG8w5QT$kF1rQQxzNXD0Duh3JxFWjPlSUNtJ/RY2zmmM44JTzQQ=','COACH','2025-09-07 08:57:38.486990',1,NULL),
(18,'Sophie Laurent','sophie.laurent@gymms.com','pbkdf2_sha256$1000000$rkAEkEJCtcvImhkYLuYdJo$yM9HSuyNJwPFwTJVoYts88lyGnx73+qXt1oT6Hh+uVc=','COACH','2025-09-07 08:57:39.395026',1,NULL),
(19,'Thomas Bernard','thomas.bernard@gymms.com','pbkdf2_sha256$1000000$l0svivk0Jl2D04YktoMu2j$TlLi+gABOFW+kogffhbTUZbJdELXDaFRG2J1zEPyjr8=','COACH','2025-09-07 08:57:40.272021',1,NULL);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-09-07 15:28:47
