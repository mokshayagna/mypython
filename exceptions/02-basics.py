'''
# catch all exceptions
try:
    ...
except:
	...

# catch just one exception
try:
    ...
except IOError:
    ...

# catch one exception and provide the exception object
try:
    ...
except IOError as errobj:
    ...

# catch more than one exception
try:
    ...
except (IOError, ValueError) as errobj:
    ...
'''

'''
#It is possible to have more than one except statements with one try.
try:
    ...
except IOError as errobj:
    print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
    exit(1)
except FormatError as e:
    print >> sys.stderr, "File is badly formatted (%s): %s" % (str(e), filename)
    exit(1)

#except with else
try:
    ...
except IOError as e:
    print >> sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
    exit(1)
else:
    print "successfully opened the file", filename


#except with finally
try:
    ...
except IOError, e:
    print (sys.stderr, "Unable to open the file (%s): %s" % (str(e), filename)
    exit(1)
else:
	...
finally:
    delete_temp_files()
	

#Exception is raised using the raised keyword.
raise Exception("error message")
'''


#what is the output?
try:
    print(" a")
    raise Exception("URE message")
except:
    print(" b")
else:
    print(" c")
finally:
    print(" d")

print("")

#what is the output?
try:
    print(" a")
except:
    print(" b")
else:
    print(" c")
finally:
    print(" d")

print("")

#what is the output
def f():
    try:
        print(" a")
        raise Exception("doom")
        print(" m")
        print(" n")
    except TypeError:
        print(" b")
    except:
        print(" x")
    else:
        print(" c")
    finally:
        print(" d")

f()
print("")

def c():
    print(" c1")
    print("Aura"[5])
    print(" c2")

def b():
    print(" b1")
    c()
    print(" b2")

def a():
    print(" a1")
    b()
    print(" a2")

def main():
    print(" main1")
    a()
    print(" main2")

print ("Start")
# main()
print ("End")
print()

def c():
    print(" c1")
    try:
        print("Aura"[5])
    except:
        print(" In c catching exception")
    print(" c2")

def b():
    print(" b1")
    c()
    print(" b2")

def a():
    print(" a1")
    b()
    print(" a2")

def main():
    print(" main1")
    a()
    print(" main2")

print ("Start")
main()
print ("End")
print()

def c():
    print(" c1")
    print("Aura"[5])
    print(" c2")

def b():
    print(" b1")
    try:
        c()
    except:
        print(" In b catching exception")
    print(" b2")

def a():
    print(" a1")
    b()
    print(" a2")

def main():
    print(" main1")
    a()
    print(" main2")

print ("Start")
main()
print ("End")
print()

def c():
    print(" c1")
    print("Aura"[5])
    print(" c2")

def b():
    print(" b1")
    c()
    print(" b2")

def a():
    print(" a1")
    try:
        b()
    except:
        print(" In a catching exception")
    print(" a2")

def main():
    print(" main1")
    a()
    print(" main2")

print ("Start")
main()
print ("End")
print()

def c():
    print(" c1")
    print("Aura"[5])
    print(" c2")

def b():
    print(" b1")
    c()
    print(" b2")

def a():
    print(" a1")
    b()
    print(" a2")

def main():
    print(" main1")
    a()
    print(" main2")
print ("Start")
try:
    main()
except:
    print(" In catching exception")
print("END")
exit(0)

