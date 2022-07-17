// https://twitter.com/jckarter/status/1428093469755527168

#include <stdbool.h>

bool collatz(unsigned int x) {
    while (true) {
        if (x <= 1)
            return true;

        if (x % 2)
            x >>= 1;
        else
            x = 3*x + 1;
    }
}

int main(int argc, char **argv) {
    if (collatz(argc)){
        return 0;
    }
    return 1;
}

/*----------------------------------------------------------------

$ clang collatz.c -S -emit-llvm -o - -O3

; ModuleID = 'collatz.c'
source_filename = "collatz.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind readnone uwtable
define dso_local zeroext i1 @collatz(i32 %0) local_unnamed_addr #0 {
  %2 = icmp ult i32 %0, 2
  br i1 %2, label %3, label %4

3:                                                ; preds = %4, %1
  ret i1 true

4:                                                ; preds = %1, %4
  %5 = phi i32 [ %11, %4 ], [ %0, %1 ]
  %6 = and i32 %5, 1
  %7 = icmp eq i32 %6, 0
  %8 = lshr i32 %5, 1
  %9 = mul i32 %5, 3
  %10 = add i32 %9, 1
  %11 = select i1 %7, i32 %10, i32 %8
  %12 = icmp ult i32 %11, 2
  br i1 %12, label %3, label %4
}

; Function Attrs: norecurse nounwind readnone uwtable
define dso_local i32 @main(i32 %0, i8** nocapture readnone %1) local_unnamed_addr #0 {
  ret i32 0                                                                                         <--------- HERE is the cursed
}

attributes #0 = { norecurse nounwind readnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="none" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 10.0.0-4ubuntu1 "}

----------------------------------------------------------------*/