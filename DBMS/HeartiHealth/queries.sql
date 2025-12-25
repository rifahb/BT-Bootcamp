-- Heartihealth DB
-- SQL Queries 1 to 51
-- PostgreSQL Compatible
-- =============================================

-- 1. Get all the predictions
SELECT
c.cardio_id,
c.cardioarrestdetected,
c.diagnosis_date,
m.member_id,
m.firstname,
m.lastname
FROM cardiodiagnosis c
JOIN memberinfo m
ON c.memberinfo_member_id = m.member_id;

-- 2. Get all the predictions for the day
SELECT
c.cardio_id,
c.cardioarrestdetected,
c.diagnosis_date,
m.member_id,
m.firstname,
m.lastname
FROM cardiodiagnosis c
JOIN memberinfo m
ON c.memberinfo_member_id = m.member_id
WHERE DATE(c.diagnosis_date) = CURRENT_DATE;

-- 3. Get all the predictions for the day sorted by highest probability
SELECT
c.cardio_id,
c.cardioarrestdetected,
c.diagnosis_date,
m.member_id,
m.firstname,
m.lastname
FROM cardiodiagnosis c
JOIN memberinfo m
ON c.memberinfo_member_id = m.member_id
WHERE DATE(c.diagnosis_date) = CURRENT_DATE
ORDER BY c.cardioarrestdetected DESC;

-- 4. Get all unique cities
SELECT DISTINCT city FROM addressinfo;

-- 5. Members from city 'Burgos'
SELECT m.member_id, m.firstname, m.lastname, a.city
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Burgos';

-- 6. Members from city 'Flora'
SELECT m.member_id, m.firstname, m.lastname, a.city
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Flora';

-- 7. Total blood tests for Aisha
SELECT COUNT(*) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE LOWER(m.firstname) = 'aisha';

-- 8. X-ray details of Ajay on 26-Jan-2019
SELECT x.xray_id, x.xray_date, x.ca
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE LOWER(m.firstname) = 'ajay'
AND DATE(c.diagnosis_date) = '2019-01-26';

-- 9. Members from cities Burgos and Flora
SELECT DISTINCT m.member_id, m.firstname, m.lastname, a.city
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city IN ('Burgos', 'Flora');

-- 10. Total blood tests for Aberson
SELECT COUNT(*) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'Aberson';

-- 11. Address details for member M303
SELECT * FROM addressinfo WHERE memberinfo_member_id = 'M303';

-- 12. X-ray details for cardio ID CID122
SELECT * FROM xray WHERE cardiodiagnosis_cardio_id = 'cid122';

-- 13. Symptoms for cardio IDs CID250 and CID300
SELECT * FROM symptom WHERE cardiodiagnosis_cardio_id IN ('cid250','cid300');

-- 14. Symptoms for July 2019
SELECT * FROM symptom
WHERE EXTRACT(MONTH FROM symptom_date) = 7
AND EXTRACT(YEAR FROM symptom_date) = 2019;

-- 15. X-ray details for last name 'Dailley'
SELECT x.xray_id, x.xray_date, x.ca
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.lastname ILIKE 'Dailley';

-- 16. Wearable data for cardio IDs between CID100 and CID200
SELECT * FROM wearabledevicedata
WHERE cardiodiagnosis_cardio_id BETWEEN 'cid100' AND 'cid200';

-- 17. Cardio diagnosis where first name starts with A
SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname ILIKE 'A%';

-- 18. Cardio diagnosis where first name starts and ends with A
SELECT c.*, m.firstname
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname ILIKE 'A%A';

-- 19. All members
SELECT * FROM memberinfo;

-- 20. All addresses
SELECT * FROM addressinfo;

-- 21. Wearable device info
SELECT * FROM wearabledevicedata;

-- 22. All blood tests
SELECT * FROM bloodtest;

-- 23. Members aged > 50
SELECT * FROM memberinfo WHERE age > 50;

-- 24. Addresses from city Flora
SELECT * FROM addressinfo WHERE city = 'Flora';

-- 25. Unique states
SELECT DISTINCT state FROM addressinfo;

-- 26. Total members
SELECT COUNT(*) AS total_members FROM memberinfo;

-- 27. Total blood tests
SELECT COUNT(*) AS total_blood_tests FROM bloodtest;

-- 28. Average cholesterol
SELECT AVG(serumcholesterol) AS avg_cholesterol FROM bloodtest;

-- 29. Maximum peak value
SELECT MAX(oldpeak) AS max_peak_value FROM symptom;

-- 30. Tests between Jan 2015 and Jan 2019
SELECT * FROM bloodtest
WHERE test_date BETWEEN '2015-01-01' AND '2019-01-31 23:59:59';

-- 31. Male and female count aged 50-60
SELECT gender, COUNT(*) AS total_count
FROM memberinfo
WHERE age BETWEEN 50 AND 60
GROUP BY gender;

-- 32. Blood pressure between 100 and 200
SELECT * FROM bloodtest WHERE bloodpressure BETWEEN 100 AND 200;

-- 33. Symptoms diagnosed for patients
SELECT m.firstname, m.lastname, s.symptom_date, s.exang, s.oldpeak, s.cp
FROM symptom s
JOIN cardiodiagnosis c ON s.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id;

-- 34. Average age of patients
SELECT AVG(age) AS average_age FROM memberinfo;

-- 35. Total cities per state
SELECT state, COUNT(DISTINCT city) AS total_cities
FROM addressinfo
GROUP BY state;

-- 36. Patient count by age group
SELECT
CASE
WHEN age BETWEEN 10 AND 20 THEN '10-20'
WHEN age BETWEEN 21 AND 30 THEN '20-30'
WHEN age BETWEEN 31 AND 40 THEN '30-40'
WHEN age BETWEEN 41 AND 50 THEN '40-50'
WHEN age BETWEEN 51 AND 60 THEN '50-60'
WHEN age BETWEEN 61 AND 70 THEN '60-70'
END AS age_group,
COUNT(*) AS patient_count
FROM memberinfo
WHERE age BETWEEN 10 AND 70
GROUP BY age_group
ORDER BY age_group;

-- 37. Members and addresses
SELECT m.member_id, m.firstname, m.lastname, a.city, a.state, a.country, a.pincode
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id;

-- 38. Members and cardio history
SELECT m.member_id, m.firstname, m.lastname, c.cardio_id, c.cardioarrestdetected, c.diagnosis_date
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id;

-- 39. Members and diseases
SELECT m.member_id, m.firstname, m.lastname, d.disease_id, d.diagnoseddate, d.recovereddate, d.isrecovered
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id;

-- 40. Females diagnosed with heart attack
SELECT m.member_id, m.firstname, m.lastname, m.gender, c.cardio_id, c.diagnosis_date
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = 'Female' AND c.cardioarrestdetected = 1;

-- 41. Female members aged > 50 with cardio info
SELECT m.member_id, m.firstname, m.lastname, m.age, c.cardio_id, c.cardioarrestdetected, c.diagnosis_date
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = 'Female' AND m.age > 50;

-- 42. Males with BP > 140 and no heart attack
SELECT DISTINCT m.member_id, m.firstname, m.lastname, b.bloodpressure
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.gender = 'Male' AND b.bloodpressure > 140 AND c.cardioarrestdetected = 0;

-- 43. Heart attack patients from Mountain Province
SELECT DISTINCT m.member_id, m.firstname, m.lastname, a.state
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE a.state = 'Mountain Province' AND c.cardioarrestdetected = 1;

-- 44. Male members < 40 with diseases and symptoms
SELECT m.member_id, m.firstname, m.lastname, d.disease_id, s.exang, s.oldpeak, s.cp
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE m.gender = 'Male' AND m.age < 40;

-- 45. Count members from Mountain Province aged 50-60
SELECT COUNT(*) AS member_count
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Mountain Province' AND m.age BETWEEN 50 AND 60;

-- 46. Count male/female with BP > 140 and heart attack
SELECT m.gender, COUNT(DISTINCT m.member_id) AS count
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE b.bloodpressure > 140 AND c.cardioarrestdetected = 1
GROUP BY m.gender;

-- 47. Avg BP for age groups 40-50 and 50-60
SELECT
CASE
WHEN m.age BETWEEN 40 AND 50 THEN '40-50'
WHEN m.age BETWEEN 50 AND 60 THEN '50-60'
END AS age_group,
AVG(b.bloodpressure) AS avg_bp
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.age BETWEEN 40 AND 60
GROUP BY age_group;

-- 48. Diseases for BP 120-180 sorted by gender
SELECT m.gender, d.disease_id, d.diagnoseddate
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
JOIN diseasedetail d ON c.cardio_id = d.cardiodiagnosis_cardio_id
WHERE b.bloodpressure BETWEEN 120 AND 180
ORDER BY m.gender;

-- 49. Monthly X-ray count from Special Province
SELECT DATE_TRUNC('month', x.xray_date) AS month, COUNT(DISTINCT x.xray_id) AS xray_count
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Special Province'
GROUP BY month
ORDER BY month;

-- 50. Avg age of heart attack patients per state and gender
SELECT a.state, m.gender, AVG(m.age) AS avg_age
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE c.cardioarrestdetected = 1
GROUP BY a.state, m.gender;

-- 51. Heart attack count per state with slope=2 and X-ray & symptom
SELECT a.state, COUNT(DISTINCT m.member_id) AS patient_count
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN wearabledevicedata w ON c.cardio_id = w.cardiodiagnosis_cardio_id
JOIN xray x ON c.cardio_id = x.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE c.cardioarrestdetected = 1 AND w.slope = 2
GROUP BY a.state;

-- ===============================
-- END OF FILE
-- ===============================
