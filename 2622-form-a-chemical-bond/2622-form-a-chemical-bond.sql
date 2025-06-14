with metal as
(select symbol
from elements where type not in ('Noble','Nonmetal')),
nonmetal as
(select symbol
from elements where type not in ('Noble','Metal'))

select A.symbol as metal, B.symbol as nonmetal
from metal A
cross join nonmetal B
