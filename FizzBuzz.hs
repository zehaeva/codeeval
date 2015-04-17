import System.Environment (getArgs)
fb (x:y:n:_) = [if num `mod` x == 0 && num `mod` y == 0 then "FB" else if num `mod` x == 0 then "F" else if num `mod` y == 0 then "B" else show num | num <- [1..n]]

con :: [String] -> [Int]
con = map read

main = do
	[inpFile] <- getArgs
	input <- readFile inpFile
	let mylines = lines input
	mapM_ putStrLn $ map (unwords . fb .con . words) mylines
