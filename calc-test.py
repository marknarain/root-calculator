from calc import *
import time

#############################################################
#
# test results of cmp()
#
#############################################################
x = cmp([1,0],[1,0]);                       assert x == 0,x
x = cmp([-1,0],[-1,0]);                     assert x == 0,x
x = cmp([1,1,2,3,4,5,6],[1,1,2,3,4,5,6]);   assert x == 0,x
x = cmp([1,0,0,0,1],[1,0,0,0,1]);           assert x == 0,x
x = cmp([1,2,3,4,5,1,2],[1,2,3,4,5,1,2]);   assert x == 0,x
x = cmp([1,8,3,5,2,5,2,8,3],[1,8,3,5,2,5,2,8,3]);       assert x == 0,x

x = cmp([1,5],[1,0]);                       assert x == 1,x
x = cmp([1,9,9,9],[1,2,3,4]);               assert x == 1,x
x = cmp([1,1,2,3,4,5,6],[1,2,3,4]);         assert x == 1,x
x = cmp([1,1,2,3],[-1,1,2,3]);              assert x == 1,x
x = cmp([1,1,2,4],[-1,1,2,3]);              assert x == 1,x
x = cmp([1,1,2,3],[-1,1,2,4]);              assert x == 1,x
x = cmp([-1,2,3,4],[-1,4,5,6]);             assert x == 1,x
x = cmp([-1,5],[-1,6]);                     assert x == 1,x

x = cmp([1,0],[1,5]);                       assert x == -1,x
x = cmp([1,1,2,3],[1,2,3,4]);               assert x == -1,x
x = cmp([1,2,3,4],[1,1,2,3,4,5,6]);         assert x == -1,x   
x = cmp([-1,1,2,3],[1,1,2,3]);              assert x == -1,x
x = cmp([-1,1,2,4],[1,1,2,3]);              assert x == -1,x
x = cmp([-1,1,2,3],[1,1,2,4]);              assert x == -1,x
x = cmp([-1,4,5,7],[-1,4,5,6]); 	        assert x == -1,x
x = cmp([-1,1,2,3,4,5,6],[-1,2,3,4,5]);     assert x == -1,x

a = [8] * 1000000
b = [8] * 1000000
a[0] = 1
b[0] = 1
x = cmp(a,b);                               assert x == 0,x

a[999] = 0
b[999] = 1
x = cmp(a,b);                               assert x == -1,x

a[999] = 1
b[999] = 0
x = cmp(a,b);                               assert x == 1,x

a = [1,2,3]*1000
b = [1,2,4]*1000
x = cmp(a,b);                               assert x == -1,x

#############################################################
#
# test timing of cmp()
#
#############################################################
tStart = time.time()
x = cmp([1]*1000001,[1]*1000001)
tEnd = time.time()
print("Comparing 1mio digits: " + str(tEnd-tStart) + " sec")

tStart = time.time()
x = cmp([1]*1001,[1]*11)
tEnd = time.time()
print("Comparing 1000 with 10 digits: " + str(tEnd-tStart) + " sec")

#tStart = time.time()
#x = cmp([1]*100000001,[1]*100000001)
#tEnd = time.time()
#print("Comparing 100mio digits: " + str(tEnd-tStart) + " sec")

tStart = time.time()
x = cmp([1,2,3]*100000,[1,2,4]*1000000)
tEnd = time.time()
print("Comparing 3000 digits: " + str(tEnd-tStart) + " sec")

#############################################################
#
# test results of plus()
#
#############################################################
x = add([1,1],[1,1]);                       assert x == [1,2],x
x = add([-1,9],[1,9]);                      assert x == [1,0],x
x = add([1,1,2],[1,2,9]);                   assert x == [1,4,1],x
x = add([1,1,2,3],[1,2,9,4]);               assert x == [1,4,1,7],x

x = add([-1,1],[1,1]);                      assert x == [1,0],x
x = add([-1,9],[-1,9]);                     assert x == [-1,1,8],x
x = add([-1,1,2],[1,2,9]);                  assert x == [1,1,7],x
x = add([-1,1,2,3],[1,2,9,4]);              assert x == [1,1,7,1],x

#############################################################
#
# test results of minus()
#
#############################################################
x = sub([1,2],[1,9]);                       assert x == [-1,7],x
x = sub([1,3],[1,9,2]);                     assert x == [-1,8,9],x
x = sub([1,4],[1,9,1,5]);                   assert x == [-1,9,1,1],x   
x = sub([1,5],[1,9,2,6,9]);                 assert x == [-1,9,2,6,4],x

x = sub([1,2],[-1,9]);                      assert x == [1,1,1],x
x = sub([1,3],[-1,9,2]);                    assert x == [1,9,5],x
x = sub([1,4],[-1,9,1,5]);                  assert x == [1,9,1,9],x   
x = sub([1,5],[-1,9,2,6,9]);                assert x == [1,9,2,7,4],x

x = sub([-1,2],[1,9]);                      assert x == [-1,1,1],x
x = sub([-1,3],[1,9,2]);                    assert x == [-1,9,5],x
x = sub([-1,4],[1,9,1,5]);                  assert x == [-1,9,1,9],x   
x = sub([-1,5],[1,9,2,6,9]);                assert x == [-1,9,2,7,4],x

x = sub([-1,2],[-1,9]);                     assert x == [1,7],x
x = sub([-1,3],[-1,9,2]);                   assert x == [1,8,9],x
x = sub([-1,4],[-1,9,1,5]);                 assert x == [1,9,1,1],x   
x = sub([-1,5],[-1,9,2,6,9]);               assert x == [1,9,2,6,4],x

x = sub([1,9],[1,2]);                       assert x == [1,7],x
x = sub([1,9,2],[1,3]);                     assert x == [1,8,9],x
x = sub([1,9,1,5],[1,4]);                   assert x == [1,9,1,1],x   
x = sub([1,9,2,6,9],[1,5]);                 assert x == [1,9,2,6,4],x

x = sub([1,9],[-1,2]);                      assert x == [1,1,1],x
x = sub([1,9,2],[-1,3]);                    assert x == [1,9,5],x
x = sub([1,9,1,5],[-1,4]);                  assert x == [1,9,1,9],x   
x = sub([1,9,2,6,9],[-1,5]);                assert x == [1,9,2,7,4],x

a = [1,1,2,3]
b = [-1,2,3,4]
x = sub(a,b)
print(a,b)

assert 1==0, "all Tests passed"