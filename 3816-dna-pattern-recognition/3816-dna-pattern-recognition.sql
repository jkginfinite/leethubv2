# Write your MySQL query statement below
select *,
case when dna_sequence LIKE 'ATG%' then 1
else 0
end as has_start,
case when dna_sequence LIKE '%TAA' or dna_sequence like '%TAG' or dna_sequence like '%TGA' then 1
else 0
end as has_stop,
case when dna_sequence LIKE '%ATAT%' then 1
else 0
end as has_atat,
case when dna_sequence LIKE '%GGG%' then 1
else 0
end as has_ggg
from samples
