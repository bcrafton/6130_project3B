output_wf 1
vname A<[5:4]> A<[3:0]> B<[5:4]> B<[3:0]> F<[5:4]> F<[3:0]>
io i i i i o o
radix 2 4 2 4 2 4
tunit 1ns
period 10
chk_window 5 5 0
trise .001
tfall .001
vih 1.0
vil 0.0
voh 0.6
vol 0.4

0 1 0 0 0 1
0 2 0 0 0 2
0 3 0 0 0 3
0 1 0 1 0 2
0 2 0 3 0 5
