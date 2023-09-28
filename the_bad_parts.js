console.log("1 == \"1\" evaluates to "+(1=="1"));
console.log("1 == true evaluates to "+(1==true));
console.log("\"1\" == true evaluates to "+("1"==true));
console.log("0 == \"0\" evaluates to "+(0=="0"));
console.log("0 == [] evaluates to "+(0==[]));
console.log("0 == false evaluates to "+(0==false));
console.log("0 == \" \" evaluates to "+(0==" "));
console.log("0 == \"\" evaluates to "+(0==""));
console.log("0 == \"\\n\" evaluates to "+(0=="\n"));
console.log("[] == false evaluates to "+([]==false));
console.log("[] == \"\" evaluates to "+([]==false));
console.log("[] == ![] evaluates to "+([]==![]));
console.log("false == \"\" evaluates to "+(false==""));
console.log("false == \" \" evaluates to "+(false==" "));
console.log("false == \"\\n\" evaluates to "+(false=="\n"));
console.log("null == undefined evaluates to "+(null==undefined));
console.log("\'b\'+\'a\'++\'a\'+\'a\' evaluates to "+('b'+'a'+ +'a' + 'a').toLowerCase());
// http://www.jsfuck.com/
console.log("++[[]][+[]]+[+[]] evaluates to "+(++[[]][+[]]+[+[]]));

function f(){
    var x = 10
    if(x == 4) {
        var y = 12
        /*
        without the brackets
        not treated as a block
        e.g. let y=12 would not be allowed
        it's not a block with one line only
        when there are no brackets
        */
    }
    /*
    when put x=4 instead, we return 12
    but here, we get undefined
    var y should be only within the scope of the if
    but it is function scoped instead
    like a var y at the top, but with no assignment
    */
    return y
}
console.log("f() gives "+f()+". Undefined is it's own cursed beast even if it is normal.")

console.log("typeof(NaN+'N') evaluates to typeof("+(NaN+'N')+") then "+typeof(NaN+'N'));
console.log("typeof(NaN+'N'-'N') evaluates to typeof("+(NaN+'N'-'N')+") then "+typeof(NaN+'N'-'N'));
console.log("typeof(NaN+'N'-'N'-'a') evaluates to typeof("+(NaN+'N'-'N'-'a')+") then "+typeof(NaN+'N'-'N'-'a'));
