-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 25, 2024 at 11:21 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `busticket`
--

-- --------------------------------------------------------

--
-- Table structure for table `buses`
--

CREATE TABLE `buses` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `seat` int NOT NULL,
  `route_id` bigint UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `buses`
--

INSERT INTO `buses` (`id`, `name`, `seat`, `route_id`, `created_at`, `updated_at`) VALUES
(1, 'Lockman, Runolfsson and Corwin Bus', 41, 11, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(2, 'Kunde and Sons Bus', 44, 12, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(3, 'Jacobs, Hauck and Orn Bus', 42, 13, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(4, 'Hickle, Trantow and Carter Bus', 40, 14, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(5, 'Fisher LLC Bus', 37, 15, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(6, 'Wunsch Inc Bus', 31, 16, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(7, 'Gerhold, Price and Wyman Bus', 40, 17, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(8, 'Kerluke, Padberg and Stiedemann Bus', 36, 18, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(9, 'Block, Wehner and Turner Bus', 39, 19, '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(10, 'Grimes Inc Bus', 43, 20, '2024-12-11 22:19:52', '2024-12-11 22:19:52');

-- --------------------------------------------------------

--
-- Table structure for table `bus_schedules`
--

CREATE TABLE `bus_schedules` (
  `id` bigint UNSIGNED NOT NULL,
  `bus_id` bigint UNSIGNED NOT NULL,
  `start_from` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `total_tickets` int NOT NULL,
  `ticket_sold` int NOT NULL DEFAULT '0',
  `remaining_tickets` int NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `bus_schedules`
--

INSERT INTO `bus_schedules` (`id`, `bus_id`, `start_from`, `date`, `time`, `total_tickets`, `ticket_sold`, `remaining_tickets`, `price`, `created_at`, `updated_at`) VALUES
(1, 3, 'rangpur', '2024-12-27', '14:30:00', 50, 42, 37, 123.00, '2024-12-11 22:20:02', '2024-12-11 22:40:48'),
(2, 3, 'Uttara', '2024-12-15', '14:30:00', 50, 50, 0, 123.00, '2024-12-11 22:40:34', '2024-12-11 22:41:29');

-- --------------------------------------------------------

--
-- Table structure for table `failed_jobs`
--

CREATE TABLE `failed_jobs` (
  `id` bigint UNSIGNED NOT NULL,
  `uuid` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_100000_create_password_reset_tokens_table', 1),
(2, '2019_08_19_000000_create_failed_jobs_table', 1),
(3, '2019_12_14_000001_create_personal_access_tokens_table', 1),
(4, '2024_12_11_091903_create_roles_table', 1),
(5, '2024_12_11_091904_create_users_table', 1),
(6, '2024_12_11_131238_create_routes_table', 1),
(7, '2024_12_11_131932_create_buses_table', 1),
(8, '2024_12_11_140106_create_bus_schedules_table', 1),
(9, '2024_12_12_033557_create_tickets_table', 1);

-- --------------------------------------------------------

--
-- Table structure for table `password_reset_tokens`
--

CREATE TABLE `password_reset_tokens` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `personal_access_tokens`
--

CREATE TABLE `personal_access_tokens` (
  `id` bigint UNSIGNED NOT NULL,
  `tokenable_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tokenable_id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `abilities` text COLLATE utf8mb4_unicode_ci,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `expires_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `created_at`, `updated_at`) VALUES
(1, 'Admin', '2024-12-11 22:19:51', '2024-12-11 22:19:51'),
(2, 'User', '2024-12-11 22:19:51', '2024-12-11 22:19:51');

-- --------------------------------------------------------

--
-- Table structure for table `routes`
--

CREATE TABLE `routes` (
  `id` bigint UNSIGNED NOT NULL,
  `route_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `routes`
--

INSERT INTO `routes` (`id`, `route_name`, `created_at`, `updated_at`) VALUES
(1, 'Dhaka - Chittagong', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(2, 'Dhaka - Sylhet', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(3, 'Dhaka - Cox\'s Bazar', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(4, 'Dhaka - Rajshahi', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(5, 'Dhaka - Khulna', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(6, 'Dhaka - Rangpur', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(7, 'Dhaka - Barisal', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(8, 'Chittagong - Cox\'s Bazar', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(9, 'Sylhet - Khulna', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(10, 'Dinajpur - Dhaka', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(11, 'South Lazarohaven - Devonport', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(12, 'Krajcikfort - North Cory', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(13, 'South Stephan - Buckridgeshire', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(14, 'Cheyannehaven - North Katelyn', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(15, 'Lucindaland - Deckowfurt', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(16, 'Annettaland - Hackettview', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(17, 'Hauckborough - New Corene', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(18, 'Port Hiram - North Casey', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(19, 'Rowlandmouth - Abigailstad', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(20, 'Ettiestad - Mohamedchester', '2024-12-11 22:19:52', '2024-12-11 22:19:52');

-- --------------------------------------------------------

--
-- Table structure for table `tickets`
--

CREATE TABLE `tickets` (
  `id` bigint UNSIGNED NOT NULL,
  `schedule_id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED NOT NULL,
  `payment_status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'pending',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tickets`
--

INSERT INTO `tickets` (`id`, `schedule_id`, `user_id`, `payment_status`, `created_at`, `updated_at`) VALUES
(3, 1, 11, 'completed', '2024-12-11 22:36:43', '2024-12-11 22:36:43'),
(4, 1, 11, 'completed', '2024-12-11 22:37:13', '2024-12-11 22:37:13'),
(5, 1, 11, 'completed', '2024-12-11 22:39:14', '2024-12-11 22:39:14'),
(6, 1, 11, 'completed', '2024-12-11 22:40:46', '2024-12-11 22:40:46'),
(7, 1, 11, 'completed', '2024-12-11 22:40:48', '2024-12-11 22:40:48'),
(8, 2, 11, 'completed', '2024-12-11 22:41:29', '2024-12-11 22:41:29');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role_id` bigint UNSIGNED NOT NULL DEFAULT '2',
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `email_verified_at`, `password`, `role_id`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, 'Crystal Jacobson', 'dkreiger@example.com', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, '6ifxAzs7Mp', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(2, 'Dena Reinger', 'grace01@example.com', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, 'DUuSnEkBxH', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(3, 'Tamara Quitzon', 'qrussel@example.org', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, 'QsUmy5re3o', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(4, 'Mr. Donnie Schuppe', 'dewitt.deckow@example.net', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, 'yC6T1tcNKJ', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(5, 'Sydnee Kemmer DVM', 'treutel.willa@example.com', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, '3uQQbnEorN', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(6, 'Issac Sipes', 'zwintheiser@example.com', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, 'PB2QEC3TmO', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(7, 'Donald Nienow', 'hbradtke@example.net', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, 'bAh5bbLs71', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(8, 'Kayli Larkin', 'walker91@example.com', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, 'F3aAmINOAE', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(9, 'Kamron Ledner', 'ahmed.batz@example.net', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, '9zG6156RkI', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(10, 'Jude Wisozk', 'ohara.freddie@example.com', '2024-12-11 22:19:52', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 2, 'yq92oe10oO', '2024-12-11 22:19:52', '2024-12-11 22:19:52'),
(11, 'zabeer', 'z@gmail.com', '2024-12-11 22:19:52', '$2y$10$4f2BtNINell0ymzyYL1pAux0v7fXC72FZwhyAUyFo.og7it7Mf8Pu', 1, 'ltmYrpHadX', '2024-12-11 22:19:52', '2024-12-11 22:19:52');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buses`
--
ALTER TABLE `buses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `buses_route_id_foreign` (`route_id`);

--
-- Indexes for table `bus_schedules`
--
ALTER TABLE `bus_schedules`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bus_schedules_bus_id_foreign` (`bus_id`);

--
-- Indexes for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  ADD KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roles_name_unique` (`name`);

--
-- Indexes for table `routes`
--
ALTER TABLE `routes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `routes_route_name_unique` (`route_name`);

--
-- Indexes for table `tickets`
--
ALTER TABLE `tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tickets_schedule_id_foreign` (`schedule_id`),
  ADD KEY `tickets_user_id_foreign` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`),
  ADD KEY `users_role_id_foreign` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buses`
--
ALTER TABLE `buses`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `bus_schedules`
--
ALTER TABLE `bus_schedules`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `routes`
--
ALTER TABLE `routes`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `tickets`
--
ALTER TABLE `tickets`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buses`
--
ALTER TABLE `buses`
  ADD CONSTRAINT `buses_route_id_foreign` FOREIGN KEY (`route_id`) REFERENCES `routes` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `bus_schedules`
--
ALTER TABLE `bus_schedules`
  ADD CONSTRAINT `bus_schedules_bus_id_foreign` FOREIGN KEY (`bus_id`) REFERENCES `buses` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `tickets`
--
ALTER TABLE `tickets`
  ADD CONSTRAINT `tickets_schedule_id_foreign` FOREIGN KEY (`schedule_id`) REFERENCES `bus_schedules` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `tickets_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_role_id_foreign` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
