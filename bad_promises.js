/*
timeout for reject and resolve cases are so close that it depends on execution which one happens
if reject wins we get "Error" passed to reject
if resolve wins then we have to wait another 1000 ms so that eventually foo can bubble up
*/
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(new Promise((resolve2,reject2)=> {
          setTimeout(() => {resolve2("foo");}, 1000);
        }));
    }, 1000);
    setTimeout(() => {reject("ErrorLabel1");},999);
    //setTimeout(() => {reject("Error2");},10_000); //if uncomment this, then it will take long the full 10s despite not being impactful
  });

const handleFulfilledA = (x) => {
    console.log(x)
    var timeBefore = time
    time = performance.now()
    console.log(time - timeBefore)
    return Promise.reject("ErrorLabel3")
}

var time = performance.now()
myPromise
    .then(handleFulfilledA,(x)=>{
      console.log(x);
      return Promise.resolve("ErrorLabel2");
    })
    .then(handleFulfilledA,(x)=>{console.log(x);return Promise.reject("ErrorLabel4");})
    .catch((x) => {console.log(x);console.log("Here");})
    .finally(() => {})

//suppose reject("ErrorLabel1") wins, then will print out ErrorLabel1, have a resolved ErrorLabel2 which then gets printed out with a time value ~1000ms
//  then have a rejected ErrorLabel3 which then gets caught and printed along with Here
//suppose resolve(...) wins, then will print out foo with a time value ~2000ms, then have a rejected ErrorLabel3
//  that gets caught (in the second then not the catch), printed out and then have a rejected ErrorLabel4, that gets caught (with the catch part) and printed along with Here