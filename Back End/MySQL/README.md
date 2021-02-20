# Installation
[How to use sql in terminal](https://askubuntu.com/questions/353460/how-to-use-sql-in-terminal)<br>
[Mac install and use sql](https://stackoverflow.com/questions/14235362/mac-install-and-open-mysql-using-terminal)<br>
[Install MySQL on macOS Sierra](https://gist.github.com/nrollr/3f57fc15ded7dddddcc4e82fe137b58e)

# How you use MySQL
1. Type "mysql -u root -p" in the terminal
2. Enter password for root
3. Type "show databases;" --> to see what databases do you have 
4. Type "use test;" --> test is the database name you want to use
5. Type "show tables;" --> to see what tables on your selected database
6. Then create, modify, update or delete your table

# Five keys
Super key 超鍵 : 符合唯一性的關聯鍵。
Candidate Key 候選鍵 : 符合唯一性以及最小性的關聯鍵。
Primary Key 主鍵 : 從候選鍵中，挑選出其中一個關聯鍵，也就是最具識別意義的關聯鍵。
Alternate Key 次要鍵 : 沒有被選為主鍵的其他候選鍵。
Foreign Key 外鍵/外部鍵 : 關聯中被用來參考到其他表格主鍵的關聯鍵，就是外鍵。

例如學生資料表(student_id, student_no, student_name, student_depid)
student_id表示學生身分證字號
student_no表示學生學號
student_name表示學生姓名
student_depid表示學生的科系代號

Super key 就可以是 {student_id}、{student_no}、 {student_id, student_no}、{student_id, student_name}、{student_id, student_depid} ... 等等，都符合唯一性的條件。

Candidate Key 就可以是 {student_id}、{student_no}，都符合唯一性及最小性的條件。

Primary Key 就可以從Candidate Key挑選一個，至於挑選哪一個，就看你的系統特性。如果你的學校是多學制的話，就可能不適合挑選學生身分證字號當主鍵，因為可能某個學生原本是國中部，畢業後再進入高中部，如果系統沒有考慮清楚，這個畢業後再變新生的個體，就可能出錯。

Alternate Key 就是沒被挑中當成Primary Key的其他Candidate Key，例如，如果挑選 {student_id}當成主鍵，Alternate Key 就是{student_no}。

如果存在科系資料表 (depid, dep_name)，而且depid當成科系資料表的主鍵，學生資料表的 student_depid就是Foreign Key。

# Sample queries
Add primary key:<br>
alter table person1 add constraint primary key(name);

select state from station where city like '%nix%';<br>
% means at least two characters<br>
_ means only one character

alter table metric_stats change `(temp_f-32)*5/9` temp_c real;

update stats set rain_i = rain_i +0.01;

CREATE TABLE STATION (ID INT(2) PRIMARY KEY, CITY VARCHAR(20),STATE VARCHAR(2),COUNTRY VARCHAR(10), ZIP INT(10), LAT_N REAL, LONG_W REAL);

INSERT INTO STATION VALUES(44,'DENVER','CO','US',80014,40,105);

CREATE TABLE STATS (ID INT(2) REFERENCES STATION(ID), MONTH INT CHECK(MONTH BETWEEN 1 AND 12), TEMP_F REAL CHECK(TEMP_F BETWEEN -80 AND 150), RAIN_I REAL CHECK(RAIN_I BETWEEN 0 AND 100), PRIMARY KEY (ID,MONTH));

show create table TRANSACTION;

# Related Link
[SQL语句大全](https://mp.weixin.qq.com/s/LDkMCYi5bejFEo5D1buUFg)<br>
[SQL数据库面试题以及答案](https://mp.weixin.qq.com/s/jf9g_s6Vro2BzzEHo6xuYQ)<br>
