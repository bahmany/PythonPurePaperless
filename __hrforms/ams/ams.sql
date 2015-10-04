/*
SQLyog  v11.01 (32 bit)
MySQL - 5.5.27 : Database - ams
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ams` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_persian_ci */;

USE `ams`;

/*Table structure for table `___dms_owner` */

DROP TABLE IF EXISTS `___dms_owner`;

CREATE TABLE `___dms_owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `expr` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `___dms_owner` */

insert  into `___dms_owner`(`id`,`name`,`expr`) values (1,'صنایع فولاد توان آور آسی',''),(2,'اعهعهاهع','عهاخهعا هعا'),(3,'عغل غعلعخغل','لعغ لغعلعغ');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_persian_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_persian_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_persian_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add owner',7,'add_owner'),(20,'Can change owner',7,'change_owner'),(21,'Can delete owner',7,'delete_owner'),(22,'Can add company',8,'add_company'),(23,'Can change company',8,'change_company'),(24,'Can delete company',8,'delete_company'),(25,'Can add person',9,'add_person'),(26,'Can change person',9,'change_person'),(27,'Can delete person',9,'delete_person'),(28,'Can add chart',10,'add_chart'),(29,'Can change chart',10,'change_chart'),(30,'Can delete chart',10,'delete_chart'),(31,'Can add poses',11,'add_poses'),(32,'Can change poses',11,'change_poses'),(33,'Can delete poses',11,'delete_poses'),(34,'Can add person tels',12,'add_persontels'),(35,'Can change person tels',12,'change_persontels'),(36,'Can delete person tels',12,'delete_persontels'),(37,'Can add dabirkhaneh',13,'add_dabirkhaneh'),(38,'Can change dabirkhaneh',13,'change_dabirkhaneh'),(39,'Can delete dabirkhaneh',13,'delete_dabirkhaneh'),(40,'Can add site',14,'add_site'),(41,'Can change site',14,'change_site'),(42,'Can delete site',14,'delete_site'),(43,'Can add user profile',15,'add_userprofile'),(44,'Can change user profile',15,'change_userprofile'),(45,'Can delete user profile',15,'delete_userprofile');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_persian_ci NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_persian_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_persian_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_persian_ci NOT NULL,
  `email` varchar(75) COLLATE utf8_persian_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$12000$DPymegfkqARY$3e3zAXzzEQufWheqedOMZh3X4JYq3KIcNqh4IfHoscM=','2014-07-09 06:44:23',1,'bahmany','','','',1,1,'2014-06-09 03:53:11');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext COLLATE utf8_persian_ci,
  `object_repr` varchar(200) COLLATE utf8_persian_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_persian_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_persian_ci NOT NULL,
  `app_label` varchar(100) COLLATE utf8_persian_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_persian_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`name`,`app_label`,`model`) values (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'owner','dms','owner'),(8,'company','dms','company'),(9,'person','dms','person'),(10,'chart','dms','chart'),(11,'poses','dms','poses'),(12,'person tels','dms','persontels'),(13,'dabirkhaneh','dms','dabirkhaneh'),(14,'site','sites','site'),(15,'user profile','dms','userprofile');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_persian_ci NOT NULL,
  `session_data` longtext COLLATE utf8_persian_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('1zv044gbbgfo1u28p82vdxcyyjf1mhaj','MmQwOWQ5ZjQyOTMwMzAyYWNkNGMwNjYwMjBlMTdiY2E3NGVjM2M3Njp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-07-23 06:44:23'),('2njcqa2ikn9b3dz2a83boypxrohdxuua','MmQwOWQ5ZjQyOTMwMzAyYWNkNGMwNjYwMjBlMTdiY2E3NGVjM2M3Njp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-06-23 05:19:37');

/*Table structure for table `django_site` */

DROP TABLE IF EXISTS `django_site`;

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) COLLATE utf8_persian_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_persian_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `django_site` */

insert  into `django_site`(`id`,`domain`,`name`) values (1,'example.com','example.com');

/*Table structure for table `dms_chart` */

DROP TABLE IF EXISTS `dms_chart`;

CREATE TABLE `dms_chart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `top_id` int(11) NOT NULL,
  `sort_no` int(11) DEFAULT NULL,
  `ow_id` int(11) NOT NULL,
  `perm` text COLLATE utf8_persian_ci,
  PRIMARY KEY (`id`),
  KEY `dms_chart_d80131ab` (`ow_id`),
  CONSTRAINT `ow_id_refs_id_281f50d8` FOREIGN KEY (`ow_id`) REFERENCES `dms_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_chart` */

insert  into `dms_chart`(`id`,`name`,`top_id`,`sort_no`,`ow_id`,`perm`) values (1,'شرکت صنایع فولاد فرخشهر',0,0,1,NULL),(2,'مدیر عامل',1,1,1,'chk_chart_vl_1___true|||chk_chart_dl_2___true|||chk_chart_dl_1___true|||chk_chart_vl_2___true|||chk_chart_sl_2___true|||chk_chart_sl_1___true|||chk_chart_ss_1___true|||semat_id___2|||chk_chart_ss_2___true|||chk_chart_vs_2___true|||chk_chart_ds_1___true|||chk_chart_ds_2___true|||chk_chart_vs_1___true|||csrfmiddlewaretoken___DQp9WO4Zwvl9lUzph5E8eMXe0ot5dCER'),(31,'معاون فنی',2,NULL,1,'chk_chart_vl_1___true|||chk_chart_dl_1___true|||chk_chart_sl_1___true|||semat_id___31|||chk_chart_ss_2___true|||chk_chart_vs_2___true|||chk_chart_ds_2___true|||csrfmiddlewaretoken___eXN9zZXgyiPMYDVBw1MRGldEz60GeMAC'),(32,'مدیر مالی',2,NULL,1,NULL),(33,'مدیر اداری',2,NULL,1,NULL),(34,'مدیر کارخانه',2,NULL,1,'semat_id___34|||csrfmiddlewaretoken___DQp9WO4Zwvl9lUzph5E8eMXe0ot5dCER|||chk_chart_ds_2___true|||chk_chart_dl_1___true|||chk_chart_ds_3___true'),(35,'سرپرست فناوری',33,NULL,1,NULL),(36,'سرپرست اداری',33,NULL,1,NULL),(37,'سرپرست دبیرخانه',33,NULL,1,NULL),(38,'نیروی انسانی',33,NULL,1,NULL),(39,'مشاور حقوقی',2,NULL,1,NULL),(44,'TOYOTA',0,NULL,65,''),(45,'مدیر عامل',44,NULL,65,'chk_chart_vl_1___true|||chk_chart_dl_2___true|||chk_chart_dl_1___true|||chk_chart_vl_2___true|||chk_chart_sl_2___true|||chk_chart_sl_1___true|||chk_chart_ss_1___true|||semat_id___45|||chk_chart_ss_2___true|||chk_chart_vs_2___true|||chk_chart_ds_1___true|||chk_chart_ds_2___true|||chk_chart_vs_1___true|||csrfmiddlewaretoken___ZW5XvZ6HA75pf7JxL3BXFOZZXzefNLLC'),(48,'مدیر بازرگانی',45,NULL,65,NULL),(49,'مدیر مالی',45,NULL,65,NULL),(50,'مدیر فروش',45,NULL,65,NULL),(51,'مدیر فروش',2,NULL,1,NULL),(52,'مدیر اداری و منابع انسانی',45,NULL,1,NULL),(53,'سرپرست فناوری اطلاعات',52,NULL,1,NULL),(54,'مسئول اداری',52,NULL,1,NULL),(55,'سرپرست حراست',52,NULL,1,NULL),(56,'یلبثقضل',0,NULL,66,''),(57,'مدیر عامل',56,NULL,66,''),(58,'ثقصلثصقل',0,NULL,67,''),(59,'مدیر عامل',58,NULL,67,''),(60,'قثصلصقثل',0,NULL,68,''),(61,'مدیر عامل',60,NULL,68,''),(62,'قثصلصثقل',0,NULL,69,''),(63,'مدیر عامل',62,NULL,69,''),(64,'قلثاثقفاقفا',0,NULL,70,''),(65,'مدیر عامل',64,NULL,70,''),(66,'قلثصقلث',0,NULL,71,''),(67,'مدیر عامل',66,NULL,71,''),(68,'فغتلثصقلثصقل',0,NULL,72,''),(69,'مدیر عامل',68,NULL,72,''),(70,'ثصقلصثلثصقل',0,NULL,73,''),(71,'مدیر عامل',70,NULL,73,''),(72,'صقثلثصقل',0,NULL,74,''),(73,'مدیر عامل',72,NULL,74,'');

/*Table structure for table `dms_company` */

DROP TABLE IF EXISTS `dms_company`;

CREATE TABLE `dms_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `shomare_sabt` varchar(10) COLLATE utf8_persian_ci DEFAULT NULL,
  `sale_sabt` int(11) DEFAULT NULL,
  `code_melli` varchar(20) COLLATE utf8_persian_ci DEFAULT NULL,
  `code_eghtesadi` varchar(20) COLLATE utf8_persian_ci DEFAULT NULL,
  `code_posti` varchar(20) COLLATE utf8_persian_ci DEFAULT NULL,
  `arzesh_afzoodeh` date DEFAULT NULL,
  `zamineh` varchar(400) COLLATE utf8_persian_ci DEFAULT NULL,
  `tels` varchar(100) COLLATE utf8_persian_ci DEFAULT NULL,
  `fax` varchar(50) COLLATE utf8_persian_ci DEFAULT NULL,
  `mail` varchar(50) COLLATE utf8_persian_ci DEFAULT NULL,
  `web` varchar(50) COLLATE utf8_persian_ci DEFAULT NULL,
  `addr1` varchar(600) COLLATE utf8_persian_ci DEFAULT NULL,
  `addr2` varchar(600) COLLATE utf8_persian_ci DEFAULT NULL,
  `date_of_create` datetime DEFAULT NULL,
  `created_user_id` int(11) DEFAULT NULL,
  `ow_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dms_company_d80131ab` (`ow_id`),
  CONSTRAINT `ow_id_refs_id_c607879d` FOREIGN KEY (`ow_id`) REFERENCES `dms_owner` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_company` */

insert  into `dms_company`(`id`,`name`,`shomare_sabt`,`sale_sabt`,`code_melli`,`code_eghtesadi`,`code_posti`,`arzesh_afzoodeh`,`zamineh`,`tels`,`fax`,`mail`,`web`,`addr1`,`addr2`,`date_of_create`,`created_user_id`,`ow_id`) values (1,'شرکت صنایع فولاد فرخشهر','22652',1382,'226554365','65465413','56465465','2013-03-21','صنایع فولادی','8865464654 - 646544648 - 564654654','65465 461 4654','info@tasico.ir','tasico.ir','تهران شهرک غرب - خیابان هرمزان 0 کوچه ششم پلاک 8','شهر کرد شهر کرد شهر کرد شهر کرد شهر کرد شهر کرد ','2014-06-10 08:54:42',-1,1),(2,'شخصیت های حقیقی','',NULL,'','','',NULL,'','','','','','','','2014-06-10 08:55:53',-1,1),(65,'TOYOTA','',NULL,'','','',NULL,'','','','','','','','2014-06-24 12:17:08',-1,1),(66,'یلبثقضل','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:09',-1,1),(67,'ثقصلثصقل','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:12',-1,1),(68,'قثصلصقثل','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:14',-1,1),(69,'قثصلصثقل','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:17',-1,1),(70,'قلثاثقفاقفا','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:20',-1,1),(71,'قلثصقلث','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:22',-1,1),(72,'فغتلثصقلثصقل','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:25',-1,1),(73,'ثصقلصثلثصقل','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:28',-1,1),(74,'صقثلثصقل','',NULL,'','','',NULL,'','','','','','','','2014-07-05 11:07:30',-1,1);

/*Table structure for table `dms_dabirkhaneh` */

DROP TABLE IF EXISTS `dms_dabirkhaneh`;

CREATE TABLE `dms_dabirkhaneh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8_persian_ci NOT NULL,
  `dakheli_letters_format` varchar(200) COLLATE utf8_persian_ci NOT NULL,
  `sadereh_letters_format` varchar(200) COLLATE utf8_persian_ci NOT NULL,
  `varede_letters_format` varchar(200) COLLATE utf8_persian_ci NOT NULL,
  `dakheli_last_id` int(11) DEFAULT NULL,
  `sadere_last_id` int(11) DEFAULT NULL,
  `varede_last_id` int(11) DEFAULT NULL,
  `ow_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dms_dabirkhaneh_d80131ab` (`ow_id`),
  CONSTRAINT `ow_id_refs_id_ffdfe5a9` FOREIGN KEY (`ow_id`) REFERENCES `dms_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_dabirkhaneh` */

insert  into `dms_dabirkhaneh`(`id`,`name`,`dakheli_letters_format`,`sadereh_letters_format`,`varede_letters_format`,`dakheli_last_id`,`sadere_last_id`,`varede_last_id`,`ow_id`) values (1,'دبیر خانه دفتر مرکزی','654564847','658464564','654564847',0,0,0,1),(2,'دبیرخانه کارخانه','5654654','654654654','64',0,0,0,1),(19,'دبیرخانه مرکزی','0','0','0',NULL,NULL,NULL,65),(20,'5e66yhrt','ty','rety','ety',NULL,NULL,NULL,1);

/*Table structure for table `dms_owner` */

DROP TABLE IF EXISTS `dms_owner`;

CREATE TABLE `dms_owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `expr` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `dop` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_owner` */

insert  into `dms_owner`(`id`,`name`,`expr`,`dop`) values (1,'صنایع فولاد فرخشهر','لقثل',NULL),(2,'توانمندسازی بازنشستگان','',NULL),(3,'تواسل','',NULL);

/*Table structure for table `dms_person` */

DROP TABLE IF EXISTS `dms_person`;

CREATE TABLE `dms_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `last_name` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `date_birth` date DEFAULT NULL,
  `mahale_tavalod` varchar(200) COLLATE utf8_persian_ci DEFAULT NULL,
  `shsh` varchar(50) COLLATE utf8_persian_ci DEFAULT NULL,
  `codemelli` varchar(12) COLLATE utf8_persian_ci DEFAULT NULL,
  `father_name` varchar(50) COLLATE utf8_persian_ci DEFAULT NULL,
  `sex` varchar(50) COLLATE utf8_persian_ci DEFAULT NULL,
  `ow_id` int(11) NOT NULL,
  `other_options` text COLLATE utf8_persian_ci,
  `date_of_create` datetime DEFAULT NULL,
  `created_user_id` int(11) DEFAULT NULL,
  `semat_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dms_person_d80131ab` (`ow_id`),
  CONSTRAINT `ow_id_refs_id_db720f74` FOREIGN KEY (`ow_id`) REFERENCES `dms_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_person` */

insert  into `dms_person`(`id`,`first_name`,`last_name`,`date_birth`,`mahale_tavalod`,`shsh`,`codemelli`,`father_name`,`sex`,`ow_id`,`other_options`,`date_of_create`,`created_user_id`,`semat_id`) values (29,'محمد رضا','بهمنی',NULL,'','','','','',1,'txt_dy_t17ctpqp5fhtxt_dy_t14ctpqp5fhtxt_dy_t15ctpqp5fhtxt_dy_t12ctpqp5fhtxt_dy_t13ctpqp5fhtxt_dy_t10ctpqp5fhtxt_dy_t11ctpqp5fhidctpq29p5fhtxt_dy_t18ctpqp5fhtxt_dy_t19ctpqp5fhcsrfmiddlewaretokenctpqDQp9WO4Zwvl9lUzph5E8eMXe0ot5dCERp5fhtxt_dy_t28ctpqp5fhtxt_dy_t27ctpqp5fhtxt_dy_t26ctpqp5fhtxt_dy_t25ctpqp5fhtxt_dy_t24ctpqp5fhtxt_dy_t23ctpqp5fhtxt_dy_t22ctpqp5fhtxt_dy_t21ctpqp5fhtxt_dy_t20ctpqp5fhtxt_dy_t8ctpqp5fhtxt_dy_t9ctpqp5fhtxt_dy_t4ctpqp5fhtxt_dy_t5ctpqp5fhtxt_dy_t6ctpqp5fhtxt_dy_t7ctpqp5fhtxt_dy_t1ctpqp5fhtxt_dy_t2ctpqp5fhtxt_dy_t3ctpq',NULL,NULL,35),(30,'اشکان','سعدوندی',NULL,'','','','','',1,'txt_dy_t17ctpqp5fhtxt_dy_t14ctpqp5fhtxt_dy_t15ctpqp5fhtxt_dy_t12ctpqp5fhtxt_dy_t13ctpqp5fhtxt_dy_t10ctpqp5fhtxt_dy_t11ctpqp5fhidctpq30p5fhtxt_dy_t18ctpqp5fhtxt_dy_t19ctpqp5fhcsrfmiddlewaretokenctpqDQp9WO4Zwvl9lUzph5E8eMXe0ot5dCERp5fhtxt_dy_t28ctpqp5fhtxt_dy_t27ctpqp5fhtxt_dy_t26ctpqp5fhtxt_dy_t25ctpqp5fhtxt_dy_t24ctpqp5fhtxt_dy_t23ctpqp5fhtxt_dy_t22ctpqp5fhtxt_dy_t21ctpqp5fhtxt_dy_t20ctpqp5fhtxt_dy_t8ctpqp5fhtxt_dy_t9ctpqp5fhtxt_dy_t4ctpqp5fhtxt_dy_t5ctpqp5fhtxt_dy_t6ctpqp5fhtxt_dy_t7ctpqp5fhtxt_dy_t1ctpqp5fhtxt_dy_t2ctpqp5fhtxt_dy_t3ctpq',NULL,NULL,33),(31,'ناصر','حجازی',NULL,'','','','','',1,'txt_dy_t17ctpqp5fhtxt_dy_t14ctpqp5fhtxt_dy_t15ctpqp5fhtxt_dy_t12ctpqp5fhtxt_dy_t13ctpqp5fhtxt_dy_t10ctpqp5fhtxt_dy_t11ctpqp5fhidctpq31p5fhtxt_dy_t18ctpqp5fhtxt_dy_t19ctpqp5fhcsrfmiddlewaretokenctpqDQp9WO4Zwvl9lUzph5E8eMXe0ot5dCERp5fhtxt_dy_t28ctpqp5fhtxt_dy_t27ctpqp5fhtxt_dy_t26ctpqp5fhtxt_dy_t25ctpqp5fhtxt_dy_t24ctpqp5fhtxt_dy_t23ctpqp5fhtxt_dy_t22ctpqp5fhtxt_dy_t21ctpqp5fhtxt_dy_t20ctpqp5fhtxt_dy_t8ctpqp5fhtxt_dy_t9ctpqp5fhtxt_dy_t4ctpqp5fhtxt_dy_t5ctpqp5fhtxt_dy_t6ctpqp5fhtxt_dy_t7ctpqp5fhtxt_dy_t1ctpqp5fhtxt_dy_t2ctpqp5fhtxt_dy_t3ctpq',NULL,NULL,36);

/*Table structure for table `dms_persontels` */

DROP TABLE IF EXISTS `dms_persontels`;

CREATE TABLE `dms_persontels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lbl` varchar(50) COLLATE utf8_persian_ci NOT NULL,
  `val` varchar(400) COLLATE utf8_persian_ci DEFAULT NULL,
  `ow_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dms_persontels_d80131ab` (`ow_id`),
  CONSTRAINT `ow_id_refs_id_f9b5e88f` FOREIGN KEY (`ow_id`) REFERENCES `dms_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_persontels` */

/*Table structure for table `dms_poses` */

DROP TABLE IF EXISTS `dms_poses`;

CREATE TABLE `dms_poses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(400) COLLATE utf8_persian_ci NOT NULL,
  `ow_id` int(11) NOT NULL,
  `oc_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dms_poses_d80131ab` (`ow_id`),
  KEY `dms_poses_4705ddba` (`oc_id`),
  CONSTRAINT `oc_id_refs_id_b709d75c` FOREIGN KEY (`oc_id`) REFERENCES `dms_person` (`id`),
  CONSTRAINT `ow_id_refs_id_648844fd` FOREIGN KEY (`ow_id`) REFERENCES `dms_chart` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_poses` */

/*Table structure for table `dms_userprofile` */

DROP TABLE IF EXISTS `dms_userprofile`;

CREATE TABLE `dms_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_b0401643` FOREIGN KEY (`user_id`) REFERENCES `dms_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

/*Data for the table `dms_userprofile` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
