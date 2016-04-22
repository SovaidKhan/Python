"""
>>> import numberutil
>>> numberutil.aswords(00)
'zero'
>>> numberutil.aswords(20)
'twenty'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(22)
'twenty two'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(120)
'one hundred and twenty'
>>> numberutil.aswords(130)
'one hundred and thirty'
>>> numberutil.aswords(125)
'one hundred and twenty five'


"""
import doctest
doctest.testmod(verbose=True)

# 1. hundreds=0 and remainder=0
# 2. hundreds=0 and remainder>0 and remainder<21
# 3. hundreds=0 and remainder>0 and remainder>=21 and units=0
# 4. hundreds=0 and remainder>0 and remainder>=21 and units>0
# 5. hundreds>0 and remainder=0
# 6. hundreds>0 and remainder>0 and remainder<21
# 7. hundreds>0 and remainder>0 and remainder>=21 and units=0
# 8. hundreds>0 and remainder>0 and remainder>=21 and units>0