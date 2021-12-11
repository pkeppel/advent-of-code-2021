class Doc:
	def __init__(self, data):
		self.data = data
		self.map = {
			"{" : "}",
			"[" : "]",
			"<" : ">",
			"(" : ")"
		}
		self.points = {
			"}" : 1197,
			"]" : 57,
			">" : 25137,
			")" : 3
		}
		self.score = 0
		
		
	def line(self,line):
		l = ["{", "<", "(", "[" ]
		r = ["}", ">", ")", "]" ]
		b = []
		print("-------------")
		print(line)
		
		for i in range(len(line)):
			a = line[i]
			if a in l:
				b.insert(0, self.map[a])
				continue
			elif b[0] == a:
				b.pop(0)
			else:
				print(f"Expected {b[0]}, but found {a} instead. Points: {self.points[a]}")
				self.score += self.points[a]
				return	
		print("incomplete")
		
	def part1(self):
		for line in self.data:
			self.line(line)
		
		return self.score


# --------------------------------------------------------------------------	
# pull the dataset from a file 
def fetch(fpath):
	dataset = []
	
	with open(fpath, "r") as infile:
		for line in infile:
			dataset.append(line.strip())
				
	return dataset


# --------------------------------------------------------------------------	
# solve the problems.
def solve(dataset):
	doc = Doc(dataset)
	result1 = doc.part1()
	result2 = None

	return (result1, result2)	


# --------------------------------------------------------------------------
# do the main 
def main():
	#fpath = "./day10-sample.txt" # this is the sample dataset.
	fpath = "./day10-data.txt"
	dataset = fetch(fpath)
	
	r1,r2 = solve(dataset)
	print(f"Part 1:\t{r1}\r\nPart 2:\t{r2}")	


# ==========================================================================
if __name__ == "__main__" :
	result = main()
