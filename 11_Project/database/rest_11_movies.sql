-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 02, 2024 at 04:52 AM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rest_11_movies`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add my stream platform', 7, 'add_mystreamplatform'),
(26, 'Can change my stream platform', 7, 'change_mystreamplatform'),
(27, 'Can delete my stream platform', 7, 'delete_mystreamplatform'),
(28, 'Can view my stream platform', 7, 'view_mystreamplatform'),
(29, 'Can add my watchlist', 8, 'add_mywatchlist'),
(30, 'Can change my watchlist', 8, 'change_mywatchlist'),
(31, 'Can delete my watchlist', 8, 'delete_mywatchlist'),
(32, 'Can view my watchlist', 8, 'view_mywatchlist'),
(33, 'Can add review', 9, 'add_review'),
(34, 'Can change review', 9, 'change_review'),
(35, 'Can delete review', 9, 'delete_review'),
(36, 'Can view review', 9, 'view_review'),
(37, 'Can add my review', 10, 'add_myreview'),
(38, 'Can change my review', 10, 'change_myreview'),
(39, 'Can delete my review', 10, 'delete_myreview'),
(40, 'Can view my review', 10, 'view_myreview');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$RFzpi6aFpGbdq3JzHnrKSe$VXtQjKKdbXHh/eqQOAqEOIIaetcUNIfBOwUu4LIlU4g=', '2024-08-01 09:43:21.587791', 1, 'siva', '', '', '', 1, 1, '2024-08-01 09:43:02.595096');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-08-01 09:45:23.216628', '1', 'NetFlix', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-08-01 09:45:33.831779', '2', 'Youtube', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-08-01 09:45:44.603906', '3', 'Spotify', 1, '[{\"added\": {}}]', 7, 1),
(4, '2024-08-01 09:46:20.385686', '1', 'Teamwork', 1, '[{\"added\": {}}]', 8, 1),
(5, '2024-08-01 09:46:41.026105', '2', 'Great Django', 1, '[{\"added\": {}}]', 8, 1),
(6, '2024-08-01 09:47:46.893638', '1', 'Review object (1)', 1, '[{\"added\": {}}]', 9, 1),
(7, '2024-08-01 09:48:45.362848', '1', 'Review object (1)', 2, '[]', 9, 1),
(8, '2024-08-01 09:49:20.689701', '1', ' Teamwork  2 star', 2, '[{\"changed\": {\"fields\": [\"Rating\"]}}]', 9, 1),
(9, '2024-08-01 09:53:39.743553', '1', ' Great Django  3 star', 1, '[{\"added\": {}}]', 10, 1),
(10, '2024-08-01 09:53:59.030220', '2', ' Teamwork  5 star', 1, '[{\"added\": {}}]', 10, 1),
(11, '2024-08-01 09:54:23.096060', '3', ' Teamwork  4 star', 1, '[{\"added\": {}}]', 10, 1),
(12, '2024-08-01 10:13:45.570121', '3', 'Python specialist', 1, '[{\"added\": {}}]', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'Movieapp', 'mystreamplatform'),
(8, 'Movieapp', 'mywatchlist'),
(9, 'Movieapp', 'review'),
(10, 'Movieapp', 'myreview');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Movieapp', '0001_initial', '2024-08-01 09:35:23.697995'),
(2, 'contenttypes', '0001_initial', '2024-08-01 09:35:23.962947'),
(3, 'auth', '0001_initial', '2024-08-01 09:35:29.296074'),
(4, 'admin', '0001_initial', '2024-08-01 09:35:30.758764'),
(5, 'admin', '0002_logentry_remove_auto_add', '2024-08-01 09:35:30.772768'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-01 09:35:30.784764'),
(7, 'contenttypes', '0002_remove_content_type_name', '2024-08-01 09:35:31.805608'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-08-01 09:35:32.190517'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-08-01 09:35:32.477467'),
(10, 'auth', '0004_alter_user_username_opts', '2024-08-01 09:35:32.488464'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-08-01 09:35:32.739420'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-08-01 09:35:32.759454'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-08-01 09:35:32.770416'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-08-01 09:35:32.969383'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-08-01 09:35:33.158349'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-08-01 09:35:33.378310'),
(17, 'auth', '0011_update_proxy_permissions', '2024-08-01 09:35:33.397305'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-08-01 09:35:33.645263'),
(19, 'sessions', '0001_initial', '2024-08-01 09:35:33.896267'),
(20, 'Movieapp', '0002_myreview_delete_review', '2024-08-01 09:52:57.048983');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('b61lxowgk1a3u1tdisj88gwaerqz4zf1', '.eJxVjEEOwiAQRe_C2hAGoaBL956hmRkYqRpISrsy3l2bdKHb_977LzXiupRx7Xkep6TOCtThdyPkR64bSHest6a51WWeSG-K3mnX15by87K7fwcFe_nWZvCRkknihJEDCAEgEYRjdCQJsxUvQC4DGEsnPziD3vrgAwNwZPX-AARoOEE:1sZSLB:55gwXXFikb-zAiHYLm99kN9DKzfWNZHXh9l1jE9mqSw', '2024-08-15 09:43:21.590790');

-- --------------------------------------------------------

--
-- Table structure for table `movieapp_myreview`
--

DROP TABLE IF EXISTS `movieapp_myreview`;
CREATE TABLE IF NOT EXISTS `movieapp_myreview` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` bigint UNSIGNED NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `update` datetime(6) NOT NULL,
  `watchlist_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Movieapp_myreview_watchlist_id_2911ebf8` (`watchlist_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `movieapp_myreview`
--

INSERT INTO `movieapp_myreview` (`id`, `rating`, `description`, `active`, `created`, `update`, `watchlist_id`) VALUES
(1, 3, 'Good', 1, '2024-08-01 09:53:39.741602', '2024-08-01 09:53:39.741602', 2),
(2, 1, 'good', 0, '2024-08-01 09:53:59.028252', '2024-08-01 11:20:14.269491', 1),
(3, 4, 'Excellent to Learn', 1, '2024-08-01 09:54:23.096060', '2024-08-01 09:54:23.096060', 1),
(4, 1, 'Best Ever', 1, '2024-08-01 11:00:25.884491', '2024-08-01 11:00:25.885441', 1);

-- --------------------------------------------------------

--
-- Table structure for table `movieapp_mystreamplatform`
--

DROP TABLE IF EXISTS `movieapp_mystreamplatform`;
CREATE TABLE IF NOT EXISTS `movieapp_mystreamplatform` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `about` varchar(150) NOT NULL,
  `website` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `movieapp_mystreamplatform`
--

INSERT INTO `movieapp_mystreamplatform` (`id`, `name`, `about`, `website`) VALUES
(1, 'NetFlix', 'Prime Videos', 'https://www.netflix.com/in/'),
(2, 'Youtube', 'Free Videos', 'https://www.youtube.com/'),
(3, 'Spotify', 'Play your Music', 'https://www.spotify.com/'),
(4, 'ee', 'ee', 'https://www.eee.com/');

-- --------------------------------------------------------

--
-- Table structure for table `movieapp_mywatchlist`
--

DROP TABLE IF EXISTS `movieapp_mywatchlist`;
CREATE TABLE IF NOT EXISTS `movieapp_mywatchlist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `storyline` varchar(200) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created` date NOT NULL,
  `platform_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Movieapp_mywatchlist_platform_id_4b65cd9f` (`platform_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `movieapp_mywatchlist`
--

INSERT INTO `movieapp_mywatchlist` (`id`, `title`, `storyline`, `active`, `created`, `platform_id`) VALUES
(1, 'Teamwork', 'Unity', 1, '2024-08-01', 2),
(2, 'Great Django', 'Django Heartbeats', 1, '2024-08-01', 1),
(3, 'Python specialist', 'Thrilling Learning', 1, '2024-08-01', 1),
(4, 'Python specialist', 'Thrilling Learning', 1, '2024-08-01', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
