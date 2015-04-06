import System.Environment (getArgs)

main = do
	[inpFile] <- getArgs
	input <- readFile inpFile
	-- print your output to stdout
	mapM_ putStrLn $ map (unwords . reverse . words) $ lines input
