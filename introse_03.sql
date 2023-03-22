-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2023 at 12:28 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `introse_03`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cart_id` varchar(40) NOT NULL,
  `userid` varchar(40) DEFAULT NULL,
  `ISBN` varchar(13) DEFAULT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `orderid` varchar(40) NOT NULL,
  `ISBN` varchar(13) DEFAULT NULL,
  `title` varchar(40) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `subtotal` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `ISBN` varchar(13) NOT NULL,
  `title` varchar(40) DEFAULT NULL,
  `author` varchar(40) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `genre` varchar(40) DEFAULT NULL,
  `pubYear` int(4) DEFAULT NULL,
  `publisher` varchar(40) DEFAULT NULL,
  `susFlag` int(11) NOT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`ISBN`, `title`, `author`, `stock`, `genre`, `pubYear`, `publisher`, `susFlag`, `price`) VALUES
('9780078022128', 'Software Engineering: A Practicioners Ap', 'Roger S. Pressman', 30, 'Educational', 2014, 'McGraw Hill', 0, 120.98),
('9780553328257', 'The Complete Sherlock Holmes', 'Sir Arthur Conan Doyle', 50, 'Mystery', 1986, 'Bantam Classics', 0, 28.49),
('9780691173221', 'The Original Folk and Fairy Tales of the', 'Jacob & Wilhelm Grimm', 37, 'Fantasy', 2016, 'Princeton University Press', 0, 25.99),
('9781119680451', 'Java for Dummies', 'Doug Lowe', 42, 'Educational', 2020, 'For Dummies', 0, 15.5),
('9781338298482', 'Five Nights At Freddys: The Silver Eyes', 'Scott Cawthon', 83, 'Nonfiction', 2019, 'Scholastic Inc.', 1, 19.87);

-- --------------------------------------------------------

--
-- Table structure for table `orderhist`
--

CREATE TABLE `orderhist` (
  `orderid` varchar(40) NOT NULL,
  `datecreated` varchar(40) DEFAULT NULL,
  `dateshipped` varchar(40) DEFAULT NULL,
  `userid` varchar(40) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `people`
--

CREATE TABLE `people` (
  `userid` varchar(40) NOT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `lastname` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `phone` varchar(14) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `type` varchar(1) NOT NULL,
  `susflag` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `people`
--

INSERT INTO `people` (`userid`, `firstname`, `lastname`, `password`, `phone`, `email`, `type`, `susflag`) VALUES
('001', 'Lisa', 'Simpson', 'mangoes', '662-294-9959', 'ls4@gmail.com', 'C', 0),
('002', 'John', 'Cena', 'cantseem3', '554-454-5544', 'jcena@gmail.com', 'C', 0),
('003', 'Charan', 'Gudla', 'Ag1le', '804-928-4768', 'gudla@cse.msstate.edu', 'A', 0),
('004', 'Edgar', 'Poe', 'R4v3n', '777-456-2324', 'egdypoetman@gmail.com', 'S', 0),
('005', 'John', 'Doe', 'an0nym0us', '575-349-9999', 'johndoe@gmail.com', 'S', 1),
('006', 'Josh', 'Crowson', 'turtl3s', '662-295-4432', 'turtl3lover@gmail.com', 'A', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cart_id`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`orderid`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`ISBN`);

--
-- Indexes for table `orderhist`
--
ALTER TABLE `orderhist`
  ADD PRIMARY KEY (`orderid`);

--
-- Indexes for table `people`
--
ALTER TABLE `people`
  ADD PRIMARY KEY (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
