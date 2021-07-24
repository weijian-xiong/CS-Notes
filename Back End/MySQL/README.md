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
