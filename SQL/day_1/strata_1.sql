--- https://platform.stratascratch.com/coding/10011-find-all-number-pairs-whose-first-number-is-smaller-than-the-second-one-and-the-product-of-two-numbers-is-larger-than-11?code_type=1---

select 
distinct n1.number as num1, n2.number as num2
from transportation_numbers n1
join transportation_numbers n2
on n1.index <> n2.index
where n1.number < n2.number 
and n1.number * n2.number > 11