import System.Environment (getArgs)

revWords :: String -> String
revWords input = (unwords . reverse . words) input

main = do
	[inpFile] <- getArgs
	input <- readFile inpFile
	let thing = map revWords $ lines input
	-- print your output to stdout
	mapM_ putStrLn thing
