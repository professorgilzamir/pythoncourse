-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 08-Jun-2017 às 16:16
-- Versão do servidor: 5.7.11
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `socialink`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `endereco`
--

CREATE TABLE `endereco` (
  `id` int(11) NOT NULL,
  `logradouro` varchar(500) NOT NULL,
  `bairro` varchar(500) NOT NULL,
  `telefone` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `localizacaogeografica`
--

CREATE TABLE `localizacaogeografica` (
  `ID` int(11) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `localizacaogeografica`
--

INSERT INTO `localizacaogeografica` (`ID`, `latitude`, `longitude`) VALUES
(1, -10.9112, -37.0621);

-- --------------------------------------------------------

--
-- Estrutura da tabela `unidadesaude`
--

CREATE TABLE `unidadesaude` (
  `id` int(11) NOT NULL,
  `idLocGeo` int(11) NOT NULL,
  `idEndereco` int(11) NOT NULL,
  `dscEstFisAmb` varchar(500) NOT NULL,
  `dscAdapFisdo` varchar(500) NOT NULL,
  `sitEquipamentos` varchar(500) NOT NULL,
  `nome` varchar(500) NOT NULL,
  `cnes` varchar(100) NOT NULL,
  `codigo_cidade` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `endereco`
--
ALTER TABLE `endereco`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `localizacaogeografica`
--
ALTER TABLE `localizacaogeografica`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `unidadesaude`
--
ALTER TABLE `unidadesaude`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cnes_unique` (`cnes`),
  ADD KEY `idLocGeo` (`idLocGeo`),
  ADD KEY `idEndereco` (`idEndereco`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `endereco`
--
ALTER TABLE `endereco`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `localizacaogeografica`
--
ALTER TABLE `localizacaogeografica`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `unidadesaude`
--
ALTER TABLE `unidadesaude`
  ADD CONSTRAINT `unidadesaude_ibfk_1` FOREIGN KEY (`idLocGeo`) REFERENCES `localizacaogeografica` (`ID`),
  ADD CONSTRAINT `unidadesaude_ibfk_2` FOREIGN KEY (`idEndereco`) REFERENCES `endereco` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
