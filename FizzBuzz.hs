import System.Environment (getArgs)
fb (x:y:n:_) = [case (mod num x, mod num y) of (0,0) -> "FB"; (0,_) -> "F"; (_,0) -> "B";_ -> show num | num <- [1..n]]

con :: [String] -> [Int]
con = map read

main = do
	[inpFile] <- getArgs
	input <- readFile inpFile
	let mylines = lines input
	mapM_ putStrLn $ map (unwords . fb .con . words) mylines
