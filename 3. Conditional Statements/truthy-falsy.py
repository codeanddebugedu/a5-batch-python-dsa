"""
Truthy Falsy

int -> bool
str -> bool
float -> bool

int (truthy) -> 1,8,-99,-66,9999
int (falsy) -> 0

float (truthy) -> 1.2,8.6,-99,0.000001
float (falsy) -> 0.0

str (truthy) -> "dawdwa", " ", "   ", "dhwakj dwagdhjkwagd jkahhdkjwa"
str (falsy) -> ""

None -> False
"""

# a = bool(0.0)
# print(a)
# a = bool("")
# print(a)
a = bool(None)
print(a)
