



accountMySQL = "SELECT * FROM wt_user WHERE id = {}"

accountMySQL2 = "Update wt_user set age = {} , gender = '{}', weight_pound = {}, height_cm = {} WHERE id = {};"

# MYQL_SC = "INSERT INTO workout(workout_name, hours, workout_set, workout_rep, log_number) VALUES('{}',{},{},{},{});"
accountMySQL3 =\
"""
SELECT CAST(avg(protein) AS UNSIGNED) AS PA
FROM workouttracker.food_drink AS FD, workouttracker.tracker_log AS TL
WHERE TL.log_number= FD.log_number AND TL.id = {} AND TL.log_date 
BETWEEN DATE_SUB(CURDATE(), INTERVAL 7 DAY) AND CURDATE();
"""

accountMySQL4 =\
"""
SELECT COUNT(TL.log_number) AS CL FROM workouttracker.workout AS WO, workouttracker.tracker_log AS TL
WHERE  WO.hours >= 1 AND WO.log_number = TL.log_number AND TL.id ={}
AND TL.log_date 
BETWEEN DATE_SUB(CURDATE(), INTERVAL 7 DAY) AND CURDATE();
"""


wtoutputMySQL =\
"""
SELECT log_date, sleep_hours 
FROM tracker_log 
WHERE id = {} 
AND log_date BETWEEN DATE_SUB(CURDATE(), INTERVAL {} DAY) AND CURDATE() 
ORDER BY log_date
"""


wtoutputMySQL2 =\
"""
SELECT SUM(WO.hours) AS workouthours, TL.log_date
FROM workouttracker.workout AS WO, workouttracker.tracker_log AS TL
WHERE WO.log_number = TL.log_number AND TL.id = {}
GROUP BY TL.log_date 
HAVING TL.log_date BETWEEN DATE_SUB(CURDATE(), INTERVAL {} DAY) AND CURDATE()
ORDER BY TL.log_date;
"""


wtoutputMySQL3 =\
"""
SELECT SUM(WO.workout_set) AS totalsets,
SUM(WO.workout_set*WO.workout_rep) AS totalreps,
SUM(WO.workout_set*WO.workout_rep*WO.EquipmentWeight) AS volume,
SUM(WO.workout_set*WO.workout_rep*WO.EquipmentWeight)/SUM(WO.hours) AS intensity,
TL.log_date , TL.id
FROM workouttracker.workout AS WO, workouttracker.tracker_log AS TL, workouttracker.workouttype AS WT
WHERE WO.log_number = TL.log_number AND WO.WorkoutTypeID = WT.WorkoutTypeID
AND TL.id = {} AND WT.WorkoutName = '{}'
GROUP BY TL.log_date 
HAVING TL.log_date BETWEEN DATE_SUB(CURDATE(), INTERVAL {} DAY) AND CURDATE()
ORDER BY TL.log_date; 
"""


wtoutputMySQL4 =\
"""
SELECT DISTINCT WT.WorkoutName
FROM workouttracker.workouttype AS WT, workouttracker.workout AS WO, workouttracker.tracker_log AS TL
WHERE WT.WorkoutTypeID = WO.WorkoutTypeID AND WO.log_number = TL.log_number AND TL.id = {};
"""

wtoutputMySQL5 = " SELECT WorkoutName FROM workouttracker.workouttype where WorkoutName = '{}' ;"

wtoutputMySQL6 =\
"""
SELECT AVG(FD.amount) AS avgWater, AVG(FD.carb) AS avgCarb, AVG(FD.protein) AS avgProtein, AVG(FD.fat) As avgFat
FROM workouttracker.food_drink AS FD, workouttracker.tracker_log AS TL 
WHERE FD.log_number = TL.log_number AND TL.id = {} 
AND TL.log_date BETWEEN DATE_SUB(CURDATE(), INTERVAL {} DAY) AND CURDATE();
"""



wtoutputMySQL7 =\
"""
SELECT COUNT(WO.WorkoutTypeID) AS countWorkout, WT.WorkoutName AS WorkoutName
FROM workouttracker.workout AS WO, workouttracker.workouttype AS WT, workouttracker.tracker_log AS TL
WHERE WO.log_number = TL.log_number AND WO.WorkoutTypeID = WT.WorkoutTypeID AND TL.id = 13
AND TL.log_date BETWEEN DATE_SUB(CURDATE(), INTERVAL {} DAY) AND CURDATE()
GROUP BY WO.WorkoutTypeID
ORDER BY COUNT(WO.WorkoutTypeID) DESC;
"""

wtoutputMySQL8 =\
"""
SELECT CAST(SUM(FD.carb) AS UNSIGNED) AS carb, CAST(SUM(FD.protein) AS UNSIGNED) AS protein,
CAST(SUM(FD.Fat) AS UNSIGNED) AS fat, TL.log_date AS logdate
FROM workouttracker.food_drink AS FD, workouttracker.tracker_log AS TL
WHERE TL.log_number= FD.log_number AND TL.id = {} 
GROUP BY TL.log_date
HAVING TL.log_date BETWEEN DATE_SUB(CURDATE(), INTERVAL {} DAY) AND CURDATE();
"""







livesearchMySQL = "SELECT distinct WorkoutName FROM workouttracker.workouttype WHERE WorkoutName like '{}%' LIMIT 5;"
# livesearchMySQL2 = "SELECT distinct MajorMuscle FROM workouttracker.workouttype WHERE WorkoutName like '{}%';"
livesearchMySQL2 = "SELECT distinct MajorMuscle FROM workouttracker.workouttype WHERE WorkoutName = '{}';"

calendarsettingMySQL = "SELECT TL.log_date, WT.WorkoutName FROM tracker_log AS TL, workout AS WO, workouttype AS WT" \
                       " WHERE WO.log_number = TL.log_number AND WT.WorkoutTypeID = WO.WorkoutTypeID AND TL.id = {};"

calendarsettingMySQL2 =\
"""
DELETE FROM tracker_log WHERE id = {} AND log_date = '{}';
"""


registerMySQL = "SELECT * FROM wt_user WHERE email = '{}'"
registerMySQL2 = "INSERT INTO wt_user(first_name,last_name, email, password) VALUES('{}', '{}', '{}', {});"

loginMySQL = "SELECT * FROM wt_user WHERE id = {};"
loginMySQL2 = "SELECT * FROM wt_user WHERE email = '{}' AND password = '{}';"

wtinputMySQL = "SELECT * FROM tracker_log WHERE id = {} AND log_date = '{}';"
wtinputMySQL2 = "INSERT INTO tracker_log(log_date, id, sleep_hours) VALUES('{}',{}, {});"




wtinputMySQL4 = "SELECT * FROM workouttracker.workouttype WHERE WorkoutName = '{}';"

wtinputMySQL3 = "INSERT INTO workout( hours, workout_set, workout_rep, log_number, EquipmentWeight, WorkoutTypeID)" \
                "VALUES({}, {}, {}, {}, {}, {});"

wtinputMySQL5 = "INSERT INTO workouttracker.workouttype( WorkoutName, Equipment, MajorMuscle, MinorMuscle)" \
                "VALUES('{}', '{}', '{}', '{}');"

wtinputMySQL6 =  "UPDATE workouttracker.workouttype set Equipment = '{}' ,  MajorMuscle = '{}', MinorMuscle = '{}' WHERE WorkoutName = '{}';"



wtinputMySQL7 = "INSERT INTO body_condition(disease_name, fatigue_level, log_number) VALUES('{}', {}, {})ON DUPLICATE KEY UPDATE log_number = VALUES(log_number);"

wtinputMySQL8 = "INSERT INTO food_drink(fd_name, amount, carb, protein, fat, log_number) VALUES('{}', {}, {}, {}, {}, {});"


