-- https://www.reddit.com/r/haskell/comments/tusnmm/creating_a_function_with_a_single_optional/
-- u/Noughtmare

{-# LANGUAGE GADTs, FlexibleInstances #-}

import GHC.Float (int2Float)

type GeneralFooReturn = Float -> Float
type GeneralFooInput = Int
defaultInput :: GeneralFooInput
defaultInput = 0
generalFoo :: GeneralFooInput -> GeneralFooReturn
generalFoo x y = y + int2Float x

class Foo r where
  foo :: r

instance {-# OVERLAPPING #-} Foo GeneralFooReturn where
  foo = generalFoo defaultInput

instance (b ~ (GeneralFooInput -> GeneralFooReturn)) => Foo b where
  foo = generalFoo

main :: IO ()
main = do
    print $ (foo :: GeneralFooReturn) 5.0
    print $ foo 4 5.0