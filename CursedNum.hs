--https://www.reddit.com/r/haskell/comments/svbfjg/adding_element_to_empty_list/hxful04/?context=3

instance Num [a] where
    fromInteger _ = []

someBrokenList :: [[()]]
someBrokenList = [5,[],[]]