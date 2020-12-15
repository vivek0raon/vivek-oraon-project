-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 14, 2020 at 08:10 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quizdata`
--

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `question` varchar(50) DEFAULT NULL,
  `option_1` varchar(30) DEFAULT NULL,
  `option_2` varchar(30) DEFAULT NULL,
  `option_3` varchar(30) DEFAULT NULL,
  `option_4` varchar(30) DEFAULT NULL,
  `correct_option` varchar(30) DEFAULT NULL,
  `marks` int(11) DEFAULT NULL,
  `hardness_level` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`question`, `option_1`, `option_2`, `option_3`, `option_4`, `correct_option`, `marks`, `hardness_level`) VALUES
('what is the state capital of jharkhand?', 'jamsedpur', 'dhanbad', 'ranchi', 'hazaribag', 'c', 2, 's'),
('where is brazil located;', 'america', 'south amaerica', 'india', 'europe', 'b', 4, 's'),
('what is cricket?', 'food', 'insect', 'game', 'country', 'c', 1, 's'),
('what sqare root of 4?', '5', '-2', '2', '1', 'c', 5, 'h');

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `name` varchar(30) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`name`, `password`) VALUES
('vivek', 'oraon'),
('jam', 'sam'),
('codi', 'code11'),
('2w3e', '1223'),
('vangens', '321'),
('gg', '132');

-- --------------------------------------------------------

--
-- Table structure for table `u_score`
--

CREATE TABLE `u_score` (
  `name` varchar(30) DEFAULT NULL,
  `s_score` int(11) DEFAULT NULL,
  `m_score` int(11) DEFAULT NULL,
  `h_score` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `u_score`
--

INSERT INTO `u_score` (`name`, `s_score`, `m_score`, `h_score`) VALUES
('codi', 7, 0, 0),
('2w3e', 0, 0, 0),
('vangens', 0, 0, 0),
('gg', 0, 0, 5),
('vivek', 100, 100, 100);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
