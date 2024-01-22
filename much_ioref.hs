import Data.IORef (IORef, newIORef, readIORef, writeIORef)
import GHC.IO (unsafePerformIO)

broadcastedOp :: a -> (a -> a -> a) -> [a] -> [a] -> [a]
broadcastedOp defaultA op [] ys = op defaultA <$> ys
broadcastedOp defaultA op xs [] = (`op` defaultA) <$> xs
broadcastedOp _ op [x] ys = op x <$> ys
broadcastedOp _ op xs [y] = (`op` y) <$> xs
broadcastedOp _ op xs ys
    | length xs == length ys = zipWith op xs ys
    | otherwise = error "incompatible lengths"

broadcastedAdd :: Num a => [a] -> [a] -> [a]
-- empty is interpreted as [0] for extra cursing
broadcastedAdd = broadcastedOp 0 (+)


myVar :: () -> IORef [a]
myVar _ = unsafePerformIO $ newIORef []

myDouble :: Num a => IORef [a] -> IO ()
myDouble var = do
    oldValue <- readIORef var
    let newValue = broadcastedAdd oldValue oldValue
    writeIORef var newValue

myPlusEquals :: Num a => IORef [a] -> IORef [a] -> IO ()
myPlusEquals var1 var2 = do
    oldValue1 <- readIORef var1
    oldValue2 <- readIORef var2
    let newValue = broadcastedAdd oldValue1 oldValue2
    writeIORef var1 newValue

createVar :: [a] -> IO (IORef [a])
createVar initialValue = do
    let test = myVar ()
    writeIORef test initialValue
    return test

main = do
    test <- createVar [42]
    bang <- readIORef test
    print (bang :: [Int])
    myDouble test
    bang <- readIORef test
    print (bang :: [Int])
    let test2 = myVar ()
    writeIORef test2 [16,16,16]
    bang <- readIORef test2
    print (bang :: [Int])
    myPlusEquals test2 test
    bang <- readIORef test2
    print (bang :: [Int])
    bang <- readIORef test2
    print (bang :: [Char])
    bang <- readIORef test2
    -- [100,100,100] becomes "ddd" ok that makes sense because 100->d in character encoding
    print (bang :: [String])
    -- now it becomes ["","",""] without complaining, why?
    bang <- readIORef test
    print (bang :: [Int])
    -- but test is still [84] this entire time
