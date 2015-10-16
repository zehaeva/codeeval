{--}
import System.Environment (getArgs)

f :: [String] -> [Int]
f = map read 
s :: [Int] -> [String]
s = map show 

fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib n = fib(n - 1) + fib(n-2)

main = do
	[inpFile] <- getArgs
	input <- readFile inpFile
	-- print your output to stdout
	let mylist_a = lines input
	let mylist_b = f mylist_a
	let mylist_a = map fib mylist_b
	mapM_ putStrLn $ s mylist_a
	--mapM_ putStrLn $ lines (show (mylist_a))
