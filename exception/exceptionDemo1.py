#try except and finally
#run time exception


try:
    no1 = int(input("enter no1 :"))
    no2 = int(input("enter no2 :"))

    print(no1 / no2)
# except ZeroDivisionError:
#     print("can not divide by zero")    

except ZeroDivisionError as e:
    print(e)        
except ValueError as e:
    print(e)    
except Exception as e:
    print(e)   
finally:
    print("handeled..")    