-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get info about the thief happened in this time date year
SELECT description FROM crime_scene_reports WHERE day = 28 AND year = 2021 AND month = 7;

-- Get info where bakery is mentioned
SELECT id, name, transcript FROM interviews WHERE day = 28 AND year = 2021 AND month = 7;

-- Get image about license_plate after 10 mins from the thief
SELECT license_plate, id FROM bakery_security_logs WHERE activity = "exit" AND day = 28 AND year = 2021 AND month = 7 AND hour = 10 AND minute BETWEEN 15 AND 35;

-- Get people's name from license_plate (here, in this list possibly the name of the thief)
SELECT name, passport_number, id FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE activity = "exit" AND day = 28 AND year = 2021 AND month = 7 AND hour = 10 AND minute BETWEEN 10 AND 35);

-- Starting from account number get atm_transaction id on that day and looking in a specific time frame
SELECT account_number FROM atm_transactions WHERE  day = 28 AND year = 2021 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw" AND day = 28;


-- Get info about person_id starting from the person who for sure withdawn some money that morning
SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE  day = 28 AND year = 2021 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw" AND day = 28);


-- Get info about people id from bank between people who have left parking about 10 am and who draft money in the atm close to bakery
SELECT person_id FROM bank_accounts WHERE person_id IN (SELECT id FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE activity = "exit" AND day = 28 AND year = 2021 AND month = 7 AND hour = 10 AND minute BETWEEN 10 AND 35));

-- Get caller and receiver from that day who had spoken less then a minut and
SELECT caller, receiver FROM phone_calls WHERE month = 7 AND year = 2021 AND day = 28 AND duration < 60;

-- Get name and id form people who has the phone's number I just founded caller
SELECT name, id FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND year = 2021 AND day = 28 AND duration < 60);

-- Get name and id form people who has the phone's number I just founded recevier
SELECT name, id FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE month = 7 AND year = 2021 AND day = 28 AND duration < 60);

-- Get info about flight next day
SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20;

-- Get passengers on the earliest flight
SELECT * FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20);

-- Double check thief's number (other option Taylor)
SELECT phone_number from people where name = "Bruce";

-- Checking who called that morning
SELECT name from people where phone_number LIKE "(676) 555-6554";

-- Checking the city
SELECT * FROM airports;
