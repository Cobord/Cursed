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
    if(x == 4)
        var y = 12
    return y
}
console.log("f() gives "+f()+". Undefined is it's own cursed beast even if it is normal.")