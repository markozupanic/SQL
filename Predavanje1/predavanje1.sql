/*rješavano https://www.sql-practice.com/ */


select * from patients where gender='F' and weight>80 and birth_date between '1990-01-01' and '2022-01-01' and allergies is null;


select first_name,last_name,weight,
(case 
  when weight>100 then 'overweight'
  else 'normal' 
 end) as 'is_overweight'
from patients;


select count(*) from patients where first_name='Daniel'

select first_name, count(*) broj from patients group by first_name having broj >10 limit 3

select first_name from patients group by first_name having count()=1

select first_name,last_name, max(height) from patients

select first_name,last_name,height from patients where weight > (select avg(weight) from patients)

select allergies,count() popularity from patients where allergies is not null group by allergies order by popularity desc




select first_name,last_name,weight,
(case 
  when height<150 then 1
  else 0
 end) as 'is_short'
from patients;


select * from  patients where patient_id in (select patient_id from admissions where diagnosis='Cancer')
select patient_id from admissions where diagnosis='Cancer'

select * from patients p
join admissions a on p.patient_id=a.patient_id where a.diagnosis='Cancer'



select * from patients p
left join admissions a on p.patient_id=a.patient_id where p.patient_id=14


select * from patients p 
join admissions a on p.patient_id=a.patient_id where a.diagnosis='Cardiac Arrest'
 
select * from patients p 
join admissions a on p.patient_id=a.patient_id
join doctors d on a.attending_doctor_id=d.doctor_id
where lower (a.diagnosis)='cardiac arrest' and d.specialty='Cardiologist'


select * from patients
left join admissions on patients.patient_id=admissions.patient_id
where admissions.patient_id is null


/*bez duplikata*/
select first_name,last_name,'patient' as role from patients
union 
select first_name,last_name,'doctor' as role from doctors

/*izlistava sve */
select first_name,last_name,'patient' as role from patients
union all
select first_name,last_name,'doctor' as role from doctors


select first_name from patients
intersect 
select first_name from doctors


select first_name from doctors
except
select first_name from patients


select * from doctors
where first_name='Claude'



select distinct year(birth_date) as years from patients order by years asc

select first_name from patients group by first_name
having count()=1


select patient_id,first_name from patients where lower(first_name) like 's____%s'



select patients.patient_id,first_name,last_name from patients
join admissions on patients.patient_id=admissions.patient_id
where diagnosis='Dementia'

select first_name from patients order by len(first_name),first_name asc


select sum (case
             when gender='M' then 1
             else 0
            end),sum(case
                     when gender='F' then 1
                     else 0
                    end)
            from patients 



select first_name,last_name,allergies from patients where allergies='Penicillin'
or allergies='Morphine' order by allergies,first_name,last_name 

select patient_id,diagnosis from admissions group by patient_id,diagnosis having count()>1
 

select city,count() as num from patients group by city order by num desc,city asc

select first_name,last_name,'patient' as role from patients
union all
select first_name,last_name,'doctor' as role from doctors


select concat(upper(last_name),',',lower(first_name)) from patients order by first_name desc



select province_id,sum(height) as num from patients group by province_id 
having num>=7000 order by num desc


select max(weight)-min(weight) from patients where last_name='Maroni' 


select day(admission_date),count() from admissions group by day(admission_date) 
order by count() desc

select * from admissions where patient_id=542 order by 
admission_date desc limit 1


select patient_id,attending_doctor_id,diagnosis from admissions
where (patient_id%2=1 and attending_doctor_id in (1,5,19))
or (attending_doctor_id like '%2%' and len(patient_id)=3)


select first_name,last_name,count() from admissions
join doctors on admissions.attending_doctor_id=doctors.doctor_id
group by attending_doctor_id


select province_names.province_name,count() from patients
join province_names on patients.province_id=province_names.province_id
group by patients.province_id order by  count() desc


select concat(p.first_name,' ',p.last_name),a.diagnosis,concat(d.first_name,' ',d.last_name) 
from admissions a 
join patients p on a.patient_id=p.patient_id
join doctors d on a.attending_doctor_id=d.doctor_id

select first_name,last_name,count() from patients
group by first_name,last_name
having count()>1


select count(),round(weight/10,0)*10 as weight_group from patients
group by weight_group
order by weight_group desc









