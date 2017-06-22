L = range(10)
def fish(i):
    return L[i]
try:
    print fish(10)
except IndexError:
    print "Out of range!"
except TypeError as e:
    print e
except (ValueError, NameError):
    raise
except:
    print "Zlapalem dowolny wyjatek!"
else:
    print "Good shot!"
finally:
    L.pop()