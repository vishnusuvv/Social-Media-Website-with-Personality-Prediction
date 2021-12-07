/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - social_media_platformrajagiri
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`social_media_platformrajagiri` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `social_media_platformrajagiri`;

/*Table structure for table `activities` */

DROP TABLE IF EXISTS `activities`;

CREATE TABLE `activities` (
  `activity_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `activity_details` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `activities` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(250) DEFAULT NULL,
  `date_time` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`receiver_id`,`message`,`date_time`) values (1,1,2,'hi','2021-03-28 22:54:48'),(2,1,2,'bro','2021-03-28 22:54:59'),(3,1,2,'hai','2021-03-29 01:24:13'),(4,1,2,'hai','2021-03-29 01:30:00'),(5,2,1,'ya','2021-03-29 01:30:23'),(6,2,1,'para','2021-03-29 01:31:47'),(7,1,2,'oo nth','2021-03-29 01:32:11'),(8,3,2,'da aliyaa','2021-03-29 01:33:18'),(9,2,2,'hi','2021-03-29 01:33:47'),(10,1,1,'aah','2021-03-29 01:34:10'),(11,3,2,'aada para','2021-03-29 01:35:42'),(12,3,1,'hi','2021-03-29 01:35:59'),(13,1,3,'who r u?','2021-03-29 01:36:22');

/*Table structure for table `comments` */

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `comment` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `comments` */

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(111) DEFAULT NULL,
  `reply` varchar(111) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback_details` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `friends` */

DROP TABLE IF EXISTS `friends`;

CREATE TABLE `friends` (
  `friend_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `fid` int(11) DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`friend_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `friends` */

insert  into `friends`(`friend_id`,`user_id`,`fid`,`status`) values (1,2,1,'accepted'),(2,1,3,'accepted'),(3,3,1,'accepted'),(4,3,2,'requested');

/*Table structure for table `keywords` */

DROP TABLE IF EXISTS `keywords`;

CREATE TABLE `keywords` (
  `keyword_id` int(11) NOT NULL AUTO_INCREMENT,
  `sentiment_id` int(11) DEFAULT NULL,
  `keyword` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`keyword_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `keywords` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(111) DEFAULT NULL,
  `password` varchar(111) DEFAULT NULL,
  `usertype` varbinary(111) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'user','user','user'),(3,'user1','user1','user'),(4,'user2','user2','user');

/*Table structure for table `posts` */

DROP TABLE IF EXISTS `posts`;

CREATE TABLE `posts` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(111) DEFAULT NULL,
  `post_content` varchar(111) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  `personality` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `posts` */

insert  into `posts`(`post_id`,`user_id`,`title`,`post_content`,`image`,`date`,`status`,`personality`) values (1,2,'good morning','kdvnjk','static/posts/c9e326de-4632-41f8-b555-0c7b3326802dgrape.jpg','2021-04-06','pending','ESTP'),(2,2,'bad work','xnvk','static/posts/a0e55cb3-35a8-4d1f-bd8e-0444258c6ddahawthorn.jpg','2021-04-06','pending','ISTJ');

/*Table structure for table `reports` */

DROP TABLE IF EXISTS `reports`;

CREATE TABLE `reports` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `reason` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `reports` */

/*Table structure for table `sentiment_types` */

DROP TABLE IF EXISTS `sentiment_types`;

CREATE TABLE `sentiment_types` (
  `sentiment_id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` varchar(111) DEFAULT NULL,
  `age` varchar(111) DEFAULT NULL,
  `openness` varchar(111) DEFAULT NULL,
  `neuroticism` varchar(111) DEFAULT NULL,
  `conscientiousness` varchar(111) DEFAULT NULL,
  `agreeableness` varchar(111) DEFAULT NULL,
  `extraversion` varchar(111) DEFAULT NULL,
  `personality` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`sentiment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `sentiment_types` */

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `gender` varchar(111) DEFAULT NULL,
  `dob` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`first_name`,`last_name`,`gender`,`dob`,`phone`,`email`) values (1,2,'ananthu','prasad','male','2021-03-17','7678975477','blandrover@gmail.com'),(2,3,'surya','dev','male','2021-03-19','8945345665','sury@mailinator.com'),(3,4,'Fuller Harmon','Todd French','male','1996-09-21','+1 (528) 911-1673','vudydi@mailinator.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
