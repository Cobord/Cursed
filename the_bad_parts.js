{
    // simple type coercions
    console.log("1 == \"1\" evaluates to " + (1 == "1"));
    console.log("1 == true evaluates to " + (1 == true));
    console.log("\"1\" == true evaluates to " + ("1" == true));
    console.log("0 == \"0\" evaluates to " + (0 == "0"));
    console.log("0 == [] evaluates to " + (0 == []));
    console.log("0 == false evaluates to " + (0 == false));
    console.log("0 == \" \" evaluates to " + (0 == " "));
    console.log("0 == \"\" evaluates to " + (0 == ""));
    console.log("0 == \"\\n\" evaluates to " + (0 == "\n"));
    console.log("[] == false evaluates to " + ([] == false));
    console.log("[] == \"\" evaluates to " + ([] == false));
    console.log("[] == ![] evaluates to " + ([] == ![]));
    console.log("false == \"\" evaluates to " + (false == ""));
    console.log("false == \" \" evaluates to " + (false == " "));
    console.log("false == \"\\n\" evaluates to " + (false == "\n"));
    console.log("null == undefined evaluates to " + (null == undefined));
    console.log("\'b\'+\'a\'++\'a\'+\'a\' evaluates to " + ('b' + 'a' + +'a' + 'a').toLowerCase());
    // http://www.jsfuck.com/
    console.log("++[[]][+[]]+[+[]] evaluates to " + (++[[]][+[]] + [+[]]));
}

{
    // scoping
    function f() {
        var x = 4
        if (x == 4) {
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
    console.log("f() gives " + f() + ". Undefined is it's own cursed beast even if it is normal.")
}

{
    // type coercions + NaN
    console.log("typeof(NaN+'N') evaluates to typeof(" + (NaN + 'N') + ") then " + typeof (NaN + 'N'));
    console.log("typeof(NaN+'N'-'N') evaluates to typeof(" + (NaN + 'N' - 'N') + ") then " + typeof (NaN + 'N' - 'N'));
    console.log("typeof(NaN+'N'-'N'-'a') evaluates to typeof(" + (NaN + 'N' - 'N' - 'a') + ") then " + typeof (NaN + 'N' - 'N' - 'a'));
    console.log("typeof(NaN+'N'-'N'-'N') evaluates to typeof(" + (NaN + 'N' - 'N' - 'N') + ") then " + typeof (NaN + 'N' - 'N' - 'N'));
    console.log((NaN+"N")+ " and it's type is "+typeof(NaN+"N")) // NaNN as a string
    console.log((NaN+"N"-"N")+ " and it's type is "+typeof(NaN+"N"-"N")) // the subtraction was as strings but it is now a number again
    console.log((NaN+"N"-"N"-"N")+ " and it's type is "+typeof(NaN+"N"-"N"-"N"))
    // now the subtraction doesn't remove the trailing N because of the last step putting it back to a number
}

{
    // Automatic Semicolon Insertion
    function g() {
        return
        5
    }

    console.log("Whitespace matters because of Automatic Semicolon Insertion with g() giving " + g());

    function h() {
        const a = 1
            (1).toString()
    }
    try {
        h()
    } catch (e) {
        console.log("More Automatic Semicolon Insertion with h() giving the following error" + e + 
        "\n\teven though it was on the later line and was just calling to string on it."+
        "\n\tIt put the 1 from the previous line together with the (1) to give 1(1) as a function call");
    }

}

{
    // Scientific notation silent parseInt
    for (i = 0; i <10; i++) {
        const as_string = "0."+"0".repeat(i)+"5";
        const as_number = Number(as_string);
        const as_number_again = Number.parseInt(as_number)
        console.log(as_string+"-> "+Number(as_string)+" -> "+as_number_again)
    }
    console.log("Scientific notation, but silently ignoring the e on the reparse without telling"+
    "that was only a part of the input that parsed to the number when it should have been an error")
}

{
    // start as an object (array) but the monoid operation on arrays doesn't work
    // instead converting it to string
    // thinking of string as array of char, would think + would still be concatenation
    let b = [1,2,3]
    console.log(b+ " is "+typeof(b))
    b = b+[4]
    console.log(b+ " is "+typeof(b))
}

{
    // reverse doing in place and causing an aliased pointer
    let b = [1,2,3]
    const c = b.reverse()
    b.push(4)
    console.log("b="+b+" and c="+c)
    console.log("Ok it is in place."+
    "But what would make more sense is if the reverse took ownership of b and so we wouldn't have both b and c here now (could still method chain in that)"+
    "Or if we have to be taking a mutable pointer, then the reverse would not return anything because the effect is on just b")
}